# Replicating the ECB's Derivation of Market Returns (Dividend Discount Model)

*Compiled from public sources as of June 2026. This report replicates the **methodology** the European Central Bank uses to derive the expected equity market return and equity risk premium; the numerical inputs are clearly-labelled, June-2026-vintage euro-area figures and are **illustrative**. They reproduce the derivation, not an official ECB estimate. Swap in live IBES / OIS / index data to refresh. A runnable implementation accompanies this report at [`../code/ecb_market_return.py`](../code/ecb_market_return.py).*

---

## Why this report

Reports 1–4 in this set treat the **market return** mostly through the lens of the **Dimson–Marsh–Staunton (DMS) historical record** — the backward-looking, survivor-bias-corrected average of realised returns since 1900 that anchors the Total Market Return (TMR) and equity risk premium (ERP) in UK and German regulatory CAPM determinations. The DMS approach answers the question *"what did equities actually deliver?"*

The **ECB** answers a different question — *"what return are investors today pricing in for the future?"* — and it does so with a **forward-looking, market-implied** method: a **multi-stage Dividend Discount Model (DDM)**. This is the other pole of the "historical vs. market-implied ERP" fault line flagged in Report 4. The US regulatory DCF (FERC, state PUCs) is a close cousin of the ECB DDM — both back the cost of equity out of current prices and expected cash-flow growth — so replicating the ECB derivation also illuminates the methodological alternative to the CAPM-RAB family that dominates European network regulation.

The ECB does not use the DDM to set a regulated return; it uses it for **financial-stability and monetary-policy analysis** — to monitor euro-area equity valuations, to decompose price moves into cash-flow, risk-free-rate and risk-premium components, and to gauge the compensation investors demand for holding equity. But the derivation is exactly the kind of forward-looking cross-check that regulators (Ofgem's "market-to-asset-ratio" and investability cross-checks; BNetzA's debates over historical vs. implied premia) increasingly place alongside the DMS history.

---

## 1. The ECB methodology, in words

The ECB's primary reference is the Economic Bulletin article **"Measuring and interpreting the cost of equity in the euro area"** (Issue 4/2018) [E1], operationalised in recurring boxes of the **Financial Stability Review** and **Economic Bulletin** (e.g. "Recent drivers of euro area equity prices", 2017 [E2]; the 2020, 2023, 2024 and 2025 equity-valuation boxes [E3][E4][E5]). The logic is the standard present-value identity:

> The current price of an equity index equals the present value of the cash flows (dividends, plus net share buybacks) that investors expect it to pay, discounted at the **required return on equity**. That required return — the rate that makes discounted expected cash flows equal the observed price — is the **implied cost of equity**, i.e. the **expected nominal equity market return**. Subtracting the long-term risk-free rate leaves the **equity risk premium**.

Four design choices define the ECB's implementation:

1. **Cash flows are expected *net payouts*, built from analyst forecasts.** Dividends (and, in the ECB's fuller version, **net share buybacks**) are projected from **IBES/Refinitiv consensus analyst forecasts** of earnings, combined with a payout ratio. The ECB's DDM "includes share buybacks, discounts future cash flows with interest rates of appropriate maturity and includes **three expected dividend growth horizons**" [E5].

2. **Three growth horizons.** Expected payout growth passes through three stages:
   - **Stage 1 — short term.** Growth follows IBES analyst forecasts (12-month-forward earnings and the I/B/E/S long-term growth forecast, a 3–5-year horizon).
   - **Stage 2 — transition.** Growth declines **linearly** from the short-term rate to the long-run rate over a medium-term window.
   - **Stage 3 — steady state.** Payouts grow in perpetuity at **long-run nominal GDP growth**, taken from the **ECB Survey of Professional Forecasters (SPF)** longer-term expectations (or Consensus Economics).

3. **The risk-free rate is the OIS curve.** The long-term risk-free rate is proxied by the **10-year overnight index swap (OIS) rate** (a near-default-free, near-credit-risk-free benchmark), rather than a specific sovereign bond, to avoid contaminating the premium with sovereign credit risk. In the fuller specification each horizon is discounted at the **maturity-matched OIS rate** plus a constant premium.

4. **The premium is the residual that fits the price.** Because the ERP "by its nature cannot be observed, it has to be estimated on the basis of a model" [E1]. The ECB notes that, rather than the H-model approximation, "a more demanding yet more precise approach is to find the implied equity risk premium that **minimises the difference between the model-implied equity price and the observed market price**" [E2] — i.e. solve for the premium (or the discount rate) that makes the model price the index exactly.

---

## 2. The equations

### 2.1 Present-value identity (three-stage DDM)

Normalise the index price to `P₀ = 1`, so the current dividend equals the **dividend yield**, `D₀ = d = D₀/P₀`. Let `gₜ` be the projected nominal payout growth in year *t*:

- Stage 1 (`t = 1 … N_s`): `gₜ = g_S` (IBES short-term growth)
- Stage 2 (`t = N_s+1 … N_s+N_τ`): `gₜ = g_S + (t − N_s)/N_τ · (g_L − g_S)` (linear taper)
- Stage 3 (`t > T`, where `T = N_s + N_τ`): constant `g_L` (long-run nominal GDP growth)

The price equation, discounted at the single implied cost of equity `r`, is:

```
        T                         D_T (1 + g_L)    1
P₀  =   Σ   D_t / (1 + r)^t   +   ─────────────  · ───────
       t=1                          (r − g_L)      (1+r)^T
```

with `D_t = D_{t−1}(1 + g_t)`. The second term is the **Gordon terminal value** of the steady-state perpetuity. We solve this for **`r` = the expected nominal equity market return (implied cost of equity)**, then:

```
ERP  =  r  −  rf            (rf = 10-year OIS)
```

### 2.2 The closed-form Fuller–Hsia H-model (cross-check)

The ECB notes the **H-model** (Fuller & Hsia, 1984) as a simplified closed form of the multi-stage model in which growth declines linearly from `g_S` to `g_L` over `2H` years. It yields the implied return directly, with no root-finding:

```
r  =  (D₀/P₀) · [ (1 + g_L)  +  H · (g_S − g_L) ]  +  g_L
```

where **H = half the length of the above-trend growth window**. This is a useful analytical anchor and a check on the numerical solver.

### 2.3 ECB term-structure refinement

The ECB's preferred specification discounts each horizon at the **maturity-matched OIS rate** `rf_t` plus a **constant** ERP, and solves for that ERP:

```
        T     D_t                     D_T (1 + g_L)            1
P₀  =   Σ   ───────────────   +   ──────────────────────  · ──────────────────
       t=1   (1 + rf_t + ERP)^t      (rf_T + ERP − g_L)       (1 + rf_T + ERP)^T
```

With a flat OIS curve this collapses to §2.1 with `r = rf + ERP`. The implementation supports an arbitrary OIS term structure.

---

## 3. Inputs used (euro area, illustrative June-2026 vintage)

| Parameter | Symbol | Value | Source / rationale |
|---|---|---|---|
| Dividend (net payout) yield | `D₀/P₀` | **3.2%** | Broad euro-area aggregate. EURO STOXX 50 forward div. yield ≈3.5%; STOXX Europe 600 trailing ≈2.5% [M1][M2]. Net-payout (incl. buybacks) variant adds ≈1.0pp. |
| Stage-1 growth (short term) | `g_S` | **8.0%** | IBES consensus near-term euro-area EPS growth (~+8% for 2026) [M3]. |
| Stage-3 growth (steady state) | `g_L` | **3.3%** | Long-run **nominal** GDP = 1.3% real (ECB SPF longer-term, 2030) + 2.0% inflation target [M4]. |
| Risk-free rate | `rf` | **2.6%** | 10-year euro OIS, mid-2026 (euro 10y AAA spot ≈2.9% end-2025; OIS sits a touch below) [M5]. |
| Stage-1 length | `N_s` | **5 yrs** | IBES forecast horizon. |
| Transition length | `N_τ` | **10 yrs** | Linear taper to steady state. |
| H-model H | `H` | **10.0** | `N_s + N_τ/2` (above-trend window of the explicit model). |

These are deliberately transparent, reproducible figures. They are **not** an ECB estimate; they reproduce the ECB's *derivation* with publicly-available current inputs.

---

## 4. Results of the replication

Running [`code/ecb_market_return.py`](../code/ecb_market_return.py):

| Method | Implied market return `r` | Equity risk premium `r − rf` |
|---|---|---|
| **(A) Three-stage DDM** (single `r`) | **8.01%** | **5.41%** |
| **(B) Fuller–Hsia H-model** (closed form, H=10) | 8.11% | 5.51% |
| **(C) ECB term-structure form** (flat OIS, solve for ERP) | 8.01% | 5.41% |
| Net-payout variant (div. + ~1.0pp buybacks) | 9.38% | 6.78% |

The three formulations agree to within ~10 bps (the H-model is a linear approximation, so a small gap is expected), and the term-structure form on a flat OIS curve reproduces the single-`r` solution exactly — an internal consistency check that the implementation is correct.

**Interpretation.** On these illustrative June-2026 inputs the euro-area equity market is pricing an expected **nominal return of ~8%** and an **equity risk premium of ~5.4%** over the 10-year OIS rate — rising to ~6.8% once net buybacks are added to the payout stream. A mid-single-digit ERP is consistent with the ECB's published characterisation that euro-area equity risk premia have been **elevated** in recent years, and with valuations the ECB's May 2026 FSR still describes as "stretched" [E6].

### 4.1 Sensitivity of the implied ERP

The implied premium is, as expected, increasing in the dividend yield (a cheaper market ⇒ higher implied return) and in the assumed near-term growth, and decreasing in the risk-free rate. The three-stage solver gives (rf = 2.6%):

| `g_S` ＼ `D₀/P₀` | 2.6% | 2.9% | 3.2% | 3.5% | 3.8% |
|---|---|---|---|---|---|
| **6%** | 4.03 | 4.40 | 4.77 | 5.14 | 5.51 |
| **7%** | 4.29 | 4.69 | 5.09 | 5.48 | 5.87 |
| **8%** | 4.57 | 4.99 | **5.41** | 5.83 | 6.24 |
| **9%** | 4.86 | 5.31 | 5.76 | 6.19 | 6.63 |
| **10%** | 5.17 | 5.64 | 6.11 | 6.58 | 7.03 |

*(ERP in %. Centre cell = base case.)* The plausible euro-area ERP spans roughly **4–7%** across this input grid — a reminder that the DDM result is only as firm as its growth and payout assumptions, the central critique of market-implied premia.

---

## 5. How the ECB derivation differs from the DMS approach (link to Report 1)

| | **DMS historical** (Report 1) | **ECB DDM** (this report) |
|---|---|---|
| Question | What *did* equities return? | What return are investors *pricing in*? |
| Direction | Backward-looking (1900–) | Forward-looking |
| Core data | 125 years of realised returns, 35 markets | Today's index price + IBES forecasts + SPF growth |
| ERP output | ~3–4.6% world, stable, slow-moving | ~4–7% euro area, time-varying with prices/yields |
| Anchored by | Long-run averages, survivor-bias-corrected | Current valuations and analyst expectations |
| Main weakness | Past need not predict future; regime change | Sensitive to growth/payout assumptions; analyst optimism bias |
| Regulatory use | TMR/ERP anchor (Ofgem, BNetzA) | Cross-check; closest to US DCF (FERC, PUCs) |

The two are complements, not substitutes. Regulators that anchor on DMS history (UK, Germany) increasingly use DDM-style implied-return estimates as a **cross-check** that the allowed return is not wildly out of line with what the market is actually pricing — the same logic that drives the US DCF approach. Replicating the ECB derivation makes the mechanics of that cross-check explicit and auditable.

---

## 5a. Interactive calculator (upload your own estimates)

For working with live, multi-security data rather than the single euro-area
aggregate above, the repo includes a **Streamlit app** —
[`../code/app.py`](../code/app.py). It lets you:

- **upload a CSV** of per-share analyst estimates and prices (dividend yield or
  dividend, near-term growth, optional terminal growth, buybacks, and weights);
- **supply the risk-free rate** three ways — pulled **live from the Deutsche
  Bundesbank SDMX API** (the German 10-year yield, the *Umlaufsrendite* that
  BNetzA itself averages, or a full term-structure curve), uploaded as a CSV, or
  typed in;
- **choose the market-return weighting** (an index-weight/market-cap column or
  equal weight); and
- compute **all five methodological variants** (Gordon, two-stage, three-stage,
  H-model, term-structure) for **each share** and then **weight-aggregate** to a
  market return and ERP, with a downloadable results table.

The DDM math is the shared engine in [`../code/ddm_engine.py`](../code/ddm_engine.py)
(the same module this report's standalone replication uses). Run it with
`pip install -r code/requirements.txt && streamlit run code/app.py`; see
[`../code/README.md`](../code/README.md) for the input schema and the Bundesbank
series keys.

---

## 6. Caveats and how to refresh

- **Illustrative inputs.** The headline ~8% return / ~5.4% ERP depend on the four inputs in §3. For a live estimate, replace the dividend/payout yield, IBES short-term growth, SPF long-run growth and the OIS curve with current data and re-run the script. The sensitivity grid (§4.1) shows the swing.
- **Buybacks matter.** Euro-area net buyback yields are smaller than in the US but non-trivial; the ECB's fuller DDM includes them, and the net-payout variant lifts the implied return by ~1.3pp.
- **Single `r` vs. term structure.** The headline uses a single discount rate; the ECB's preferred form discounts each horizon on the OIS curve plus a constant ERP. The script implements both; on a flat curve they coincide.
- **Analyst-optimism bias.** IBES growth forecasts are known to be upward-biased at long horizons; this inflates the implied ERP. The ECB mitigates this by tapering quickly to GDP-anchored long-run growth — exactly the role of Stage 2/3 here.
- **Not a regulated return.** This is a financial-stability/monetary-analysis construct, not an allowed WACC. Do not read the ~8% as a determination input without the adjustments (beta, gearing, taxes, real/nominal conversion) that a CAPM-RAB framework requires.

---

## Sources

**ECB methodology**

[E1] ECB, *Measuring and interpreting the cost of equity in the euro area*, Economic Bulletin Issue 4/2018, Article 2 — https://www.ecb.europa.eu/press/economic-bulletin/articles/2018/html/ecb.ebart201804_02.en.html
[E2] ECB, *Recent drivers of euro area equity prices*, Economic Bulletin box (2017) — https://www.ecb.europa.eu/pub/pdf/other/ebbox201705_02.en.pdf
[E3] ECB, *Euro area equity markets and shifting expectations for an economic recovery*, Economic Bulletin box, Issue 5/2020 — https://www.ecb.europa.eu/press/economic-bulletin/focus/2020/html/ecb.ebbox202005_04~1b3e9fcb8f.en.html
[E4] ECB, *Euro area bank fundamentals, valuations and cost of equity*, Financial Stability Review box (Nov 2023) — https://ecb.europa.eu/pub/financial-stability/fsr/focus/2023/html/ecb.fsrbox202311_05~519e436375.en.html
[E5] ECB, *What's behind the resilience of US equity prices — market structure, earnings expectations or equity risk premia?*, Economic Bulletin box (2024/25) — https://www.ecb.europa.eu/press/economic-bulletin/focus/2025/html/ecb.ebbox202408_01~d2c7bd5eba.en.html
[E6] ECB, *Financial Stability Review, May 2026* — https://www.ecb.europa.eu/press/financial-stability-publications/fsr/html/ecb.fsr202605~50566915a7.en.html

**Method corroboration (DDM / H-model / ERP)**

[B1] J. Gálvez, *Measuring the equity risk premium with dividend discount models*, Banco de España Occasional Paper 2207 (2022) — https://www.bde.es/f/webbde/SES/Secciones/Publicaciones/PublicacionesSeriadas/DocumentosOcasionales/22/Files/do2207e.pdf
[B2] W. Lemke & T. Werner, *The term structure of equity premia*, ECB Working Paper 1045 — https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp1045.pdf
[B3] R. J. Fuller & C. Hsia, *A simplified common stock valuation model* (the "H-model"), Financial Analysts Journal, 1984.
[B4] ECB, *Euro area equity risk premia and monetary policy*, Working Paper 2535 — https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp2535~a236a0a5fe.en.pdf

**Inputs (illustrative, June-2026 vintage)**

[M1] iShares EURO STOXX 50 UCITS ETF — forward dividend yield ≈3.5% (Jun 2026) — https://www.digrin.com/stocks/detail/EUEA.AS/
[M2] iShares STOXX Europe 600 UCITS ETF — trailing distribution yield ≈2.5% (Jun 2026) — https://www.ishares.com/ch/individual/en/products/251931/ishares-stoxx-europe-600-ucits-etf-de-fund
[M3] IBES/Refinitiv consensus — euro-area 2026 EPS growth ≈+8% (per Investing.com summary) — https://au.investing.com/news/stock-market-news/are-eurozone-earnings-expectations-really-too-high-4370890
[M4] ECB, *Survey of Professional Forecasters*, Q2 2026 — longer-term (2030) real GDP growth 1.3% — https://www.ecb.europa.eu/stats/ecb_surveys/survey_of_professional_forecasters/html/ecb.spf2026q2.en.html
[M5] ECB Data Portal, *AAA-rated euro area government bond yield curve — 10-year spot* (≈2.9% end-2025; OIS marginally lower) — https://data.ecb.europa.eu/data/datasets/YC/YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_10Y
