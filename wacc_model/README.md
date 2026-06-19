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

Randl/Zechner leiten das Beta nicht als Einzelwert ab, sondern aus einer **Peer
Group** börsennotierter Vergleichsnetzbetreiber — exakt der Schritt, den du mit
**Bloomberg-Rohdaten** selbst nachbauen kannst. Die Kette:

```
1. Roh-Beta je Peer        (Bloomberg-Regression gegen Marktindex)
2. Adjustment (optional)   β_adj = 2/3·β_raw + 1/3        (Bloomberg/Blume)
3. Unlevering je Peer       β_asset = β_equity / (1 + D/E)   (Harris/Pringle)
                            β_asset = β_equity / (1 + (1−T)·D/E)  (Hamada)
4. Aggregation              Median (Standard) oder Mittelwert der Asset-Betas
5. Re-Levering              β_equity* = β_asset · (1 + D/E_reg)   @ Gearing 40/60
```

**Verwendung mit Bloomberg-Daten:**

```python
from wacc.cases.peer_groups import gas_fernleitung_2023
from wacc.beta import estimate_beta, UnleverMethod

# Roh-Betas (z.B. BETA_RAW_OVERRIDABLE) + Gearing (Net Debt / Equity) aus Bloomberg:
pg = gas_fernleitung_2023({
    "Snam":           {"raw_beta": 0.62, "gearing": 0.58, "tax_rate": 0.24},
    "Enagás":         {"raw_beta": 0.70, "gearing": 0.55, "tax_rate": 0.25},
    "Italgas":        {"raw_beta": 0.66, "gearing": 0.60, "tax_rate": 0.24},
    "Fluxys Belgium": {"raw_beta": 0.55, "gearing": 0.50, "tax_rate": 0.25},
    "National Grid":  {"raw_beta": 0.64, "gearing": 0.52, "tax_rate": 0.19},
    "REN":            {"raw_beta": 0.60, "gearing": 0.62, "tax_rate": 0.21},
})
est = estimate_beta(pg, target_gearing=0.60, adjusted=True,
                    method=UnleverMethod.HARRIS_PRINGLE, aggregation="median")
print(est.summary())          # Zerlegung je Peer + Asset-Beta + Equity-Beta
# est.asset_beta -> in template_case(..., asset_beta=est.asset_beta) einsetzen
```

**Verifizierte Peer Group — E-Control Gas-Fernleitung 2023** (Bloomberg-Index
`BIEGTRDT`): Snam (IT), Enagás (ES), Italgas (IT), Fluxys Belgium (BE), National
Grid (GB), REN (PT). Weitere Gruppen (Strom-Übertragung/-Verteilung, BNetzA)
werden ergänzt, sobald die Namen aus den Gutachten bestätigt sind.

**Noch zu bestätigen (aus den Gutachten, siehe [`SOURCES.md`](SOURCES.md)):**
Schätzfenster (z.B. 5 J. monatlich vs. 2 J. wöchentlich), Referenzindex,
Roh- vs. adjustiertes Beta, Unlevering-Verfahren (Harris/Pringle vs. Hamada) und
das Debt-Beta. Diese Schalter sind im Modul als Parameter angelegt — du stellst
sie auf die im Gutachten dokumentierte Wahl.

---

## Was noch fehlt (für die exakte AT-Replikation)

Aus den E-Control-PDFs zu entnehmen (siehe [`SOURCES.md`](SOURCES.md), Doc-Nrn.):
risikoloser Zins je Jahr, Roh-/Asset-/Equity-Beta + vollständige Peer-Liste,
Debt-Premium-Zerlegung, Inflationsannahme, Country Risk Premium. Trägt man diese
ein, reproduziert die Vorwärtsrechnung die veröffentlichten WACCs exakt.

Siehe [`SOURCES.md`](SOURCES.md) für alle Primärquellen-URLs und die jeweils
zu prüfende Tabelle.
