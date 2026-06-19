"""Österreich — E-Control klassischer WACC (Randl/Zechner-Gutachten).

E-Control weist einen **klassischen WACC, real, vor Steuern** aus, getrennt für
**Bestandsanlagen** und **Neuinvestitionen**. Methodik (Randl/Zechner):

    CoE = r_f + Beta * ERP + CRP        (Eigenkapitalkosten, nominal, nach KöSt)
    CoD = r_f + DP                       (Fremdkapitalkosten, nominal, vor KöSt)

    WACC_nominal_vor_St = E/V * CoE/(1−t) + D/V * CoD
    WACC_real_vor_St    = (1 + WACC_nominal_vor_St)/(1 + Inflation) − 1
    WACC_nominal_nach_St = E/V * CoE + D/V * CoD*(1−t)

mit
    ERP = Marktrisikoprämie (Randl/Zechner: historisch nach DMS, ~5,0 %)
    CRP = Country Risk Premium (Länderrisikozuschlag, häufig 0)
    DP  = Debt Premium / Kreditaufschlag (Bloomberg EUR Europe Utilities)
    t   = österr. Körperschaftsteuer (KöSt) — wirkt nur auf die EK-Kosten
    Gearing: typ. EK 40 % / FK 60 %  →  E/V = 0,4, D/V = 0,6, D/E = 1,5

Das Equity-Beta wird aus den Asset-Betas der Peer Group beim regulatorischen
Verschuldungsgrad re-leveraged (siehe ``wacc.capm``); alternativ kann ein bereits
verschuldetes Beta direkt übergeben werden.
"""

from __future__ import annotations

from dataclasses import dataclass

from .capm import (
    UnleverMethod,
    cost_of_debt,
    cost_of_equity,
    debt_to_equity_from_gearing,
    relever_beta,
)
from .conversions import fisher_real


@dataclass(frozen=True)
class AustrianCase:
    """Parametersatz einer E-Control-WACC-Bestimmung (ein Jahr, eine Sparte, ein Anlagentyp)."""

    name: str
    sector: str            # "Strom" oder "Gas"
    asset_type: str        # "Bestand" oder "Neuinvestition"
    network_level: str     # z.B. "Fernleitung", "Verteilung", "Übertragung"
    year: int

    # --- CAPM / WACC-Inputs ---
    risk_free: float           # r_f
    mrp: float                 # ERP / Marktrisikoprämie
    country_risk_premium: float  # CRP
    debt_premium: float        # DP / Kreditaufschlag
    gearing: float             # D/V (Fremdkapitalquote), z.B. 0.60
    tax_rate: float            # KöSt
    inflation: float           # für real/nominal

    # Beta: entweder verschuldetes Equity-Beta direkt ...
    equity_beta: float | None = None
    # ... oder Asset-Beta (wird auf das regulatorische Gearing re-leveraged).
    asset_beta: float | None = None
    # Randl/Zechner nutzen Modigliani-Miller (Hamada) zum Re-Levering -> Default.
    unlever_method: UnleverMethod = UnleverMethod.HAMADA

    # Referenz / Validierung.
    source: str = ""
    published_wacc_real_pretax: float | None = None
    # Manche Gutachten weisen eine Bandbreite aus (geom.–arithm. Mittelung):
    published_wacc_real_pretax_low: float | None = None
    published_wacc_real_pretax_high: float | None = None

    def levered_beta(self) -> float:
        """Liefert das verschuldete Beta (direkt oder re-leveraged aus Asset-Beta)."""
        if self.equity_beta is not None:
            return self.equity_beta
        if self.asset_beta is not None:
            d_e = debt_to_equity_from_gearing(self.gearing)
            return relever_beta(
                self.asset_beta, d_e, self.tax_rate, method=self.unlever_method
            )
        raise ValueError(f"{self.name}: weder equity_beta noch asset_beta gesetzt.")


@dataclass(frozen=True)
class AustrianResult:
    case: AustrianCase
    equity_beta: float
    coe_after_tax: float           # nominal, nach KöSt
    cod_pretax: float              # nominal, vor KöSt
    wacc_nominal_pretax: float
    wacc_real_pretax: float
    wacc_nominal_posttax: float

    def as_dict(self) -> dict[str, float | str]:
        return {
            "Fall": self.case.name,
            "Sparte": self.case.sector,
            "Anlagentyp": self.case.asset_type,
            "Jahr": self.case.year,
            "r_f": self.case.risk_free,
            "ERP": self.case.mrp,
            "Beta (lev.)": self.equity_beta,
            "CoE (n. St.)": self.coe_after_tax,
            "CoD (v. St.)": self.cod_pretax,
            "Gearing D/V": self.case.gearing,
            "WACC nom. v. St.": self.wacc_nominal_pretax,
            "WACC real v. St.": self.wacc_real_pretax,
            "WACC nom. n. St.": self.wacc_nominal_posttax,
        }


def wacc(case: AustrianCase) -> AustrianResult:
    """Berechnet den E-Control-WACC (real/nominal, vor/nach Steuern)."""
    beta = case.levered_beta()
    coe = cost_of_equity(case.risk_free, beta, case.mrp) + case.country_risk_premium
    cod = cost_of_debt(case.risk_free, case.debt_premium)

    equity_share = 1.0 - case.gearing
    # Pre-Tax: Tax Wedge nur auf Eigenkapital (FK-Zinsen steuerlich abzugsfähig).
    wacc_nom_pre = equity_share * coe / (1.0 - case.tax_rate) + case.gearing * cod
    wacc_real_pre = fisher_real(wacc_nom_pre, case.inflation)
    wacc_nom_post = equity_share * coe + case.gearing * cod * (1.0 - case.tax_rate)

    return AustrianResult(
        case=case,
        equity_beta=beta,
        coe_after_tax=coe,
        cod_pretax=cod,
        wacc_nominal_pretax=wacc_nom_pre,
        wacc_real_pretax=wacc_real_pre,
        wacc_nominal_posttax=wacc_nom_post,
    )


def implied_equity_beta(
    target_wacc_real_pretax: float,
    risk_free: float,
    mrp: float,
    debt_premium: float,
    gearing: float,
    tax_rate: float,
    inflation: float,
    country_risk_premium: float = 0.0,
) -> float:
    """Rückrechnung des verschuldeten Betas aus einem veröffentlichten WACC.

    Da E-Control die Detail-Parameter teils nur in (hier nicht zugänglichen)
    PDF-Tabellen ausweist, erlaubt diese Funktion, das implizite Equity-Beta zu
    bestimmen, das einen bekannten **realen Vor-Steuer-WACC** reproduziert —
    sobald r_f, Debt Premium, Gearing, KöSt und Inflation vorliegen.

    Invertiert:
        WACC_nom_pre = (1+WACC_real)*(1+i) − 1
        E/V * CoE/(1−t) = WACC_nom_pre − D/V * CoD
        CoE = (...)*(1−t)/(E/V) ;  beta = (CoE − CRP − r_f)/MRP
    """
    equity_share = 1.0 - gearing
    cod = risk_free + debt_premium
    wacc_nom_pre = (1.0 + target_wacc_real_pretax) * (1.0 + inflation) - 1.0
    coe = (wacc_nom_pre - gearing * cod) * (1.0 - tax_rate) / equity_share
    return (coe - country_risk_premium - risk_free) / mrp
