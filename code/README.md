# DDM market-return calculator (code)

Tools that back the **implied cost of equity** (expected nominal market return)
and the **equity risk premium (ERP)** out of share prices and analyst estimates,
across the methodological DDM variants the ECB uses. Methodology write-up:
[`../reports/05_ecb_market_return_ddm.md`](../reports/05_ecb_market_return_ddm.md).

## Files

| File | What it is |
|---|---|
| `ddm_engine.py` | Canonical, dependency-free DDM engine: the five variants + weighted market aggregation. Single source of truth. |
| `ecb_market_return.py` | Standalone, single-aggregate replication of the ECB euro-area derivation (prints results + a sensitivity grid). Imports `ddm_engine`. |
| `app.py` | **Streamlit app**: upload estimates, pull/upload the risk-free rate, choose weights, compute every variant per share and for the weighted market. |
| `bundesbank.py` | Client for the Deutsche Bundesbank SDMX REST API (German government-bond yields / Umlaufsrendite / full curve). |
| `sample_data/` | `analyst_estimates.csv` (the European energy-network peer group) and `risk_free.csv` (a German curve). |
| `requirements.txt` | `streamlit`, `pandas`, `requests`. |

## Run

```bash
pip install -r requirements.txt

# the interactive app
streamlit run app.py

# or the standalone single-aggregate replication
python3 ecb_market_return.py
```

## The methodological variants

For each security the app solves for the implied return `r` (and `ERP = r − rf`,
`rf` = 10-year risk-free) under:

1. **Gordon (one-stage)** — `r = D1/P0 + g_long`.
2. **Two-stage** — `g_short` for the short window, then a step to `g_long` perpetuity.
3. **Three-stage (ECB primary)** — `g_short`, a **linear transition**, then `g_long`; solved numerically for `r`.
4. **Fuller–Hsia H-model** — closed form, growth declining linearly over `2H` years.
5. **Term-structure** — discount each horizon at the curve rate + a **constant ERP**; solve for the ERP (needs a curve / `rf`).

The per-security results are then **weight-aggregated** to a market return and ERP
(weights from a `weight` column, `market_cap`, or equal-weight).

## Input CSV — analyst estimates

One row per share. Column names are matched flexibly (aliases in parentheses):

| Column | Required | Notes |
|---|---|---|
| `name` (`ticker`, `company`, `isin`) | yes | Label. |
| `price` (`p0`, `share_price`) | yes | Current share price `P0`. |
| `dividend` (`d0`, `dps`) **or** `dividend_yield` (`dy`) | yes (one) | `dividend_yield = D0/P0`. |
| `g_short` (`ltg`, `eps_growth`, `g1`) | yes | Near-term (IBES) growth. |
| `g_long` (`terminal_growth`, `g2`) | no | Per-share terminal growth; else the sidebar default (nominal GDP). |
| `buyback_yield` (`buyback`) | no | Net buyback yield, added to the dividend yield. |
| `weight` **or** `market_cap` | no | Market-return weight; else equal-weight. |

**Units:** set the sidebar toggle. By default all rates are read as **percent**
(`3.2` = 3.2%); switch to decimal if your file uses `0.032`. Prices and market
caps are taken as-is. See `sample_data/analyst_estimates.csv`.

## Risk-free rate

Three options in the app:

- **Bundesbank API (live)** — pulls the German **10-year estimated yield**, the
  **Umlaufsrendite** (the series BNetzA itself averages), or a **full
  term-structure curve**. Requires outbound access to
  `api.statistiken.bundesbank.de` (works from a normal machine; may be blocked in
  locked-down CI). `python3 bundesbank.py` is a quick connectivity smoke test.
- **Upload CSV** — columns `maturity` (years) and `yield`.
- **Single value** — one 10-year rate.

A multi-point curve enables the term-structure variant with maturity-matched
discounting; a single rate uses a flat curve.

## Notes

- A blank result cell means no real root exists for that share/variant
  (typically `r ≤ g_long`, i.e. the assumed growth meets or exceeds the implied
  return) — a feature, not a crash.
- These are analytical tools for research, not a regulated-return determination.
  Implied returns still need beta/gearing/tax/real-nominal adjustments before
  they map to a CAPM-RAB allowed WACC.
