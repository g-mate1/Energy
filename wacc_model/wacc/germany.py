"""Deutschland — BNetzA kalkulatorischer Eigenkapitalzinssatz (§7 StromNEV/GasNEV).

Die Bundesnetzagentur bestimmt **kein klassisches WACC**, sondern einen
regulierten Eigenkapitalzinssatz nach einem (gekappten) CAPM:

    EK I (Neuanlagen, nominal, vor KSt) = (r_f + Wagniszuschlag) * Steuerfaktor
    EK II (Altanlagen, real, vor KSt)   = EK I − Ø-Inflation (10-J.-VPI)

Dabei ist
    Wagniszuschlag = Beta * Marktrisikoprämie  (3. Periode)
                   = Beta * MRP + Aufschlag     (4. Periode: +0,395 pp)

Der **Steuerfaktor** (≈ 1,225) rechnet den Nach-Steuer-CAPM-Wert auf den Wert
*vor* Körperschaftsteuer hoch (er bündelt Gewerbesteuer + KSt 15 % + Soli 5,5 %).
r_f und die Inflationsrate sind jeweils 10-Jahres-Durchschnitte (Bundesbank-
Umlaufrenditen bzw. Verbraucherpreisindex).

Innerhalb einer Regulierungsperiode sind die Parameter für Strom und Gas
**identisch**; es unterscheidet sich nur der Geltungszeitraum.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GermanCase:
    """Parametersatz einer BNetzA-Festlegung (eine Periode, eine Sparte)."""

    name: str
    period: int           # Regulierungsperiode (3 oder 4)
    sector: str           # "Strom" oder "Gas"
    valid_from: int
    valid_to: int

    # --- CAPM-Inputs ---
    risk_free: float                    # r_f, 10-J.-Ø Umlaufrenditen
    mrp: float                          # Marktrisikoprämie
    beta: float                         # verschuldetes Beta (Peer Group)
    tax_factor: float                   # Steuerfaktor (Hochrechnung vor KSt)
    inflation: float                    # 10-J.-Ø VPI (für EK II / real)

    # Optionaler expliziter Wagniszuschlag (4. Periode: 3,39 % statt β·MRP).
    # Wenn None -> Wagniszuschlag = beta * mrp.
    risk_surcharge_override: float | None = None

    # Aktenzeichen + veröffentlichte Referenzwerte (zur Validierung).
    aktenzeichen: str = ""
    published_ek1: float | None = None  # EK I (Neuanlagen, nominal, vor KSt)
    published_ek2: float | None = None  # EK II (Altanlagen, real, vor KSt)

    @property
    def risk_surcharge(self) -> float:
        """Wagniszuschlag = β·MRP, sofern kein expliziter Wert hinterlegt ist."""
        if self.risk_surcharge_override is not None:
            return self.risk_surcharge_override
        return self.beta * self.mrp


@dataclass(frozen=True)
class GermanResult:
    """Ergebnis einer EK-Zinssatz-Berechnung."""

    case: GermanCase
    risk_surcharge: float       # Wagniszuschlag
    coe_after_tax: float        # r_f + Wagniszuschlag (nach KSt, nominal)
    ek1_nominal_pretax: float   # EK I (Neuanlagen)
    ek2_real_pretax: float      # EK II (Altanlagen)

    def as_dict(self) -> dict[str, float | str]:
        return {
            "Fall": self.case.name,
            "Sparte": self.case.sector,
            "Periode": self.case.period,
            "Geltung": f"{self.case.valid_from}–{self.case.valid_to}",
            "r_f": self.case.risk_free,
            "MRP": self.case.mrp,
            "Beta": self.case.beta,
            "Wagniszuschlag": self.risk_surcharge,
            "EK n. St.": self.coe_after_tax,
            "Steuerfaktor": self.case.tax_factor,
            "EK I (nom., vor St.)": self.ek1_nominal_pretax,
            "EK II (real, vor St.)": self.ek2_real_pretax,
        }


def ek_zinssatz(case: GermanCase) -> GermanResult:
    """Berechnet EK I (Neuanlagen) und EK II (Altanlagen) nach BNetzA-Methodik."""
    surcharge = case.risk_surcharge
    coe_after_tax = case.risk_free + surcharge
    ek1 = coe_after_tax * case.tax_factor          # nominal, vor KSt
    ek2 = ek1 - case.inflation                     # real, vor KSt
    return GermanResult(
        case=case,
        risk_surcharge=surcharge,
        coe_after_tax=coe_after_tax,
        ek1_nominal_pretax=ek1,
        ek2_real_pretax=ek2,
    )
