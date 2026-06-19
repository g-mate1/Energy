"""WACC-Replikationsmodell — Randl/Zechner-Gutachten (DE BNetzA & AT E-Control).

Reproduziert die regulatorisch festgelegten Kapitalkosten für Strom- und
Gasnetze:

* ``wacc.germany``   — BNetzA kalkulatorischer Eigenkapitalzinssatz (EK I/EK II),
                       3. & 4. Regulierungsperiode.
* ``wacc.austria``   — E-Control klassischer WACC (real, vor Steuern),
                       Strom & Gas, Bestand & Neuinvestition.
* ``wacc.capm``      — gemeinsame CAPM-/Beta-Mathematik.
* ``wacc.conversions`` — real/nominal- und Steuer-Umrechnungen.
"""

from . import austria, capm, conversions, germany

__all__ = ["austria", "capm", "conversions", "germany"]
