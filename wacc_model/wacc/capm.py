"""CAPM-Kernfunktionen (regulierungsunabhängig).

Dieses Modul enthält die reine Finanzmathematik des Capital Asset Pricing Model
(CAPM) und der Beta-Umrechnung. Die Funktionen sind bewusst frei von
regulatorischen Annahmen — die jeweilige Behörden-Methodik (BNetzA, E-Control)
wird in ``wacc.germany`` bzw. ``wacc.austria`` zusammengesetzt.

Alle Zinssätze/Renditen werden als Dezimalzahlen geführt (z.B. 0.0691 = 6,91 %).
"""

from __future__ import annotations

from enum import Enum


class UnleverMethod(str, Enum):
    """Verfahren zur Umrechnung verschuldetes <-> unverschuldetes Beta."""

    #: Hamada (1972): berücksichtigt den steuerlichen Tax Shield des Fremdkapitals.
    #:   beta_a = beta_e / (1 + (1 - T) * D/E)         (Debt-Beta = 0)
    HAMADA = "hamada"

    #: Harris/Pringle (1985): kein Tax Shield im Beta (kontinuierliches
    #: Rebalancing, typisch für regulierte Netze):
    #:   beta_a = beta_e / (1 + D/E)
    HARRIS_PRINGLE = "harris_pringle"


def cost_of_equity(risk_free: float, equity_beta: float, market_risk_premium: float) -> float:
    """Eigenkapitalkosten nach CAPM (nominal, nach Unternehmenssteuer).

    r_E = r_f + beta_e * MRP

    Args:
        risk_free: Risikoloser Zins r_f.
        equity_beta: Verschuldetes (Equity-)Beta.
        market_risk_premium: Marktrisikoprämie MRP = E[r_m] - r_f.
    """
    return risk_free + equity_beta * market_risk_premium


def cost_of_debt(risk_free: float, debt_premium: float) -> float:
    """Fremdkapitalkosten als risikoloser Zins zzgl. Kreditaufschlag.

    r_D = r_f + debt_premium
    """
    return risk_free + debt_premium


def unlever_beta(
    equity_beta: float,
    debt_to_equity: float,
    tax_rate: float = 0.0,
    debt_beta: float = 0.0,
    method: UnleverMethod = UnleverMethod.HARRIS_PRINGLE,
) -> float:
    """Verschuldetes Beta -> unverschuldetes (Asset-)Beta.

    Args:
        equity_beta: Beobachtetes verschuldetes Beta (Equity Beta).
        debt_to_equity: Verschuldungsgrad D/E zum beobachteten Beta.
        tax_rate: Unternehmenssteuersatz (nur für Hamada relevant).
        debt_beta: Beta des Fremdkapitals (i.d.R. 0).
        method: Umrechnungsverfahren (Hamada oder Harris/Pringle).

    Returns:
        Asset-Beta (unverschuldet).
    """
    if method is UnleverMethod.HAMADA:
        factor = 1.0 + (1.0 - tax_rate) * debt_to_equity
        return (equity_beta + debt_beta * (1.0 - tax_rate) * debt_to_equity) / factor
    # Harris/Pringle: ohne Tax Shield
    factor = 1.0 + debt_to_equity
    return (equity_beta + debt_beta * debt_to_equity) / factor


def relever_beta(
    asset_beta: float,
    debt_to_equity: float,
    tax_rate: float = 0.0,
    debt_beta: float = 0.0,
    method: UnleverMethod = UnleverMethod.HARRIS_PRINGLE,
) -> float:
    """Unverschuldetes (Asset-)Beta -> verschuldetes Beta beim Ziel-Gearing.

    Args:
        asset_beta: Unverschuldetes Beta.
        debt_to_equity: Ziel-Verschuldungsgrad D/E (regulatorisch).
        tax_rate: Unternehmenssteuersatz (nur für Hamada relevant).
        debt_beta: Beta des Fremdkapitals (i.d.R. 0).
        method: Umrechnungsverfahren (Hamada oder Harris/Pringle).

    Returns:
        Equity-Beta beim Ziel-Verschuldungsgrad.
    """
    if method is UnleverMethod.HAMADA:
        return asset_beta + (asset_beta - debt_beta) * (1.0 - tax_rate) * debt_to_equity
    # Harris/Pringle
    return asset_beta + (asset_beta - debt_beta) * debt_to_equity


def debt_to_equity_from_gearing(gearing: float) -> float:
    """D/E aus Gearing D/V berechnen.

    Args:
        gearing: Fremdkapitalquote D/V (z.B. 0.6 für 60 % FK / 40 % EK).
    """
    if not 0.0 <= gearing < 1.0:
        raise ValueError(f"Gearing D/V muss in [0, 1) liegen, war {gearing!r}")
    return gearing / (1.0 - gearing)


def equity_share_from_gearing(gearing: float) -> float:
    """Eigenkapitalquote E/V = 1 - D/V."""
    return 1.0 - gearing
