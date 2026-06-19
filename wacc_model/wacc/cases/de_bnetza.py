"""BNetzA-Fälle: kalkulatorischer Eigenkapitalzinssatz, 3. & 4. Regulierungsperiode.

Parameter Strom = Gas innerhalb einer Periode (nur Geltungszeitraum unterscheidet
sich). Werte quer-verifiziert über BGH-Pressemitteilung (3. Periode), OLG
Düsseldorf 3 Kart 311/21 & 689/21 (4. Periode) und das Randl/Zechner/Frontier-
Gutachten (Juli 2021).

Zahlen sind als Dezimal geführt (0.0249 = 2,49 %). Steuerfaktor 1,225 bündelt
Gewerbesteuer + KSt 15 % + Soli 5,5 % (Hochrechnung Nach-Steuer → vor KSt).

ROUNDING-HINWEIS (4. Periode): Mit den dokumentierten Inputs ergibt sich EK I =
(0,74 % + 3,39 %)·1,225 = 5,06 %; die BNetzA weist 5,07 % aus (Rundung der
Zwischenwerte). Die Validierungstests erlauben daher 3 Basispunkte Toleranz.
"""

from __future__ import annotations

from ..germany import GermanCase

TAX_FACTOR = 1.225  # Steuerfaktor (Gewerbesteuer + KSt + Soli), beide Perioden

# ---------------------------------------------------------------------------
# 3. Regulierungsperiode — Festlegung 05.10.2016
#   EK I = (2,49 % + 3,80 %·0,83)·1,225 = 6,91 %  ;  EK II = EK I − 1,79 % = 5,12 %
# ---------------------------------------------------------------------------
DE_P3_STROM = GermanCase(
    name="DE BNetzA P3 Strom",
    period=3,
    sector="Strom",
    valid_from=2019,
    valid_to=2023,
    risk_free=0.0249,
    mrp=0.0380,
    beta=0.83,
    tax_factor=TAX_FACTOR,
    inflation=0.0179,           # 10-J.-Ø VPI (= EK I − EK II)
    aktenzeichen="BK4-16-160",
    published_ek1=0.0691,
    published_ek2=0.0512,
)

DE_P3_GAS = GermanCase(
    name="DE BNetzA P3 Gas",
    period=3,
    sector="Gas",
    valid_from=2018,
    valid_to=2022,
    risk_free=0.0249,
    mrp=0.0380,
    beta=0.83,
    tax_factor=TAX_FACTOR,
    inflation=0.0179,
    aktenzeichen="BK4-16-161",
    published_ek1=0.0691,
    published_ek2=0.0512,
)

# ---------------------------------------------------------------------------
# 4. Regulierungsperiode — Festlegung 12.10.2021
#   Wagniszuschlag 3,39 % = Beta 0,81 · MRP 3,70 % (=3,00 %) + 0,395 pp Aufschlag
#   EK I = (0,74 % + 3,39 %)·1,225 = 5,07 %  ;  EK II = EK I − 1,56 % = 3,51 %
# ---------------------------------------------------------------------------
DE_P4_STROM = GermanCase(
    name="DE BNetzA P4 Strom",
    period=4,
    sector="Strom",
    valid_from=2024,
    valid_to=2028,
    risk_free=0.0074,
    mrp=0.0370,
    beta=0.81,
    risk_surcharge_override=0.0339,   # inkl. +0,395 pp Aufschlag über β·MRP
    tax_factor=TAX_FACTOR,
    inflation=0.0156,
    aktenzeichen="BK4-21-0055",
    published_ek1=0.0507,
    published_ek2=0.0351,
)

DE_P4_GAS = GermanCase(
    name="DE BNetzA P4 Gas",
    period=4,
    sector="Gas",
    valid_from=2023,
    valid_to=2027,
    risk_free=0.0074,
    mrp=0.0370,
    beta=0.81,
    risk_surcharge_override=0.0339,
    tax_factor=TAX_FACTOR,
    inflation=0.0156,
    aktenzeichen="BK4-21-0056",
    published_ek1=0.0507,
    published_ek2=0.0351,
)

ALL_CASES = [DE_P3_STROM, DE_P3_GAS, DE_P4_STROM, DE_P4_GAS]
