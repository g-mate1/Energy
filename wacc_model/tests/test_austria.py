"""Tests des E-Control-WACC-Moduls und der Beta-Kalibrierung.

Da die exakten E-Control-Inputs (Beta, r_f, Debt Premium, Inflation) hier nicht
verifizierbar waren, prüfen diese Tests die **Konsistenz der Formel** (Vorwärts-
rechnung vs. Inversion) sowie die verifizierten Strukturkonstanten — nicht die
Reproduktion der veröffentlichten Punktwerte aus erfundenen Komponenten.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest  # noqa: E402

from wacc.austria import implied_equity_beta, wacc  # noqa: E402
from wacc.cases import at_econtrol  # noqa: E402


def test_calibration_roundtrip():
    """implied_equity_beta invertiert die WACC-Formel exakt."""
    case = at_econtrol.template_case(
        sector="Strom", network_level="Verteilung", asset_type="Neuinvestition",
        year=2024, risk_free=0.0308, debt_premium=0.0104, inflation=0.02,
        equity_beta=1.05,
    )
    r = wacc(case)
    beta_back = implied_equity_beta(
        target_wacc_real_pretax=r.wacc_real_pretax, risk_free=case.risk_free,
        mrp=case.mrp, debt_premium=case.debt_premium, gearing=case.gearing,
        tax_rate=case.tax_rate, inflation=case.inflation,
    )
    assert beta_back == pytest.approx(1.05, abs=1e-9)


def test_template_uses_verified_constants():
    case = at_econtrol.template_case(
        sector="Gas", network_level="Verteilung", asset_type="Bestand",
        year=2024, risk_free=0.03, debt_premium=0.01, inflation=0.02, equity_beta=1.0,
    )
    assert case.mrp == at_econtrol.MRP_DMS == 0.05
    assert case.gearing == at_econtrol.GEARING == 0.60
    assert case.tax_rate == 0.23  # KöSt ab 2024


def test_wacc_pretax_above_posttax():
    case = at_econtrol.template_case(
        sector="Strom", network_level="Übertragung", asset_type="Neuinvestition",
        year=2025, risk_free=0.025, debt_premium=0.012, inflation=0.018, equity_beta=1.0,
    )
    r = wacc(case)
    assert r.wacc_nominal_pretax > r.wacc_nominal_posttax
    assert r.wacc_nominal_pretax > r.wacc_real_pretax  # Inflation > 0


def test_asset_beta_relevering():
    """Asset-Beta wird auf Gearing 40/60 (D/E=1,5) re-leveraged."""
    case = at_econtrol.template_case(
        sector="Strom", network_level="Verteilung", asset_type="Bestand",
        year=2024, risk_free=0.03, debt_premium=0.01, inflation=0.02, asset_beta=0.40,
    )
    r = wacc(case)
    # Harris/Pringle: beta_e = 0.40 * (1 + 1.5) = 1.00
    assert r.equity_beta == pytest.approx(1.00, abs=1e-12)


def test_published_reference_data_present():
    # Verifizierte Kopfzahlen vorhanden (Stichproben).
    labels = {p.label(): p for p in at_econtrol.PUBLISHED}
    assert any("Strom Verteilung Bestand 2024" in k for k in labels)
    bestand = next(p for p in at_econtrol.PUBLISHED
                   if p.sector == "Strom" and p.asset_type == "Bestand")
    assert bestand.wacc_real_pretax == pytest.approx(0.0416)
