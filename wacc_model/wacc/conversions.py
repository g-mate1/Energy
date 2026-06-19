"""Umrechnungen zwischen real/nominal und vor/nach Steuern.

Regulatorische WACC-Festlegungen werden je nach Behörde in unterschiedlichen
"Geschmacksrichtungen" ausgewiesen:

* **Deutschland (BNetzA):** *nominaler* Eigenkapitalzinssatz *vor*
  Körperschaftsteuer (EK I für Neuanlagen, EK II für Altanlagen).
* **Österreich (E-Control):** klassischer *realer* WACC *vor* Steuern.

Dieses Modul stellt die nötigen exakten (Fisher-)Umrechnungen bereit.
"""

from __future__ import annotations


def fisher_real(nominal: float, inflation: float) -> float:
    """Nominal -> real nach Fisher: (1+n)/(1+i) - 1."""
    return (1.0 + nominal) / (1.0 + inflation) - 1.0


def fisher_nominal(real: float, inflation: float) -> float:
    """Real -> nominal nach Fisher: (1+r)*(1+i) - 1."""
    return (1.0 + real) * (1.0 + inflation) - 1.0


def pre_tax(post_tax: float, tax_rate: float) -> float:
    """Nach-Steuer-Größe auf Vor-Steuer hochrechnen: r / (1 - T)."""
    if tax_rate >= 1.0:
        raise ValueError("Steuersatz muss < 1 sein.")
    return post_tax / (1.0 - tax_rate)


def post_tax(pre_tax_value: float, tax_rate: float) -> float:
    """Vor-Steuer-Größe auf Nach-Steuer reduzieren: r * (1 - T)."""
    return pre_tax_value * (1.0 - tax_rate)


def corporate_tax_with_soli(corporate_rate: float, solidarity_surcharge: float) -> float:
    """Deutscher Körperschaftsteuersatz inkl. Solidaritätszuschlag.

    s = corporate_rate * (1 + solidarity_surcharge)
    z.B. 0.15 * (1 + 0.055) = 0.158250  (15,825 %)
    """
    return corporate_rate * (1.0 + solidarity_surcharge)
