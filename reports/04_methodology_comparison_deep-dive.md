# Comparison of Regulatory Cost-of-Capital Methodologies: EU, US, UK and Asia — Deep Dive

*This deep-dive expands the summary report (`04_methodology_comparison.md`) region by region and adds an annotated comparative-literature review. Compiled from public sources as of June 2026. Regulatory frameworks change frequently and many parameters reset annually or mid-period; all figures should be checked against the current primary determinations before use, and are labelled by vintage and by basis (real/nominal, pre-/post-tax) where material. The research sub-agents that compiled this material were largely unable to open primary PDFs directly (automated fetching was blocked across regulator domains); figures rest on cross-verified search extracts of those primary sources, with load-bearing items flagged where they could not be confirmed verbatim.*

---

## Executive summary

Across the world, every monopoly network regulator answers the same question — what return should investors earn on sunk, price-controlled assets? — but they answer it through two distinct intellectual traditions:

- A **CAPM + indexed-RAB** tradition (the UK, most of continental Europe, Australia, New Zealand): build the cost of equity *top-down* from CAPM components, anchor the Total Market Return (TMR) and equity risk premium on long-run history (the DMS dataset), apply the result to an **inflation-indexed** Regulated Asset Base using a **notional** capital structure, and reset on a **fixed multi-year cycle**.
- A **DCF + original-cost rate-of-return** tradition (the United States): infer the cost of equity *bottom-up* from market prices and expected dividend growth (DCF, supplemented by CAPM), apply it to an **original (historical) cost** rate base using the utility's **actual** capital structure, in **episodic** rate cases under the open-ended *Hope/Bluefield* "end-result" standard.

The deepest fault line is therefore **CAPM-RAB vs DCF-rate-of-return**. Around it run three more: **real vs nominal** returns (and whether the asset base is inflation-indexed); **historical (DMS) vs market-implied** equity premia; and **rules vs discretion** (Australia's binding instrument and New Zealand's Input Methodologies at one pole; the US "battle of the models" and Germany's post-C-718/18 discretion at the other). The headline allowed returns can converge despite the philosophical gulf — a US allowed ROE of ~9.7% nominal on ~50% equity is, once inflation and gearing are normalised, not far from a European ~5–6% real cost of equity — but the *machinery* and the *contestability* differ profoundly.

This deep-dive treats the UK, EU/continental Europe, the US and the Asia-Pacific in turn, then draws the synthesis together with an expanded comparison table and an annotated review of the comparative literature (CEER/ACER, NERA, Frontier, Oxera, CEPA/KPMG, Brattle, the UKRN study, the Dobbs "aiming-up" foundations, the AER international review, and the IEA Cost of Capital Observatory).

---

## 1. United Kingdom — Ofgem, Ofwat and the CMA

The UK pioneered the modern incentive-based, RAB-anchored price control and remains the reference case for the CAPM-RAB family. Allowed revenue is built up from: a **return on capital** (allowed WACC × RAB), a **return *of* capital** (regulatory depreciation), operating costs, and incentive adjustments. Ofgem and Ofwat now **index the RAB to CPIH** (having migrated off RPI), so inflation compensation is delivered through asset-base indexation and the allowed return is quoted in **CPIH-real** terms.

### 1.1 The TMR-based method and the UKRN doctrine

The defining UK methodological choice is to estimate the **Total Market Return directly from long-run history** (which is comparatively stable across mature markets) and then derive the **ERP as a balancing figure** against the prevailing risk-free rate — the "TMR-based" rather than "ERP-based" approach. This rests on the **UKRN study (Wright, Burns, Mason & Pickford, 2018)**, which found "greater evidence of stability in the real market return than in the excess return," recommended CAPM for both cost of debt and equity, and supported a TMR of roughly **6–7% CPIH-real (≈5–6% RPI-real)**. The **UKRN Cost of Capital guidance (22 March 2023)** — which Ofgem, Ofwat, Ofcom, the CAA, ORR and the Utility Regulator must "have regard to" — codified the cross-sector consistency, naming the DMS dataset as "a useful starting point" for historical averages and endorsing CAPM as the primary model with cross-checks.

### 1.2 Ofgem (RIIO)

Ofgem uses DMS as its **primary** TMR source, cross-checked against forward-looking models (a dividend-discount/DDM-style estimate, investment-manager forecasts, market-to-asset ratios, OFTO bid-implied returns).

- **RIIO-2 / RIIO-ED2 (2021–2026 / 2023–2028):** TMR **6.25–6.75% CPIH-real** (midpoint 6.5%); allowed CPIH-real cost of equity **4.55%** (RIIO-2, at 60% gearing) and **5.23%** (RIIO-ED2). Two controversies defined RIIO-2: a **three-step equity methodology** (a CAPM range; six cross-checks pulling it down; and a ~**25 bps "outperformance wedge"** deducted on the theory that companies would systematically beat their allowance), and cost-of-debt set by a lengthening trailing average of the **iBoxx GBP Utilities 10yr+** index (~10→14-year "trombone" window).
- **RIIO-3 (Final Determinations 4 December 2025; 1 April 2026 – 31 March 2031):** Ofgem **raised the TMR**, assigning **equal weight to ex-ante and ex-post** estimates: an ex-ante lower bound of **6.8%** and an ex-post upper bound of **6.9%**, adopting **6.9% CPIH-real as the midpoint** (a refinement on the SSMD's 6.5–7% range). It set the allowed CPIH-real cost of equity at **5.70% for electricity transmission (gearing cut to 55%)** and **6.12% for the gas networks (60%)**, with a sector unweighted-average WACC of ~**5.62%**, citing the **UBS** (no longer Credit Suisse) Global Investment Returns Yearbook 2025. Critically, Ofgem **dropped the outperformance wedge** (following the CMA, below) and introduced a **"semi-nominal" cost-of-debt allowance** (~30% real for gas, ~10% for ET), so the headline RIIO-3 WACC is **not directly comparable** to RIIO-2's fully-real ~2.81% — much of the apparent jump reflects higher rates plus this change of convention. Ofgem also expressly **declined to follow the CMA's PR24 "stable ERP" approach**, reaffirming the TMR-based framing.

### 1.3 Ofwat (PR24) and the CMA

- **Ofwat PR24 (Final Determinations 19 December 2024; 2025–2030):** a fixed, DMS-anchored TMR of **6.00–6.92% CPIH-real**, with an ex-post midpoint near **6.92%** (arithmetic average on overlapping 10- and 20-year samples, 2022 back-cast CPIH series), and the ERP inferred as a balancing item. CEPA's advice used DMS data with the Blume and JKM estimators. Ofwat set the allowed CPIH-real cost of equity at **5.10%** — above the mechanical CAPM midpoint (~4.83%), a form of **"aiming up"** (a ~27 bps benchmark-index adjustment) — at 55% notional gearing, with an appointee WACC of **4.03%**.
- **The CMA on appeal.** In the **PR19 redeterminations (March 2021)** the CMA estimated the TMR from the same DMS dataset using **arithmetic, Blume and JKM** estimators, landing at ~**6.95% CPIH-real (≈5.85% RPI-real**, the same history on a different deflator with a ~0.9-point wedge), and **explicitly aimed up ~25 bps** on the cost of equity, citing the asymmetric consumer-welfare cost of under-investment. In the **RIIO-2 energy appeals (October 2021)** the CMA **upheld Ofgem's 4.55% cost of equity but removed the outperformance wedge**, while declining to *require* Ofgem to aim up — the now-defining asymmetry of UK appellate practice (aim up where it redetermines, defer where it reviews).

---

## 2. EU / Continental Europe

Continental regulators overwhelmingly use **CAPM within a WACC**, but diverge on real-vs-nominal convention and on how the risk-free rate is averaged. **CEER's** annual *Report on Regulatory Frameworks for European Energy Networks* (2025 edition, 22 January 2026; ~29 members + Northern Ireland + 5 Energy Community members) finds WACC the dominant construct, CAPM near-universal for the cost of equity, the risk-free rate set on government-bond yields "with only marginal differences across systems," and a **nominal pre-tax WACC** most popular for electricity (real pre-tax also frequent for gas). **ACER's** investment-risk report (June 2023) and electricity-tariff-practices report (March 2025) corroborate CAPM's dominance and catalogue how the allowed revenue is translated into tariffs.

### 2.1 Germany — BNetzA and the NEST reform

Germany is the central link to the companion reports 02 and 03. For the **4th regulatory period** (gas 2023–2027, electricity 2024–2028), BNetzA set a pre-tax equity return of **5.07% for new assets / 3.51% for existing (electricity)** via a **global CAPM** combining a German risk-free base rate (**0.74%**, a 10-year trailing average of the Umlaufsrendite over 2011–2020), a **DMS world market risk premium of 3.70%**, and a **peer-group beta of 0.81** (the Randl/Zechner + Frontier methodology — see report 02). (A frequent confusion is resolved: the **3.03%** sometimes cited for gas is the *third-period* "EK-II" rate — the reduced return on the equity tranche above the 40% notional cap — cut to ~2.02–2.04% for the 4th period; it is **not** the 4th-period existing-asset rate.) The OLG Düsseldorf annulled the determination (30 August 2023) for relying on DMS history "without supplementary plausibility checks," but the **BGH reversed and upheld BNetzA** (electricity 17 December 2024, EnVR 85/23; gas 25 February 2025, EnVR 83/23, 86/23, 90/23, 93/23) — see report 03.

The forward-looking story is the **NEST reform** ("Netze. Effizient. Sicher. Transformiert."; final determinations **10 December 2025**), enabled by the post-C-718/18 EnWG amendment (November 2023) that handed BNetzA a direct *Festlegungskompetenz*. From the **5th regulatory period** NEST:

- moves to a **single standardised WACC**, **eliminating the old-asset/new-asset equity split** and the EK-I/EK-II tranche mechanism, on a fixed **40% equity / 60% debt** notional structure;
- keys the **risk-free rate to recent quarters** rather than a 10-year trailing average;
- shifts the **MRP from a global DMS premium toward a local/eurozone CAPM** (weighted historical eurozone excess returns), and is expected to lower the beta — which is why the projected unified pre-tax equity rate of **~6.5–7%** leans toward 6.5% (a *BET Consulting projection*, not a verbatim BNetzA figure; BNetzA's own stated outcome is "+1.4% revenue for electricity DSOs");
- makes the **cost of debt market-indexed** (a 7-year trailing average of bond/credit-yield series, investment-volume-weighted, with no issuance-cost add-on);
- **important correction:** the **5th period remains 5 years** (gas 2028–2032; electricity 2029–2033); the **shortening to 3-year periods happens only from the 6th period** (gas 2033; electricity 2034).

### 2.2 Netherlands — ACM

The Authority for Consumers and Markets (adviser: **The Brattle Group**) sets a CAPM-based WACC splitting an **existing-capital WACC** (fixed at period start) from an annually re-computed **new-capital WACC**. For **2022–2026**: MRP **5.0%**, notional gearing ~**50%**, risk-free rate blending Dutch and German bond yields; electricity ran **"real-plus"** (the WACC set at the midpoint of the real and nominal WACC, ≈50% inflation compensated up front via degressive depreciation), gas fully nominal. TenneT's nominal pre-tax WACC declined to ~**2.77% (2026)** — the **low end of the European range**. A **CBb court ruling (4 July 2023, ECLI:NL:CBB:2023:318)** forced the risk-free rate onto **20-year government bonds with a 0.5% floor**. The new method, **REG2027 (final decisions 16 February 2026; 2027–2031)**, moves **electricity to a fully nominal WACC**, shifts the regime "from output to input" (a more cost-plus-leaning model), phases out TenneT's construction interest, and sets **MRP 5.20%** (the 2025 DMS eurozone realised ERP rose to 5.27%) and a fixed **risk-free rate of 2.69%** for the period — so the REG2027 nominal pre-tax WACC is materially **higher** than 2026's 2.77% (the exact per-operator headline sits in the WACC-model spreadsheets and was not verbatim-confirmable).

### 2.3 Italy, Austria, Spain

- **Italy — ARERA** operates a unified cross-sector framework, the **TIWACC** (founding act 614/2021 for 2022–2027), expressed **real, pre-tax**, with one common set of market parameters across electricity and gas (only beta and gearing service-specific) and an annual **"trigger"** that resets the WACC mid-period if a parameter moves it by more than ~30 bps. For **2025–2027** (deliberation 513/2024) real pre-tax WACCs were cut to about **5.5% (electricity transmission), 5.6% (electricity distribution), 5.5% (gas transport), 5.9% (gas distribution)**.
- **Austria — E-Control** sets a **nominal pre-tax WACC** via CAPM (Randl/Zechner; Frontier for gas) with 40% equity, a ~0.325 unlevered beta and a 5.0% MRP, and is distinctive for an **efficiency-dependent WACC** (median-efficiency DSOs receive the average WACC; more efficient operators earn more). Existing assets earn ~**4.16%**, with annually-updated new-investment WACCs of **6.33% (2024), 6.24% (2025), ~5.70% (2026)** — the per-vintage "old asset / new investment" laddering CEER highlights.
- **Spain — CNMC** uses a single **financial remuneration rate (TRF)**, nominal pre-tax, on a WACC basis since Circular 2/2019. The electricity T&D rate was **5.58% (2020–2025)**; on **22 December 2025** the CNMC raised it to **6.58% (2026–2031)** (Circular 9/2025), with gas at 5.44%/5.83% (2021–2026) and a 2027–2032 gas proposal of 6.46%/6.67%.

### 2.4 The cross-country picture

NERA's international comparison for BDEW found a **17-country average allowed equity return of ~6.05% after-tax** (range **3.74% Portugal to 8.70%**, on a nominal, post-tax, 40%-gearing basis), against which Germany's 4th-period **4.59% after-tax** sits markedly low — the empirical core of the "Germany lags its peers" argument. CEER's series points to broad convergence on incentive regulation, more incentive mechanisms in electricity than gas, and a representative cross-country WACC band of roughly **5.2–6.7%** with implied total market returns of **7.6–9.1%** (basis/vintage indicative).

---

## 3. United States — FERC and the state commissions

The US is the principal alternative to the CAPM-RAB world. Investor-owned utilities are regulated on a **cost-of-service / rate-of-return** basis:

> Revenue Requirement = Operating Expenses + Depreciation + Taxes + (Rate Base × Allowed Rate of Return)

Three features distinguish it from Europe: the **rate base is original (historical) cost** (a minority of states allow "fair value"); returns are **nominal** (inflation recovered through the nominal return and depreciation on original-cost plant, not via asset-base indexation); and rate cases are **episodic** — triggered by a utility filing or a complaint (FPA §206) — increasingly overlaid with multi-year rate plans, formula rates and trackers.

### 3.1 The constitutional standard

Two Supreme Court cases set the constitutional floor. **Bluefield Waterworks v. PSC of West Virginia (1923)** requires a return "equal to that generally being made … on investments in other business undertakings which are attended by corresponding risks," "sufficient to assure confidence in the financial soundness of the utility" and to "maintain and support its credit" — and notes a return "reasonable at one time" may "become too high or too low" as conditions change (the doctrinal hook for resetting ROEs). **FPC v. Hope Natural Gas (1944)** added the **"end result" test**: "it is the result reached not the method employed which is controlling," and freed regulators from the older "fair value" rate base. Because Hope makes the *overall* just-and-reasonable rate the test rather than any prescribed formula, commissions enjoy **wide latitude to choose and weight** cost-of-equity models — which is exactly why FERC has switched models repeatedly without offending the Constitution (the binding constraint has been reasoned decision-making under the APA, enforced by the D.C. Circuit, not Hope itself).

### 3.2 DCF as the primary tool

US regulatory practice historically treats the **Discounted Cash Flow (DCF)** model as **primary**, with CAPM, risk-premium and comparable/expected-earnings methods as supplements. The **constant-growth (Gordon) DCF** infers k = D₁/P₀ + g (forward dividend yield plus expected growth), suited to stable dividend-payers; **multi-stage / two-step** variants blend near-term analyst (IBES/Value Line) growth with long-run **GDP** growth. DCF is favoured because it is **market-grounded and largely observable** (actual price, dividend, published growth forecasts), minimising reliance on the contestable ERP and beta estimates at the heart of CAPM — the mirror image of Europe's parameter-driven CAPM preference.

### 3.3 The FERC electric-transmission ROE saga ("battle of the models")

FERC's electric-transmission ROE methodology is the canonical example of US ROE instability. All figures are **nominal base ROEs** (before incentive adders):

| Stage | Date | Opinion / Court | Change | MISO / NETO base ROE |
|---|---|---|---|---|
| 1 | 19 Jun 2014 | **Opinion 531** | Adopted two-step DCF; placed ROE at the midpoint of the upper half of the zone | NETOs **10.57%** |
| 2 | 14 Apr 2017 | **Emera Maine v. FERC** (D.C. Cir.) | Vacated/remanded Opinion 531 | — |
| 3 | 21 Nov 2019 | **Opinion 569** | Moved to **average of DCF and CAPM**; electric DCF growth weighting 80/20 | MISO **9.88%** (from 12.38%) |
| 4 | 21 May 2020 | **Opinion 569-A** | Re-added **Risk Premium** → DCF + CAPM + Risk Premium | MISO **10.02%** |
| 5 | 19 Nov 2020 | **Opinion 569-B** | Affirmed 569-A | MISO **10.02%** |
| 6 | Aug 2022 | **MISO TOs v. FERC** (D.C. Cir.) | Vacated/remanded — inadequate justification for the Risk Premium model | — |
| 7 | **17 Oct 2024** | **Order on Remand** (current) | Reverted to **DCF + CAPM only**, equally weighted; ROE at the **central midpoint** of the composite zone | MISO **9.98%** |

The model set lurched DCF-only → DCF+CAPM → DCF+CAPM+Risk-Premium → back to DCF+CAPM, with the headline number swinging 12.38% → 9.88% → 10.02% → **9.98%**. **Emera Maine** also established that in a §206 complaint FERC must *first* find the existing ROE unjust before setting a new one, and must justify any departure from the central midpoint. The current MISO base ROE is **9.98%** (DCF+CAPM, dockets EL14-12/EL15-45), though it is itself under further appeal.

### 3.4 Gas/oil pipelines and the state commissions

For **gas and oil pipelines**, FERC's two-step DCF (2/3 short-term analyst growth, 1/3 long-term GDP) survives, but since the **May 2020 Policy Statement** the pipeline ROE is set by **averaging DCF and CAPM 50/50** (the 2/3–1/3 weighting living *inside* the DCF leg); the Risk Premium model is excluded for lack of pure-play pipeline data. A April 2026 oil-pipeline index determination applied a uniform CAPM return of **8.3%** averaged with each pipeline's DCF ROE, confirming the blend is live.

At the **state level**, public utility commissions set most retail ROEs under *Hope/Bluefield*, weighing DCF, CAPM and risk-premium models. Per S&P Global / Regulatory Research Associates, **full-year 2024 median authorised ROEs were ~9.70%** for both electric and gas (≈9.78% electric / 9.71% gas on an ex-rider average basis), edging to ~**9.70–9.78%** in partial-2025 vintages, with authorised **common-equity ratios clustering ~50%** (many recent cases 50–54%). Rate-case *requests* have hit successive records (2022–2025).

---

## 4. Asia-Pacific

### 4.1 Australia — AER (the rules pole)

Australia operates the most rules-based regime: a **binding Rate of Return Instrument (RORI)** the AER must remake every four years, which then applies automatically to all network determinations and is **not separately re-litigated** at each reset. The **2022 RORI** (final decision 24 February 2023) is a **nominal vanilla WACC** built on a Sharpe-Lintner **CAPM with fixed parameters**: equity beta **0.60**, market risk premium **6.2%** (historical excess returns 1988–2022), a risk-free rate from **10-year Commonwealth Government Securities** averaged over a short nominated window (term *retained* at 10 years after a 5-year proposal was rejected), a **10-year trailing-average cost of debt** updated annually at a **BBB+** benchmark, **60% gearing**, and a distinctive **imputation-credit (gamma) allowance of 0.585** (absent from UK/EU/US WACCs). Indicative overall WACC sat in the high-5% to ~6.5% range over the instrument's life. The **2026 RORI review** is underway (discussion paper 4 August 2025): the live issues are the **equity beta** (the domestic listed-comparator pool has shrunk to ~one firm, prompting the eligible experts to recommend adding international comparators) and a possible move to a **weighted** trailing-average cost of debt.

### 4.2 New Zealand — Commerce Commission (aiming-up made numerical)

New Zealand runs a transparent CAPM/WACC regime under binding **Input Methodologies**, using the domestic **Simplified Brennan-Lally CAPM** (which taxes the risk-free component and uses a **tax-adjusted market risk premium, TAMRP**, reflecting NZ dividend imputation). Its hallmark is the **WACC percentile uplift** above the midpoint to guard against under-investment — the cleanest real-world implementation of "aiming up." The percentile history is **75th → 67th (2014) → 65th**: the **2023 IM Review (final 13 December 2023)** cut the price-quality percentile to the **65th for EDBs and Transpower** and to the **50th (midpoint) for gas pipeline businesses** (gas being a declining/transitioning sector), and reset the **TAMRP to 7.0%** (asset beta 0.35 electricity / 0.40 gas; notional leverage ~42%). The rate environment lifted recent resets sharply: the **EDB DPP4 and Transpower RCP4 vanilla WACC rose to ~7.10% (65th percentile)** from 4.57% in the prior period, with the DY2026 information-disclosure midpoint vanilla WACC around 6.5%.

### 4.3 Japan — METI (rate base → revenue cap)

Japan historically set tariffs by the total-cost method — **business return = rate base × fair rate of return** — administered by METI with scrutiny by the Electricity and Gas Market Surveillance Commission (EGC). From **1 April 2023** it introduced **revenue-cap regulation** for the ten transmission-and-distribution operators (first period FY2023–FY2027), with OCCTO coordinating the framework and the METI Minister approving each five-year revenue ceiling on EGC advice. The fair return is a WACC on a **30% equity / 70% debt** structure: cost of equity via a CAPM that, because the unbundled networks are unlisted, uses a **pre-Fukushima (2006–2011) parent beta ~0.8**, combined with an all-industry-ROE upper bound and a bond-yield floor; the FY2023 determinations imply an overall **rate of return ~2.7–2.8% nominal** (cost of equity ~7.4%, cost of debt ~0.7%, 30:70). A 2026 reform is adding inflation/interest-rate escalation, confirming the first-period figures were fixed and nominal. (Note: "0.5%" in this regime is the efficiency coefficient, *not* the rate of return.)

### 4.4 Singapore, Hong Kong, India, Korea

- **Singapore — EMA** regulates SP PowerAssets on a **RAB × WACC building-block** model with a five-year reset (current period to 31 March 2030), using a 20-year Singapore Government Securities risk-free rate, ~60% gearing and an "A" benchmark rating; the specific numeric T&D WACC is not routinely published (a commonly cited ~5.38% figure, finalised 2021, should be confirmed and not conflated with the separate vesting-contract WACC for a hypothetical new-entrant generator).
- **Hong Kong** is the clearest **return-on-assets cap** rather than a CAPM-WACC: under the Scheme of Control Agreements with CLP Power and HK Electric (signed 25 April 2017; effective 1 Oct 2018 / 1 Jan 2019 to 31 December 2033), the permitted return is **8% of average net fixed assets** (reduced from 9.99%) — a single negotiated, **uniform** rate with no risk-free-rate-plus-beta build-up, overseen by the Environment and Ecology Bureau. (The 2017 SCA **abolished** the previous scheme's separate higher rate for renewables — under the pre-2018 SCAs renewable-energy investment earned 11% versus 9.99% on other assets; renewables are now incentivised through feed-in tariffs, renewable-energy certificates and performance schemes rather than a higher permitted return.)
- **India — CERC** sets inter-state transmission tariffs cost-plus over five-year blocks (2024–2029), with a **base Return on Equity of 15.50%** (post-tax, grossed up), cut to **15.00% for new transmission projects** commissioned on/after 1 April 2024, on a 70:30 debt:equity norm.
- **South Korea** has **no transparently published regulatory WACC**: KEPCO's tariffs are set administratively by MOTIE with a bounded fuel-cost pass-through.

---

## 5. Cross-cutting synthesis

### 5.1 Comparison across jurisdictions

| Jurisdiction (regulator) | Primary CoE model | Real vs nominal | Asset-base model | Cost-of-debt approach | RFR / ERP setting | Gearing | Reset cycle | Appeal mechanism |
|---|---|---|---|---|---|---|---|---|
| **UK** (Ofgem, Ofwat) | CAPM | Real (CPIH); RIIO-3 debt semi-nominal | Indexed RAB (CPIH) | iBoxx trailing average (10–14yr) | RFR on 20yr ILGs; TMR on DMS history + ex-ante (6.9% CPIH-real, RIIO-3) | Notional 55–60% | 5yr price control | CMA appeal / redetermination |
| **Germany** (BNetzA) | CAPM (global DMS → eurozone-local under NEST) | Real (old assets) → single WACC under NEST | RAB | Static → **7yr market index** (NEST) | Umlaufsrendite 10yr avg → recent quarters; MRP 3.70% → eurozone | 40% equity | 5yr (3yr from RP6) | Courts (OLG, BGH); ECJ on independence |
| **Netherlands** (ACM) | CAPM | Nominal (all sectors from 2027) | RAB | Embedded in WACC | 20yr govt bonds + 0.5% floor (CBb); ERP 5.0% → **5.20%**; RFR 2.69% | Notional ~50% | ~5yr method decision | CBb (Trade & Industry Appeals Tribunal) |
| **Italy** (ARERA) | CAPM (TIWACC) | Real, pre-tax | RAB | iBoxx BBB indices | DE/FR/BE/NL basket + Italian CRP; annual trigger | Notional ~50% | 6yr, 3yr sub-period + trigger | Administrative courts (TAR/Consiglio di Stato) |
| **Austria** (E-Control) | CAPM (efficiency-dependent) | Nominal, pre-tax | RAB | — | 5.0% MRP; per-vintage new-investment WACC | 40% equity | multi-year | Administrative courts |
| **Spain** (CNMC) | CAPM (TRF) | Nominal, pre-tax | RAB | Mixed historical + forward | Spanish 10yr bono avg | Regulatory parameter | 6yr | Administrative courts |
| **United States** (FERC, state PUCs) | **DCF primary** (+ CAPM, risk premium) | **Nominal** | **Original-cost rate base** | **Embedded (actual) cost of debt** | Market DCF growth; CAPM w/ 30yr Treasury | Often **actual** ~50% equity | **Episodic** rate cases (+ multi-year plans) | Rehearing → federal courts of appeal |
| **Australia** (AER) | CAPM (fixed MRP) | Nominal | RAB (indexed) | 10yr trailing average, annual update | 10yr CGS; MRP fixed 6.2%; **gamma 0.585** | Notional 60% | **Binding 4yr instrument** | Limited merits review |
| **New Zealand** (ComCom) | Simplified Brennan-Lally CAPM | Real / post-tax vanilla | RAB | Risk-free + debt premium | TAMRP 7.0%; **65th-percentile WACC uplift** | Notional ~42% | 5yr (with annual ID) | High Court / merits appeal on IMs |
| **Japan** (METI/EGC) | CAPM (pre-2011 parent beta) | Nominal | Rate base | Bond yields | JGB risk-free; all-industry-ROE cap | 30% equity | 5yr revenue cap (from FY2023) | Administrative review |
| **Singapore** (EMA) | CAPM / building block | Post-tax real (indicative) | RAB | "A"-rated benchmark | 20yr SGS RFR | ~60% | 5yr | Administrative |
| **Hong Kong** (Govt SCAs) | **None (negotiated cap)** | Nominal book value | Net fixed assets | n/a | n/a | n/a | ~15yr agreement | Bilateral renegotiation |
| **India** (CERC) | Cost-plus regulated RoE | Nominal, post-tax (grossed up) | Rate base | Actual debt cost | Fixed base RoE 15.0–15.5% | 70% debt norm | 5yr tariff block | Appellate Tribunal (APTEL) |

*All values reflect the most recent determinations identified as of June 2026; several (Germany's NEST WACC, Australia's headline annual WACC, Japan's allowed WACC, Singapore's T&D WACC) are not published as single transparent figures and are characterised accordingly. Indicative parameters are approximate.*

### 5.2 The four methodological fault lines

**(1) CAPM-RAB versus DCF-rate-of-return.** The deepest divide is between the US and almost everyone else. The US infers the cost of equity from **market prices and expected dividend growth** (DCF), applied to an **original-cost rate base** in **episodic** rate cases with the utility's **actual** capital structure. The UK, EU, Australia and New Zealand instead **build up** the cost of equity from CAPM, apply it to an **inflation-indexed RAB**, use a **notional** capital structure, and reset on a **fixed multi-year cycle**. FERC's oscillation (DCF-only → DCF+CAPM → +Risk Premium → DCF+CAPM) shows how the DCF approach, for all its market-grounding, struggles for stability; the European CAPM approach is more stable but more parameter-contestable (the German litigation). Outcomes can nonetheless converge once normalised for inflation and gearing.

**(2) Real versus nominal.** RAB-indexation and the real/nominal choice are two sides of one coin: where the asset base is uplifted by inflation (UK, Italy, Australia, NZ) the return is real; where it is held at historic cost (US) the return is nominal. The trend is **not** monotonic — the Netherlands moves electricity **to** nominal from 2027, the UK's RIIO-3 introduces a semi-nominal debt allowance, and Germany's NEST collapses the old real-return-on-old-assets split into a single WACC — all responses to a higher, more volatile rate environment in which fully-real allowances under-delivered cash.

**(3) Historical (DMS) versus market-implied ERP.** The UK and Germany **anchor the ERP/TMR on the DMS long-run historical dataset** (Ofgem on UK history; BNetzA via a "global CAPM" on the DMS world premium — now shifting eurozone-local under NEST). Australia fixes the MRP for four years (6.2%); New Zealand fixes a TAMRP (7.0%). The US instead derives its forward equity expectation **from current market dividend yields and analyst growth forecasts** (DCF) and an explicit CAPM with a 30-year Treasury risk-free rate — inherently more market-implied and time-varying. The contrast is concrete: a German allowance moves with a ten-year (soon recent-quarter) average; a US ROE moves with this quarter's prices and forecasts.

**(4) Rules versus discretion.** Australia's **binding RORI** and New Zealand's **Input Methodologies** sit at the rules pole — parameters fixed for four to five years, applied mechanically, with appeal rights deliberately narrowed. The US sits at the discretion pole — a "battle of the models" resolved case by case under *Hope/Bluefield*. Germany captures the tension: **ECJ C-718/18 forced a shift *toward* discretion**, stripping binding legislative formulae and handing methodology-setting to BNetzA — the mirror image of Australia's move toward rules. The UK sits between, regulator-led but disciplined by CMA appeal.

### 5.3 Two cross-cutting features and a market benchmark

- **"Aiming up."** The asymmetric-loss case for setting the allowed return above the central estimate — formalised by **Dobbs (2004; and the welfare-loss-asymmetry literature)** — is implemented numerically in **New Zealand's WACC percentile** (65th), and applied judgmentally by the **CMA** (PR19, ~25 bps) and **Ofwat** (PR24, ~27 bps). Its absence is itself a choice elsewhere (Ofgem declined to aim up at RIIO-2).
- **Imputation credits (gamma).** Australia (0.585) and New Zealand (via the Brennan-Lally TAMRP) explicitly value dividend-imputation tax credits — a component absent from UK, EU and US WACCs, important to normalise in any cross-jurisdiction comparison.
- **Allowed vs market cost of capital.** The IEA's **Cost of Capital Observatory** shows the *market* (project-finance) cost of capital — e.g. nominal post-tax local-currency solar-PV WACCs of ~8–9.4% in Indonesia/Vietnam/Philippines in 2024, "well over twice" advanced-economy levels — a reminder that *regulatory-allowed* WACCs (the subject of this report) and *market-charged* WACCs can diverge widely, especially across emerging Asia.

---

## 6. Comparative literature and primary determinations — annotated

**Cross-country benchmarking (regulators' own).**
1. **CEER, *Report on Regulatory Frameworks for European Energy Networks* (annual; 2025 ed. 22 Jan 2026).** The flagship cross-country benchmark (~29 members + NI + 5 ECRB). Establishes that WACC is dominant, CAPM near-universal, RFR on government bonds, nominal-pre-tax most popular for electricity. Series-level WACC band ~5.2–6.7%.
2. **ACER, *Report on investment evaluation, risk assessment and regulatory incentives* (June 2023)** and ***Electricity Network Tariff Practices in Europe* (March 2025).** The first frames the "extra-WACC" risk-mitigation/incentive layer for PCIs; the second covers translating allowed revenue into tariffs.

**Consultant comparative studies.**
3. **NERA for BDEW, "Internationaler Vergleich der EK-Zins-Festlegungen."** The core "Germany lags peers" evidence: 17-country average allowed equity **6.05% after-tax** (range 3.74–8.70%, nominal/post-tax/40% gearing) vs Germany's 4.59%.
4. **Frontier Economics (with Zechner & Randl), "Estimating cost of equity for German gas and electricity networks."** The regulator-side defence: CAPM-consistent 4.59% (4th period) vs 6.91% (3rd), benchmarked to European peers.
5. **Oxera, "Allowed cost of equity for German energy networks"** and **"Aiming high in setting the WACC."** The operator-side critique of BNetzA's global-CAPM/DMS approach, and the articulation of the asymmetric-loss "aiming up" case.
6. **CEPA, "PR24 Cost of Equity" (Ofwat, 11 July 2024)** and **KPMG, "Estimating the cost of equity for PR24."** The regulator-adviser and company-adviser poles of the UK water debate; both anchor a stable TMR (~6.0–6.96%) on DMS and layer CAPM cross-checks (MARs, debt-implied CoE).
7. **The Brattle Group for ACM, Dutch network WACC reports.** Document the nominal-WACC move and the ~2.77% (2026) low-end European WACC; the REG2027 MRP 5.20% / RFR 2.69% calibration.

**Foundations.**
8. **UKRN — Cost of Capital guidance (2023)** and **Wright, Burns, Mason & Pickford (2018).** The keystone UK cross-regulator consistency document and its academic foundation (TMR-based framing; equity betas ~0.3–0.5; CAPM primary).
9. **Dobbs (2004), "Intertemporal price cap regulation under uncertainty," *Economic Journal*; and the welfare-loss-asymmetry literature.** The analytical engine behind "aiming up."
10. **Whitaker, "The DCF Methodology … Estimating a Utility's Cost of Equity," *Energy Law Journal* 12 (1991); Damodaran, "Equity Risk Premiums" (annual).** The US DCF tradition and the implied-ERP cross-check, respectively.

**Cross-cutting / Asia-Pacific primary determinations.**
11. **AER, "International regulatory approaches to rate of return" (2020)** and the **2022 Rate of Return Instrument.** A regulator-authored cross-jurisdiction comparison and the binding Australian determination (with the distinctive gamma component).
12. **NZ Commerce Commission, Cost of Capital Input Methodologies (2023 IM Review).** The canonical "aiming-up made numerical" jurisdiction (65th percentile).
13. **Hong Kong Scheme of Control Agreements (2017).** A rare asset-base × fixed-percentage-return model (8% of net fixed assets), not CAPM-based.
14. **Cambini & Rondi, "Incentive regulation and investment" (*J. Regulatory Economics*, 2010); and the price-cap-vs-rate-of-return / Averch–Johnson literature.** The empirical and theoretical framing for the central CAPM-RAB-vs-rate-of-return synthesis.
15. **IEA, Cost of Capital Observatory.** Observed (market) cost of capital across emerging/Asian economies — the project-finance counterpart to the regulatory-allowed WACC.

---

## Sources

**United Kingdom**
1. Oxera, "RIIO-3 Final Determinations" (Dec 2025). https://www.oxera.com/insights/agenda/articles/riio-3-final-determinations/
2. Ofgem, RIIO-3 Final Determinations — Finance Annex (4 Dec 2025) / decision page. https://www.ofgem.gov.uk/decision/riio-3-final-determinations-electricity-transmission-gas-distribution-and-gas-transmission-sectors
3. Ashurst, "RIIO-3: Ofgem's Final Determinations at a glance." https://www.ashurst.com/en/insights/riio-3-ofgems-final-determinations-at-a-glance/
4. Oxera, "RIIO-ED2 Final Determinations" (Nov 2022). https://www.oxera.com/insights/agenda/articles/riio-ed2-final-determinations/
5. Ofgem, RIIO-ED2 Final Determinations Finance Annex. https://www.ofgem.gov.uk/sites/default/files/2022-11/RIIO-ED2%20Final%20Determinations%20Finance%20Annex.pdf
6. Ofwat, PR24 Final Determinations — Aligning risk and return (Dec 2024). https://www.ofwat.gov.uk/wp-content/uploads/2024/12/PR24-final-determinations-Aligning-risk-and-return-1.pdf
7. CEPA for Ofwat, "PR24 Cost of Equity" (11 Jul 2024). https://www.ofwat.gov.uk/wp-content/uploads/2024/07/CEPA_PR24-cost-of-equity-1.pdf
8. CMA, Water redeterminations (PR19) — summary (17 Mar 2021). https://assets.publishing.service.gov.uk/media/604fa141e90e077fe7a5f45a/-_CMA_water_redeterminations_-_summary_-_online_version_---_-.pdf
9. CMA, RIIO-2 Energy Licence Modification Appeals — Summary of final determination (28 Oct 2021). https://assets.publishing.service.gov.uk/media/61791296d3bf7f55ff1fc099/Energy_appeals_-_Summary_of_final_determination_28.10.21.pdf
10. UK Regulators Network, Cost of Capital guidance (22 Mar 2023). https://ukrn.org.uk/app/uploads/2023/03/CoC-guidance_22.03.23.pdf
11. Wright, Burns, Mason & Pickford, "Estimating the cost of capital for … UK regulators" (UKRN, 2018). https://ukrn.org.uk/app/uploads/2018/06/2018-CoE-Study.pdf

**EU / Continental Europe**
12. CEER, Report on Regulatory Frameworks for European Energy Networks 2025 (22 Jan 2026). https://www.ceer.eu/publication/report-on-regulatory-frameworks-for-european-energy-networks-2025/
13. ACER, Report on investment evaluation, risk assessment and regulatory incentives (Jun 2023). https://www.acer.europa.eu/sites/default/files/documents/Publications/ACER_Report_Risks_Incentives.pdf
14. ACER, Electricity Network Tariff Practices in Europe (Mar 2025). https://www.acer.europa.eu/sites/default/files/documents/Publications/2025-ACER-Electricity-Network-Tariff-Practices.pdf
15. Grant Thornton, "Neue WACC-Berechnung für Netzbetreiber" (NEST, 2025). https://www.grantthornton.de/themen/2025/aktuelle-entwicklungen-zur-eigenkapitalverzinsung-von-netzbetreibern-neue-wacc-berechnung-im-fokus/
16. Herbert Smith Freehills Kramer, "NEST Decisions Set New Course for German … Network Regulation" (2026). https://www.hsfkramer.com/notes/energy/2026-posts/nest-decisions-set-new-course-for-german-electricity-and-gas-network-regulation
17. BNetzA press release, NEST cost-regulation determinations (9–10 Dec 2025). https://www.bundesnetzagentur.de/SharedDocs/Pressemitteilungen/EN/2025/20251210_NEST.html
18. NERA for BDEW, "Internationaler Vergleich der EK-Zins-Festlegungen." https://www.bdew.de/media/documents/NERA_Internationaler_Vergleich_EK_Zins_Festlegungen.pdf
19. Frontier Economics, "Estimating cost of equity for German gas and electricity networks." https://www.frontier-economics.com/uk/en/news-and-insights/news/news-article-i8670-estimating-cost-of-equity-for-german-gas-and-electricity-networks/
20. Oxera, "Allowed cost of equity for German energy networks." https://www.oxera.com/insights/reports/allowed-cost-of-equity-for-german-energy-networks/
21. ACM/Brattle, "The WACC for the Dutch Electricity TSO and Electricity and Gas DSOs." https://www.acm.nl/sites/default/files/documents/the-wacc-for-the-dutch-electricity-tso-and-electricity-and-gas-dsos.pdf
22. CBb ruling ECLI:NL:CBB:2023:318 (4 Jul 2023). https://www.omgevingsweb.nl/jurisprudentie/eclinlcbb2023318/
23. ACM, "Methodebesluit TenneT op land 2027-2031" (final, 16 Feb 2026). https://www.acm.nl/nl/publicaties/methodebesluit-tennet-op-land-2027-2031
24. Oxera, "Note on ACM's draft method decisions for REG2027" (Sep 2025). https://www.oxera.com/wp-content/uploads/2025/09/Note-on-ACMs-draft-method-decisions-for-REG2027.pdf
25. ARERA, Deliberazione 614/2021/R/com (TIWACC) and 513/2024 (2025–2027 update). https://www.arera.it/atti-e-provvedimenti/dettaglio/24/513-24
26. E-Control, Cost Methodology 2021–2024 and WACC Neuinvestitionen 2025/2026. https://www.e-control.at/documents/1785851/1811582/E-Control_Cost_Methodology_2021_2024_EN.pdf
27. CNMC, Circular 2/2019 and Circular 9/2025 (TRF; 6.58% 2026–2031). https://www.cnmc.es/prensa/circulares-retribucion-electrica-20251222
28. White & Case, "ECJ on Independence of German Energy Regulator (C-718/18)." https://www.whitecase.com/insight-alert/european-court-justice-independence-german-energy-regulator

**United States**
29. FPC v. Hope Natural Gas Co., 320 U.S. 591 (1944). https://supreme.justia.com/cases/federal/us/320/591/
30. Bluefield Waterworks v. PSC, 262 U.S. 679 (1923). https://supreme.justia.com/cases/federal/us/262/679
31. FERC, "FERC Revises Public Utility ROE Methodology; Sets Policy for Natural Gas, Oil Pipelines" (May 2020). https://www.ferc.gov/news-events/news/ferc-revises-public-utility-roe-methodology-sets-policy-natural-gas-oil-pipelines
32. RTO Insider, "FERC Sets MISO TOs' ROE at 9.98%, Again Eliminates Risk Premium Model" (Oct 2024). https://www.rtoinsider.com/89798-ferc-sets-miso-tos-roe-eliminates-risk-premium-model/
33. Baker Botts, "FERC Revises ROE Methodology for Transmission Owners" (Oct 2024). https://www.bakerbotts.com/thought-leadership/publications/2024/october/ferc-revises-roe-methodology-for-transmission-owners
34. National Law Review, "DC Circuit Sends FERC Back to the Drawing Board on ROE Policy" (Emera Maine, 2017). https://natlawreview.com/article/dc-circuit-sends-ferc-back-to-drawing-board-roe-policy
35. Akin Gump, "FERC Reduces New England Transmission Owners' Base ROE to 10.57 percent" (Opinion 531). https://www.akingump.com/en/insights/blogs/speaking-energy/ferc-reduces-new-england-transmission-owners-base-roe-to-10-57
36. Jones Day, "FERC Revises ROE Methodology for Utilities, Again" (pipeline DCF+CAPM). https://www.jonesday.com/en/insights/2020/06/ferc-revises-roe-methodology-for-utilities-again
37. S&P Global Market Intelligence, "Underearning spread widens for gas, electric utilities in ROE analysis" (authorised ROE/equity-ratio data). https://www.spglobal.com/market-intelligence/en/news-insights/research/underearning-spread-widens-for-gas-electric-utilities-in-roe-analysis
38. Whitaker, "The DCF Methodology … Estimating a Utility's Cost of Equity," Energy Law Journal 12 (1991). https://www.eba-net.org/wp-content/uploads/2023/02/26_12EnergyLJ2651991.pdf

**Asia-Pacific**
39. AER, Rate of Return Instrument — Explanatory Statement (24 Feb 2023). https://www.aer.gov.au/system/files/AER%20-%20Rate%20of%20Return%20Instrument%20-%20Explanatory%20Statement%20-%2024%20February%202023_1.pdf
40. AER, "International regulatory approaches to rate of return" (working paper, 16 Dec 2020). https://www.aer.gov.au/industry/registers/resources/reviews/international-regulatory-approaches-rate-return-pathway-rate-return-2022
41. AER, 2026 RORI Review Discussion Paper (4 Aug 2025). https://www.aer.gov.au/system/files/2025-08/AER%20-%202026%20RORI%20review%20discussion%20paper%20-%204%20August%202025.pdf
42. NZ Commerce Commission, 2023 IM Review — Cost of capital topic paper (13 Dec 2023). https://www.comcom.govt.nz/__data/assets/pdf_file/0022/337612/Part-4-IM-Review-2023-Final-decision-Cost-of-capital-topic-paper-13-December-2023.pdf
43. NZ Commerce Commission, [2024] NZCC 21 — Cost of capital determination EDB DPP4 and Transpower RCP4 (25 Sep 2024). https://www.comcom.govt.nz/assets/pdf_file/0022/362524/5B20245D-NZCC-21-Cost-of-capital-determination-EDB-DPP4-and-Transpower-RCP4-25-September-2024.pdf
44. METI/EGC, Revenue-cap regulation portal and "Rate base & business profit rate." https://www.egc.meti.go.jp/info/revenue_cap/
45. Global Legal Insights, "Energy Laws & Regulations 2026 — Japan." https://www.globallegalinsights.com/practice-areas/energy-laws-and-regulations/japan/
46. GovHK, Scheme of Control Agreements; HK Government press release (25 Apr 2017). https://www.gov.hk/en/residents/environment/sustainable/energy/schemeofca.htm
47. EMA Singapore — Transmission Code and electricity market overview. https://www.ema.gov.sg/regulations-licences/licences/industry-licences
48. CERC, Tariff Regulations 2024 (base RoE 15.0–15.5%). https://www.cercind.gov.in/regulations/notification-2024.pdf

**Cross-cutting / foundations**
49. Dobbs, "Intertemporal price cap regulation under uncertainty," Economic Journal 114 (2004). https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-0297.2004.00215.x
50. Cambini & Rondi, "Incentive regulation and investment: evidence from European energy utilities," J. Regulatory Economics (2010). https://link.springer.com/article/10.1007/s11149-009-9111-6
51. Damodaran, "Equity Risk Premiums: Determinants, Estimation and Implications" (annual, NYU Stern). https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/riskprem.pdf
52. IEA, Cost of Capital Observatory. https://www.iea.org/reports/cost-of-capital-observatory
