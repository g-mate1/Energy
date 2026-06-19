# Historic Investment Returns — The Dimson–Marsh–Staunton (DMS) Dataset: Deep Dive

*This deep-dive expands the summary report (`01_historic_returns_dms.md`) chapter by chapter and adds an annotated review of the cited literature. Compiled from public sources as of June 2026. The underlying dataset is a paid/subscriber publication (the UBS Global Investment Returns Yearbook and the licensed DMS Database); figures below are drawn from the public summary editions, the authors' academic papers, regulator determinations, and reputable secondary reporting, with vintages and windows stated throughout. The research sub-agents that compiled this material were largely unable to open primary PDFs directly (automated fetching was blocked), so figures rest on cross-verified search extracts of those primary sources; all numbers should be checked against the primary Yearbook and the DMS Database before being relied upon in a regulatory determination. Points that could not be verbatim-verified are flagged in the text.*

---

## Executive summary

The Dimson–Marsh–Staunton (DMS) dataset is the world's most authoritative long-run record of financial-asset returns: 126 years (1900–2025) of equities, bonds, bills, inflation, currencies and now gold across 35 markets and five composite indices, built explicitly to be free of survivorship and "success" bias. Its central, and frequently misread, message is a *caution*: the realised twentieth-century equity premium overstates what investors should expect going forward, because part of the historical return came from a non-repeatable re-rating and because the most-cited evidence (the US) is the single most successful market chosen with hindsight.

Three numbers anchor everything that follows. Over 1900–2024/25 the **World** index returned roughly **5.2% real** on equities, **1.7%** on bonds and **0.5%** on bills, for an equity risk premium (ERP) of about **4.3–4.6%** versus bills. The **United States** returned **6.6% real** on equities — about **2.3 percentage points** above the **4.3%** earned by the rest of the world, the cleanest single measure of US "success bias." And the authors' own **forward-looking** World premium is only **~3–3.5%** geometric, well below the realised figure.

These properties make DMS the empirical backbone of regulatory cost-of-capital decisions — the Total Market Return (TMR) and ERP in the CAPM used by Ofgem, Ofwat and the CMA in the UK, and by the German Bundesnetzagentur (BNetzA) via the Randl/Zechner expert reports. But the dataset sets a *range*, not a number: the determination still turns on the estimation window, the geometric-vs-arithmetic averaging convention, the inflation deflator, and the weight given to forward-looking cross-checks (Damodaran's implied ERP, the Fernandez survey, Fama–French dividend-growth models).

---

## 1. Origins, authorship and the dataset's pedigree

### 1.1 The three authors

The dataset is the work of **Elroy Dimson, Paul Marsh and Mike Staunton** ("DMS"), all of London Business School (LBS):

- **Elroy Dimson** — Professor of Finance and Director of Research (Finance) at **Cambridge Judge Business School**, where he co-founded and chairs the **Centre for Endowment Asset Management (CEAM)**; **Emeritus Professor of Finance at LBS**, where he took his PhD. He co-designed the **FTSE 100** index and chaired the FTSE Russell advisory/policy boards, co-designed the Numis (Hoare Govett) Smaller Companies Index with Marsh, and chaired the Strategy Council of **Norway's sovereign wealth fund** (Government Pension Fund Global). He has won the Financial Analysts Journal *Graham and Dodd Award* and the CFA Institute Research Foundation's *James R. Vertin Award*. (Note: he sat on the *Financial Analysts Journal* Advisory Council; a full FAJ *editorship* could not be verified.)
- **Paul Marsh** — **Emeritus Professor of Finance at LBS** (BSc Econ, LSE, 1968; PhD, LBS, 1977). Former Chair of the LBS Finance area, Faculty Dean and Dean of the Finance Programmes; part of the team that designed the FTSE 100, and co-creator (with Dimson) of the Numis Smaller Companies Index and the LBS Risk Measurement Service (published since 1979). Awarded Fellowship of CFA UK.
- **Mike Staunton** — **Professor Emeritus of Finance** and Director of the **London Share Price Database (LSPD)** at LBS; co-author of *Triumph of the Optimists* and co-producer of the Yearbook and the Risk Measurement Service. (Public biographical detail on Staunton is thinner than for his co-authors.)

### 1.2 *Triumph of the Optimists* and the "Millennium Book"

Preliminary versions of the data circulated privately as **The Millennium Book (2000)** and **Millennium Book II (2001)**, supported by **ABN AMRO** and LBS to compile an authoritative century-long record of UK (and then international) market performance. This became the 2002 monograph:

> **Dimson, E., Marsh, P. & Staunton, M. (2002). *Triumph of the Optimists: 101 Years of Global Investment Returns*. Princeton University Press.** ISBN 0-691-09194-3 / 978-0-691-09194-5; e-book 9781400829477; xii + 339 pp.; ~130 colour diagrams.

The book assembled internally consistent total-return series for equities, bonds, bills, currencies and inflation across **16 countries** for 1900–2000: the US, UK, Japan, France, Germany, Canada, Italy, Spain, Switzerland, Australia, the Netherlands, Sweden, Belgium, Ireland, Denmark and South Africa. The title is deliberately ironic — equity optimists were rewarded *ex post*, but the very record that vindicates them is drawn from surviving, successful markets, so optimism looks wiser in hindsight than it was *ex ante* (the ebook page quotes Don Marquis: "an optimist is someone who never had much experience").

### 1.3 The Yearbook and its publisher chain

Since 2000 the dataset has been refreshed annually as the **Global Investment Returns Yearbook**, with two publisher transitions:

| Era | Editions | Publisher / sponsor |
|---|---|---|
| ABN AMRO | 2000 – ~2009 | ABN AMRO with LBS (the 2008 edition was the 9th) |
| Credit Suisse | 2010 – 2023 | **Credit Suisse Research Institute** (first CS edition Feb 2010, adding Finland and New Zealand to reach 19 markets) |
| UBS | 2024 – present | **UBS** (Investment Bank + Global Wealth Management CIO), following UBS's acquisition of Credit Suisse |

UBS **announced** the all-stock acquisition of Credit Suisse (CHF 3bn; exchange ratio 1 UBS share per 22.48 CS shares) on **19 March 2023** and **completed** it on **12 June 2023**. The **2024 edition** (28 February 2024) was the first UBS-branded Yearbook, described by UBS as marking "the continuity of a longstanding partnership with the authors" and as being "in its 25th year." Subsequent editions: **2025** (4 March 2025, 125 years, 1900–2024); **2026** (3 March 2026, "26th year," up to 126 years, 1900–2025, with the LBS strapline "History, risk and return in turbulent times").

### 1.4 The DMS Database (via Morningstar) and the academic record

The underlying data is licensed for research as the **Dimson-Marsh-Staunton (DMS) Global Investment Returns data module, distributed through Morningstar Inc.** The module is described as providing annual total returns for stocks, government bonds, treasury bills, inflation, exchange rates and maturity/equity premiums for roughly **40 markets** (28 from 1900), supplied as a documented Excel file at an annual licence quoted around **GBP 4,000 + VAT** (the 40-market module is a larger universe than the ~35 markets profiled in the Yearbook; the exact count and pricing should be re-checked on a current Morningstar page). The project also underpins LBS's REF impact case study *"Long-Run Global Asset Returns"* (case study Id 44521), which credits the data with informing major investors' strategy and "guiding regulation of … utilities."

---

## 2. Coverage and data construction

### 2.1 Markets, composites and the 21-vs-23 distinction

The 2024–2026 editions cover **35 markets** plus **five composite indices** — World, World ex-US, Europe, Developed and Emerging. Of the 35, **23 reach back to 1900**, but only **21 have continuous (unbroken) histories**: **China and Russia have "broken" histories** because their pre-revolution markets suffered total losses and were re-started later. This is the source of the long-standing "21 vs 23" ambiguity — older write-ups cite 21 (continuous only), current editions cite 23 (including China and Russia). The remaining 12 of the 35 markets begin in the second half of the twentieth century with close to or more than 50 years of data. (The full enumeration of all 35 — especially the 12 later starters — could not be verified from public summaries; one stray secondary reference to "40 markets" conflates the Yearbook with the larger Morningstar module and should be disregarded.)

Beyond the 35 core markets, the Yearbook's equity world index is built on a **~90-country investable universe** back to 1900 — "a comprehensive all-country investable universe." The 23 markets with 1900 histories covered **~98% of global equity market capitalisation in 1900**; for the older 17-country academic sample DMS reported 91% of world cap in 2006 and 90% in 1900. As of the 2026 edition the **US alone is ~62%** of world equity market capitalisation.

### 2.2 Asset classes

For each market the dataset gives annual **real and nominal** returns on **equities, long-term government bonds and treasury bills**, plus **inflation (CPI)** and **currencies/exchange rates**, with **GDP** as a supporting series. The 2025/2026 editions **added gold** as an asset class (spot gold over the post-Bretton-Woods period from **1972**, sourced from the World Gold Council). The Yearbook also publishes evidence on **factor/style premia** (size, value, income/yield, momentum, low volatility). All equity/bond/bill series are **total returns with income reinvested**.

### 2.3 How the indices are constructed

- **Currency and weighting.** The World index is **USD-denominated**, with each country **weighted by its start-of-year equity market capitalisation** where cap data exist, and by **GDP** for the early decades before capitalisations were available. A common-currency basis makes cross-country returns comparable and makes exchange-rate movements an explicit return component. There are several "world" indices (World, World ex-US, Europe, Developed, Emerging).
- **Splicing of historical series.** DMS splice their own back-histories onto modern index data. For the **US**, the lineage runs through **CRSP** (University of Chicago) post-1926, spliced to Cowles Commission and earlier reconstructions; for the **UK**, the back-history rests on the **London Share Price Database (LSPD)** maintained at LBS. Other countries are assembled from national exchange records, official statistics and academic reconstructions, documented in the Yearbook/Sourcebook country-by-country sources appendix.
- **Handling market closures and gaps.** Where exchanges closed or data are missing (e.g. France 1940, Portugal 1974–77, the 1945 dislocations in Germany and Japan), DMS fill gaps by interpolation/generated estimates rather than dropping the period — a known limitation (Barro and others caution that the war-period entries are partly interpolated). The precise interpolation rule for a closed market is not documented in accessible summaries.

### 2.4 Survivorship and "success" bias — the defining contribution

The dataset's signature is the correction of two biases:

- **Survivorship bias** — indices that quietly drop failed companies/markets overstate returns.
- **Success bias** — extrapolating from a market chosen *because* it succeeded (the US) overstates what a global investor could have expected.

DMS deliberately retain markets that did badly — Germany, Japan, Italy, Austria, Belgium — rather than excising them. Austria-Hungary (~5% of the 1900 World index) was the worst-performing equity market among the 21 continuous-history countries. Crucially, DMS **do not drop Germany's 1922–23 hyperinflation** to flatter the figures; on the contrary, including it is what makes German bonds the worst long-run fixed-income market. The residual critique runs the *other* way: the dataset still omits some total-loss markets (Poland, Hungary, Czechoslovakia), so the global average is, if anything, still slightly **upward** biased — what the EH.net reviewer (John A. James, University of Virginia) and DMS themselves call **"easy-data bias."** Later editions added **Austria, China and Russia** (Russia was ~6% of 1900 world cap) precisely to reduce this bias.

### 2.5 Revisions over time

The database is "updated, extended and analysed annually," and back-history is periodically revised as upstream sources improve (e.g. the 2025 Yearbook noted changes to US factor premia "from revisions to the historical data on Professor Ken French's website"). Coverage has grown from 16 countries (2002) → 17 (2006 paper) → 19 (2010) → 21 continuous / 23-from-1900 → **35 markets** today, with the five composites, the 90-country world index, and gold added over successive editions. Because the back-history is revised and the window lengthens each year, **headline numbers shift slightly edition to edition** — a point that matters when a determination cites "the latest Yearbook."

---

## 3. Headline long-run returns and risk premia

All headline figures are **real (inflation-adjusted), geometric (compound) means** unless stated. A recurring confusion must be flagged up front: the 2026 launch led with **US** numbers (6.6% real equity), which are well above the **World** figure (~5.2%).

### 3.1 The World index (multiple windows)

| Metric | Figure | Window / edition |
|---|---|---|
| Real equity return | **5.2%** | 1900–2024 (GIRY 2025) and 1900–2025 (GIRY 2026) |
| Real bond return | **1.7%** | 1900–2024/25 |
| Real bill return | **0.5%** | 1900–2024/25 |
| Real equity return | 5.5% | 1900–2010, 19 countries ("Equity Premia Around the World") |
| ERP vs bills | **4.3–4.6%** | recent editions / 1900–2010 (4.5%) |
| ERP vs bonds | **3.1–3.8%** | window-dependent (3.2% to 1900–2015; 3.8% to 1900–2010) |
| Real equity, since 2000 | **3.5%** (ERP vs bills 4.3%) | 2000–2024/25 (reported in BOTH 2025 and 2026 editions) |

The headline World real-equity figure drifts with window, currency basis and country count (5.0–5.5%), but ~5% is the durable "unbiased prior."

### 3.2 The United States

US real equity returned **6.6% p.a.** over 1900–2025 (the same 6.6% appears for 1900–2024 in the 2025 edition), versus **1.6%** for bonds. **USD 1 invested in US equities in 1900 grew to USD 3,296 in real terms** (USD 124,854 nominal) by end-2025, against USD 284 (long bonds) and USD 69 (bills) nominal. From the original book (1900–2000), US equities returned **10.1% nominal / 6.7% real** (σ = 20.2%). The historical US ERP versus bills was **5.3% geometric / 7.2% arithmetic** (1900–2002) — a ~1.9-point arithmetic-geometric gap — with a DMS forward-looking estimate of **4.3%**.

### 3.3 Country detail and the best/worst markets

From the original book (1900–2000, real geometric), returns ranged from **2.5% (Belgium, worst) to 7.6% (Sweden, best)**, with equity standard deviations of 17–32%. The US (6.7%) and UK (5.8%) are firmly verified; the often-quoted **Germany ~3.6%** and **Japan ~4.5%** figures come from secondary reviews of the book's tables and should be treated as book-vintage figures rather than independently confirmed. On recent USD-basis windows (1900–2022) the best continuous markets were **Australia (6.43%)** and the **US (6.38%)**, with **South Africa** at ~7.2% local / 6.4% USD — so the "best market" label flips between Sweden, Australia and South Africa depending on edition and local-vs-USD basis. Critically, in the latest editions **every market with a continuous 1900 history — Germany included — has delivered a positive real equity return.**

| Market | Real equity (geo, % p.a.) | Window / basis |
|---|---|---|
| World | ~5.2 | 1900–2025 |
| World ex-US | ~4.3 | 1900–2024 |
| United States | 6.6 (6.7 in book) | 1900–2025 (1900–2000) |
| United Kingdom | 5.8 | 1900–2000 (book) |
| Germany | ~3.6 (book, via secondary review) | 1900–2000 |
| Japan | ~4.5 (book, via secondary review) | 1900–2000 |
| Sweden | 7.6 (best, book) | 1900–2000 |
| Belgium | 2.5 (worst, book) | 1900–2000 |
| Australia | 6.43 (best, recent) | 1900–2022, USD |
| South Africa | 7.2 local / 6.4 USD | recent editions |

### 3.4 Germany and the 1922–23 hyperinflation — a case study

Germany is the canonical illustration of why a global, not US-centric, record matters. The mark collapsed from ~320/USD (mid-1922) to ~**4.2 trillion marks/USD by November 1923**. Equity holders survived in real terms over the full century (~3.6% in the book), but **bond and bill holders were wiped out** (−100% in 1922–23). Germany is one of **five countries — with Japan, Italy, France and Belgium — showing negative real returns on both bonds and bills over 1900–2000.** Because the hyperinflation so distorts the statistics, DMS **exclude 1922–23 for Germany** (and 1921–22 for Austria) from bond/bill and equity-premium computations, so the German premium is measured over 109 years. German real-equity volatility (σ ≈ 31.7%) is among the highest in the sample. (The often-repeated claim that German bondholders lost a *further* ~92% in real terms after WWII appears in secondary reviews but could not be independently verified.)

### 3.5 The twenty-first-century window

Since 2000 the World real equity return has been only **3.5%** (ERP vs bills 4.3%) — well below the ~5% full-history figure — which is exactly why the choice of estimation window can move a regulatory TMR by more than a percentage point.

---

## 4. Methodology in depth

### 4.1 Real versus nominal

DMS emphasise **real** returns for long-run, cross-country comparison because inflation experiences differ enormously (Germany's hyperinflation being the extreme). For cross-country aggregation they convert to a **common currency (USD)**, so exchange-rate changes enter explicitly. Headline figures are quoted in real geometric terms; the long-run scale of inflation is illustrated by DMS's own example that USD 1 in 1900 had the purchasing power of ~USD 37 today.

### 4.2 Geometric versus arithmetic means — and the estimators in between

The **geometric** mean is the realised compound (buy-and-hold) rate — correct for *describing* past multi-period performance. The **arithmetic** mean is higher for any volatile series and is, in principle, the unbiased estimate of *next period's* expected return. DMS illustrate the gap with two equally likely returns of **+25% and −20%**: arithmetic mean **2.5%**, geometric mean **0%** (since 1.25 × 0.80 − 1 = 0).

- **The half-variance rule.** Geometric ≈ Arithmetic − ½σ² (exact under log-normality). For equities with σ ≈ 17–20%, the gap is ~**1.5–2 points** (e.g. the US ERP: 7.2% arithmetic vs 5.3% geometric ≈ 1.9 points).
- **Which mean for cost of capital?** The textbook (Damodaran) position: arithmetic suits a one-period CAPM with serially uncorrelated annual returns; as the horizon lengthens or returns mean-revert, the geometric figure becomes more appropriate. Because a finite-sample arithmetic mean is itself an upward-biased estimate of long-horizon compound wealth, practitioners use a **blend**:
  - **Blume (1974)**: unbiased N-period estimate = [(T−N)/(T−1)]·Arithmetic + [(N−1)/(T−1)]·Geometric (T = sample length, N = horizon); equals the arithmetic mean at N = 1 and the geometric mean at N = T.
  - **Jacquier–Kane–Marcus (2003)**: compounding at the arithmetic mean over-forecasts terminal wealth; the unbiased compound rate ≈ **(1 − H/T)·Arithmetic + (H/T)·Geometric** (H = horizon), shifting weight to the geometric mean as H rises toward T. For 40-year horizons the bias in cumulative-value forecasts "can easily exceed a factor of 2."
  - **Cooper (1996)**: derives an unbiased *discount factor* correcting for estimation error and serial correlation; concludes the corrected rate sits **closer to the arithmetic than the geometric** mean — the result regulators lean on to justify discount rates above the geometric figure. (Kaserer (2022) surveys these and notes Cooper-type estimators are more robust to serial correlation than Blume.)

This is precisely why UK regulators estimate a TMR *range* spanning both bases, and why the CMA uses arithmetic, Blume and JKM estimators side by side (Section 5).

### 4.3 Decomposition of equity returns

DMS decompose the real equity return / premium into: **mean dividend yield + real (geometric) dividend growth + expansion of the price/dividend multiple (re-rating) + change in the real exchange rate − the real risk-free rate**. The qualitative finding is load-bearing: **the dividend (income) yield is overwhelmingly the dominant, repeatable driver of long-run returns**; real dividend growth is small (~0.7%/yr, single-source); and multiple expansion ("repricing") contributed materially to *realised* returns but is **not repeatable** — the empirical hinge of the ex-post/ex-ante distinction below.

### 4.4 Mean reversion and serial correlation

DMS find **no convincing evidence of decade-to-decade mean reversion**: poor returns in one decade are not reliably followed by good ones; equities behave "much like a random walk," and the popular belief that long horizons reduce equity risk is, in the Yearbook's phrase, an **"optical illusion."** This engages a long literature: **Poterba–Summers (1988)** and **Fama–French (1988)** found returns positively autocorrelated at short horizons and negatively autocorrelated at long horizons (evidence *for* mean reversion), but later work (Kim–Nelson–Startz) showed variance-ratio tests "have little power against the principal interesting alternatives," and that the results can reverse after small-sample corrections — the weak-evidence reading DMS endorse. The practical implication: one cannot rely on mean reversion either to shrink long-horizon risk or to assume historical averages will "self-correct."

### 4.5 Ex-post versus ex-ante premia

DMS sharply separate the **ex-post (realised, measurable)** premium from the **ex-ante (prospective, expected)** premium, arguing realised excess returns should be called *excess returns*, not "the equity risk premium." Their load-bearing claim:

> "The mean equity premium will overstate the prospective risk premium … because historical returns are inflated by past repricings that were triggered by a reduction in the risk premium."

Stripping out the non-repeatable repricing yields a **prospective World premium of ~3–3.5% geometric (~4.5–5% arithmetic)** — about a point below the realised figure. Their 2003 country estimates put the **forward-looking** premium (vs bills) at **US 4.3%, UK 3.9%, World 3.5%**, against historical comparators of 5.3%, 4.2% and 4.5%.

---

## 5. Regulatory relevance

DMS data are the empirical backbone of network cost-of-capital decisions in the UK and, increasingly, continental Europe. Regulators run a CAPM in which the **TMR** (and hence **ERP = TMR − risk-free rate**) is anchored on long-run history.

### 5.1 TMR-based versus ERP-based framing, and the UKRN study

UK regulators favour a **"TMR-based"** approach: estimate the *total* market return directly from long-run history (comparatively stable across mature markets), then derive the ERP as a **balancing figure** against the prevailing risk-free rate — preferred to an "ERP-based" approach because the evidence for a stable ERP is weaker than for a stable TMR. This was codified by the **UKRN study (Wright, Burns, Mason & Pickford, 2018)**, which recommended anchoring the equity building block on a stable long-run **DMS-based TMR** and supported a real **TMR of ~6–7% CPI-real (≈5–6% RPI-real)**, and by the subsequent UKRN cost-of-capital guidance (2023).

### 5.2 Ofgem (RIIO)

Ofgem uses DMS as its **primary** TMR source, cross-checked against the Bank of England dividend-discount model. In **RIIO-2/ED2** the TMR was **6.25–6.75% CPIH-real** (midpoint 6.5%), giving an allowed CPIH-real cost of equity of **4.55%** (RIIO-2) and **5.23%** (RIIO-ED2, Nov 2022) at 60% notional gearing. For **RIIO-3** (Final Determinations, 4 December 2025) Ofgem raised the TMR range to **6.5–7%**, weighting ex-ante and ex-post estimates equally (ex-post assessed at ~7%), and set the allowed CPIH-real cost of equity at about **5.70% for electricity transmission (at 55% gearing)** and **6.12% for the gas networks (at 60%)** — both citing the latest DMS Yearbook — while dropping the RIIO-2 "outperformance wedge."

### 5.3 Ofwat (PR24) and the CMA

For **PR24** (Final Determinations, December 2024) Ofwat retained a fixed, DMS-anchored TMR with an ex-post midpoint near **6.9% CPIH-real**, inferring the ERP as a balancing item and setting an allowed CPIH-real cost of equity of about **5.10%**. The **CMA**, in the 2021 **PR19 redeterminations**, estimated the TMR from the same DMS dataset using **arithmetic, Blume and JKM** estimators, arriving at ~**5.85–6.5% RPI-real** and **"aiming up"** ~25 bps on the cost of equity; in the parallel **RIIO-2 appeals** it upheld Ofgem's DMS-anchored cost of equity but removed the outperformance wedge.

### 5.4 Germany and continental Europe

The **Bundesnetzagentur (BNetzA)** derives its market risk premium from **long-run historical data using the worldwide DMS series** — explicitly the Credit Suisse Global Investment Returns Yearbook 2021 (up to 90 countries, 1900–2020) — taking the **mean of the geometric and arithmetic** historical MRP. The technical basis came from the **Randl/Zechner (WU Vienna) + Frontier Economics** Gutachten, which use DMS as their primary MRP source and derive a DMS-based MRP range of **6.1–7.3%** before adjustments. The resulting fourth-period pre-tax equity return was **5.07% (new assets) / 3.51% (existing)**. The reliance on DMS history was contested — DMS themselves were commissioned to rebut for one operator, and the OLG Düsseldorf initially criticised BNetzA for using historical data "without supplementary plausibility checks," though the BGH ultimately upheld the determination (see report 03). Randl/Zechner applied the same DMS-based methodology in the Austrian (E-Control) determinations.

---

## 6. Critiques and the academic debate

### 6.1 The self-critique and "Irrational Optimism"

The DMS thesis is itself a corrective to naive extrapolation. In **"Irrational Optimism"** (Financial Analysts Journal, 60(1), 2004) the authors argue investors "overestimate the rewards and underestimate the risks" of long-run equity investing; using 16 countries over 1900–2002 they note that real long-run equity returns have not reached 10% anywhere, "a more typical figure … being **4–6 percent**," and warn against "success bias" from looking only at US data.

### 6.2 Arnott–Bernstein and the forward-looking school

**Arnott & Bernstein, "What Risk Premium Is 'Normal'?"** (FAJ, 58(2), 2002) estimate the objective forward-looking US equity premium (vs bonds) back to 1802 at only **~2.4%**, far below the ~5% consensus, which they attribute to "deeply rooted naivete … where most participants have a career span reaching no farther back than the … bull market of 1975–1999." Their *contemporaneous* (2002) estimate of the prospective premium was near zero. Method: a dividend-discount decomposition (expected yield + expected real dividend/GDP growth − dilution).

### 6.3 Forward-looking and survey cross-checks

These are the standard counterweights to a purely historical (DMS) anchor:

- **Damodaran implied ERP** — an internal rate of return for the index net of the risk-free rate, computed monthly. As of **1 January 2026**: S&P 500 at **6,845.5**, expected return **8.41%**, risk-free **4.18%** → **implied ERP 4.23%** (≈ the 1960–2025 average). Damodaran also quantifies *why* historical premia are unreliable: with ~80 years and ~20% volatility the standard error is ~2.26%, so the 1928–2022 estimate "falls somewhere from 2.34%–10.94%."
- **Fernandez (IESE) survey** — practitioner consensus on the MRP/risk-free rate *actually used*; 2025 edition (54 countries): **US MRP 5.5%, risk-free 4.1%**. (Germany ~5.7% in a 2023 proxy; current-vintage Germany/UK figures unconfirmed.)
- **Welch surveys** of financial economists (2001): a 30-year arithmetic premium consensus of ~**5–5.5%**.
- **Fama–French (2002)** — dividend-growth-implied premium **2.55%** and earnings-growth-implied **4.32%**, versus a realised **7.43%** (1951–2000), concluding realised returns substantially overstate the expected premium because of an unanticipated decline in discount rates (re-rating).

### 6.4 Window and country-choice sensitivity

The two biggest "judgement" levers:

- **Window.** Pre-WWII equity returns were generally lower than the post-war bull market, so windows starting in 1926 (CRSP) or mid-century overstate the long-run premium; and since 2000 the World real equity return has been only 3.5%.
- **Country choice (success bias).** Over 1900–2024 **US equities returned 6.6% real vs 4.3% for the rest of the world** — a ~2.3-point gap that *is* the success-bias adjustment. DMS counter the strong "it's all survivorship" view (Jorion–Goetzmann, 1999) by noting the premium "in fifteen other countries … was as large as that in the US," so survivorship inflates the *level* but does not manufacture the premium.

### 6.5 Mehra–Prescott and the "smaller puzzle"

**Mehra & Prescott (1985)** named the equity-premium puzzle: a standard consumption-based model can justify at most ~0.35% with plausible risk aversion, against a realised US premium of ~6% (1889–1978: equity ~6.98%, riskless ~0.80%). DMS shrink the puzzle in **"The Worldwide Equity Premium: A Smaller Puzzle"** (2006) by (a) using an unbiased *global* sample, (b) stripping non-repeatable repricing, and (c) deriving a *forward-looking* premium of ~3–3.5% geometric — much smaller than the US-based figure that defined the puzzle.

### 6.6 Methodological criticisms of DMS specifically

- **Easy-data bias (acknowledged):** estimates are "still likely to be upward biased because the study is confined to the countries for which total returns can currently be estimated" — the sample is itself the set of markets with recoverable data.
- **A common misconception, corrected:** DMS do **not** "cherry-pick by dropping Germany 1922–23"; they deliberately *retain* the hyperinflation episodes (the exclusion applies narrowly to certain bond/bill and premium computations). The accurate concern is the opposite — which whole *countries* are missing.
- **Index-construction scrutiny:** Le Bris & Hautcoeur, "A challenge to triumphant optimists? A blue-chips index for the Paris stock exchange, 1854–2007" (Financial History Review), reconstruct French returns and question DMS's French index levels — a concrete example of peer scrutiny of the underlying country indices.

### 6.7 Bottom line for regulatory use

The DMS dataset is the indispensable empirical starting point for TMR and ERP — uniquely long, broad and bias-corrected — but it sets a **range, not a number**. The determination still turns on the window, the averaging convention (geometric / arithmetic / Blume / JKM), the deflator (RPI vs CPIH and the wedge), and the weight given to forward-looking cross-checks. The recurring "applicability" objection — whether a global historical average is the right prior for one country and one five-year control period — is exactly what underlay the German litigation and remains the central methodological debate in the field.

---

## 7. Cited literature and primary sources — annotated

**Primary DMS works**

1. **Dimson, Marsh & Staunton, *Triumph of the Optimists* (Princeton UP, 2002).** The foundational monograph; 16 countries, 1900–2000; first internally consistent, survivorship-bias-controlled cross-country record. Use: the bedrock long-run TMR/ERP citation worldwide. Limitation: 16 developed markets; snapshot to 2000 (kept current via the Yearbook).
2. **Global Investment Returns Yearbook (annual, 2000–2026).** The living dataset; ABN AMRO → Credit Suisse (2010–2023) → UBS (2024–). 2026: 126 years, 35 markets, five composites, gold added. Free "public summary edition" each year; full data licensed via Morningstar. The most-cited current source for regulatory TMR/ERP. Limitation: full data paywalled; headline numbers shift slightly each edition.
3. **DMS, "Global Evidence on the Equity Risk Premium," *J. Applied Corporate Finance* 15(4), 2003 (pp. 27–38).** 16 countries, 1900–2002; historical ERP vs bills US 5.3% / UK 4.2% / World 4.5%, with forward-looking 4.3% / 3.9% / 3.5%. The canonical practitioner-facing multi-country ERP reference.
4. **DMS, "The Worldwide Equity Premium: A Smaller Puzzle" (2006; Ch. 11 in Mehra (ed.), *Handbook of the Equity Risk Premium*, Elsevier, 2008, pp. 467–514).** 17 countries, 1900–2005; world premium 4.7% vs bills / 4.0% vs bonds; prospective 3–3.5% geometric. Directly engages Mehra–Prescott. Contains the +25%/−20% example and the "repricing overstates the premium" argument.
5. **DMS, "Irrational Optimism," *Financial Analysts Journal* 60(1), 2004 (pp. 15–25).** Long-horizon equities are less "safe" than believed; real long-run returns are 4–6%, not 10%. Conceptual groundwork for *Triumph*.
6. **DMS, "Equity Premia Around the World" (in *Rethinking the Equity Risk Premium*, CFA Institute Research Foundation, 2011).** 19 countries, 1900–2010; world real equity 5.5%, ERP vs bills 4.5% / vs bonds 3.8%; expected premium ~3–3.5%. The standard post-GFC update.
7. **Chambers, Dimson, Ilmanen & Rintamäki, "Long-Run Asset Returns," *Annual Review of Financial Economics* 16 (2024, pp. 435–458).** Current scholarly survey of multi-asset long-run premia and the pitfalls of long-run data (equity premium ~3.3% vs bonds / ~4.6% vs bills, indicative). (Often mis-cited to the FAJ; the venue is the *Annual Review of Financial Economics*.)

**Theory and estimator literature**

8. **Mehra & Prescott, "The Equity Premium: A Puzzle," *J. Monetary Economics* 15(2), 1985 (pp. 145–161).** Names the puzzle; the theoretical benchmark DMS's "smaller puzzle" responds to.
9. **Jacquier, Kane & Marcus, "Geometric or Arithmetic Mean: A Reconsideration," *FAJ* 59(6), 2003 (pp. 46–53).** Horizon-weighted unbiased forecast: weight on geometric = H/T. Central to the regulatory averaging debate (UK, Australia).
10. **Blume, "Unbiased Estimators of Long-Run Expected Rates of Return," *JASA* 69(347), 1974 (pp. 634–638).** The original horizon-weighted interpolation between arithmetic and geometric means; the "Blume adjustment" used by the CMA.
11. **Cooper, "Arithmetic versus geometric mean estimators," *European Financial Management*, 1996.** Unbiased discount factor correcting for estimation error and serial correlation; result sits closer to the arithmetic mean — used to justify regulatory discount rates above the geometric figure.

**Regulatory and cross-check literature**

12. **Wright, Burns, Mason & Pickford, *Estimating the Cost of Capital for … UK Regulators* (UKRN, 2018).** Established the TMR-based, DMS-anchored approach; TMR ~6–7% CPI-real. Shaped RIIO-2/3 and PR19/PR24.
13. **Fernandez et al., IESE MRP/risk-free survey (annual).** Practitioner-consensus cross-check; 2025: US MRP 5.5%, risk-free 4.1%.
14. **Damodaran, *Equity Risk Premiums* (annual; 2026 edition).** The leading market-implied ERP cross-check; implied US ERP 4.23% (Jan 2026); also the definitive critique of the statistical noise in realised premia.
15. **Arnott & Bernstein, "What Risk Premium Is 'Normal'?" *FAJ* 58(2), 2002; Fama & French, "The Equity Premium," *J. Finance*, 2002.** Forward-looking/dividend-growth estimates well below realised premia — the intellectual counterweight to a purely historical anchor.

---

## Sources

*UK regulatory primary/secondary sources, German determination and court sources, and the regulator citations below are given in full in the companion reports 03 and 04; key DMS-specific sources follow.*

1. Cambridge Judge Business School — Elroy Dimson profile. https://www.jbs.cam.ac.uk/people/elroy-dimson/
2. Cambridge Judge — Centre for Endowment Asset Management / "Global investment returns." https://www.jbs.cam.ac.uk/centres/ceam/research/investing-over-the-long-term/global-investment-returns/
3. London Business School — Paul Marsh profile. https://www.london.edu/faculty-and-research/faculty-profiles/m/marsh-p
4. London Business School — London Share Price Database (Mike Staunton). https://www.london.edu/faculty-and-research/finance/london-share-price-database
5. Princeton University Press — *Triumph of the Optimists* (hardcover). https://press.princeton.edu/books/hardcover/9780691091945/triumph-of-the-optimists
6. Princeton University Press — *Triumph of the Optimists* (ebook 9781400829477). https://press.princeton.edu/books/ebook/9781400829477/triumph-of-the-optimists
7. REF Impact Case Study — "Long-Run Global Asset Returns" (Id 44521; Millennium Book; Morningstar distribution). https://impact.ref.ac.uk/casestudies/CaseStudy.aspx?Id=44521
8. London Business School — "Credit Suisse Global Investment Returns Yearbook 2010" (transition to Credit Suisse). https://www.london.edu/news/credit-suisse-global-investment-returns-yearbook-2010
9. UBS — "Acquisition of Credit Suisse" (announced 19 Mar 2023). https://www.ubs.com/global/en/media/display-page-ndp/en-20230319-tree.html
10. UBS — "UBS completes Credit Suisse acquisition" (12 Jun 2023). https://www.ubs.com/global/en/media/display-page-ndp/en-20230612-ubs-credit-suisse-acquisition.html
11. UBS — "Global Investment Returns Yearbook 2024" (first UBS edition, 25th year). https://www.ubs.com/global/en/media/display-page-ndp/en-20240228-yearbook.html
12. UBS — "Global Investment Returns Yearbook 2025" (125 years; 23 of 35 markets from 1900). https://www.ubs.com/global/en/media/display-page-ndp/en-20250304-global-investment-returns-yearbook-2025.html
13. UBS — "Global Investment Returns Yearbook 2026" (126 years; 35 markets; gold; US 62% of world cap; since-2000 3.5%). https://www.ubs.com/global/en/media/display-page-ndp/en-20260303-global-investment-returns-yearbook-2026.html
14. London Business School — "UBS Global Investment Returns Yearbook 2026" (US real equity 6.6%, 1900–2025). https://www.london.edu/news/ubs-global-investment-returns-yearbook-2026-history-risk-and-return-in-turbulent-times
15. Cambridge Judge — "Stocks have far outperformed over the past 125 years" (World real: equity 5.2%, bonds 1.7%, bills 0.5%). https://www.jbs.cam.ac.uk/2025/report-stocks-have-far-outperformed-over-the-past-125-years/
16. WealthBriefing — "Equities Have Beaten Bonds Since 1900 – UBS Yearbook" (USD 1 → USD 3,296 real). https://www.wealthbriefing.com/html/article.php/equities-have-beaten-bonds-since-1900--ubs-yearbook-
17. T. Rowe Price — "125 years of returns" (US 6.6% vs ex-US 4.3% real, 1900–2024). https://www.troweprice.com/en/us/investment-institute/insights/one-hundred-twenty-five-years-of-returns-timeless-lessons-in-investing
18. Credit Suisse Global Investment Returns Yearbook 2023 (markets table; 90-country world index). https://www.newealth.com.au/wp-content/uploads/2023/03/2023-03-02-CSG-Investment-Returns-Yearbook-2023.pdf
19. Macrosynergy — "Lessons from long-term global equity performance" (continuous histories; Austria worst; Germany σ 31.7%; 1922–23 exclusion). https://macrosynergy.com/research/lessons-from-long-term-global-equity-performance/
20. EH.net — review of *Triumph of the Optimists* (reviewer John A. James; survivorship/success/easy-data bias). https://eh.net/book_reviews/triumph-of-the-optimists-101-years-of-global-investment-returns/
21. DMS — "Global Evidence on the Equity Risk Premium," JACF 2003 (SSRN 431901). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=431901
22. DMS — "The Worldwide Equity Premium: A Smaller Puzzle" (SSRN 891620). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=891620
23. DMS — "Irrational Optimism," FAJ 2004 (CFA Institute). https://rpc.cfainstitute.org/research/financial-analysts-journal/2004/irrational-optimism
24. DMS — "Equity Premia Around the World" (SSRN 1940165; in *Rethinking the Equity Risk Premium*, CFA Institute RF 2011). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1940165
25. Chambers, Dimson, Ilmanen & Rintamäki — "Long-Run Asset Returns," Annual Review of Financial Economics 16 (2024). https://www.annualreviews.org/content/journals/10.1146/annurev-financial-082123-105515
26. Mehra & Prescott — "The Equity Premium: A Puzzle," J. Monetary Economics 15(2), 1985. https://www.sciencedirect.com/science/article/abs/pii/0304393285900613
27. Jacquier, Kane & Marcus — "Geometric or Arithmetic Mean: A Reconsideration," FAJ 2003 (CFA Institute). https://rpc.cfainstitute.org/research/financial-analysts-journal/2003/geometric-or-arithmetic-mean-a-reconsideration
28. Blume — "Unbiased Estimators of Long-Run Expected Rates of Return," JASA 69, 1974. https://www.tandfonline.com/doi/abs/10.1080/01621459.1974.10480180
29. Cooper — "Arithmetic versus geometric mean estimators," European Financial Management, 1996. https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1468-036X.1996.tb00036.x
30. Kaserer — "Estimating the market risk premium: arithmetic or geometric mean …?", J. Business Economics, 2022. https://link.springer.com/article/10.1007/s11573-022-01104-w
31. Poterba & Summers — "Mean Reversion in Stock Prices" (NBER w2343). https://www.nber.org/papers/w2343
32. Fama & French — "The Equity Premium," J. Finance, 2002. https://onlinelibrary.wiley.com/doi/10.1111/1540-6261.00437
33. Arnott & Bernstein — "What Risk Premium Is 'Normal'?", FAJ 58(2), 2002 (SSRN 296854). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=296854
34. Damodaran — "Data Update 2 for 2026: Equities" (implied ERP 4.23%, 1 Jan 2026). https://aswathdamodaran.blogspot.com/2026/01/data-update-2-for-2026-equities-get.html
35. Damodaran — "Equity Risk Premiums: Determinants, Estimation and Implications — 2026 Edition" (SSRN 6361419). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6361419
36. Fernandez, García de la Garza & Fernández Acín — "Survey: MRP and Risk-Free Rate … 2025" (SSRN 5260463). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5260463
37. Welch — "The Equity Premium Consensus Forecast Revisited" (SSRN 285169). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=285169
38. Le Bris & Hautcoeur — "A challenge to triumphant optimists? A blue-chips index for the Paris stock exchange, 1854–2007," Financial History Review. https://www.cambridge.org/core/journals/financial-history-review/article/abs/challenge-to-triumphant-optimists-a-blue-chips-index-for-the-paris-stock-exchange-18542007/5BD48866FA7B79DBD447AD3402107A5B
39. UK Regulators Network — Wright, Burns, Mason & Pickford, "Estimating the Cost of Capital …" (2018) and CoC guidance (2023). https://ukrn.org.uk/app/uploads/2023/03/CoC-guidance_22.03.23.pdf
40. Oxera — "RIIO-3 Final Determinations" (TMR 6.5–7%; ex-post ~7%). https://www.oxera.com/insights/agenda/articles/riio-3-final-determinations/
41. CEPA for Ofwat — "PR24 Cost of Equity" (DMS Yearbook as TMR source; ex-post TMR ~6.9%). https://www.ofwat.gov.uk/wp-content/uploads/2024/07/CEPA_PR24-cost-of-equity-1.pdf
42. Economic Insight — "The CMA redetermination of PR19" (TMR from arithmetic, Blume and JKM; ~5.85–6.5% RPI-real). https://www.economic-insight.com/wp-content/uploads/2021/06/Assessment-of-CMA-redetermination-of-PR19-15-04-21-stc.pdf
43. NERA for BDEW — "Eigenkapitalzinssatz — internationaler Vergleich der Festlegungen" (BNetzA uses DMS MRP, mean of geometric and arithmetic). https://www.bdew.de/media/documents/NERA_Internationaler_Vergleich_EK_Zins_Festlegungen.pdf
