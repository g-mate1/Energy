# The German Legal Battle over the Network Equity Return and the Randl/Zechner Expert Reports — Deep-Dive

*Compiled from public sources as of June 2026. This document is for information only, is **not legal advice**, and reflects an evolving body of regulatory and judicial material. It should be verified against the primary court and regulatory documents before being relied upon in any determination, transaction, or proceeding. Many primary documents (the Bundesnetzagentur determinations and press releases, the full OLG Düsseldorf and BGH decision texts, the Frontier/Zechner/Randl Gutachten, and the ECJ judgment) were available during research only through search-engine extraction of their content because the underlying servers blocked direct retrieval; where a figure, date, case number, or holding could not be confirmed against verbatim primary text it is flagged explicitly. This deep-dive expands the base report `03_german_legal_battle.md`; where the two differ, several figures and one chamber/date attribution have been **corrected** here and the corrections are noted in §10.*

---

## 1. Executive summary

Between 2021 and 2026 Germany fought a high-stakes legal battle over the allowed return on equity (the *kalkulatorischer Eigenkapitalzinssatz*) for regulated electricity and gas networks. The Bundesnetzagentur (BNetzA), relying on a scientific expert report (*Gutachten*) by Professors **Otto Randl** and **Josef Zechner** of WU Vienna together with **Frontier Economics**, cut the pre-tax equity return for **new** network assets to **5.07 %** and for **existing** assets to **3.51 %** for the fourth regulatory period — a reduction of more than 25 % from the third-period figures. Network operators, supported by the industry associations BDEW and VKU, brought roughly **900 appeals** before the **3. Kartellsenat** of the Oberlandesgericht (OLG) Düsseldorf, bundled into **14 model proceedings** (*Musterverfahren*).

By decision of **30 August 2023** the OLG **annulled** the determinations and ordered redetermination — but on a single, narrow ground: the BNetzA had derived the **market risk premium (MRP)** from one historical data series (the Dimson–Marsh–Staunton dataset) **without the supplementary plausibility check** the senate considered necessary given contrary market and international signals. The operators **lost on every other ground** they raised, including the beta/peer-group challenge, the CAPM framework, the base rate and the level of the risk premium; and the senate held the agency's **written reasons satisfied the formal requirements of § 73 EnWG**, so the defect was **substantive, not formal**.

The Bundesgerichtshof (BGH) then **reversed the OLG** across a series of *Rechtsbeschwerde* decisions — **electricity on 17 December 2024** (lead case **EnVR 79/23**), **gas on 25 February 2025** (lead cases **EnVR 83/23, 86/23, 90/23, 93/23**), and a further confirmatory electricity decision **EnVR 82/23 on 9 September 2025** — confirming the BNetzA's figures and entrenching a markedly **deferential standard of judicial review** of the regulator's choice of method. The dispute unfolded against the backdrop of the European Court of Justice's (ECJ) ruling in **Commission v Germany, C-718/18** (2 September 2021), which stripped the German federal government of detailed rule-making power over network tariffs and pushed the equity-return exercise into the BNetzA's own discretionary determination (*Festlegung*). The forward-looking sequel is the BNetzA's **NEST** reform, whose final decisions of **December 2025** move Germany from the fifth regulatory period onward to a standardised **WACC** (40 % equity / 60 % debt) with a market-indexed cost of debt and a base rate keyed to recent rather than decade-old yields.

---

## 2. The BNetzA determinations

### 2.1 The 12 October 2021 *Festlegungen*

On **12 October 2021** the BNetzA's Beschlusskammer 4 issued two parallel determinations (announced via press release on **20 October 2021**) setting the calculatory equity return for the fourth regulatory period:

- **BK4-21-055** — electricity network operators;
- **BK4-21-056** — gas network operators.

The two decisions were issued *im Wesentlichen inhaltsgleich* (with essentially identical content). The figures (each pre-corporate-tax) were uniform across electricity and gas:

| Asset class | 4th period (Oct 2021) | 3rd period (for contrast) | 2nd period (for contrast) |
|---|---|---|---|
| **New assets** (*Neuanlagen*) | **5.07 %** (≈ 5.8 % incl. trade tax) | **6.91 %** | **9.05 %** |
| **Existing assets** (*Bestands-/Altanlagen*) | **3.51 %** (≈ 4.0 % incl. trade tax) | **5.12 %** | ≈ 7.14 % |

The fourth regulatory period runs **2023–2027 for gas** and **2024–2028 for electricity**. The new-asset rate of 5.07 % was widely treated as the headline figure and the binding anchor for revenue-cap calculations. The trajectory had been steeply downward for over a decade.

> **Resolved — the "3.03 % for gas" question.** The base report and a sibling report disagreed over whether the existing-asset rate was a uniform 3.51 % or split (3.51 % electricity / 3.03 % gas). The final existing-asset rate is **3.51 % pre-tax, uniform for both electricity and gas**. The "3.03 %" figure is real but belongs to two *different* parameters: (i) it was the **July 2021 draft** existing-asset rate, which was raised to 3.51 % in the final decision; and (ii) it is the third-period **"Eigenkapitalzinssatz II" (EK-II) rate for gas** — the lower return on the equity *tranche exceeding the 40 % regulatory equity quota* (third-period EK-II: 3.03 % gas / 2.71 % electricity; fourth-period EK-II falls to roughly 2.04 % gas / 1.73 % electricity). It is **not** the in-force existing-asset (EK-I) rate. The 3.03 %/3.51 % confusion is therefore a conflation of the draft rate and the EK-II rate.

### 2.2 Legal architecture and the build-up of the rate

The legal architecture layered three instruments: the **EnWG** (Energiewirtschaftsgesetz), the incentive-regulation ordinance (**ARegV**, Anreizregulierungsverordnung) and **§ 7 StromNEV / GasNEV** (the network-charge ordinances governing the *kalkulatorische Eigenkapitalverzinsung*). The relevant sub-sections, as resolved during research:

- The **competence and timing** to fix the equity rate by *Festlegung* before the period begins sits in **§ 7 Abs. 6 StromNEV / GasNEV** — confirmed by the official decision-page titles ("Festlegung von Eigenkapitalzinssätzen nach § 7 Abs. 6 StromNEV [resp. GasNEV] für die vierte Regulierungsperiode"), referencing **§ 29 Abs. 1 EnWG** (the procedure for determinations) in conjunction with the adequacy standard of **§ 21 Abs. 2 EnWG**.
- The **substantive methodology** — the ceiling on the base rate and the risk surcharge — sits in **§ 7 Abs. 4 and Abs. 5**. Abs. 4 caps the base rate at the ten-year average of the *Umlaufsrendite* plus an appropriate surcharge; Abs. 5 governs the "angemessener Zuschlag zur Abdeckung netzbetriebsspezifischer unternehmerischer Wagnisse" (the risk premium, the *Wagniszuschlag*), to be computed via the CAPM, and (in § 7 Abs. 5 Nr. 2) directs the agency to have regard to the equity-return determinations of foreign regulatory authorities.

The equity return is a calculatory cost element rolled into the **revenue cap (Erlösobergrenze)** for the period. It is applied to the operationally necessary equity up to the **40 % regulatory equity quota** at the EK-I rate (5.07 %/3.51 %); equity above 40 % earns the lower EK-II rate. New investments are remunerated currently via the **capital-cost surcharge (*Kapitalkostenaufschlag*, KKAuf)** rather than waiting for the next base year.

The full build-up of the fourth-period rate (after-tax, then grossed up):

- **Base rate (Basiszins): 0.74 %.** This is the **ten-year trailing average of the *Umlaufsrendite*** (yields on outstanding domestic public bonds, per the Deutsche Bundesbank), over the last ten completed calendar years. It had fallen **1.75 percentage points** from **2.49 %** in the third period — a direct consequence of the 2010s low-rate environment.
- **Risk premium (Wagniszuschlag): 3.39 %**, built in two steps:
  - **CAPM core ≈ 3.0 %** = market risk premium **3.70 %** × network beta/risk factor **0.81** (3.70 × 0.81 = 2.997).
  - **+ 0.395 percentage-point uplift** applied after consultation, in which term and liquidity (*Laufzeit-/Liquiditäts-*) effects were analysed more closely — to offset the risk that the very low base rate had understated the appropriate surcharge. The result is the **3.39 %** network-specific surcharge actually applied.
- **After-tax equity cost rate = 0.74 % + 3.39 % = 4.13 %.**
- **Tax factor ≈ 1.226** grosses this up for corporate income tax: **4.13 % × 1.226 = 5.07 %** pre-tax (new assets).

> Note on a common garbled summary: some secondary write-ups present the gross-up as "3.51 % × 1.22 = 5.07 %," which is arithmetically wrong (3.51 × 1.22 = 4.28). That version mistakenly substitutes the *existing-asset* rate (3.51 %) for the after-tax *new-asset* cost rate (4.13 %). The internally consistent build-up is **4.13 % × 1.226 = 5.07 %**.

This resolves the "3.0 % vs 3.39 %" question in the base report: **3.0 %** is the raw CAPM surcharge (the round number the BNetzA later re-uses verbatim as the "constant 3 % surcharge" in the January-2024 regime); **3.39 %** is the final surcharge after the 0.395 pp uplift. The draft-to-final move in the headline new-asset rate (4.59 % → 5.07 %, +0.48 pp pre-tax) is the tax-grossed-up reflection of that 0.395 pp after-tax uplift.

### 2.3 Why the cut was contentious — timing in a rising-rate environment

The reduction was deeply contentious because it arrived just as inflation and market interest rates turned sharply **upward** in 2022–2023. The complaint was structural: anchoring the base rate to a **ten-year trailing average** mechanically embeds stale, ultra-low yields and cannot capture a rate reversal. The 2010s low-rate decade entered the base rate **in full** (pulling it to 0.74 %), and — the operators argued — had a *countervailing* effect inside the DMS bond-return leg of the MRP, producing an internal asymmetry. All of this fell precisely when Germany needed to mobilise **hundreds of billions of euros** of grid investment for the energy transition (one widely cited IMK/Hans-Böckler study puts the German power-grid investment need at roughly **€651 billion to 2045**).

The reactions split sharply:

- **Operators / industry.** BDEW (Kerstin Andreae) and VKU (Ingbert Liebing) issued a joint statement calling the cut **"ein völlig falsches Signal"** ("a completely wrong signal"), arguing it endangered operators' capacity to make the investments needed for climate protection and security of supply. VKU later pressed repeatedly for further increases.
- **Consumer side.** The Verbraucherzentrale Bundesverband (vzbv) took the opposite view — that the rates were still too generous, should fall further, and that increases would be "Milliardengeschenke" (billion-euro gifts) burdening consumers through higher network charges. The Bundesverband Neue Energiewirtschaft (bne) aligned with this position.

### 2.4 The January 2024 partial uplift for new investment

Responding both to the rate environment and to the OLG's August-2023 ruling, the BNetzA published a fresh determination on **24 January 2024** (file BK4-23-0004) introducing a **time-variable** equity return for **new investments made from 1 January 2024** within the capital-cost surcharge. The mechanics:

- The base rate switched from the ten-year average to a **recent / most-recently-completed period of the *Umlaufsrendite***, plus a **constant 3 % surcharge**, then grossed up.
- On then-current figures this implied roughly **7.09 %** (≈ 8.1 % including trade tax) for 2024 — an illustrative value, since the rate now moves year to year with yields.
- Remuneration was also extended to assets under construction (*Anlagen im Bau*), not only finished assets.

> **Resolved — the base report's internal inconsistency.** The base report at one point states that the January-2024 step left "the existing-asset rate unchanged at 5.07 % (incl. trade tax)." That pairing is a paraphrase error: **5.07 % (≈ 5.8 % incl. trade tax) is the NEW-asset rate**, and **3.51 % is the EXISTING-asset rate**. What actually "stayed unchanged" in January 2024 was the **October-2021 determination itself** (and its 5.07 %/3.51 % rates) for all assets *other than* the newly carved-out category; only **new investments booked in the KKAuf from 1 January 2024** received the new, annually-variable rate. The existing-asset (*Bestandsanlagen*) rate **remained 3.51 %**. The result was a three-tier landscape: legacy assets, fourth-period new assets under the 2021 figure, and post-2024 new investments under the time-variable rate.

---

## 3. The Randl/Zechner *Gutachten* and the methodological attack

### 3.1 The Gutachten and its authors

The determination rested on the **"Wissenschaftliches Gutachten zur Ermittlung der Zuschläge für unternehmerische Wagnisse von Strom- und Gasnetzbetreibern"** (July 2021) by **Prof. Josef Zechner**, **Prof. Otto Randl** (both finance professors at WU Vienna — Wirtschaftsuniversität Wien) and **Frontier Economics Ltd**. The same consortium had authored the predecessor reports (2008, 2011, 2016) and authors the BNetzA's **railway** cost-of-capital reviews (the "Methodenbericht Zins 2021," with Frontier and IGES) and the Austrian regulator **E-Control's** WACC Gutachten for gas and electricity networks. The same consortium therefore sets the regulated cost of capital across German energy networks, German railways, and Austrian energy networks — a notable concentration of methodological influence. A companion report on the market risk premium for earlier periods was authored by Professors **Stehle and Betzer**.

### 3.2 The DMS market-risk-premium recommendation

The Gutachten's most consequential recommendation was to estimate the market risk premium from a single long-run **historical** source — the **Dimson, Marsh & Staunton (DMS)** dataset as published in the **Credit Suisse Global Investment Returns Yearbook 2021**. The build-up, as recited in the court decisions:

- The MRP was set at the **average of the arithmetic mean (≈ 4.30 %) and the geometric mean (≈ 3.10 %) of the DMS world equity-over-bond excess return = 3.70 %.** (For comparison, the third-period values were an MRP of 3.8 % and a beta of 0.83.)
- The figure is best understood as a **historical realised *excess return* of equities over a portfolio of long-term government bonds** — a differential return that is largely inflation-neutral by construction — which is then **added to the (nominal) forward-looking base rate** of 0.74 % inside the CAPM. Frontier acknowledged the **mismatch** between the forward-looking domestic *Umlaufsrendite* base rate and the backward-looking realised DMS bond leg, and provided for a **markup of 0–25 basis points** to bridge the maturity/issuer difference. The construction is thus a deliberate hybrid (a historical excess-return premium on a current base rate), which the operators attacked as conceptually inconsistent.

> **DMS coverage, precisely.** The Yearbook 2021 covers **32 individual markets plus a 90-country world index**; only **23 of those countries have the full 121-year history (1900–2020)**. Equity indices are **market-cap-weighted over the full ~90-country universe**; bond indices are **GDP-weighted over the 32 markets**. Both the "~90 countries" and the "23 countries / 120 years" descriptions are therefore correct facets of the same dataset — and this dual, blended structure is exactly what the operators weaponised (see §3.3). The affirmative rationale Frontier/BNetzA offered for using a single broad *international* historical source was the **increasing integration of capital markets** (especially within the euro area / globally), which they said makes a **global** market risk premium more appropriate than a German-only DAX/REX series.

### 3.3 The methodological attack, ground by ground

The fullest single statement of the operators' attack is the **Oxera** report for Netze BW / EnBW, *"Bestimmung des Wagniszuschlags — Stellungnahme zum Gutachten von Frontier Economics"* (19 August 2021). Strikingly, a companion assessment by **DMS themselves** (Dimson/Marsh/Staunton, 24 August 2021) was submitted via **E.ON** — i.e., the *authors of the dataset* were brought in on the operators' side to address the applicability of a world MRP to the German determination.

1. **DMS-only / no cross-check ("Methodenmonismus").** The central charge: the MRP was fixed from DMS historical averages **alone**, with no forward-looking or implied-cost-of-equity (ICE) cross-check. Hachmeister/Pedell framed this as "methodological monism" failing the scientific standards of *Methodenpluralismus*, input consistency, and plausibility checking. The OLG accepted this point.

2. **Non-replicability and non-disclosure of the country weighting** — the strongest technical point. Critics argued the world MRP result is **not replicable** and that the **country-weighting scheme was not disclosed**. The OLG recited this precisely: the DMS authors did not publish consistent weightings; only the weightings for the **endpoint years 1900 and 2020** were available, and these revealed **unexplained differences** versus other data sources — undermining the plausibility of the world MRP. (This dovetails with the Yearbook's own disclosure that equities are cap-weighted over ~90 countries while bonds are GDP-weighted over 32, so the blend producing "the" MRP is opaque.)

3. **The *Umlaufsrendite* window / inflation asymmetry.** The ten-year trailing-average base rate fully absorbed the low-interest 2010s, dragging the base rate to 0.74 % and suppressing the post-2021 rate rebound, understating the cost of equity in an inflationary environment. Oxera added that the method **never produces a base rate that matches, numerically or conceptually, the risk-free rate embedded in the DMS MRP**.

4. **Time-variability of the MRP.** A static historical average ignores that the MRP varies over time. The literature marshalled against the BNetzA included **Stehle & Betzer (2019)** (an MRP above 4.8 % said to be unjustifiable) and **Stehle (2016)** (≈ 4.73 %), and the broader framing of a **time-varying ("Total Market Return") vs. time-stable ("constant")** MRP. *(Caveat: the base report's statement that "Randl himself acknowledged the MRP varies over time" could not be confirmed from a direct Randl quotation; the time-variability point is firmly attributable to Stehle/Betzer and the TMR-vs-constant literature. The closest documented Zechner/Randl concession is the fifth-period statement that "the one correct method does not exist" — see §6.4.)*

5. **Beta / peer group too narrow / downward-biased.** Operators argued the comparator set was arbitrarily restricted to European countries and that "double-averaging" drove the **unlevered (asset) beta to ≈ 0.40**, below other European regulators' determinations, biasing the surcharge down. (The re-levered equity beta of **0.81** was derived from a combined European peer group of listed "pure" network operators — documented in the sibling report `02_randl_zechner_peer_groups.md` as Snam, Terna, Enagás, Red Eléctrica, REN, Elia and National Grid, with E.ON screened out for failing a >75 % network-revenue purity test.)

6. **The "golden age of bonds" argument** — Oxera's distinctive, opposite-signed contribution. Oxera argued the DMS historical equity-over-bond premium is **downward** biased because it embeds a historical bond **term premium inflated by unrepeatable "golden age" events** (a century of generally falling yields / rising bond prices), well above today's expected term premium for German government bonds. On this logic the DMS excess return *understates* the true required equity premium — the reverse of the conventional assumption that historical premia overstate forward-looking ones.

7. **International comparison — "restrictive and singular."** Operators argued reliance on DMS alone was *restriktiv und singulär* and that **no peer regulator fixes the premium on DMS data alone**, with German allowed returns sitting at the bottom of the European range. This linked directly to § 7 Abs. 5 Nr. 2 StromNEV/GasNEV (the duty to have regard to foreign regulators' determinations) and was legally decisive at the OLG.

### 3.4 The counter-Gutachten — and that the dispute cut both ways

A notable feature of the episode is that the expert dispute ran in **both directions**: operators argued the return was too low; the consumer side argued it was too high.

| Report | Commissioned by | Core argument |
|---|---|---|
| **NERA**, *Vergleich internationaler Eigenkapitalzinssätze* (11 Jun 2021) | **BDEW** | International regulatory comparison: an EU average of ≈ **7.13 % after tax**, about **1.49 pp above** the BNetzA's determination; German rates among the lowest in Europe despite large grid-expansion needs. |
| **ValueTrust**, *Gutachtliche Stellungnahme … CAPM-basierter Eigenkapitalkosten* (9 Jul 2021) | **BDEW** | CAPM/beta and methodology critique on a multi-method basis (midpoint ≈ 5.85 % for gas networks per a snippet); a *reduction* of the regulatory equity cost is not justifiable by any method; faults the lack of *Methodenpluralismus*. |
| **Oxera**, *Bestimmung des Wagniszuschlags …* (19 Aug 2021) | **Netze BW / EnBW** | The full DMS attack (items 1–7 above), including the "golden age of bonds" downward-bias argument and the base-rate/MRP inconsistency. |
| **Hachmeister / Pedell** Kurzgutachten (2021) | **BDEW** (Profs. Dirk Hachmeister, Hohenheim; Burkhard Pedell, Stuttgart) | "Methodological monism": sole CAPM use without real-data plausibility checks fails scientific standards and reduces robustness. |
| **Prof. Thomas Wein** (Univ. Lüneburg) | **LichtBlick** (consumer side, aligned with vzbv) | The rate is **too HIGH**: use the geometric mean only → MRP **3.10 %**, beta **0.76**, surcharge **2.36 %**; restrict comparators to incentive-regulated firms; would cut the existing-asset rate to ≈ 3.47 %. |
| **DMS (Dimson/Marsh/Staunton)** own assessment (24 Aug 2021) | submitted via **E.ON** | The dataset's authors addressed the applicability of a world MRP — on the operators' side. |

In the final fourth-period decision the BNetzA made a **partial concession** — raising the surcharge by the 0.395 pp noted above, partly citing the Netze BW/Oxera material — but **retained the DMS-only MRP method**.

---

## 4. The OLG Düsseldorf proceedings (first instance)

### 4.1 The court, the scale and the case numbers

Roughly **900 network operators** filed appeals (*Beschwerden*) with the **3. Kartellsenat** of the **OLG Düsseldorf** (presiding judge **Vorsitzende Richterin am OLG Anne Frister**), which bundled them into **14 representative test cases** (*Musterverfahren*). By decision of **30 August 2023** the senate **annulled** the BNetzA's determinations (BK4-21-055 / -056) and ordered redetermination "unter Beachtung der Rechtsauffassung des Senats."

**Case numbers (Aktenzeichen).** The proceedings carry references in the form **3 Kart …/21**. Confirmed members of the cluster, all bearing the 30 August 2023 date, include **3 Kart 129/21, 311/21, 498/21, 544/21, 689/21, 757/21, 775/21, 878/21 and 908/21**. (Different sources nominate slightly different "lead" cases — 311/21, 498/21 and 757/21 each appear in that role — so the base report's identification of 311/21 as *the* lead case should be treated as one of several plausible leads rather than settled.) Two points of nomenclature were confirmed:

- The senate's decisions appear in the official OLG/press materials as **"VI-3 Kart …/21 (V)"** (the "VI-" denoting the Kartellsenat in the court's internal numbering, "(V)" a *Verwaltungssache*); the NRWE database and openJur drop the "VI-" prefix, rendering them as "3 Kart …/21." They are the same cases. Older (third-period) decisions used the "VI-3 Kart" form (e.g. VI-3 Kart 143/16 (V) and 335/16 (V), 22 March 2018).
- The **openJur permalink 2475051** corresponds to **3 Kart 878/21** — *not* 311/21. 878/21 was, in fact, an outlier: a complaint by a nationwide green-electricity/green-gas supplier arguing the rate was **too HIGH** (alleging improper political influence via the BNetzA advisory board); that complaint was **dismissed**, so it ran the opposite direction to the network-operator cases.

### 4.2 What the court held — the operative ruling

The senate **annulled** the BNetzA *Festlegung* of 12 October 2021 and **ordered the agency to re-determine** the equity-return rates for old and new assets for the relevant sector (BK4-21-055 for the electricity cluster, BK4-21-056 for the gas cluster), respecting the senate's legal view. The senate **admitted the *Rechtsbeschwerde*** (appeal on points of law) to the BGH. The electricity and gas proceedings ran in parallel on materially identical reasoning. *(The exact cost allocation and the value of the matter per case could not be confirmed from the accessible material.)*

### 4.3 The reasoning — grounds won and grounds lost

This is the analytical heart of the decision, and it resolves an apparent tension between the sibling reports (one of which said the OLG "dismissed the operators' complaints" on beta/peer-group, while the base report stressed the annulment).

**The single ground the operators WON on (the basis of annulment): the MRP/DMS plausibility-check point.** The senate held the determination substantively unlawful because the BNetzA had derived the MRP **solely from the DMS historical series without securing (*absichern*) that result by any further method — at minimum a supplementary plausibility check (*Plausibilisierung*)**. The senate's logic was that there were **concrete indications (*konkrete Anhaltspunkte*)** requiring verification: (i) the after-effects of the preceding low-interest phase; (ii) the marked **divergence** of the German result from the average of other (foreign) regulators' determinations; and (iii) the **non-replicability and undisclosed country-weighting** of the DMS world MRP (only the 1900 and 2020 endpoint weights being available, with unexplained discrepancies). Because of these red flags, the senate reasoned, a single-method derivation was not apt to ensure the resulting return was *angemessen, wettbewerbsfähig und risikoangepasst* (appropriate, competitive and risk-adjusted), and the approach therefore did not meet the normative requirements of **§ 7 Abs. 5 Nr. 2 StromNEV/GasNEV**. The court's characterisation of the agency's "restrictive and singular" reliance on the one DMS data series maps directly onto this finding.

**The grounds the operators LOST on (the BNetzA's approach CONFIRMED).** The senate **expressly confirmed the BNetzA's overall methodological approach** as not objectionable, including:

- **CAPM as the framework** (consistent with prior OLG/BGH jurisprudence);
- the **base rate** and its averaging window (the structure of an annually-variable base rate plus a constant surcharge, capped to the period, was the framework the court worked within and treated as within the agency's *Beurteilungsspielraum*);
- the **beta / risk factor and the peer group** (the comparator set of foreign listed pure network operators producing β ≈ 0.81 was treated as within the agency's discretion);
- the **level and method of the *Wagniszuschlag*** (including the 0.395 pp uplift);
- the **inflation and time-variability** sub-grounds (these were *not* the basis of annulment);
- and the green-supplier "too high" complaint (878/21), which was dismissed.

**The § 73 EnWG point — substantive, not formal.** Critically, the senate **accepted that the agency's written reasons satisfied § 73 EnWG** (the duty to give reasons): the BNetzA had engaged comprehensively with consultation submissions and expert opinions and explained why it used long-run DMS data and how it addressed criticism of replicability and the undisclosed weighting. The defect was therefore **materielle Rechtswidrigkeit** (substantive illegality) — a failure to ensure an adequate result — **not a *Begründungsmangel*** (formal reasoning defect). In short: the operators won on a single, narrow substantive ground (sufficient to annul, because the MRP feeds the whole equity return) and lost on everything else; and the court did not hold the rate "too low" in substance, but rather that the agency had not adequately *tested* whether its singular-method result was plausible given contrary market and international signals.

### 4.4 The contested figures the OLG relied on

The senate pointed to expert benchmarks materially above the BNetzA's result to show a lack of plausibility. The reliably attributable one:

- **6.82 %–7.04 %** — the **realised / implicit cost of equity for comparable companies**, per the **Bogner/Rabel *Gutachten*** referenced in the decision (the range depending on the assumed growth rate). This is the firmest of the OLG's "plausibility" benchmarks and is newly attributed here to Bogner/Rabel (the base report cited the figure without the source).

> **Verification flag.** The base report also cited a **"17-country comparison" producing ≈ 6.05 % after-tax cost of equity (range 4.30 %–7.50 %)**. These specific numbers **could not be independently confirmed** during research. A *different* international comparison surfaced repeatedly — the **NERA / BNetzA** figures of a German after-tax equity rate of about **5.64 %** versus an international average of about **6.83 % (≈ 7.13 % on the updated NERA basis)** — which should not be conflated with the "6.05 % / 17-country" figure. Treat the "6.05 %, range 4.30–7.50 %, 17 countries" trio as **uncertain pending the primary text**; the Bogner/Rabel 6.82–7.04 % and the NERA ≈ 6.83–7.13 % comparators are the better-supported benchmarks.

---

## 5. The BGH dimension and the EU-law backdrop

### 5.1 ECJ C-718/18 (2 September 2021) — the regulator's expanded discretion

On **2 September 2021** the ECJ ruled in **European Commission v Federal Republic of Germany, Case C-718/18** (ECLI:EU:C:2021:662) that Germany had failed to fulfil its obligations under the 2009 Electricity and Gas Directives.

> **Correction to the base report.** The judgment was rendered by the **Fourth Chamber (Vierte Kammer)**, *not* the Grand Chamber. This is confirmed across the Official Journal notice, the EUR-Lex CELEX metadata (62018CJ0718), the vLex digest, and the FRA case-law reference. The procedure was an infringement action under Article 258 TFEU (application lodged 16 November 2018), and the Court **fully upheld** the Commission's action.

The Commission's complaints (and the breaches found) spanned four areas:

1. **Definition of a "vertically integrated undertaking" (VIU)** — Art. 2(21) of Dir 2009/72/EC and Art. 2(20) of Dir 2009/73/EC: German law wrongly confined the VIU definition to activities *within the EU*; activities outside EU territory must also count.
2. **ITO unbundling / "cooling-off" transitional rules** — Art. 19(3), (5) and (8) of both directives: incomplete transposition of the independence/role-switching requirements for ITO staff and management.
3. and 4. **Independence and exclusive competence of the national regulatory authority (NRA)** — **Art. 37(1)(a) and (6)(a) and (b) of Dir 2009/72/EC** and **Art. 41(1)(a) and (6)(a) and (b) of Dir 2009/73/EC**.

> **Correction / precision on the Articles.** The base report attributed the independence point to "§ 24 EnWG ordinances" and to the directives generally. The **operative breaches concerning the regulator were of Art. 37 / Art. 41** (the provisions reserving to the NRA the powers and duties to fix or approve tariffs and the methodologies for calculating them, and to act with decisional independence). Commentary often invokes **Art. 35 (electricity) / Art. 39 (gas)** as the institutional-independence backdrop, but it could not be confirmed that Art. 35(4)/(5) or Art. 39(4)/(5) appear in the Court's **operative declaration**; the safest precise statement is that the regulator-related breaches were declared under **Art. 37 / Art. 41**.

The substance of the two regulator-related findings:

- **Independence.** The NRA must take its decisions **autonomously, solely in the public interest, and free from external instructions** from any other public or private body — including not only the government but also the **national legislature**. The German mechanism found non-compliant was the broad ordinance-making power in **§ 24 EnWG**, which let the federal government prescribe, by detailed *Rechtsverordnungen*, the "conditions and methods" of network access and charges binding on the BNetzA.
- **Exclusive competence.** Setting or approving the **methodologies** for calculating network-access terms and tariffs is a competence **directly and exclusively reserved to the independent NRA**; a Member State's legislature or executive may not pre-determine those regulatory decisions. The specific instruments condemned as encroaching on this competence were the detailed federal ordinances under § 24 EnWG — **StromNEV, GasNEV, StromNZV and the ARegV**. German commentary described this as "the end of *normative* (i.e. ordinance-driven) regulation."

As a successful Art. 258 action, Germany was (per the default rule, Art. 138(1) of the Rules of Procedure) **ordered to pay the costs**, though the verbatim costs order could not be confirmed from the operative part.

**The consequence for the equity-return litigation** was pivotal: the exercise migrated from the application of binding ordinance parameters to a **discretionary regulatory *Festlegung*** within the BNetzA's own **margin of appreciation (*Beurteilungsspielraum / Regulierungsermessen*)** — which in turn raised the central question of how intensively courts may review the agency's **choice of method**.

### 5.2 The interim window — how the October 2021 Festlegung was based

A subtlety important to the litigation: the BNetzA's equity-return *Festlegung* of October 2021 was issued **after** the 2 September 2021 ECJ ruling but **before** the implementing EnWG reform of late 2023. It was therefore grounded in the **still-in-force pre-reform ordinance framework** — expressly **§ 7 StromNEV/GasNEV** (and § 10a ARegV in conjunction with § 7 for the capital-cost surcharge), not the new BNetzA *Festlegungskompetenz* (which did not yet exist). The live legal question the BGH ultimately had to address was whether the agency, in that interim window, acted within an effectively-discretionary margin or remained bound by the (EU-incompatible) ordinance parameters. The BGH resolved it in the agency's favour.

### 5.3 The November/December 2023 EnWG reform

The implementing legislation was the **"Gesetz zur Anpassung des Energiewirtschaftsrechts an unionsrechtliche Vorgaben und zur Änderung weiterer energierechtlicher Vorschriften."**

> **Correction to the base report's "November 2023."** The **Bundestag adopted** the law on **10 November 2023**; it was published in **Bundesgesetzblatt 2023 I Nr. 405 (dated 28 December 2023)** and the EnWG amendments **entered into force on 29 December 2023**. So "November 2023" is the adoption date; the operative entry into force was the **end of December 2023**.

The reform implemented C-718/18 by **abolishing the broad federal ordinance-making power in § 24 EnWG** over network access and charges (and the § 24a transmission-charge authorisation), folding substantive content (e.g. parts of §§ 14a–d StromNEV) into the EnWG itself, and **transferring a determination competence (*Festlegungskompetenz*) to the BNetzA**. The key new/amended provisions (well-corroborated from secondary summaries, to be confirmed against the consolidated statute):

- the substantive BNetzA competence over network-tariff-system elements, **including the determination of the appropriate equity-capital remuneration (*Eigenkapitalverzinsung*) and the calculation of eligible network costs** — the provision most directly relevant to the equity-return exercise. *(Secondary summaries cite this competence variously as the new § 21 Abs. 3 EnWG and as § 21a EnWG; the precise section should be confirmed against the consolidated statute.)*
- **§ 23a EnWG** — powers to structure the tariff-approval procedure;
- **§ 29 EnWG** — the procedural backbone for BNetzA *Festlegungen*.

Independence was reinforced through a new **"Große Beschlusskammer"** (Grand Ruling Chamber) for fundamental determinations and the replacement of executive direction with autonomous BNetzA decision-making; residual democratic accountability runs through an advisory **Beirat** of **16 members of parliament** (consultative only), designed to stay within the ECJ's independence limits.

### 5.4 The BGH reverses the OLG

The BGH (Kartellsenat) reversed the OLG across a series of *Rechtsbeschwerde* decisions:

- **17 December 2024 — electricity** (decision name *"Eigenkapitalzinssatz IV"*). Lead decision **EnVR 79/23** (ECLI:DE:BGH:2024:171224BENVR79.23.0), with related same-day decisions including **EnVR 80/23, 85/23, 88/23, 91/23 and 94/23**, holding that the BNetzA had set the equity return for electricity networks **without legal error**.
- **25 February 2025 — gas** (likely *"Eigenkapitalzinssatz V"*). Lead decisions **EnVR 83/23, 86/23, 90/23 and 93/23** (e.g. ECLI:DE:BGH:2025:250225BENVR93.23.0), with further same-day siblings reported (e.g. EnVR 89/23, 92/23), rejecting the appeals of (per reporting) originally **937 gas network operators**, reversing the OLG's 30 August 2023 ruling, and imposing the **costs on the operator side**.
- **9 September 2025 — further confirmation.** **EnVR 82/23** (ECLI:DE:BGH:2025:090925BENVR82.23.0), which expressly endorses the increased risk surcharge as plausible and adequately reasoned, citing the standard set in EnVR 94/23 (17 Dec 2024).

> **Corrections to the base/sibling reports on EnVR 82/23.** Resolved during research: **EnVR 82/23 is a 9 September 2025 *electricity* decision** (its ECLI date-stamp is "090925"; its reasoning tracks the electricity ordinance, § 7 Abs. 4/5 StromNEV, and the 2.49 % → 0.74 % base-rate fall), **not** a 25 February 2025 gas decision. The February-2025 gas quartet is **83/23, 86/23, 90/23, 93/23**. Separately, general-press references to "a February 2024 reversal" are a **transposition error for February 2025**; the correct dates are 17 Dec 2024 (electricity) and 25 Feb 2025 (gas).

**The legal standard (the *Leitsatz*).** The BGH's guiding principle sets a markedly **deferential** bar. As reconstructed from the headnotes (verify the exact wording against the primary text), the regulator's **selection decision** among recognised scientific methods can be set aside **only** if:

- the chosen approach — resting on a recognised scientific method — is **"grundlegend ungeeignet"** / **"von vornherein ungeeignet"** (*fundamentally / from the outset unsuitable*) to fulfil the function assigned to it within the underlying model; **or**
- **another methodological approach would be "deutlich überlegen"** / **"so deutlich überlegen"** (*clearly / so clearly superior*) — weighing **suitability, data availability, the effort of ascertainment, and the precision and reliability of the results** — such that choosing a different method can no longer be regarded as compatible with the normative requirements.

(Both phrasings circulate in the headnote summaries; "von vornherein ungeeignet" and "so deutlich überlegen" appear to be the literal wording, with "grundlegend ungeeignet" a common paraphrase. Confirm against the primary text before quoting verbatim.)

A second, related headnote addresses the plausibility check directly: a *Plausibilisierung* of a result reached through the faultless selection and application of a method is required **only** where concrete circumstances make it appear necessary; the **mere conceivability** of such circumstances does **not** suffice, **because otherwise a methodologically pluralistic approach would always be required**. The trial judge (*Tatrichter*) may **not** impose on the regulator the application of another (allegedly superior) method, a mixing of methods, or a correction of an error-free result. The BGH also clarified a **division of labour**: whether the governing legal standard *requires* a plausibility check at all is a **question of law subject to full review**, but whether the concrete facts trigger one is for the *Tatrichter*; and the regulator has **no discretion** over *when* such concrete indications exist.

**Why the BGH reversed.** Applying that standard, the BGH held the OLG had **wrongly** treated the DMS-based approach as defective. The mere existence of other recognised methods, or the conceivability of a plausibility cross-check, does **not compel** one — to require a cross-check whenever one is conceivable would force methodological pluralism the statute does not demand. The court accepted that the **risk-premium uplift** the BNetzA had made — to offset the risk that the fallen base rate (0.74 % vs 2.49 %) understated the surcharge — was **plausible and adequately reasoned**, and rejected the OLG's criticism that the 1.75 pp base-rate fall was only partly offset by the 0.395 pp surcharge adjustment, holding that an *arithmetic* matching of the two was methodologically neither required nor appropriate. The court further noted the BNetzA had in fact checked that its result fell within the range of European comparator countries, which was legally sufficient.

> **One residual tension to verify.** A snippet from the EnVR 82/23 (9 Sep 2025) materials suggested the BGH there also addressed the **independence-of-the-NRA** dimension (§ 29 Abs. 1 i.V.m. § 21 Abs. 2 EnWG 2021) and the **international-comparison limb** (§ 7 Abs. 5 Nr. 2). It could not be confirmed from snippets alone whether the BGH affirmed the BNetzA *entirely* or affirmed the MRP-cross-check point while expecting better treatment of the international-comparison limb. The precise scope of what the BGH affirmed versus required should be checked against the full EnVR 82/23 and EnVR 83/23 texts. The overall outcome — reversal of the OLG and reinstatement of the BNetzA's determination — is, however, firmly established.

The BGH expressly linked its deference to the BNetzA's **post-C-718/18 status**: where the ordinance leaves room, the agency holds a *Beurteilungsspielraum* that courts may police at its outer limits but may **not hollow out** by themselves selecting among several lawful regulatory options. This tied the standard of review to the strengthened independence and competences confirmed by C-718/18 and the 2023 EnWG reform. *(The base report attributed a signal of this position to the presiding judge Wolfgang Kirchhoff at the December 2024 hearing; the identity of the presiding judge could not be independently confirmed from a retrievable source and should be treated as unverified.)*

---

## 6. Current status (mid-2026), stakes and outlook

### 6.1 Status of the fourth-period litigation

As of mid-2026 the litigation over the **fourth-period** equity return is, in substance, **closed in the BNetzA's favour**. The OLG's annulment was reversed; the **5.07 % (new) / 3.51 % (existing)** pre-tax figures stand, supplemented by the January-2024 time-variable uplift (~7.09 % for 2024) for post-2024 new investment. Because the BGH **upheld** the original determination (legality being judged as at the date of issuance), the redetermination the OLG had ordered did **not** materialise as a forced re-do of the methodology.

### 6.2 Financial stakes

The economic significance is large. Equity returns are an input to the *kalkulatorische Kapitalverzinsung*, which feeds the **revenue cap (Erlösobergrenze)** and thus the **network charges (Netzentgelte)** paid by households, businesses and industry. Each tenth of a percentage point, applied across a multi-billion-euro regulated asset base and the roughly **900** distribution operators in each sector, translates into substantial sums over a period running to 2027/2028; the *Energiewende* grid build-out implies investment needs of **hundreds of billions of euros** (≈ €651 bn in power grids to 2045 on one widely cited estimate).

Operators argued the rates were too low to attract the equity needed for the build-out; consumer and some analytical voices countered that headline regulatory rates understate actual returns. The most-cited example is a **Bundesverband Neue Energiewirtschaft (bne)** analysis finding that the **market-share-weighted commercial (HGB book) equity return of the 18 largest distribution operators averaged 30.1 % in 2024** (up from 16.6 % in 2023), with outliers such as EWE Netz (~61 %), Westnetz (~45 %) and Bayernwerk Netz (~38 %) — framed by bne as roughly six times the regulatory 5.07 %/3.51 %. This figure is **contested and is not a regulatory parameter**: as the regulatory analyst Marcel Linnemann (writing in ZfK) set out, it mixes **leverage effects** (return on a thin book-equity base is mechanically inflated for highly debt-financed utilities, before debt service) and an **accounting-basis mismatch** (HGB book equity is not the regulated asset base to which the 5.07 %/3.51 % rates apply), so comparing 30 % against 5.07 % is apples-to-oranges.

### 6.3 The fifth period and the new WACC — the NEST reform

The most important forward-looking change is methodological, and it is now **decided**, not merely proposed.

> **NEST** stands for **"Netze. Effizient. Sicher. Transformiert."** (Networks. Efficient. Secure. Transformed.) — a *Festlegungs*-reform package run by the BNetzA's **Große Beschlusskammer Energie** since 2024 that overhauls incentive regulation beyond the fourth period and sets the methodology for the fifth. (A gloss seen in one source, "Neue Energienetze Struktur und Technologie," is incorrect.)

The **final decisions (Festlegungen) were issued in December 2025**: the capital-return methodology was adopted on **8 December 2025**, announced by press release on **9 December 2025** ("Bundesnetzagentur legt Kostenregulierung für Strom- und Gasnetzbetreiber fest"), with the full package published on **10 December 2025**. The package comprises an overarching framework (RAMEN Strom/Gas), the network-charge methodology (StromNEF/GasNEF), the **capital-return (Kapitalverzinsung)** methodology, the efficiency benchmark (*Effizienzvergleich*) and the productivity factor.

The new cost-of-capital methodology:

- A **standardised WACC** ("Weighted Average Cost of Capital") replaces the separate equity-rate *Festlegung*, expressing the calculatory capital return in an internationally common format.
- A fixed notional capital structure of **40 % equity / 60 % debt** (the equity quota is held at the prior 40 % level).
- A **market-indexed, index-based cost of debt (*Fremdkapitalzins*)**: for **existing** assets, a **seven-year (where relevant investment-weighted) average** drawn from bond and loan interest-rate time series; for **new** investments, the **actual year-of-acquisition value**.
- An equity-side **base rate keyed to the current *Umlaufrendite*, now annually variable**, expressly **replacing the prior ten-year trailing average**, plus a constant risk surcharge of currently ~3 %.
- On the BNetzA's 2025 projections the implied **equity return could rise to roughly 6.5 %–7 %** (a projection that moves year-to-year with the *Umlaufrendite*; a related figure on 2024 yields is the ~7.09 % time-variable rate). The BNetzA estimates the WACC conversion alone lifts electricity-DSO revenues by about **+1.4 %**.

> **Corrections on the "3-year periods" and the debt window.** The **fifth period remains five years** (gas **2028–2032**, electricity **2029–2033**); the shortening of the regulatory cycle to **three years** is contemplated **from the sixth period** (gas 2033 / electricity 2034), not from the fifth. And the abandoned "ten-year average" refers specifically to the **equity-side base rate**; the new **debt** component uses a **seven-year** average (existing) or the current year-of-acquisition value (new).

The agency launched method-determination consultations on **30 June 2025** (deadline 18 August 2025), again drawing on a **Frontier/Zechner/Randl (2025)** methodology report (dated 13 January 2025, consultation to 28 February 2025), with **BDEW commissioning a competing case** — a **NERA** international-comparison study (positioning the international average as a lower bound) and a **Hachmeister/Pedell** methodology critique. *(Note: both the Hachmeister/Pedell brief and the NERA study were BDEW-commissioned; the existence of a separately-named, agency-commissioned independent plausibility *Kurzgutachten* distinct from these could not be confirmed.)* Industry reaction to the December finals was hostile — the VKU called them "enttäuschend und inadäquat," with the slogan that the BNetzA "baut kein stabiles NEST."

### 6.4 Doctrinal legacy

The episode's lasting legacy is the **judicial-review standard**. After C-718/18 and the BGH's 2024–2025 jurisprudence, the BNetzA enjoys a **wide, only thinly reviewable margin** in choosing among recognised cost-of-capital methods. Future challenges must clear the high **"fundamentally unsuitable / clearly superior"** threshold rather than merely show that a different, plausible method would have produced a higher number. That bar is reinforced by the BNetzA's own **method-pluralism** defence — and, tellingly, the fifth-period Frontier/Zechner/Randl report now itself **embraces multi-method plausibility checking**, stating that "the one single correct method does not exist" for the MRP. That is at once a direct response to the OLG's 2023 critique and an acknowledgement that the methodological debate the operators lost in court has nonetheless reshaped the agency's practice going forward.

---

## 7. Expanded timeline of key events

| Date | Event |
|---|---|
| **16 Nov 2018** | Commission lodges the infringement application in C-718/18. |
| **Jul 2021** | Frontier / Zechner / Randl *Gutachten* delivered (DMS-based MRP of 3.70 %); draft new-asset rate 4.59 %, draft existing-asset rate 3.03 %. |
| **9 Jul – 24 Aug 2021** | Counter-*Gutachten* filed: ValueTrust (9 Jul, BDEW), NERA (11 Jun, BDEW), Oxera (19 Aug, Netze BW/EnBW), Hachmeister/Pedell (BDEW), Wein (LichtBlick), and the DMS authors' own assessment via E.ON (24 Aug). |
| **2 Sep 2021** | ECJ (**Fourth Chamber**), **C-718/18**: Germany breached Dir 2009/72 & 2009/73 (VIU definition, ITO cooling-off, and — decisively — NRA independence and exclusive competence under Art. 37 / Art. 41); the § 24-EnWG ordinance regime (StromNEV/GasNEV/StromNZV/ARegV) condemned. |
| **12 Oct 2021** | BNetzA *Festlegungen* **BK4-21-055** (electricity) and **BK4-21-056** (gas): **5.07 %** (new) / **3.51 %** (existing), pre-tax, 4th period — base rate 0.74 %, surcharge 3.39 % (CAPM 3.70 % × 0.81, +0.395 pp). Announced 20 Oct 2021. |
| **2023** | 4th regulatory period begins for **gas**; ~900 operators appeal to the OLG Düsseldorf. |
| **30 Aug 2023** | **OLG Düsseldorf, 3. Kartellsenat** (Frister), 14 *Musterverfahren* (incl. 3 Kart 129/21, 311/21, 498/21, 544/21, 689/21, 757/21, 775/21, 878/21, 908/21): **annuls** BK4-21-055/-056 on the narrow DMS-plausibility ground; confirms beta/CAPM/base rate; holds § 73 EnWG reasons adequate (substantive defect); admits the *Rechtsbeschwerde*. |
| **10 Nov 2023** | Bundestag adopts the EnWG-amending law implementing C-718/18. |
| **29 Dec 2023** | EnWG amendment enters into force (BGBl 2023 I Nr. 405): § 24 ordinance-making for network charges abolished; new BNetzA *Festlegungskompetenz* (esp. § 21 Abs. 3, § 23a, § 29 EnWG); Große Beschlusskammer; 16-MP Beirat. |
| **24 Jan 2024** | BNetzA introduces a **time-variable** higher return (~7.09 % for 2024) for **new investments from 1 Jan 2024** in the KKAuf; existing-asset (3.51 %) and 2021-new-asset (5.07 %) rates otherwise unchanged. |
| **2024** | 4th regulatory period begins for **electricity**. |
| **17 Dec 2024** | **BGH** (**EnVR 79/23** + 85/23, 88/23, 94/23) **reverses** the OLG for **electricity**; confirms the BNetzA's methodology. |
| **13 Jan 2025** | Frontier/Zechner/Randl 5th-period methodology *Gutachten*; consultation to 28 Feb 2025; NERA (30 Jan 2025) and Hachmeister/Pedell counter-material for BDEW. |
| **25 Feb 2025** | **BGH** (**EnVR 83/23, 86/23, 90/23, 93/23**) **reverses** the OLG for **gas**; rejects ~937 operators' appeals; costs on operators. |
| **30 Jun 2025** | BNetzA opens consultations on the fifth-period method *Festlegungen* (deadline 18 Aug 2025). |
| **9 Sep 2025** | **BGH EnVR 82/23** (electricity) — further confirmatory decision. |
| **8–10 Dec 2025** | **NEST** final decisions: standardised **WACC** (40/60), 7-yr indexed debt cost, variable *Umlaufrendite* base + ~3 % surcharge; projected equity return ~6.5–7 %. |
| **2028 / 2029** | Planned start of the **fifth regulatory period** (gas/electricity), 5-year period; 3-year cycle contemplated from the 6th period (gas 2033 / electricity 2034). |

---

## 8. Key decisions and cited sources — annotated

**ECJ — Commission v Germany, C-718/18 (2 September 2021), Fourth Chamber, ECLI:EU:C:2021:662 (CELEX 62018CJ0718).** Infringement action under Art. 258 TFEU. *Held:* Germany failed to fulfil its obligations under Directives 2009/72/EC (electricity) and 2009/73/EC (gas) on four counts — the over-narrow (EU-only) definition of a "vertically integrated undertaking" (Art. 2(21)/2(20)); incomplete transposition of the ITO independence/"cooling-off" rules (Art. 19(3),(5),(8)); and, decisively, the encroachment on the NRA's **independence** and its **exclusive competence** to fix or approve network tariffs and the methodologies for calculating them (Art. 37(1)(a),(6)(a),(b) / Art. 41(1)(a),(6)(a),(b)). *Reasoning:* the NRA must decide autonomously, solely in the public interest, and free from instructions from government **or** legislature; the federal government's detailed ordinances under § 24 EnWG (StromNEV, GasNEV, StromNZV, ARegV) unlawfully pre-determined decisions reserved to the regulator. *Effect:* Germany had to remove the ordinance-based pre-determination and equip the BNetzA with its own determination competence; for the equity-return exercise, this converted the task into a discretionary *Festlegung* within the agency's margin of appreciation, with consequences for the depth of judicial review. Germany was ordered to pay the costs (per the default rule).

**OLG Düsseldorf, 3. Kartellsenat, 30 August 2023 — 14 Musterverfahren (e.g. 3 Kart 129/21, 311/21, 498/21, 544/21, 689/21, 757/21, 775/21, 878/21, 908/21).** Presiding judge Anne Frister. *Held:* the BNetzA's *Festlegungen* BK4-21-055 (electricity) and BK4-21-056 (gas) of 12 October 2021 are annulled; the agency must re-determine the equity rates respecting the senate's legal view; *Rechtsbeschwerde* admitted. *Reasoning:* the determination was **substantively** unlawful because the BNetzA derived the MRP solely from the DMS historical series without the required plausibility check, despite concrete indications (low-rate after-effects; divergence from foreign regulators; non-replicable, undisclosed country weighting) — failing § 7 Abs. 5 Nr. 2 StromNEV/GasNEV. The agency's CAPM framework, base rate, peer-group beta (β ≈ 0.81) and the level of the surcharge were **confirmed** as within its discretion; the § 73 EnWG **reasoning was adequate** (the defect was substantive, not formal). The senate cited the Bogner/Rabel *Gutachten* (implicit cost of equity 6.82 %–7.04 %) as a contrary plausibility benchmark. *Effect:* first-instance victory for operators — but a narrow, method-specific one — later reversed by the BGH. The openJur permalink for 878/21 is 2475051 (an outlier "rate-too-high" complaint, dismissed).

**BGH (Kartellsenat), 17 December 2024 — EnVR 79/23 (electricity; "Eigenkapitalzinssatz IV"; + same-day siblings incl. EnVR 80/23, 85/23, 88/23, 91/23, 94/23).** *Held:* the OLG is reversed; the BNetzA set the electricity equity return without legal error. *Reasoning / Leitsatz:* the regulator's choice among recognised scientific methods is reviewable only if the chosen method is "grundlegend ungeeignet" / "von vornherein ungeeignet" or another is "(so) deutlich überlegen" (weighing suitability, data availability, effort, precision/reliability); the mere conceivability of a plausibility cross-check does not compel one. The base-rate fall (2.49 % → 0.74 %) and the 0.395 pp surcharge uplift were plausible and adequately reasoned; arithmetic matching of base-rate fall and surcharge is not required. *Effect:* the lead authority confirming the BNetzA's electricity determination.

**BGH (Kartellsenat), 25 February 2025 — EnVR 83/23, 86/23, 90/23, 93/23 (gas; likely "Eigenkapitalzinssatz V"; further siblings reported, e.g. 89/23, 92/23).** *Held:* the OLG's 30 August 2023 ruling is reversed; the appeals of the gas operators (reportedly ~937) are rejected; costs on the operator side. *Reasoning:* it was legally erroneous to require the BNetzA to subject an unobjectionably-calculated MRP to an additional plausibility review; the DMS-based MRP (3.70 %) and beta (0.81) were plausible and consistent given the low-interest phase; the international-comparison/§ 7 Abs. 5 Nr. 2 duty was satisfied by the agency's check that its result lay within the European range. *Effect:* extends the December-2024 result to the gas sector.

**BGH (Kartellsenat), 9 September 2025 — EnVR 82/23 (electricity), ECLI:DE:BGH:2025:090925BENVR82.23.0.** *Held:* further confirmatory decision in the electricity strand, resolving a remaining proceeding consistent with the 17 December 2024 reasoning, and (per a snippet) touching the EU-law-guaranteed independence of the NRA. *Caveat:* despite some source labelling, this is a **9 September 2025 electricity** decision, not a February-2025 gas case; and the precise scope of what it affirmed versus required on the international-comparison limb should be confirmed against the primary text.

**BNetzA Festlegungen BK4-21-055 / BK4-21-056 (12 October 2021).** Legal basis § 7 Abs. 6 StromNEV/GasNEV (competence/timing; via § 29 Abs. 1 / § 21 Abs. 2 EnWG) and § 7 Abs. 4/5 (methodology). *Effect:* set the fourth-period pre-tax equity rates — 5.07 % (new) / 3.51 % (existing), uniform across electricity and gas — from a base rate of 0.74 % and a surcharge of 3.39 % (CAPM 3.70 % × 0.81, plus a 0.395 pp uplift), grossed up by a tax factor of ~1.226.

**BNetzA Festlegung of 24 January 2024 (BK4-23-0004).** *Effect:* introduced a time-variable equity return for new investments in the capital-cost surcharge from 1 January 2024 (recent-*Umlaufsrendite* base + constant 3 % surcharge), implying ~7.09 % for 2024; left the 2021 rates otherwise in force.

**EnWG amendment, "Gesetz zur Anpassung des Energiewirtschaftsrechts an unionsrechtliche Vorgaben …" (Bundestag 10 Nov 2023; BGBl. 2023 I Nr. 405, gazetted 28 Dec 2023; in force 29 Dec 2023).** *Effect:* abolished § 24 (and § 24a) ordinance-making for network charges; created the BNetzA *Festlegungskompetenz* (the equity-remuneration / network-cost-methodology competence cited as § 21 Abs. 3 or § 21a EnWG; plus § 23a and § 29); established the Große Beschlusskammer and a 16-MP advisory Beirat — implementing C-718/18.

**NEST final decisions (8–10 December 2025).** *Effect:* from the fifth regulatory period, a standardised WACC (40 % equity / 60 % debt), a market-indexed cost of debt (7-year average for existing assets; year-of-acquisition value for new), and an annually variable *Umlaufrendite* base rate plus ~3 % surcharge; projected equity return ~6.5–7 %; estimated +1.4 % electricity-DSO revenue effect; 5-year fifth period, with a 3-year cycle contemplated from the sixth.

---

## 9. Source-status note (research conditions)

Across all research streams, the primary-source servers — bundesnetzagentur.de, the NRW courts database (nrwe.justiz.nrw.de), openJur, juris/bundesgerichtshof.de, NWB (datenbank.nwb.de), dejure.org, rechtsportal.de, curia.europa.eu, EUR-Lex, the consultants' sites (oxera.com, frontier-economics.com, the ctfassets CDN), and most legal blogs — returned **HTTP 403 to automated retrieval**. The findings above were therefore triangulated from **search-engine extraction** of those same pages plus reputable secondary commentary (beck-aktuell, BBH/die-bbh-gruppe, Noerr, Raue, White & Case, Chatham Partners, Herbert Smith Freehills Kramer, JUVE, Handelsblatt, Energie & Management, ZfK, IWR, pv-magazine, Grant Thornton, rhenag-legal, ebnerstolz). The numbers, dates and case numbers are **multiply corroborated**, but the **verbatim** *Tenor*, *Leitsätze* and reasoning paragraphs — and the costs orders — were **not read in primary text** and should be confirmed against the originals at the URLs in §11.

---

## 10. Caveats on verification (and corrections to the base report)

**Corrections made in this deep-dive relative to the base report:**

- **C-718/18 was decided by the Fourth Chamber, not the Grand Chamber.** The regulator-related breaches were of **Art. 37 / Art. 41** (not Art. 35/39, which are commentary-level context).
- **The EnWG reform entered into force on 29 December 2023** (Bundestag adoption 10 November 2023), not "November 2023" as an entry-into-force date.
- **EnVR 82/23 is a 9 September 2025 electricity decision**, not a 25 February 2025 gas decision; the February-2025 gas quartet is 83/23, 86/23, 90/23, 93/23.
- **The existing-asset rate is 3.51 % uniform** for electricity and gas; the "3.03 % for gas" is the **July-2021 draft** rate and, separately, the **EK-II** rate — not the in-force existing-asset rate.
- **The CAPM build-up is 4.13 % after-tax × 1.226 = 5.07 %**; the "3.51 % × 1.22" gross-up sometimes seen is a garbled summary.
- **The January-2024 step left the existing-asset rate at 3.51 %** (not "5.07 % incl. trade tax"); 5.07 %/5.8 % is the new-asset figure.

**Items still to verify against primary text:**

- **The "6.05 % / range 4.30–7.50 % / 17-country" OLG figures could not be confirmed.** The supportable OLG benchmark is the **Bogner/Rabel** implicit cost of equity of **6.82–7.04 %**; the supportable international comparison is **NERA's** German ≈ 5.64 % vs international ≈ 6.83–7.13 % after tax. Do not state the 6.05 %/17-country trio as verified.
- **The exact roster of all 14 *Musterverfahren*** and the single authoritative "lead" case per sector (311/21, 498/21 and 757/21 each appear as a lead in different sources).
- **The precise new EnWG section** carrying the equity-remuneration *Festlegungskompetenz* — cited as both § 21 Abs. 3 and § 21a in secondary summaries; confirm against the consolidated statute. The BGBl citation (2023 I Nr. 405, gazetted 28 Dec 2023, in force 29 Dec 2023) is firm.
- **The exact same-day sibling rosters** of the BGH decisions (additional electricity siblings EnVR 80/23, 91/23; additional gas siblings EnVR 89/23, 92/23 are reported but not fully confirmed) and the official decision names ("Eigenkapitalzinssatz IV" for the electricity tranche; "Eigenkapitalzinssatz V" for gas is probable but unconfirmed).
- **The exact verbatim *Leitsätze* and *Tenor*** of the OLG and BGH decisions, and the costs orders.
- **The presiding-judge identity at the BGH** (Wolfgang Kirchhoff) — not independently confirmed.
- **The precise scope of the BGH's holding in EnVR 82/23** on the international-comparison limb and NRA independence.
- **The claim that "Randl himself acknowledged time-variability"** — not confirmed; attributable instead to Stehle/Betzer and to the fifth-period "no single correct method" statement.
- **The "~30 % commercial equity return"** is a contested third-party (bne) analysis mixing leverage and accounting effects — not a regulatory parameter.
- **The fifth-period WACC has no fixed headline number**, by design: it is recalculated annually from the *Umlaufrendite*. The ~6.5–7 % is a projection; cite it as such.

---

## 11. Sources

1. IWR, "Bundesnetzagentur senkt Eigenkapitalzinssätze für Netze – Branche gespalten." https://www.iwr.de/news/bundesnetzagentur-senkt-eigenkapitalzinssaetze-fuer-netze-branche-gespalten-news37644
2. IWR, "BNetzA legt neue Festlegung zur Eigenkapitalverzinsung von Neuanlagen … vor." https://www.iwr.de/news/bnetza-legt-neue-festlegung-zur-eigenkapitalverzinsung-von-neuanlagen-im-strom-und-gas-netzbereich-vor-news38552
3. Energie & Management, "Letzte Instanz winkt Eigenkapitalzins Gas durch." https://www.energie-und-management.de/nachrichten/recht/detail/letzte-instanz-winkt-eigenkapitalzins-gas-durch-254213
4. Bundesnetzagentur, "Der Eigenkapitalzinssatz" (Fachthemen / Aktuelles_enwg). https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/Aktuelles_enwg/EKZ/artikel.html
5. § 7 StromNEV (Kalkulatorische Eigenkapitalverzinsung), buzer.de. https://www.buzer.de/gesetz/6824/a96934.htm
6. Bundesnetzagentur, press release "Bundesnetzagentur veröffentlicht Festlegung der Eigenkapitalverzinsung" (20 Oct 2021). https://www.bundesnetzagentur.de/SharedDocs/Pressemitteilungen/DE/2021/20211020_EKZins.html
7. Bundesnetzagentur, press release "Bundesnetzagentur veröffentlicht Entwürfe für zukünftige Eigenkapitalverzinsung für Strom- und Gasnetze" (14 Jul 2021). https://www.bundesnetzagentur.de/SharedDocs/Pressemitteilungen/DE/2021/20210714_EKZins.html
8. Bundesnetzagentur, decision pages **BK4-21-0055** (electricity) / **BK4-21-0056** (gas). https://www.bundesnetzagentur.de/DE/Beschlusskammern/1_GZ/BK4-GZ/2021/BK4-21-0055/BK4-21-0055_Beschluss.html and https://www.bundesnetzagentur.de/DE/Beschlusskammern/1_GZ/BK4-GZ/2021/BK4-21-0056/BK4-21-0056_Beschluss.html
9. Bundesnetzagentur, Zechner/Randl (Frontier Economics), "Wissenschaftliches Gutachten zur Ermittlung der Zuschläge für unternehmerische Wagnisse von Strom- und Gasnetzbetreibern" (Jul 2021). https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Energie/Unternehmen_Institutionen/Netzentgelte/Anreizregulierung/Gutachten/GutachtenZuschlaegeWagnisse.pdf
10. Bundesnetzagentur, press release "Festlegung zur Eigenkapitalverzinsung von Neuanlagen im Strom- und Gasbereich" (24 Jan 2024). https://www.bundesnetzagentur.de/SharedDocs/Pressemitteilungen/DE/2024/20240124_EKZins.html
11. ZfK, "Nur Neuanlagen werden höher verzinst." https://www.zfk.de/politik/regulierung/neuanlagen-werden-hoeher-verzinst
12. ZfK, "Eigenkapitalzins-Satz-Debatte gewinnt Fahrt" (6.5–7 % projection). https://www.zfk.de/politik/regulierung/eigenkapitalzins-satz-debatte-gewinnt-fahrt
13. Verbraucherzentrale Bundesverband (vzbv), Stellungnahme zu den BNetzA-EK-Zins-Beschlüssen (25 Aug 2021). https://www.vzbv.de/sites/default/files/2021-09/2021_08_25_Stellungnahme_vzbv_Beschl%C3%BCsse_BNetzA_EKZS_final.pdf
14. VKU, "Netzausbau: VKU unterstreicht Notwendigkeit weiterer Anhebungen bei der Eigenkapitalverzinsung." https://www.vku.de/presse/pressemitteilungen/netzausbau-vku-unterstreicht-notwendigkeit-weiterer-anhebungen-bei-der-eigenkapitalverzinsung/
15. OLG Düsseldorf, Beschluss vom 30.08.2023, **3 Kart 311/21** (NRWE). https://nrwe.justiz.nrw.de/olgs/duesseldorf/j2023/3_Kart_311_21_Beschluss_20230830.html
16. OLG Düsseldorf, Beschluss vom 30.08.2023, **3 Kart 498/21** (NRWE). https://nrwe.justiz.nrw.de/olgs/duesseldorf/j2023/3_Kart_498_21_Beschluss_20230830.html
17. OLG Düsseldorf, Beschluss vom 30.08.2023, **3 Kart 544/21** (NRWE). https://nrwe.justiz.nrw.de/olgs/duesseldorf/j2023/3_Kart_544_21_Beschluss_20230830.html
18. OLG Düsseldorf, Beschluss vom 30.08.2023, **3 Kart 689/21** (NRWE). https://nrwe.justiz.nrw.de/olgs/duesseldorf/j2023/3_Kart_689_21_Beschluss_20230830.html
19. OLG Düsseldorf, Beschluss vom 30.08.2023, **3 Kart 757/21** (NRWE). https://nrwe.justiz.nrw.de/olgs/duesseldorf/j2023/3_Kart_757_21_Beschluss_20230830.html
20. OLG Düsseldorf, Beschluss vom 30.08.2023, **3 Kart 878/21** (also openJur 2475051). https://openjur.de/u/2475051.html
21. OLG Düsseldorf, Pressemitteilung 30.08.2023, "Erfolg für Strom- und Gasnetzbetreiber: Renditenfestsetzung der Bundesnetzagentur aufgehoben." https://www.olg-duesseldorf.nrw.de/behoerde/presse/Archiv/Pressemitteilungen_aus_2023/20230830_PM_Netzentgeltregulierung/index.php
22. Otto Schmidt, "Eigenkapitalzinssätze für Strom- und Gasnetzbetreiber aufgehoben" (cites VI-3 Kart 129/21 (V); Frister; 14 Musterverfahren). https://www.otto-schmidt.de/news/wirtschaftsrecht/eigenkapitalzinssatze-fur-strom-und-gasnetzbetreiber-aufgehoben-2023-08-31.html
23. Ebner Stolz, "Eigenkapitalverzinsung für Strom- und Gasnetze rechtswidrig." https://www.ebnerstolz.de/de/unser-angebot/branchen/energie-und-infrastruktur/eigenkapitalverzinsung-fuer-strom-und-gasnetze-rechtswidrig-21849.html
24. BGH, Beschluss vom 17.12.2024, **EnVR 79/23** (electricity; NWB summary). https://datenbank.nwb.de/Dokument/1062739/
25. beck-aktuell, "Eigenkapitalzinssätze der Stromnetzbetreiber: BGH bestätigt Bundesnetzagentur" (19.12.2024). https://www.beck-aktuell.de/heute-im-recht/rechtsprechung/bgh-rendite-eigenkapital-zinsaetze-stromnetzbetreiber-2024-12-19
26. Handelsblatt, "Strom: Netzbetreiber scheitern vor BGH mit Rendite-Beschwerde." https://www.handelsblatt.com/unternehmen/energie/strom-netzbetreiber-scheitern-vor-bgh-mit-rendite-beschwerde/100095639.html
27. BGH, Beschluss vom 25.02.2025, **EnVR 93/23** (gas; NWB summary). https://datenbank.nwb.de/Dokument/1069152/
28. BGH, Beschluss vom 25.02.2025, **EnVR 83/23** (gas; NWB summary). https://datenbank.nwb.de/Dokument/1069161/
29. BGH, Beschluss vom 25.02.2025, **EnVR 86/23** (gas; NWB summary). https://datenbank.nwb.de/Dokument/1068740/
30. BGH, Beschluss vom 09.09.2025, **EnVR 82/23** (electricity; ECLI:DE:BGH:2025:090925BENVR82.23.0). https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/UebrigeSenate/KartS/2023/EnVR__82-23.pdf
31. Rechtsportal, BGH-Leitsatz "Festlegung der Eigenkapitalzinssätze für die vierte Regulierungsperiode …" https://www.rechtsportal.de/Rechtsprechung/Rechtsprechung/2024/BGH/Festlegung-der-Eigenkapitalzinssaetze-fuer-die-vierte-Regulierungsperiode-Ermittlung-angemessener-Eigenkapitalzinssaetze-durch-die-Bundesnetzagentur2
32. JUVE, "Bundesgerichtshof kassiert erneut Urteil des OLG Düsseldorf." https://www.juve.de/verfahren/bundesgerichtshof-kassiert-erneut-urteil-des-olg-duesseldorf/
33. rhenag-legal, "BGH bestätigt die Festlegung der Eigenkapitalzinssätze der Bundesnetzagentur für die vierte Regulierungsperiode." https://rhenag-legal.de/blog/bgh-bestaetigt-die-festlegung-der-eigenkapitalzinssaetze-der-bundesnetzagentur-fuer-die-vierte-regulierungsperiode
34. ECJ, Urteil vom 02.09.2021, **C-718/18**, Commission v Germany (EUR-Lex, CELEX 62018CJ0718; ECLI:EU:C:2021:662). https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62018CJ0718
35. LTO, "EuGH: Bundesnetzagentur nicht unabhängig genug." https://www.lto.de/recht/nachrichten/n/eugh-71818-bundesnetzagentur-bnetza-politische-einflussnahme-unabhaengigkeit-netzentgelt-energiewende
36. White & Case, "European Court of Justice on the independence of the German energy regulator (C-718/18)." https://www.whitecase.com/insight-alert/european-court-justice-independence-german-energy-regulator
37. Chatham Partners, "ECJ attests to lack of independence of the Federal Network Agency." https://chatham.partners/insights/ecj-attests-to-lack-of-independence-of-the-federal-network-agency/
38. VKU, "Energiewirtschaftsgesetz wird novelliert." https://www.vku.de/themen/recht/artikel/energiewirtschaftsgesetz-wird-novelliert/
39. buzer.de, Änderungen EnWG vom 29.12.2023 (Gesetz zur Anpassung des Energiewirtschaftsrechts an unionsrechtliche Vorgaben). https://www.buzer.de/gesetz/2151/v306746-2023-12-29.htm
40. BDEW, Zusammenfassung EnWG-Novelle 2023. https://www.bdew.de/media/original_images/2023/11/16/bdew_zusammenfassung_enwg-novelle_2023_10112023.pdf
41. dejure.org, § 29 EnWG (Verfahren zur Festlegung und Genehmigung). https://dejure.org/gesetze/EnWG/29.html
42. NERA Economic Consulting (for BDEW), "Eigenkapitalzinssatz – internationaler Vergleich der EK-Zins-Festlegungen." https://www.bdew.de/media/documents/NERA_Internationaler_Vergleich_EK_Zins_Festlegungen.pdf
43. NERA Economic Consulting (for BDEW), "Vergleich internationaler Eigenkapitalzinssätze" (11 Jun 2021). https://www.bdew.de/media/documents/NERA_EK_I_internationaler_Vergleich_11_06_2021_final.pdf
44. Oxera (for Netze BW/EnBW), "Bestimmung des Wagniszuschlags — Stellungnahme zum Gutachten von Frontier Economics" (19 Aug 2021, EN version). https://www.oxera.com/wp-content/uploads/2021/09/Bestimmung-des-Wagniszuschlags-Stellungnahme-zum-Gutachten-von-Frontier-Economics-EN-1.pdf
45. ValueTrust (for BDEW), "Gutachtliche Stellungnahme zur kapitalmarktkonformen Ermittlung CAPM-basierter Eigenkapitalkosten" (9 Jul 2021). https://www.bdew.de/media/documents/ValueTrust_Gutachten_Methodik_Eigenkapitalkostenermittlung_final_09_07_2021.pdf
46. Hachmeister/Pedell, Stellungnahme/Gutachten (BK4-21-0055 Stellungnahmen). https://www.bundesnetzagentur.de/DE/Beschlusskammern/1_GZ/BK4-GZ/2021/BK4-21-0055/Stellungnahmen/5_G/BK4-21-0055_Stellungnahme_Gutachten%20Hachmeister%20Pedell.pdf
47. Dimson/Marsh/Staunton assessment for E.ON (BK4-21-0055 Stellungnahmen, 24 Aug 2021). https://www.bundesnetzagentur.de/DE/Beschlusskammern/1_GZ/BK4-GZ/2021/BK4-21-0055/Stellungnahmen/5_G/BK4-21-0055_Stellungnahme_E.ON_DMS-Report.pdf
48. Credit Suisse Research Institute, "Global Investment Returns Yearbook 2021 — Summary Edition" (32 markets + 90-country world index; 23 with full history). https://www.credit-suisse.com/media/assets/corporate/docs/about-us/research/publications/credit-suisse-global-investment-returns-yearbook-2021-summary-edition.pdf
49. Solarserver, "Gutachten: BNetzA setzt Zinsen für Netzbetreiber zu hoch an" (Prof. Wein / LichtBlick). https://www.solarserver.de/2021/09/06/gutachten-bnetza-setzt-zinsen-fuer-netzbetreiber-zu-hoch-an/
50. Bundesnetzagentur, Methodenfestlegung Kapitalverzinsung ab 5. RP (GBK), Verfahrensseite. https://www.bundesnetzagentur.de/DE/Beschlusskammern/GBK/Methoden_Ebene2/Kapitalverzinsung/start.html
51. Bundesnetzagentur, press release "Konsultationen zu Methodenfestlegungen für Strom und Gas" (30 Jun 2025). https://www.bundesnetzagentur.de/SharedDocs/Pressemitteilungen/DE/2025/20250630_MethodenfestlegungGBK.html
52. Bundesnetzagentur, press release "Bundesnetzagentur legt Kostenregulierung für Strom- und Gasnetzbetreiber fest" (NEST, 9 Dec 2025). https://www.bundesnetzagentur.de/SharedDocs/Pressemitteilungen/DE/2025/20251209_NEST.html
53. pv-magazine, "NEST-Prozess: Bundesnetzagentur legt Anreizregulierung für Netze fest" (10 Dec 2025). https://www.pv-magazine.de/2025/12/10/nest-prozess-bundesnetzagentur-legt-anreizregulierung-fuer-netze-fest/
54. VKU, "VKU zur Anreizregulierung: Bundesnetzagentur baut kein stabiles NEST für Investitionsanreize" (10 Dec 2025). https://www.vku.de/presse/pressemitteilungen/vku-zur-anreizregulierung-bundesnetzagentur-baut-kein-stabiles-nest-fuer-investitionsanreize/
55. Noerr, "NEST-Beschlüsse bringen Dynamik in die Netzentgeltregulierung für Strom und Gas." https://www.noerr.com/de/insights/nest-beschlusse-bringen-dynamik-in-die-netzentgeltregulierung-fur-strom-und-gas
56. Grant Thornton, "Aktuelle Entwicklungen zur Eigenkapitalverzinsung von Netzbetreibern: Neue WACC-Berechnung im Fokus" (2025). https://www.grantthornton.de/themen/2025/aktuelle-entwicklungen-zur-eigenkapitalverzinsung-von-netzbetreibern-neue-wacc-berechnung-im-fokus/
57. Herbert Smith Freehills Kramer, "NEST Decisions set new course for German electricity and gas network regulation." https://www.hsfkramer.com/notes/energy/2026-posts/nest-decisions-set-new-course-for-german-electricity-and-gas-network-regulation
58. bne, "bne-Analyse: Netzbetreiber erzielen Rekordrenditen — dennoch gibt es eine Netzkrise." https://www.bne-online.de/bne-analyse-netzbetreiber-erzielen-rekordrenditen-dennoch-gibt-es-eine-netzkrise/
59. ZfK (Marcel Linnemann), "Stromnetz-Rendite: Wie die Zahlen wirklich zu lesen sind." https://www.zfk.de/politik/regulierung/stromnetz-rendite-marcel-linnemann-wie-zahlen-wirklich-zu-lesen-sind
60. Energie-Chronik (udo-leuschner.de), "Stromnetzbetreiber scheitern mit Klagen auf höhere Eigenkapitalrenditen." https://www.energie-chronik.de/250104.htm
61. IMK / Hans-Böckler-Stiftung, "Studie berechnet Investitionsbedarf in deutsche Stromnetze" (~€651 bn to 2045). https://www.imk-boeckler.de/de/pressemitteilungen-15992-studie-berechnet-investitionsbedarf-in-deutsche-stromnetze-65371.htm
62. Frontier Economics, "Estimating cost of equity for German gas and electricity networks." https://www.frontier-economics.com/uk/en/news-and-insights/news/news-article-i8670-estimating-cost-of-equity-for-german-gas-and-electricity-networks/
63. E-Control (Randl/Zechner), "Gutachten zur Ermittlung von angemessenen Finanzierungskosten für Gas-Fernleitungsbetreiber" (3 Nov 2019). https://www.e-control.at/documents/1785851/0/GutachtenRandlZechner20191103_KapitalkostenGasfernleitungsbetreiber+(3).pdf
64. Bundesnetzagentur (railway), "Methodenbericht Zins 2021" (Frontier/IGES/Zechner/Randl). https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Eisenbahn/VeroeffentlichungenGutachten/MethodenberichtZins2021.pdf
65. WIK, Working Paper No. 11 (Dec 2025) — German network cost-of-capital / NEST context. https://www.wik.org/fileadmin/user_upload/Unternehmen/Veroeffentlichungen/Working_Papers/2025/WIK-Working_Paper_No11.pdf
