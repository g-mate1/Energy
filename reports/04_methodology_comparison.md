# Comparison of Regulatory Cost-of-Capital Methodologies: EU, US, UK and Asia

*Compiled from public sources as of June 2026. Regulatory frameworks change frequently and many cost-of-capital parameters are reset annually or mid-period; all figures below should be checked against the current primary determinations of the relevant regulator before use. Figures are labelled by vintage and by basis (real/nominal, pre-/post-tax) wherever material; figures described as indicative are approximate or analyst-derived rather than a single regulator-stated number.*

---

## Introduction and scope

Every regulator of an energy or water network monopoly must answer the same question: what return should investors be allowed to earn on capital sunk into an asset whose prices the state controls? The answer — the allowed rate of return, or weighted average cost of capital (WACC) — is the most contested number in utility regulation, because it simultaneously determines consumer bills, the financeability of the network, and the incentive to invest in the energy transition.

This report compares how regulators in the **United Kingdom, the European Union, the United States and the Asia-Pacific** set that number. It is a companion to two related notes — one on the Dimson–Marsh–Staunton (DMS) historic-returns dataset and one on the German Bundesnetzagentur (BNetzA) / Randl–Zechner approach — and draws on both where relevant. The central story is a fault line between two families: a **CAPM-plus-indexed-Regulated-Asset-Base (RAB)** model used across the UK, continental Europe, Australia and New Zealand; and a **Discounted-Cash-Flow-plus-rate-of-return** model used in the United States. Around it sit further dividing lines — real versus nominal returns, historical versus market-implied equity risk premia, and rules versus discretion.

---

## 1. United Kingdom — Ofgem, Ofwat and the CMA

The UK pioneered the modern incentive-based, RAB-anchored price control, and its method is the reference case for the CAPM-RAB family. Allowed revenue is built up from components: a **return on capital** (allowed WACC × RAB), a **return *of* capital** (regulatory depreciation), operating costs, and incentive adjustments [21][22]. Both Ofgem and Ofwat now **index the RAB to CPIH** (having migrated off RPI), so inflation compensation is delivered through asset-base indexation and the allowed return is quoted in **CPIH-real** terms [21].

**Cost of equity — CAPM anchored on DMS.** The cost of equity uses the Capital Asset Pricing Model — risk-free rate + equity beta × equity risk premium, parameterised around a **Total Market Return (TMR)**. The TMR is anchored primarily on **long-run realised UK equity returns from the DMS dataset** (the ~125-year London Business School / UBS *Global Investment Returns Yearbook* series, with a world real equity return of roughly 5.2% p.a. since 1900) [11], blended in recent controls with forward-looking estimates on a broadly equal weighting [1]. The **risk-free rate is indexed annually** to 20-year index-linked gilt yields on a CPIH basis [10].

**RIIO-2 (gas/electricity transmission and gas distribution, 2021–2026).** In its December 2020 Final Determinations Ofgem set an allowed cost of equity of **4.55% CPIH-real** at 60% notional gearing, a TMR range of **6.25–6.75%** (midpoint 6.5%), an asset beta of ~0.35, and a headline vanilla WACC of approximately **2.81% CPIH-real** [1][8]. Ofgem applied a controversial three-step equity methodology: a CAPM range (Step 1), a set of six cross-checks that pulled the range down (Step 2), and an "outperformance wedge" of ~25 basis points deducted from the CAPM figure on the theory that companies would systematically beat their allowance (Step 3) [1][6]. Cost of debt was set by a trailing average of the **iBoxx GBP Utilities 10yr+ index**, using a lengthening "trombone" window (~10 to 14 years) plus a borrowing-cost allowance [1]. **RIIO-ED2** (electricity distribution, 2023–2028) followed the same template, landing at a higher **5.23% CPIH-real** cost of equity by its November 2022 Final Determination as gilt yields rose [3].

**RIIO-3 (2026–2031).** Ofgem published Final Determinations on **4 December 2025** for the electricity-transmission, gas-distribution and gas-transmission sectors covering 1 April 2026 to 31 March 2031 [5]. The allowed CPIH-real cost of equity rose to about **6.12% at 60% gearing** for the gas networks and **5.70% at 55% gearing** for electricity transmission (Ofgem cut ET notional gearing to 55%), versus 4.3–4.55% in RIIO-2 [5][7][9]. The TMR midpoint rose to ~6.75% [5], and — importantly — Ofgem **dropped the outperformance wedge** following the CMA's RIIO-2 ruling [4]. RIIO-3 also introduced a **"semi-nominal" cost-of-debt allowance** (mostly nominal, with only ~30% real for gas and ~10% for ET), which means the headline RIIO-3 WACCs of roughly 5.2–5.7% are **not directly comparable** to RIIO-2's fully-real ~2.81%; much of the apparent jump reflects higher interest rates plus this change of convention [5][9].

**Ofwat PR24 (water, 2025–2030).** In its December 2024 Final Determinations Ofwat set, all CPIH-real and at 55% notional gearing: an allowed cost of equity of **5.10%**, a cost of debt of **3.15%**, a wholesale return of **3.97%**, and an **appointee WACC of 4.03%** [14][15]. Ofwat took the cost of equity towards the upper end of its CAPM range and applied a positive benchmark-index adjustment — a form of **"aiming up"** [14][15].

**The CMA on appeal.** The Competition and Markets Authority hears appeals and redeterminations. In the **PR19 water redeterminations** (March 2021) the CMA, acting as redetermining body, **explicitly aimed up by ~25 basis points** above its cost-of-equity midpoint (to ~4.7% CPIH-real), citing the asymmetric consumer-welfare cost of under-investment [17][18]. In the **RIIO-2 energy appeals** (October 2021) the CMA, acting in a narrower error-correction role, **upheld Ofgem's 4.55% cost of equity but removed the outperformance wedge**, while declining to *require* Ofgem to aim up [6][19]. This asymmetry — aiming up where it redetermines, deference where it reviews — is the defining feature of UK appellate practice.

---

## 2. EU / Continental Europe

Continental regulators overwhelmingly use **CAPM to set the cost of equity within a WACC**, but diverge sharply on real-versus-nominal convention and on how the risk-free rate is averaged. The Council of European Energy Regulators' annual *Report on Regulatory Frameworks for European Energy Networks* (2025 edition published January 2026, ~35 countries) finds WACC the preferred construct, CAPM near-universal, and the risk-free rate "most often" set off 10-year (sometimes 5-year) government-bond yields with heavy but non-uniform use of historical averages [E1]. For **electricity** the popular construct is a **nominal pre-tax WACC**; for **gas**, nominal pre-tax is common but **real pre-tax is also frequently used**, tracking each regulator's RAB-indexation choice [E1]. ACER corroborates that "the rate of return in most Member States is calculated using the CAPM" and catalogues per-country WACCs in its investment-risk and DSO revenue-setting reports [E4][E5].

**Germany — BNetzA.** Germany is the key link to the companion BNetzA/Randl–Zechner note. BNetzA sets a calculated equity-return rate (*Eigenkapitalzinssatz*) via CAPM, historically deriving the base rate from the **Umlaufsrendite** (Bundesbank-published bond yields) averaged over the **last ten calendar years**, with a **global CAPM** combining a German risk-free rate with a **world market risk premium estimated from the DMS dataset** and a **peer-group beta** from listed European networks per the **Randl/Zechner** methodology (with Frontier Economics) [4][5][8]. For the **4th regulatory period** (gas 2023–2027, electricity 2024–2028) it set the pre-tax rate at **5.07% for new assets and 3.51% for old assets** (after-tax ≈4.13%, from a 3.7% market risk premium × 0.81 beta plus a surcharge); old assets earn a real return as their rate is reduced by trailing inflation [3][8]. The Federal Court of Justice upheld these figures in February 2025 [3]. The landmark backdrop is **ECJ case C-718/18 (2 September 2021)**, which held that Germany breached the EU electricity and gas directives by leaving tariff methodologies in government ordinances (StromNEV/GasNEV) and required methodology-setting to lie **exclusively with the independent NRA** [1][2]. Germany abolished the government's ordinance-making power in favour of a BNetzA *Festlegungskompetenz*, which from the 5th period drives the **NEST reform** (final decisions 10 December 2025), moving Germany to a full **WACC method** with CAPM cost of equity, 40/60 equity/debt and shorter 3-year periods [9][10].

**Netherlands — ACM.** The Authority for Consumers and Markets sets a CAPM-based WACC (adviser: Brattle), splitting an existing-capital WACC (fixed at period start) from an annually re-computed new-capital WACC. For 2022–2026 it used a 5.0% market risk premium, ~50% notional gearing, and a risk-free rate blending Dutch and German bond yields; electricity ran "real-plus", gas nominal [N1][N2][N5]. A 2023 court ruling forced a move to 20-year bonds and a 0.5% floor [N4]. From **REG2027 (2027–2031, final decisions February 2026)** electricity moves to a **fully nominal WACC** [N6][N7].

**Italy — ARERA.** Italy operates a unified cross-sector framework, the **TIWACC** (founding act 614/2021 for 2022–2027), expressed **real, pre-tax**, with one common set of market parameters across electricity and gas (only beta and gearing are service-specific) and an annual "trigger" that resets the WACC mid-period if a parameter shifts it by more than ~30 bps [I1][I2]. For the **2025–2027 sub-period** (513/2024) real pre-tax WACCs were cut to about **5.5% (electricity transmission), 5.6% (electricity distribution), 5.5% (gas transport) and 5.9% (gas distribution)** [I3][I5].

**Austria — E-Control.** Austria sets a **nominal pre-tax WACC** via CAPM (Randl/Zechner; Frontier for gas) with 40% equity, a 0.325 unlevered beta and a 5.0% market risk premium, and is distinctive for an **efficiency-dependent WACC** rewarding more-efficient operators [A12][A18]. Existing assets earn ~**4.16%**, with annually-updated new-investment WACCs of **6.33% (2024), 6.24% (2025) and ~5.70% (2026)** [A14][A15].

**Spain — CNMC.** Spain uses a single **financial remuneration rate (TRF)**, nominal pre-tax, on a WACC basis since Circular 2/2019. The electricity T&D rate was **5.58% for 2020–2025**; on **22 December 2025** the CNMC raised it to **6.58% for 2026–2031** (Circular 9/2025), up 100 bps, with gas at 5.44%/5.83% (2021–2026) and a 2027–2032 gas proposal of 6.46%/6.67% [S1][S3][S4][S9].

---

## 3. United States — FERC and the state commissions

The US is the principal alternative to the CAPM-RAB world. Investor-owned utilities are regulated on a **cost-of-service / rate-of-return** basis: the regulator sets a revenue requirement equal to operating expenses + depreciation + taxes + (**rate base × allowed rate of return**) [1us][3us]. Three features distinguish it from Europe. First, the **rate base is original (historical) cost**, not inflation-indexed — a minority of states permit a "fair value" base [3us][4us]. Second, returns are **nominal**: inflation is recovered through the nominal return and depreciation on original-cost plant rather than asset-base indexation [3us]. Third, rate cases are **episodic** — triggered by a utility filing or a complaint — though many states now add multi-year rate plans and formula rates [9us][30us].

**Legal foundation.** Two Supreme Court cases, *Bluefield* (1923) and *Hope* (1944), establish the constitutional "fair return" standard: the allowed return must be **commensurate with returns on investments of comparable risk**, sufficient to maintain credit and attract capital [5us][7us]. *Hope* added the "end result" test — what matters is whether the overall rate is just and reasonable, not the formula used [7us][8us].

**Cost of equity — DCF as primary tool.** Unlike Europe's CAPM-centrism, US regulators have historically treated the **Discounted Cash Flow (DCF) model** as the primary tool, supplemented by CAPM, risk-premium and comparable/expected-earnings methods [4us][10us]. The constant-growth (Gordon) DCF infers the cost of equity as **k = D₁/P₀ + g** — forward dividend yield plus expected growth — which suits stable, dividend-paying utilities; **multi-stage** variants blend near-term analyst growth with long-run GDP growth [10us][11us].

**FERC.** The Federal Energy Regulatory Commission regulates interstate transmission and interstate gas/oil pipelines. For **natural-gas and oil pipelines**, FERC still relies primarily on a **two-step DCF** (two-thirds short-term analyst growth, one-third long-term GDP growth) [12us][13us]. For **electric transmission**, FERC's methodology has been famously unstable. Opinion No. 531 (2014) imported the two-step DCF and set a New England base ROE of **10.57%** [14us][15us]; after a court remand, **Opinion No. 569 (November 2019)** moved to an average of **DCF and CAPM**, setting the MISO base ROE at **9.88%** (down from 12.38%) [17us][9us]. On rehearing, **Opinion No. 569-A (May 2020)** re-added the **Risk Premium** model — blending DCF, CAPM and Risk Premium — and raised the MISO base ROE to **10.02%**, which **Opinion No. 569-B (November 2020)** affirmed [18us][20us]. Following a further remand, an **October 2024 order reverted to DCF + CAPM only**, eliminating the Risk Premium model and setting the MISO base ROE at **9.98%** [22us][24us] — the current position, and a vivid illustration of the "battle of the models" that characterises US ROE litigation.

**State commissions.** State public utility commissions set most retail ROEs and exercise broad judgment under *Hope/Bluefield*, weighing DCF, CAPM and risk-premium models. Authorised ROEs have clustered in the **~9.5–9.8%** range (nominal): per S&P Global / Regulatory Research Associates, full-year 2024 median authorised ROEs were about **9.70% for both electric and gas** utilities, edging to ~9.70–9.75% in 2025, with authorised common-equity ratios near **50%** [25us][26us][27us].

---

## 4. Asia-Pacific

**Australia — AER.** Australia operates the most rules-based regime of all: a **binding Rate of Return Instrument (RORI)** the AER must remake every four years, which then applies automatically to all network determinations. The **2022 RORI** (final decision 24 February 2023) is a **nominal vanilla WACC** built on a Sharpe-Lintner **CAPM with fixed parameters**: equity beta **0.60**, market risk premium **6.2%**, a risk-free rate from 10-year Commonwealth Government Securities averaged over a short nominated window, and a **10-year trailing-average cost of debt updated annually** at a BBB+ benchmark, with **60% gearing** [au-es][au-land]. The indicative overall WACC sat in the high-5% to ~6.5% range over the instrument's life [au-update]. The **2026 RORI review** is underway (discussion paper 4 August 2025), focused on the equity beta — the domestic listed-comparator pool has shrunk to roughly one firm — and on a possible move to a **weighted** trailing-average cost of debt; a draft is expected in 2026 [au-disc].

**New Zealand — Commerce Commission.** New Zealand runs a notably transparent CAPM/WACC regime under binding Input Methodologies, using the domestic **simplified Brennan-Lally CAPM** (which taxes the risk-free component and uses a tax-adjusted market risk premium, TAMRP). Its hallmark is a **WACC percentile uplift** above the midpoint to guard against under-investment. The history is **75th → 67th (2014) → 65th**: the **2023 IM Review (final decision 13 December 2023) cut the percentile to the 65th** and reset the **TAMRP to 7.0%** (from 7.5%) [nz-im][nz-2014]. Recent determinations show the rate environment lifting WACCs sharply — the Commission reported the electricity distribution price path WACC rising from **4.6% (DPP3) to 7.1% (DPP4)**, with the DY2026 information-disclosure vanilla WACC mid-point around **6.5%** [nz-dpp4][nz-id].

**Japan.** Japan historically set tariffs by the total-cost method — **business profit = rate base × fair rate of return** — administered by METI with scrutiny by the Electricity and Gas Market Surveillance Commission. From **1 April 2023** it introduced **revenue-cap regulation** for the ten transmission-and-distribution operators (first period FY2023–FY2027), with OCCTO coordinating the framework and METI approving each five-year revenue ceiling [jp-egc][jp-gli]. The fair return is a WACC on a **30% equity / 70% debt** structure with a CAPM cost of equity that, because the unbundled networks are unlisted, uses the **pre-Fukushima (2006–2011) parent beta**; the headline WACC, however, is **not published in a single transparent source** [jp-egc2].

**Singapore.** The Energy Market Authority regulates SP PowerAssets on a standard **RAB × WACC building-block** model with a five-year reset, using a 20-year Singapore Government Securities risk-free rate and an "A" benchmark rating. The last firmly documented figure is a **WACC of 5.38%**, finalised in April 2021 for the period to March 2025 [sg-sp][sg-sp2]. (Note: the EMA does not routinely publish the transmission-and-distribution WACC; this figure should be confirmed against the EMA price-control determination, and not conflated with the separate vesting-contract WACC set for a hypothetical new-entrant generator.)

**Hong Kong.** Hong Kong is the clearest example of a **return-on-assets cap rather than a CAPM-WACC**. Under the bilateral Scheme of Control Agreements with CLP Power and HK Electric (signed 2017; effective 2018/2019 to ~2033), the permitted return is **8% of average net fixed assets**, reduced from **9.99%** under the previous scheme [hk-gov][hk-pr] — a single negotiated rate on the whole asset base, with no risk-free-rate-plus-beta build-up, separate cost of debt, or gearing weighting.

**India.** The Central Electricity Regulatory Commission sets inter-state transmission and central-generation tariffs cost-plus over five-year blocks (current: 2024–2029). The **base Return on Equity is 15.50%** (post-tax, grossed up by the effective tax rate), but the 2024–29 regulations **cut the base RoE to 15.00% for new transmission projects** commissioned on or after 1 April 2024 [in-cerc][in-pl]. **South Korea** has **no transparently published regulatory WACC**: KEPCO's tariffs are set administratively by MOTIE with a bounded fuel-cost pass-through, and the statutory "fair return on capital" is not translated into a disclosed percentage [kr-lex].

---

## 5. Cross-cutting synthesis

### Comparison across jurisdictions

| Jurisdiction (regulator) | Primary CoE model | Real vs nominal | Asset-base model | Cost-of-debt approach | RFR / ERP setting | Gearing | Reset cycle | Appeal mechanism |
|---|---|---|---|---|---|---|---|---|
| **UK** (Ofgem, Ofwat) | CAPM | Real (CPIH); RIIO-3 debt semi-nominal | Indexed RAB (CPIH) | iBoxx trailing average (10–14yr) | RFR indexed to 20yr ILGs; TMR on DMS history + ex-ante | Notional 55–60% | 5yr price control | CMA appeal / redetermination |
| **Germany** (BNetzA) | CAPM (global, DMS world ERP) | Real (old assets) / quasi-nominal (new) | RAB, partial inflation reduction | Bond-yield series; 7yr avg under NEST | Umlaufsrendite 10yr avg; world ERP from DMS | Notional 40% equity | 5yr (3yr from NEST) | Courts (OLG, BGH); ECJ on independence |
| **Netherlands** (ACM) | CAPM | Nominal (all sectors from 2027) | RAB | NL bond, trailing avg; 10yr step | 3yr trailing govt bonds (NL/DE) → 20yr; ERP 5.0% | Notional ~50% | ~5yr method decision | CBb (Trade & Industry Appeals Tribunal) |
| **Italy** (ARERA) | CAPM | Real, pre-tax | RAB | iBoxx BBB corporate indices | DE/FR/BE/NL 10yr basket + Italian CRP; TMR ~6% | Notional ~50% | 6yr, 3yr sub-period + annual trigger | Administrative courts (TAR/Consiglio di Stato) |
| **Spain** (CNMC) | CAPM (TRF) | Nominal, pre-tax | RAB | Mixed historical + forward | Spanish 10yr bono 5yr avg (QE-adjusted) | Regulatory parameter | 6yr | Administrative courts |
| **United States** (FERC, state PUCs) | **DCF primary** (+ CAPM, risk premium) | **Nominal** | **Original-cost rate base** | **Embedded (actual) cost of debt** | Market DCF growth; CAPM/risk-premium supplement | Often **actual** ~50% equity | **Episodic** rate cases (+ multi-year plans) | Rehearing → federal courts of appeal |
| **Australia** (AER) | CAPM (fixed MRP) | Nominal | RAB (indexed) | 10yr trailing average, annual update | 10yr CGS over averaging period; MRP fixed 6.2% | Notional 60% | **Binding 4yr instrument** | Limited merits review (now constrained) |
| **New Zealand** (ComCom) | Brennan-Lally CAPM | Real / post-tax vanilla | RAB | Risk-free + debt premium | TAMRP 7.0%; **65th-percentile WACC uplift** | Notional ~42% | 5yr (with annual ID) | High Court / merits appeal on IMs |
| **Japan** (METI/EGC) | CAPM (pre-2011 parent beta) | n/a (not disclosed) | Rate base | Bond yields | JGB risk-free | 30% equity | 5yr revenue cap (from FY2023) | Administrative review |
| **Hong Kong** (Govt SCAs) | **None (negotiated cap)** | n/a | Net fixed assets | n/a | n/a | n/a | ~15yr agreement | Bilateral renegotiation |
| **India** (CERC) | Cost-plus regulated RoE | Nominal, post-tax (grossed up) | Rate base | Actual debt cost | Fixed base RoE 15.0–15.5% | 70% debt norm | 5yr tariff block | Appellate Tribunal (APTEL) |

*All values reflect the most recent determinations identified as of June 2026; several (notably Germany's NEST WACC, Australia's headline annual WACC, and Japan's allowed WACC) are not published as single transparent figures and are characterised accordingly. Indicative parameters are approximate.*

### The methodological fault lines

**CAPM-RAB versus DCF-rate-of-return.** The deepest divide is between the US and almost everyone else. The US infers the cost of equity from **market prices and expected dividend growth** (DCF), applied to an **original-cost rate base** in **episodic** rate cases with the utility's **actual** capital structure. The UK, EU, Australia and New Zealand instead **build up** the cost of equity from CAPM components, apply it to an **inflation-indexed RAB**, use a **notional** capital structure, and reset on a **fixed multi-year cycle**. The approaches can converge in outcome — a US allowed ROE of ~9.7% nominal on ~50% equity is, once inflation and gearing are reconciled, not far from a European real CoE of 5–6% — but they rest on opposite philosophies of what "the cost of capital" is: an observed market-implied number versus a constructed risk-premium estimate. FERC's oscillation between DCF-only, DCF+CAPM and DCF+CAPM+Risk-Premium shows how the DCF approach, for all its market-grounding, struggles for stability [22us][24us].

**Real versus nominal.** The RAB-indexation and real/nominal choices are two sides of one coin. Where the asset base is uplifted by inflation (UK, Italy, Australia, New Zealand) the return is real; where it is held at historic cost (US, and increasingly Dutch and Spanish nominal practice) the return is nominal, recovering inflation through the return plus depreciation. The trend is not monotonic: the Netherlands moves its electricity networks **to** nominal from 2027 [N6], and the UK's RIIO-3 "semi-nominal" debt allowance is a partial move the same way [5] — both responses to a higher, more volatile rate environment in which fully-real allowances under-delivered cash.

**Historical versus forward-looking ERP.** The equity risk premium is where the companion DMS note bites hardest. The UK and Germany **anchor the ERP/TMR on the DMS long-run historical dataset** — Ofgem on UK history, BNetzA via a "global CAPM" on the DMS world premium [1][4]. Australia fixes the MRP for four years (6.2%) [au-es]; New Zealand fixes a TAMRP (7.0%) [nz-im]. The US instead derives its forward equity expectation **from current market dividend yields and analyst growth forecasts** — inherently more market-implied and time-varying. The debate is concrete: a German allowance moves with a ten-year Umlaufsrendite average; a US DCF result moves with this quarter's share prices and analyst estimates.

**Rules versus discretion.** Jurisdictions differ in how much they bind the regulator. Australia's **binding RORI** and New Zealand's **Input Methodologies** sit at the rules end — parameters fixed for four to five years, applied mechanically, with appeal rights deliberately narrowed. The US sits at the discretion end — a "battle of the models" resolved case by case under the open-ended *Hope/Bluefield* standard. Germany captures the tension: the **ECJ's C-718/18 ruling forced a shift *toward* discretion**, stripping binding legislative formulae and handing methodology-setting to BNetzA [1][2] — the mirror image of Australia's move toward rules. The UK sits between, with regulator-led reviews disciplined by CMA appeal; the CMA's willingness to "aim up" when it redetermines (PR19) but defer when it reviews (RIIO-2) shows how much the *institutional role* of the appellate body shapes the cost of capital consumers ultimately pay [6][17].

---

## Sources

**United Kingdom**

[1] Oxera, *RIIO-2 Final Determinations: how final?* (Dec 2020) — https://www.oxera.com/insights/agenda/articles/riio-2-final-determinations-how-final/
[3] Oxera, *RIIO-ED2 Final Determinations* (Nov 2022) — https://www.oxera.com/insights/agenda/articles/riio-ed2-final-determinations/
[4] Ofgem, *RIIO-3 Sector Specific Methodology Decision — Finance Annex* (18 Jul 2024) — https://www.ofgem.gov.uk/sites/default/files/2024-07/RIIO-3_SSMD_Finance_Annex.pdf
[5] Ofgem, *RIIO-3 Final Determinations — Finance Annex* (4 Dec 2025) — https://www.ofgem.gov.uk/sites/default/files/2025-12/RIIO-3-Final-Determinations-Finance-Annex.pdf ; decision page — https://www.ofgem.gov.uk/decision/riio-3-final-determinations-electricity-transmission-gas-distribution-and-gas-transmission-sectors
[6] Oxera, *RIIO-2 appeals: CMA Final Determination* (Oct 2021) — https://www.oxera.com/insights/agenda/articles/riio-2-appeals-cma-final-determination/
[7] National Grid, *Ofgem's RIIO-T3 Final Determination published: National Grid response* (4 Dec 2025) — https://www.nationalgrid.com/ofgems-riio-t3-final-determination-published-national-grid-response
[8] Ofgem, *RIIO-2 Final Determinations — Finance Annex (revised)* (Feb 2021) — https://www.ofgem.gov.uk/sites/default/files/docs/2021/02/final_determinations_-_finance_annex_revised_002.pdf
[9] Oxera, *RIIO-3 Final Determinations* (Dec 2025) — https://www.oxera.com/insights/agenda/articles/riio-3-final-determinations/
[10] Ofgem, *RIIO-ED2 SSMD Annex 3 — Finance* (RFR indexation to 20yr ILGs) — https://www.ofgem.gov.uk/sites/default/files/docs/2021/03/riio_ed2_ssmd_annex_3_finance_0.pdf
[11] London Business School / UBS, *Global Investment Returns Yearbook 2025/2026* (Dimson–Marsh–Staunton) — https://www.london.edu/news/ubs-global-investment-returns-yearbook-2026-history-risk-and-return-in-turbulent-times
[14] Ofwat, *PR24 Final Determinations — Aligning risk and return* (19 Dec 2024) — https://www.ofwat.gov.uk/wp-content/uploads/2024/12/PR24-final-determinations-Aligning-risk-and-return-1.pdf
[15] Ofwat, *PR24 Final Determinations — Allowed return appendix* (Dec 2024) — https://www.ofwat.gov.uk/wp-content/uploads/2024/12/PR24-final-determinations-Aligning-risk-and-return-Allowed-return-Appendix.pdf
[17] CMA, *Water redeterminations (PR19) — summary* (17 Mar 2021) — https://assets.publishing.service.gov.uk/media/604fa141e90e077fe7a5f45a/-_CMA_water_redeterminations_-_summary_-_online_version_---_-.pdf
[18] Oxera, *CMA PR19 Final Determinations* — https://www.oxera.com/insights/agenda/articles/cma-pr19-final-determinations/
[19] CMA, *RIIO-2 Energy Licence Modification Appeals — Summary of final determination* (28 Oct 2021) — https://assets.publishing.service.gov.uk/media/61791296d3bf7f55ff1fc099/Energy_appeals_-_Summary_of_final_determination_28.10.21.pdf
[21] Slaughter and May, *Regulated Asset Base Models* — https://www.slaughterandmay.com/insights/new-insights/regulated-asset-base-models-their-role-in-energy-and-infrastructure-investment-in-the-uk/
[22] UK Regulators Network, *Cost of Capital — guidance* (22 Mar 2023) — https://ukrn.org.uk/app/uploads/2023/03/CoC-guidance_22.03.23.pdf

**EU / Continental Europe**

[1eu/2eu] White & Case, *ECJ on Independence of German Energy Regulator (C-718/18)* — https://www.whitecase.com/insight-alert/european-court-justice-independence-german-energy-regulator ; Recht energisch, *Donnerschlag: EuGH v. 2.9.2021 (C-718/18)* — https://recht-energisch.de/2021/09/03/donnerschlag-die-entscheidung-des-eugh-v-2-9-2021-zur-bundesnetzagentur-c-718-18/
[3eu] rhenag-legal, *BGH bestätigt EK-Zinssätze der BNetzA für die 4. Regulierungsperiode* — https://rhenag-legal.de/blog/bgh-bestaetigt-die-festlegung-der-eigenkapitalzinssaetze-der-bundesnetzagentur-fuer-die-vierte-regulierungsperiode
[4eu] Frontier Economics, *Estimating cost of equity for German gas and electricity networks* — https://www.frontier-economics.com/uk/en/news-and-insights/news/news-article-i8670-estimating-cost-of-equity-for-german-gas-and-electricity-networks/
[5eu] Randl/Zechner Gutachten for BNetzA (*Zuschläge/Wagnisse*) — https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Energie/Unternehmen_Institutionen/Netzentgelte/Anreizregulierung/Gutachten/GutachtenZuschl%C3%A4geWagnisse.pdf
[8eu] Grant Thornton, *Neue WACC-Berechnung für Netzbetreiber* (2025) — https://www.grantthornton.de/themen/2025/aktuelle-entwicklungen-zur-eigenkapitalverzinsung-von-netzbetreibern-neue-wacc-berechnung-im-fokus/
[9eu/10eu] WIK Working Paper No. 11 (Dec 2025) — https://www.wik.org/fileadmin/user_upload/Unternehmen/Veroeffentlichungen/Working_Papers/2025/WIK-Working_Paper_No11.pdf ; Herbert Smith Freehills Kramer, *NEST Decisions* — https://www.hsfkramer.com/notes/energy/2026-posts/nest-decisions-set-new-course-for-german-electricity-and-gas-network-regulation
[N1] ACM/Brattle, *The WACC for the Dutch Electricity TSO and Electricity and Gas DSOs* — https://www.acm.nl/sites/default/files/documents/the-wacc-for-the-dutch-electricity-tso-and-electricity-and-gas-dsos.pdf
[N2] ACM, *Bijlage 3 — WACC (methodebesluit 2022-2026)* — https://www.acm.nl/sites/default/files/documents/bijlage-3-wacc-elektriciteit.pdf
[N4] CBb ruling ECLI:NL:CBB:2023:318 — https://www.omgevingsweb.nl/jurisprudentie/eclinlcbb2023318/
[N5] Lexology, *Regulation of electricity and gas network tariffs for 2022 to 2026 (Netherlands)* — https://www.lexology.com/library/detail.aspx?g=f0449e6b-146b-4b52-ae7a-2be459040324
[N6] Oxera, *Note on ACM's draft method decisions for REG2027* (Sep 2025) — https://www.oxera.com/wp-content/uploads/2025/09/Note-on-ACMs-draft-method-decisions-for-REG2027.pdf
[N7] ACM, *Methodebesluit TenneT op land 2027-2031* — https://www.acm.nl/nl/publicaties/methodebesluit-tennet-op-land-2027-2031
[I1] ARERA, *Deliberazione 614/2021/R/com (TIWACC)* — https://www.arera.it/atti-e-provvedimenti/dettaglio/21/614-21
[I2] ARERA, *TIWACC 2022-2027 — Criteri per la determinazione del WACC* — https://www.arera.it/fileadmin/allegati/docs/21/614-21tiwacc.pdf
[I3] ARERA, *Deliberazione 513/2024/R/com (2025-2027 update)* — https://www.arera.it/atti-e-provvedimenti/dettaglio/24/513-24
[I5] ARERA, *513/2024 Allegato A* — https://www.arera.it/fileadmin/allegati/docs/24/513-2024-R-com-ALLEGATO_A.pdf
[A12] E-Control, *Cost Methodology 2021–2024 (EN)* — https://www.e-control.at/documents/1785851/1811582/E-Control_Cost_Methodology_2021_2024_EN.pdf
[A14] E-Control, *WACC Neuinvestitionen 2025* — https://www.e-control.at/documents/1785851/0/WACC_Neuinvestitionen_2025.pdf
[A15] E-Control, *Aktualisierung des WACC für Neuinvestitionen 2026* (Sep 2025) — https://www.e-control.at/documents/1785851/1811582/20250903_Gasverteiler_Stromverteiler_Stromübertragung_WACC_Neuinvest.pdf
[A18] NERA, *Innovation in incentive regulation — efficiency-dependent WACC (Austria)* — https://www.nera.com/experience/2019/innovation-in-incentive-regulation---introduction-of-an-efficien.html
[S1] CNMC, *Circulares de retribución de las redes eléctricas — tasa 6,58%* (22 Dec 2025) — https://www.cnmc.es/prensa/circulares-retribucion-electrica-20251222
[S3] BOE, *Circular 2/2019 (TRF electricidad y gas)* — https://www.boe.es/buscar/doc.php?id=BOE-A-2019-16639
[S4] BOE, *Circular 9/2025 (modifica Circular 2/2019)* — https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-27019
[S9] El Periódico de la Energía, *CNMC metodología WACC: 5,58% / 5,44% / 5,83%* — https://elperiodicodelaenergia.com/la-cnmc-aprueba-la-metodologia-wacc-la-tasa-de-retribucion-a-electricas-cae-al-558-la-del-transporte-de-gas-al-544-y-la-distribucion-de-gas-al-583/
[E1] CEER, *Report on Regulatory Frameworks for European Energy Networks 2025* (22 Jan 2026) — https://www.ceer.eu/publication/report-on-regulatory-frameworks-for-european-energy-networks-2025/
[E4] ACER, *Report on investment evaluation, risk assessment and regulatory incentives* (Jun 2023) — https://www.acer.europa.eu/sites/default/files/documents/Publications/ACER_Report_Risks_Incentives.pdf
[E5] ACER, *Electricity Network Tariff Practices in Europe* (Mar 2025) — https://www.acer.europa.eu/sites/default/files/documents/Reports/2025-ACER-Electricity-Network-Tariff-Practices.pdf

**United States**

[1us] NARUC, *What is "Cost of Service" Regulation?* — https://pubs.naruc.org/pub.cfm?id=538E730E-2354-D714-51A6-5B621A9534CB
[3us] M. Jamison (Univ. of Florida PURC), *Rate of Return: Regulation* — https://bear.warrington.ufl.edu/centers/purc/docs/papers/0528_jamison_rate_of_return.pdf
[4us] *The DCF Methodology: Its Use in Estimating a Utility's Cost of Equity*, 12 Energy L.J. 265 (1991) — https://www.eba-net.org/wp-content/uploads/2023/02/26_12EnergyLJ2651991.pdf
[5us] *Bluefield Waterworks v. Public Service Comm'n*, 262 U.S. 679 (1923) — https://www.law.cornell.edu/supremecourt/text/262/679
[7us/8us] *FPC v. Hope Natural Gas Co.*, 320 U.S. 591 (1944) — https://supreme.justia.com/cases/federal/us/320/591/
[9us] FERC, *FERC Revises Public Utility ROE Methodology; Sets Policy for Natural Gas, Oil Pipelines* (21 May 2020) — https://www.ferc.gov/news-events/news/ferc-revises-public-utility-roe-methodology-sets-policy-natural-gas-oil-pipelines
[10us] A. Damodaran (NYU Stern), *Dividend Discount Models* — https://pages.stern.nyu.edu/~adamodar/pdfiles/ddm.pdf
[11us] Wall Street Prep, *Gordon Growth Model* — https://www.wallstreetprep.com/knowledge/gordon-growth-model/
[12us] Blank Rome, *FERC Establishes Revised ROE Methodologies for Public Utilities and Pipelines* — https://www.blankrome.com/publications/ferc-establishes-revised-roe-methodologies-public-utilities-and-pipelines
[13us] Jones Day, *FERC Acts to Ensure Utility Cost-Based Rates Include an Adequate Return on Equity* (2014; two-step DCF) — https://www.jonesday.com/en/insights/2014/06/ferc-acts-to-ensure-that-utility-cost-based-rates-include-an-adequate-return-on-equity
[14us/15us] National Law Review, *FERC Establishes New England ROE (Opinion 531)* — https://natlawreview.com/article/ferc-establishes-new-england-return-equity-roe-sets-miso-roe-hearing
[17us] Davis Wright Tremaine, *FERC Revises Methodology (Opinion 569, 9.88%)* — https://www.dwt.com/blogs/energy--environmental-law-blog/2019/12/ferc-revises-methodology-for-evaluating-base
[18us] National Law Review, *FERC Again Revises ROE Methodology: Opinion 569-A (10.02%)* — https://natlawreview.com/article/ferc-again-revises-methodology-governing-public-utility-return-equity-opinion-no-569
[20us] Troutman, *FERC Issues Minor Revisions: Opinion 569-B* — https://www.troutmanenergyreport.com/2020/11/ferc-issues-minor-revisions-to-public-utility-roe-methodology/
[22us] Baker Botts, *FERC Revises ROE Methodology for Transmission Owners* (Oct 2024; 9.98%) — https://www.bakerbotts.com/thought-leadership/publications/2024/october/ferc-revises-roe-methodology-for-transmission-owners
[24us] RTO Insider, *FERC Sets MISO TOs' ROE at 9.98%, Again Eliminates Risk Premium Model* — https://www.rtoinsider.com/89798-ferc-sets-miso-tos-roe-eliminates-risk-premium-model/
[25us] S&P Global Market Intelligence, *Rate requests by US energy utilities set record in 2023* — https://www.spglobal.com/market-intelligence/en/news-insights/research/rate-requests-by-us-energy-utilities-set-record-in-2023-for-3rd-straight-year
[26us] S&P Global Market Intelligence, *Underearning spread widens for gas, electric utilities in ROE analysis* — https://www.spglobal.com/market-intelligence/en/news-insights/research/underearning-spread-widens-for-gas-electric-utilities-in-roe-analysis
[30us] RMI, *Multi-Year Rate Plans* — https://affordability-toolkit.rmi.org/policies/multi-year-rate-plans

**Asia-Pacific**

[au-es] AER, *Rate of Return Instrument — Explanatory Statement* (24 Feb 2023) — https://www.aer.gov.au/system/files/AER%20-%20Rate%20of%20Return%20Instrument%20-%20Explanatory%20Statement%20-%2024%20February%202023_1.pdf
[au-update] AER, *Rate of Return Annual Update 2025* (Nov 2025) — https://www.aer.gov.au/system/files/2025-11/AER%20-%20Rate%20of%20Return%20annual%20update%202025.pdf
[au-disc] AER, *2026 RORI Review Discussion Paper* (4 Aug 2025) — https://www.aer.gov.au/system/files/2025-08/AER%20-%202026%20RORI%20review%20discussion%20paper%20-%204%20August%202025.pdf
[nz-im] NZ Commerce Commission, *2023 IM Review — Cost of capital topic paper* (13 Dec 2023) — https://www.comcom.govt.nz/__data/assets/pdf_file/0022/337612/Part-4-IM-Review-2023-Final-decision-Cost-of-capital-topic-paper-13-December-2023.pdf
[nz-dpp4] NZ Commerce Commission, *[2024] NZCC 21 — Cost of capital determination EDB DPP4 and Transpower RCP4* (25 Sep 2024) — https://www.comcom.govt.nz/assets/pdf_file/0022/362524/5B20245D-NZCC-21-Cost-of-capital-determination-EDB-DPP4-and-Transpower-RCP4-25-September-2024.pdf
[nz-id] NZ Commerce Commission, *[2025] NZCC 7 — Cost of capital determination EDBs and WIAL ID* (6 May 2025) — https://www.comcom.govt.nz/assets/pdf_file/0028/366076/2025-NZCC-7-Cost-of-capital-determination-EDBs-and-WIAL-ID-6-May-2025.pdf
[nz-2014] NZ Commerce Commission, *Amendment to the WACC percentile (75th → 67th)* (30 Oct 2014) — https://comcom.govt.nz/__data/assets/pdf_file/0029/88517/Commerce-Commission-Amendment-to-the-WACC-percentile-for-price-quality-regulation-Reasons-Paper-30-October-2014.PDF
[jp-egc] METI/EGC, *Revenue-cap regulation portal* — https://www.egc.meti.go.jp/info/revenue_cap/
[jp-egc2] METI/EGC, *Rate base & business profit rate* (Tariff System meeting, 19 Jan 2023) — https://www.egc.meti.go.jp/activity/emsc_electricity/pdf/0032_07_02.pdf
[jp-gli] Global Legal Insights, *Energy Laws & Regulations 2026 — Japan* — https://www.globallegalinsights.com/practice-areas/energy-laws-and-regulations/japan/
[sg-sp] EMA, *Electricity Market overview* — https://www.ema.gov.sg/our-energy-story/energy-market-landscape/electricity
[sg-sp2] S&P Global Ratings, *SP PowerAssets Ltd* (EMA-finalized WACC 5.38%, Apr 2021) — https://www.alacrastore.com/s-and-p-credit-research/SP-PowerAssets-Ltd-2764619
[hk-gov] GovHK, *Scheme of Control Agreements* — https://www.gov.hk/en/residents/environment/sustainable/energy/schemeofca.htm
[hk-pr] HK Government press release, new SCAs (25 Apr 2017) — https://www.info.gov.hk/gia/general/201704/25/P2017042500763.htm
[in-cerc] CERC, *Tariff Regulations 2024* (No. L-1/268/2022/CERC) — https://www.cercind.gov.in/regulations/notification-2024.pdf
[in-pl] Power Line, *RoE Adjustments: CERC's draft tariff regulations* (5 Feb 2024) — https://powerline.net.in/2024/02/05/roe-adjustments-key-highlights-of-cercs-draft-tariff-regulations/
[kr-lex] Lexology, *Regulation of power sales in South Korea* — https://www.lexology.com/library/detail.aspx?g=4ba2ca91-58bc-4310-8077-a5e7d708f6c1
