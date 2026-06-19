# Energy Network Regulation — Cost-of-Capital Report Set

*Compiled from public sources as of June 2026. These reports are research syntheses for analytical use; all specific figures, dates, case numbers, and peer-group constituents should be confirmed against the cited primary documents before being relied upon in a determination, transaction, or legal proceeding.*

This folder contains four linked reports on the allowed return on capital for regulated
gas and electricity networks, with a focus on the German regulatory dispute and the
methodological context surrounding it.

| # | Report | File |
|---|--------|------|
| 1 | Historic investment returns: the Dimson–Marsh–Staunton (DMS) dataset | [`01_historic_returns_dms.md`](01_historic_returns_dms.md) |
| 2 | Peer groups in the Randl/Zechner expert reports (German gas & electricity) | [`02_randl_zechner_peer_groups.md`](02_randl_zechner_peer_groups.md) |
| 3 | The German legal battle over the network equity return | [`03_german_legal_battle.md`](03_german_legal_battle.md) |
| 4 | Comparison of regulatory cost-of-capital methodologies: EU, US, UK, Asia | [`04_methodology_comparison.md`](04_methodology_comparison.md) |
| 5 | Replicating the ECB's derivation of market returns (multi-stage DDM) | [`05_ecb_market_return_ddm.md`](05_ecb_market_return_ddm.md) |
| 6 | Methodological extensions: beta estimation & applying implied returns *(in German)* | [`06_beta_und_implizite_renditen_methodische_erweiterungen.md`](06_beta_und_implizite_renditen_methodische_erweiterungen.md) |

### Deep-dive companions

Each report has a deep-dive companion (~2.5–4.5× longer) that expands every chapter
and adds an annotated review of the cited literature/primary sources. Each was built
by a team of parallel research sub-agents, one per chapter. Where firmer sources were
found, the deep-dives **refine or correct** the base reports (corrections are noted in
the deep-dive text) — e.g. the 4th-period existing-asset rate is **3.51% uniform** (the
3.03% gas figure was the July-2021 draft / the EK-II tranche rate); ECJ C-718/18 was
decided by the **Fourth Chamber**; the Randl/Zechner asset beta is **~0.34–0.42**,
re-levered to the 0.81 equity beta; "BIEGTRDT" is Bloomberg's *BI Europe Gas
Transmission & Distribution* peer index.

| # | Deep dive | File |
|---|-----------|------|
| 1 | DMS dataset — deep dive | [`01_historic_returns_dms_deep-dive.md`](01_historic_returns_dms_deep-dive.md) |
| 2 | Randl/Zechner peer groups — deep dive | [`02_randl_zechner_peer_groups_deep-dive.md`](02_randl_zechner_peer_groups_deep-dive.md) |
| 3 | German legal battle — deep dive | [`03_german_legal_battle_deep-dive.md`](03_german_legal_battle_deep-dive.md) |
| 4 | Methodology comparison — deep dive | [`04_methodology_comparison_deep-dive.md`](04_methodology_comparison_deep-dive.md) |

## Key findings at a glance

**1 — DMS historic returns.** The Dimson–Marsh–Staunton dataset (now the *UBS Global
Investment Returns Yearbook 2026*, covering 1900–2025, 35 markets + composites) is the
dominant long-run, survivor-bias-corrected record of asset returns. Headline geometric
real figures: world equities ~5.2% p.a., bonds ~1.7%, bills ~0.5%; world equity risk
premium ~4.3–4.6% vs bills and ~3.1–3.3% vs bonds. It is the empirical anchor for the
Total Market Return (TMR) and ERP in CAPM-based regulatory determinations — including the
UK (Ofgem/Ofwat/CMA) and Germany (BNetzA via Randl/Zechner).

**2 — Randl/Zechner peer groups.** The Frontier/Zechner/Randl Gutachten (July 2021) used a
single **combined European energy-network peer group** to estimate beta. The
FOI-disclosed constituents are **E.ON, Elia, Enagás, National Grid, Red Eléctrica, REN,
Snam and Terna**, screened from a ~71-company sample to "pure" network operators (E.ON
excluded from the asset-beta set for failing a >75% network-revenue test). Result:
β ≈ 0.81, market risk premium 3.70%, risk surcharge ≈3%.

**3 — German legal battle.** BNetzA cut the pre-tax equity return to **5.07% (new
assets) / 3.51% (existing)** for the 4th period. ~900 operators appealed; the **OLG
Düsseldorf annulled the determination (30 Aug 2023)**, but the **BGH reversed and upheld
BNetzA** (electricity 17 Dec 2024; gas 25 Feb 2025), setting a deferential review
standard against the backdrop of ECJ **C-718/18** (which expanded BNetzA's discretion).

**4 — Methodology comparison.** The central fault line is **CAPM + indexed RAB**
(UK, EU, Australia, New Zealand) versus **DCF + original-cost rate-of-return** (US, where
FERC and state PUCs allow ROEs of ~9.7–10%). Secondary divides: real vs nominal returns,
historical (DMS) vs market-implied ERP, and rules (Australia's binding RORI, NZ's Input
Methodologies) vs discretion (US "battle of the models"; Germany's post-C-718/18 shift).
Asia-Pacific is heterogeneous, from Australia's rules-based CAPM to Hong Kong's negotiated
8%-of-assets cap.

**5 — ECB market-return replication.** A runnable replication of the ECB's forward-looking,
market-implied derivation of the equity market return — a **multi-stage Dividend Discount
Model** that solves the index price for the implied cost of equity, then nets off the 10-year
OIS rate to get the ERP. On illustrative June-2026 euro-area inputs (3.2% dividend yield, ~8%
IBES near-term growth, 3.3% long-run nominal GDP growth, 2.6% OIS) the three-stage DDM, the
closed-form Fuller–Hsia H-model and the ECB term-structure form all imply a **~8% expected
nominal market return and a ~5.4% equity risk premium** (~6.8% with buybacks). This is the
forward-looking counterpart to Report 1's backward-looking DMS history. An
accompanying **Streamlit app** ([`../code/app.py`](../code/app.py)) generalises
this to uploaded multi-share analyst estimates, pulls the risk-free rate live
from the **Deutsche Bundesbank API**, and weight-aggregates every variant to a
market return. Code: [`../code/`](../code/) (engine, app, Bundesbank client).

**6 — Beta & implied-return extensions (DE).** A methodological deep-dive (in
German) on extending the Report 2 beta machinery and applying the Report 5
implied returns. Part A: the **temporally rolling beta** (a rolling-window beta
*time series* summarised by a trailing average rather than a single Stichtag
value, as the UK regulators do), plus state-space/Kalman & DCC-GARCH conditional
betas, rule-based handling of **temporary crisis distortions** (COVID-2020,
energy-crisis-2022), and Dimson/Blume/Vasicek corrections. Part B: applying
**implied returns** — implied vs. historical MRP, the **reverse-CAPM implied
("forward-looking") beta**, and the time-consistent coupling
`k_{i,t}=rf_t+β_{i,t}·ERP_impl,t` with its pro-cyclicality caveat. Runnable in
[`../code/beta_tools.py`](../code/beta_tools.py).

## How the reports connect

The reports are designed to be read together:

- **Report 1 (DMS)** explains the long-run historical return dataset that anchors the
  Total Market Return (TMR) and equity risk premium (ERP) in most CAPM-based
  determinations — including the German one.
- **Report 2 (peer groups)** documents the listed comparator companies Randl/Zechner
  used to estimate the beta factor feeding the German allowed equity return.
- **Report 3 (legal battle)** covers the litigation over the Bundesnetzagentur's reduced
  equity return, in which the Randl/Zechner methodology (the DMS-based market risk
  premium from Report 1 and the peer-group beta from Report 2) was central.
- **Report 4 (international comparison)** places the German CAPM/RAB approach against the
  UK, wider EU, US (DCF/rate-of-return) and Asia-Pacific frameworks.
- **Report 5 (ECB market-return replication)** provides the forward-looking, market-implied
  counterpart to Report 1: a runnable replication of the ECB's multi-stage DDM derivation of
  the expected equity market return and ERP — the same family as the US DCF approach in
  Report 4, and a cross-check on the DMS history that anchors the regulatory TMR.
- **Report 6 (beta & implied-return extensions, DE)** ties Reports 2 and 5 together: it
  extends the peer-group beta estimation (temporally rolling / time-varying betas, crisis
  handling) and shows how the implied returns of Report 5 are applied (implied MRP, reverse-
  CAPM implied beta, and a consistent time-varying cost-of-equity panel).

## Sources and verification

Each report carries its own numbered "Sources" section with full citations. Primary
sources (regulator determinations, expert reports, court decisions) are preferred over
secondary commentary. Where a primary document (e.g. certain BNetzA, AER, Commerce
Commission NZ or Asian government PDFs) could not be machine-read directly, figures were
triangulated across multiple independent sources and are flagged accordingly in the
relevant report. Treat the reports as a well-sourced starting point, not a substitute for
the primary determinations.
