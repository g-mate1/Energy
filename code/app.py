"""
app.py — Streamlit app: implied cost of equity / equity risk premium from
analyst estimates and share prices, across the methodological DDM variants.

Run:
    pip install -r requirements.txt
    streamlit run app.py

What it does
------------
1. Upload a CSV of per-share analyst estimates and prices (one row per share).
2. Supply the risk-free rate by either:
     - retrieving German government-bond yields LIVE from the Bundesbank API
       (10-year, the Umlaufsrendite, or a full term-structure curve), or
     - uploading a CSV of (maturity, yield), or
     - typing a single value.
3. Choose the market-return weighting (column weights, market cap, or equal).
4. The app computes, for every share, the implied return under each variant —
   Gordon, two-stage, three-stage (ECB primary), Fuller-Hsia H-model, and the
   ECB term-structure form — then weight-aggregates to a MARKET return and ERP.
5. Download the per-share and market results as CSV.

The DDM math lives in ddm_engine.py; the Bundesbank client in bundesbank.py.
See reports/05_ecb_market_return_ddm.md for the methodology.
"""

from __future__ import annotations

from typing import Callable, Dict, List, Optional

import pandas as pd
import streamlit as st

import ddm_engine as E
import bundesbank as BBK

st.set_page_config(page_title="DDM market-return calculator", layout="wide")

# Column aliases accepted in the uploaded estimates file.
ALIASES = {
    "name": ["name", "ticker", "company", "security", "isin"],
    "price": ["price", "p0", "share_price", "px"],
    "dividend": ["dividend", "d0", "dps", "dividend_per_share"],
    "dividend_yield": ["dividend_yield", "div_yield", "dy", "yield"],
    "g_short": ["g_short", "growth_short", "ltg", "eps_growth", "ibes_growth",
                "short_term_growth", "g1"],
    "g_long": ["g_long", "growth_long", "terminal_growth", "g2", "gdp_growth"],
    "buyback_yield": ["buyback_yield", "buyback", "net_buyback", "buyback_yld"],
    "weight": ["weight", "index_weight", "w"],
    "market_cap": ["market_cap", "mcap", "marketcap", "cap"],
}


def _match(colnames: List[str], options: List[str]) -> Optional[str]:
    low = {c.lower().strip(): c for c in colnames}
    for o in options:
        if o in low:
            return low[o]
    return None


def map_columns(df: pd.DataFrame) -> Dict[str, Optional[str]]:
    return {field: _match(list(df.columns), opts) for field, opts in ALIASES.items()}


def build_securities(df: pd.DataFrame, m: Dict[str, Optional[str]],
                     default_g_long: float, rate_factor: float) -> List[E.Security]:
    """rate_factor scales rate inputs to decimals (0.01 if the file is in
    percent, 1.0 if already in decimal fractions)."""
    secs: List[E.Security] = []
    for i, row in df.iterrows():
        def g(field, default=None):
            col = m.get(field)
            if col is None or pd.isna(row.get(col)):
                return default
            return row[col]

        def rate(field, default=None):
            v = g(field, default)
            return None if v is None else float(v) * rate_factor

        name = g("name", default=f"row{i+1}")
        price = float(g("price")) if g("price") is not None else None
        dividend = float(g("dividend")) if g("dividend") is not None else None
        dy = rate("dividend_yield")
        gs = rate("g_short")
        gl = rate("g_long")
        gl = default_g_long if gl is None else gl
        bb = rate("buyback_yield", 0.0) or 0.0
        weight = g("weight")
        mcap = g("market_cap")
        secs.append(E.Security(
            name=str(name), price=price, g_short=gs, g_long=gl,
            dividend=dividend, dividend_yield=dy, buyback_yield=bb,
            weight=float(weight) if weight is not None else None,
            market_cap=float(mcap) if mcap is not None else None,
        ))
    return secs


def make_curve(points: Dict[int, float]) -> Callable[[int], float]:
    """Linear-interpolating, flat-extrapolating discount curve (rates in
    decimals) from a {maturity_years: rate} dict."""
    ms = sorted(points)

    def curve(t: int) -> float:
        if t <= ms[0]:
            return points[ms[0]]
        if t >= ms[-1]:
            return points[ms[-1]]
        for a, b in zip(ms, ms[1:]):
            if a <= t <= b:
                w = (t - a) / (b - a)
                return points[a] + w * (points[b] - points[a])
        return points[ms[-1]]

    return curve


# --------------------------------------------------------------------------- #
#  Sidebar — global parameters                                                #
# --------------------------------------------------------------------------- #

st.title("Implied market return & equity risk premium — DDM variants")
st.caption("Back the cost of equity out of prices + analyst estimates, the way "
           "the ECB does. Methodology: reports/05_ecb_market_return_ddm.md")

with st.sidebar:
    st.header("Input units")
    unit = st.radio("Rate inputs are in",
                    ["Percent (3.2 = 3.2%)", "Decimal (0.032)"],
                    help="Applies to all yields and growth rates in your CSVs.")
    rate_factor = 0.01 if unit.startswith("Percent") else 1.0

    st.header("Model parameters")
    n_short = st.number_input("Stage-1 (short-term) length, years", 1, 20, 5)
    n_transition = st.number_input("Stage-2 (transition) length, years", 0, 30, 10)
    include_bb = st.checkbox("Include buybacks in net payout yield", value=True)
    custom_H = st.checkbox("Override H-model H", value=False)
    H = st.number_input("H (half the above-trend window)", 0.5, 30.0,
                        float(n_short + n_transition / 2.0)) if custom_H else None

    st.header("Default long-run growth")
    st.caption("Used when a share has no g_long. Nominal GDP = real + inflation.")
    real_g = st.number_input("Long-run REAL GDP growth, %", 0.0, 10.0, 1.3) / 100
    infl = st.number_input("Long-run inflation, %", 0.0, 10.0, 2.0) / 100
    default_g_long = (1 + real_g) * (1 + infl) - 1
    st.write(f"→ default nominal g_long = **{100*default_g_long:.2f}%**")

params = E.Params(n_short=int(n_short), n_transition=int(n_transition),
                  include_buybacks=include_bb, H=H)

# --------------------------------------------------------------------------- #
#  1. Estimates upload                                                         #
# --------------------------------------------------------------------------- #

st.header("1 · Analyst estimates & share prices")
st.caption("CSV, one row per share. Recognised columns (aliases ok): name, "
           "price, dividend or dividend_yield, g_short, [g_long], "
           "[buyback_yield], [weight] or [market_cap]. Yields/growth may be "
           "entered as 3.2 or 0.032.")
up = st.file_uploader("Upload estimates CSV", type=["csv"], key="est")

if up is None:
    st.info("Upload a CSV to begin. A sample is provided at "
            "`sample_data/analyst_estimates.csv`.")
    st.stop()

df = pd.read_csv(up)
m = map_columns(df)
missing = [f for f in ("name", "price", "g_short") if m[f] is None]
if m["dividend"] is None and m["dividend_yield"] is None:
    missing.append("dividend or dividend_yield")
if missing:
    st.error(f"Missing required column(s): {', '.join(missing)}. "
             f"Detected columns: {list(df.columns)}")
    st.stop()

st.dataframe(df, use_container_width=True)
secs = build_securities(df, m, default_g_long, rate_factor)

# --------------------------------------------------------------------------- #
#  2. Risk-free rate                                                          #
# --------------------------------------------------------------------------- #

st.header("2 · Risk-free rate / discount curve")
mode = st.radio("Source", ["Bundesbank API (live)", "Upload CSV", "Single value"],
                horizontal=True)

curve_points: Dict[int, float] = {}
rf_10y: Optional[float] = None

if mode == "Bundesbank API (live)":
    series = st.selectbox(
        "Series",
        ["10-year estimated yield", "Umlaufsrendite (current yield)",
         "Full term-structure curve"])
    if st.button("Fetch from Bundesbank"):
        try:
            if series == "Full term-structure curve":
                raw = BBK.yield_curve()
                curve_points = {k: v / 100.0 for k, v in raw.items()}
                rf_10y = curve_points.get(10, list(curve_points.values())[-1])
                st.success(f"Fetched {len(curve_points)} curve points.")
                st.write({f"{k}y": f"{100*v:.3f}%" for k, v in curve_points.items()})
            elif series == "Umlaufsrendite (current yield)":
                d, v = BBK.umlaufrendite()
                rf_10y = v / 100.0
                st.success(f"Umlaufsrendite {v:.3f}% (as of {d})")
            else:
                d, v = BBK.yield_10y()
                rf_10y = v / 100.0
                st.success(f"German 10y {v:.3f}% (as of {d})")
            st.session_state["rf_10y"] = rf_10y
            st.session_state["curve_points"] = curve_points
        except Exception as exc:
            st.error(f"Bundesbank retrieval failed: {exc}\n\n"
                     "Use 'Upload CSV' or 'Single value' instead.")
    rf_10y = st.session_state.get("rf_10y", rf_10y)
    curve_points = st.session_state.get("curve_points", curve_points)

elif mode == "Upload CSV":
    st.caption("CSV with columns: maturity (years), yield (% or fraction).")
    rf_up = st.file_uploader("Upload risk-free CSV", type=["csv"], key="rf")
    if rf_up is not None:
        rdf = pd.read_csv(rf_up)
        rdf.columns = [c.lower().strip() for c in rdf.columns]
        mcol = _match(list(rdf.columns), ["maturity", "tenor", "years", "m"])
        ycol = _match(list(rdf.columns), ["yield", "rate", "value", "y"])
        if mcol and ycol:
            curve_points = {int(r[mcol]): float(r[ycol]) * rate_factor
                            for _, r in rdf.iterrows()}
            rf_10y = make_curve(curve_points)(10)
            st.success(f"Loaded {len(curve_points)} curve points; "
                       f"10y ≈ {100*rf_10y:.3f}%")
        else:
            st.error("Need 'maturity' and 'yield' columns.")

else:  # Single value
    v = st.number_input("Risk-free rate (10y), %", 0.0, 15.0, 2.6)
    rf_10y = v / 100.0

if rf_10y is None:
    st.warning("Set a risk-free rate to compute the ERP and the term-structure "
               "variant.")

ois_curve = make_curve(curve_points) if curve_points else (
    (lambda t: rf_10y) if rf_10y is not None else None)

# --------------------------------------------------------------------------- #
#  3. Weighting                                                                #
# --------------------------------------------------------------------------- #

st.header("3 · Market-return weights")
scheme = st.radio("Weighting scheme",
                  ["As provided (weight/market_cap column)", "Market cap", "Equal"],
                  horizontal=True)
if scheme == "Equal":
    for s in secs:
        s.weight, s.market_cap = None, None
        s.weight = 1.0
elif scheme == "Market cap":
    for s in secs:
        s.weight = None  # force market_cap path (falls back to equal if absent)

# --------------------------------------------------------------------------- #
#  4. Compute                                                                  #
# --------------------------------------------------------------------------- #

st.header("4 · Results")

res = E.aggregate_market(secs, params, ois_curve=ois_curve, rf_10y=rf_10y)
weights = res["weights"]

variant_cols = ["gordon", "two_stage", "three_stage", "h_model"]
if ois_curve is not None and "term_structure" in res["per_security"][0]:
    variant_cols.append("term_structure")
labels = {"gordon": "Gordon (1-stage)", "two_stage": "Two-stage",
          "three_stage": "Three-stage (ECB)", "h_model": "H-model",
          "term_structure": "Term-structure"}

# Per-security table
rows = []
for s, w, pr in zip(secs, weights, res["per_security"]):
    row = {"security": s.name, "weight": w,
           "net_payout_yield": pr["net_payout_yield"]}
    for c in variant_cols:
        row[labels[c] + " r"] = pr.get(c)
        if rf_10y is not None:
            row[labels[c] + " ERP"] = pr.get(c + "_erp")
    rows.append(row)
per_df = pd.DataFrame(rows)

def _fmt_pct(df_in: pd.DataFrame) -> pd.DataFrame:
    out = df_in.copy()
    for c in out.columns:
        if c == "security":
            continue
        out[c] = out[c].map(lambda x: f"{100*x:.2f}%" if pd.notna(x) else "—")
    return out

st.subheader("Per-security implied returns")
st.dataframe(_fmt_pct(per_df), use_container_width=True)

# Market aggregate
st.subheader("Weighted market aggregate")
mk = res["market"]
cards = st.columns(len(variant_cols))
for col, c in zip(cards, variant_cols):
    r = mk.get(c)
    erp = mk.get(c + "_erp")
    col.metric(labels[c] + " — market return",
               f"{100*r:.2f}%" if r == r else "—",
               (f"ERP {100*erp:.2f}%" if erp is not None and erp == erp else None))

market_row = {"security": "MARKET (weighted)", "weight": 1.0,
              "net_payout_yield": mk.get("net_payout_yield")}
for c in variant_cols:
    market_row[labels[c] + " r"] = mk.get(c)
    if rf_10y is not None:
        market_row[labels[c] + " ERP"] = mk.get(c + "_erp")
full_df = pd.concat([per_df, pd.DataFrame([market_row])], ignore_index=True)

# Downloads
st.download_button("Download results CSV",
                   full_df.to_csv(index=False).encode(),
                   file_name="ddm_results.csv", mime="text/csv")

with st.expander("Notes & caveats"):
    st.markdown(
        "- **Gordon** uses the single perpetual growth `g_long`; **two-stage** "
        "applies `g_short` for the short window then steps to `g_long`; "
        "**three-stage** adds a linear transition (ECB primary); **H-model** is "
        "the Fuller–Hsia closed form; **term-structure** discounts each horizon "
        "at the curve rate + a constant ERP (needs a curve / rf).\n"
        "- A blank cell (—) means no real root exists for that share/variant "
        "(typically `r ≤ g_long`, i.e. assumed growth ≥ implied return).\n"
        "- ERP = implied return − 10y risk-free. Market figures are "
        "weight-averaged across shares.\n"
        "- Yields/growth entered as values > 1 are read as percentages."
    )
