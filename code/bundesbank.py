"""
bundesbank.py — minimal client for the Deutsche Bundesbank SDMX REST API.

Retrieves German government-bond yields (the risk-free proxy) directly from
https://api.statistiken.bundesbank.de/rest/data/{flow}/{key}?format=csv

Two useful sets of series in flow BBSIS:

  * Estimated term-structure yields ("ZAR"), one key per residual maturity,
    used to build a discount curve:
        D.I.ZAR.ZI.EUR.S1311.B.A604.R{NN}XX.R.A.A._Z._Z.A
    where {NN} is the maturity in years, zero-padded to 2 digits
    (R01XX = 1y, R10XX = 10y, ...).  The 10-year key is confirmed working.

  * The classic Umlaufsrendite (current yield of listed Federal securities) —
    the very series BNetzA averages over ten years for its risk-free base:
        D.I.UMR.RD.EUR.A604.000000.0.A

Only the standard library + `requests` are required.  If the host is
unreachable (e.g. behind a restrictive network), every function raises a clear
error so the app can fall back to a manual CSV upload.
"""

from __future__ import annotations

from typing import Dict, List, Tuple
import csv
import io

try:
    import requests
except ImportError:  # pragma: no cover
    requests = None  # the app surfaces a friendly message if missing

BASE = "https://api.statistiken.bundesbank.de/rest/data"

# Confirmed-working 10-year estimated yield series.
TERM_KEY = "D.I.ZAR.ZI.EUR.S1311.B.A604.R{nn}XX.R.A.A._Z._Z.A"
UMLAUFRENDITE_KEY = "D.I.UMR.RD.EUR.A604.000000.0.A"

# Maturities (years) offered for the discount curve.  The 10-year key is
# verified; the others follow the documented R{NN}XX pattern.  The app degrades
# gracefully for any key the API rejects.
CURVE_MATURITIES: Tuple[int, ...] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30)


def _fetch_csv(flow: str, key: str, last_n: int = 1,
               timeout: int = 30) -> List[dict]:
    """Fetch a single series as a list of {date, value} dicts (newest last)."""
    if requests is None:
        raise RuntimeError("The 'requests' package is required for live retrieval.")
    url = f"{BASE}/{flow}/{key}"
    params = {"format": "csv", "lang": "en"}
    if last_n:
        params["lastNObservations"] = last_n
    resp = requests.get(url, params=params, timeout=timeout,
                        headers={"Accept": "text/csv"})
    resp.raise_for_status()
    return _parse_bbk_csv(resp.text)


def _parse_bbk_csv(text: str) -> List[dict]:
    """Parse Bundesbank CSV (semicolon-delimited; first two columns are the
    observation date and value; a metadata header precedes the data block)."""
    rows: List[dict] = []
    reader = csv.reader(io.StringIO(text), delimiter=";")
    for cells in reader:
        if len(cells) < 2:
            continue
        date, val = cells[0].strip(), cells[1].strip()
        # Data rows start with an ISO-ish date (YYYY-MM-DD or YYYY).
        if not date[:4].isdigit():
            continue
        val = val.replace(",", ".")  # German decimal comma -> dot
        try:
            value = float(val)
        except ValueError:
            continue
        rows.append({"date": date, "value": value})
    return rows


def latest_value(flow: str, key: str) -> Tuple[str, float]:
    """Return (date, value) of the most recent observation of a series."""
    rows = _fetch_csv(flow, key, last_n=1)
    if not rows:
        raise RuntimeError(f"No observations returned for {flow}/{key}.")
    last = rows[-1]
    return last["date"], last["value"]


def umlaufrendite() -> Tuple[str, float]:
    """Latest Umlaufsrendite (current yield of listed Federal securities), %."""
    return latest_value("BBSIS", UMLAUFRENDITE_KEY)


def yield_10y() -> Tuple[str, float]:
    """Latest 10-year estimated Federal yield, in percent."""
    return latest_value("BBSIS", TERM_KEY.format(nn=10))


def yield_curve(maturities: Tuple[int, ...] = CURVE_MATURITIES
                ) -> Dict[int, float]:
    """Latest estimated yield (in percent) for each maturity that the API
    returns.  Maturities the API rejects are skipped silently."""
    curve: Dict[int, float] = {}
    for m in maturities:
        try:
            _, v = latest_value("BBSIS", TERM_KEY.format(nn=f"{m:02d}"))
            curve[m] = v
        except Exception:
            continue
    if not curve:
        raise RuntimeError("Bundesbank returned no curve points "
                           "(host unreachable or all keys rejected).")
    return curve


if __name__ == "__main__":  # pragma: no cover
    # Smoke test (needs network access to the Bundesbank host).
    try:
        d, v = yield_10y()
        print(f"German 10y estimated yield: {v:.3f}% (as of {d})")
        d, v = umlaufrendite()
        print(f"Umlaufsrendite:             {v:.3f}% (as of {d})")
        print("Curve:", yield_curve())
    except Exception as exc:
        print("Live retrieval failed (expected if offline):", exc)
