# WACC-Replikationsmodell — Randl/Zechner-Gutachten (Strom & Gas)

Reproduzierbares Python-Modell zur Nachrechnung der regulatorisch festgelegten
Kapitalkosten für Strom- und Gasnetze, aufgesetzt für eine Masterarbeit. Es
deckt zwei regulatorische Regime ab, die beide auf den Gutachten von
**Univ.-Prof. Dr. Otto Randl** und **Univ.-Prof. Dr. Josef Zechner** (WU Wien)
beruhen:

| Regime | Größe | Methodik | Status im Modell |
|---|---|---|---|
| **DE — Bundesnetzagentur** | kalkulatorischer Eigenkapitalzinssatz (EK I/EK II), 3. & 4. Regulierungsperiode, Strom & Gas | gekappter CAPM nach §7 StromNEV/GasNEV | **voll rekonstruiert** (reproduziert die veröffentlichten Werte) |
| **AT — E-Control** | klassischer WACC (real, vor Steuern), Strom & Gas, Bestand & Neuinvestition | Textbook-WACC, Tax-Wedge auf EK | **Struktur + Zielwerte + Kalibrierung**; Detail-Inputs aus PDFs zu ergänzen |

> ⚠️ **Datenlage / Validierung:** Die Behörden-PDFs (bundesnetzagentur.de,
> e-control.at) waren in der Bau-Umgebung durch eine Egress-Firewall gesperrt.
> Alle Werte stammen aus quer-verifizierten Sekundär-/Indexquellen und sind im
> Code als **verifiziert** bzw. **zu verifizieren** gekennzeichnet. Vor
> Verwendung in der Arbeit bitte gegen die Original-Festlegungen prüfen (siehe
> [`SOURCES.md`](SOURCES.md)).

---

## Schnellstart

```bash
cd wacc_model
python scripts/run_all.py          # Vergleichstabellen DE + AT
pip install pytest && pytest -q    # Validierung gegen veröffentlichte Werte
```

Das Modell selbst nutzt **nur die Python-Standardbibliothek** (Python ≥ 3.10);
`pytest` wird nur für die Tests benötigt.

---

## Aufbau

```
wacc_model/
├── wacc/
│   ├── capm.py          # CAPM-Kern: Kosten EK/FK, Un-/Relevering von Beta
│   ├── conversions.py   # real↔nominal (Fisher), vor↔nach Steuern
│   ├── germany.py       # BNetzA EK-Zinssatz (EK I/EK II)
│   ├── austria.py       # E-Control WACC + Beta-Kalibrierung
│   └── cases/
│       ├── de_bnetza.py   # Parametersätze DE P3/P4 Strom & Gas
│       └── at_econtrol.py # Konstanten + veröffentlichte WACCs + Template
├── scripts/run_all.py   # reproduziert alle Kopfzahlen
└── tests/               # Validierung & Formel-Konsistenz
```

---

## Methodik

### Deutschland — BNetzA (§7 StromNEV/GasNEV)

Die Bundesnetzagentur bestimmt **kein klassisches WACC**, sondern einen
regulierten Eigenkapitalzinssatz nach einem gekappten CAPM. Es gibt zwei
Sätze: **EK I** für Neuanlagen (nominal) und **EK II** für Altanlagen (real).

```
Wagniszuschlag       = Beta · Marktrisikoprämie            (+ ggf. Aufschlag)
EK I (nom., vor KSt) = (r_f + Wagniszuschlag) · Steuerfaktor
EK II (real, vor KSt)= EK I − Ø-Inflation (10-J. VPI)
```

* `r_f` = 10-Jahres-Durchschnitt der Umlaufrenditen (Dt. Bundesbank).
* `Steuerfaktor ≈ 1,225` rechnet vom Nach-Steuer-CAPM-Wert auf den Wert *vor*
  Körperschaftsteuer hoch (bündelt Gewerbesteuer + KSt 15 % + Soli 5,5 %).
* Innerhalb einer Periode sind **Strom- und Gas-Parameter identisch** — nur der
  Geltungszeitraum unterscheidet sich (Gas läuft dem Strom je ~1 Jahr voraus).

**Parameter & Ergebnis (im Modell hinterlegt):**

| | 3. Periode (S 2019–23 / G 2018–22) | 4. Periode (S 2024–28 / G 2023–27) |
|---|---|---|
| Basiszins r_f | 2,49 % | 0,74 % |
| MRP | 3,80 % | 3,70 % |
| Beta | 0,83 | 0,81 |
| Wagniszuschlag | 3,15 % (= 3,80 %·0,83) | 3,39 % (= 3,00 % + 0,395 pp) |
| Steuerfaktor | 1,225 | 1,225 |
| **EK I** (nom., vor KSt) | **6,91 %** | **5,07 %** (Modell: 5,06 %\*) |
| **EK II** (real, vor KSt) | **5,12 %** | **3,51 %** (Modell: 3,50 %\*) |
| Aktenzeichen | BK4-16-160 (S) / -161 (G) | BK4-21-0055 (S) / -0056 (G) |

\* Mit den dokumentierten, gerundeten Inputs ergibt sich EK I = 5,06 %; die
BNetzA weist 5,07 % aus (Rundung der Zwischenwerte). Abweichung ≤ 2 bp; die
Tests berücksichtigen diese Toleranz.

> Rechtlicher Hinweis: Die 4.-Perioden-Festlegung wurde vom OLG Düsseldorf am
> 30.08.2023 (u. a. 3 Kart 311/21, 689/21) aufgehoben; Folgeverfahren beim BGH.
> Die Werte oben sind die *ursprünglich festgelegten* — relevant für die
> Replikation der Gutachten-Methodik.

### Österreich — E-Control (klassisches WACC)

```
CoE = r_f + Beta·ERP + CRP                       (EK-Kosten, nominal, nach KöSt)
CoD = r_f + DP                                    (FK-Kosten, nominal, vor KöSt)
WACC_nom_vorSt  = E/V · CoE/(1−t) + D/V · CoD
WACC_real_vorSt = (1 + WACC_nom_vorSt)/(1 + i) − 1
```

* **Verifiziert:** Gearing 40 % EK / 60 % FK; MRP/ERP = 5,0 % (historisch, DMS);
  KöSt 24 % (2023) → 23 % (ab 2024); Tax-Wedge nur auf EK.
* **Zwei-WACC-System (5. RP):** ein für die Periode fixer **Bestands-WACC**
  (Verteilung 4,16 %) plus ein **jährlich** (Stichtag 31.08.) aktualisierter
  **Neuinvestitions-WACC** (2024: 6,33 %, 2025: 6,24 %, 2026: 5,70 %).
* **Peer Group** ("Core", börsennotierte Vergleichsnetzbetreiber). Für Gas-
  Fernleitung 2023 verifiziert: Snam, Enagás, Italgas, Fluxys Belgium,
  National Grid, REN.

**Detail-Inputs (r_f, Beta, Debt Premium, Inflation) lagen nur in den gesperrten
PDF-Tabellen vor.** Daher zwei nutzbare Wege im Modell:

1. **Template befüllen** — sobald die Werte aus dem Gutachten vorliegen:
   ```python
   from wacc.cases.at_econtrol import template_case
   from wacc.austria import wacc
   case = template_case("Strom", "Verteilung", "Bestand", 2024,
                         risk_free=..., debt_premium=..., inflation=...,
                         asset_beta=...)          # MRP/Gearing/KöSt vorbefüllt
   print(wacc(case).wacc_real_pretax)
   ```
2. **Beta rückrechnen** — aus einem veröffentlichten WACC:
   ```python
   from wacc.austria import implied_equity_beta
   beta = implied_equity_beta(target_wacc_real_pretax=0.0416, risk_free=...,
                              mrp=0.05, debt_premium=..., gearing=0.60,
                              tax_rate=0.23, inflation=...)
   ```

---

## Peer Group & Beta-Berechnung (`wacc/beta.py`)

Randl/Zechner leiten das Beta aus einer **Peer Group** börsennotierter Vergleichs-
netzbetreiber ab — exakt der Schritt, den du mit **Bloomberg-Rohdaten** selbst
nachbaust. Die fünfstufige Kette (`estimate_beta`):

```
1. Roh-Beta je Peer    OLS-Regression Aktienrendite ~ Marktindex (Bloomberg)
2. Adjustment          Vasicek (Bayes-Shrinkage z. Prior) | Blume (⅔β+⅓) | roh
3. Unlevering je Peer  Modigliani-Miller/Hamada: β_a = β_e/(1+(1−T)·D/E), Debt-β 0
4. Aggregation         arithm. Mittel | Median der Asset-Betas
5. Re-Levering         β_e* = β_a·(1+(1−T)·D/E_reg)   @ Gearing 40/60 (D/E=1,5)
```

**Recherchierte Methodik je Regime** (Quelle: Gutachten, s. [`SOURCES.md`](SOURCES.md);
firewall-bedingt aus Index-Snippets, vor Verwendung gegen PDF prüfen):

| Schritt | 🇩🇪 BNetzA (R/Z 4. P.) | 🇦🇹 E-Control (R/Z) |
|---|---|---|
| Frequenz/Fenster | wöchentlich, 2 & 3 J. | wöchentlich, 5/3/1 J. (Basis 5) |
| Referenzindex | lokaler Heimatmarkt-Index | MSCI World (USD) |
| Adjustment | Vasicek (3. P.: roh) | Vasicek |
| Unlevering | Modigliani-Miller, Debt-β 0 | Modigliani-Miller, Debt-β 0 |
| Aggregation | arithm. Mittel (11 Peers) | Mittel (Gutachten: „Mittel o. Median") |
| Re-Levering | 40/60, Steuer des Festlegungsjahres | 40/60, KöSt 25 %→23 % |

Diese Profile sind als `BNETZA_P3`, `BNETZA_P4`, `ECONTROL` (`wacc/beta.py`)
hinterlegt — `profil.estimate(peer_group, target_tax_rate)` setzt alle Schalter.

**Validierung gegen dokumentierte Anker-Betas** (Re-Levering, `pytest`-getestet):

| Regime | Asset-β (dok.) | → Equity-β (Modell) | veröffentlicht |
|---|---|---|---|
| E-Control (regulatorisch fix) | 0,325 | **0,700** | ~0,69–0,70 |
| BNetzA 3. Periode | 0,40 | **0,82** | 0,83 |
| BNetzA 4. Periode | 0,40 | **0,82** | 0,81 |

**Verwendung mit Bloomberg-Daten** (Vasicek braucht den Standardfehler je Beta):

```python
from wacc.cases.peer_groups import gas_fernleitung
from wacc.beta import ECONTROL

pg = gas_fernleitung({   # Roh-Beta, Std.-Fehler, Marktwert-Gearing aus Bloomberg
    "Snam":           {"raw_beta": 0.62, "beta_std_error": 0.07, "gearing": 0.58, "tax_rate": 0.24},
    "Enagás":         {"raw_beta": 0.70, "beta_std_error": 0.08, "gearing": 0.55, "tax_rate": 0.25},
    # ... Italgas, Fluxys Belgium, National Grid, REN, A2A
}, year=2023)
est = ECONTROL.estimate(pg, target_tax_rate=0.23)   # MM + Vasicek + Mittel, 40/60
print(est.summary())          # Zerlegung je Peer + Asset-Beta + Equity-Beta
# est.equity_beta -> template_case(..., equity_beta=est.equity_beta)
```

**Peer Groups** (Recherche, mit Konfidenz — in `wacc/cases/peer_groups.py`):

- **E-Control Gas-Fernleitung** (BIEGTRDT, *bestätigt*): Snam, Enagás, Italgas,
  Fluxys Belgium, National Grid, REN, A2A (erweitert: Ascopiave, Centrica).
- **E-Control Strom-Übertragung** (APG, *unsicher*): Terna, Red Eléctrica/Redeia,
  Elia, National Grid, REN, Snam.
- **BNetzA 3./4. Periode** (Kern *bestätigt*): Snam, Terna, Enagás, Red Eléctrica,
  National Grid, REN, Elia; 4. P. = arithm. Mittel von **11** Unternehmen
  (wahrsch. + Italgas, Fluxys). ⚠️ A2A/Ascopiave gehören zu E-Control, **nicht**
  zu BNetzA.

**Noch aus den PDFs zu verifizieren:** Vasicek-Prior-Gewichte, Net- vs. Gross-Debt,
exakte Alternativ-Indizes, Debt-Beta (0 vs. positiv), vollständige Peer-Tabellen
mit Per-Peer-Betas. Die Schalter sind als Parameter angelegt.

---

## Was noch fehlt (für die exakte AT-Replikation)

Aus den E-Control-PDFs zu entnehmen (siehe [`SOURCES.md`](SOURCES.md), Doc-Nrn.):
risikoloser Zins je Jahr, Roh-/Asset-/Equity-Beta + vollständige Peer-Liste,
Debt-Premium-Zerlegung, Inflationsannahme, Country Risk Premium. Trägt man diese
ein, reproduziert die Vorwärtsrechnung die veröffentlichten WACCs exakt.

Siehe [`SOURCES.md`](SOURCES.md) für alle Primärquellen-URLs und die jeweils
zu prüfende Tabelle.
