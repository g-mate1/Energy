"""Tests der CAPM-/Beta-Kernmathematik und Umrechnungen."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest  # noqa: E402

from wacc import capm, conversions  # noqa: E402


def test_cost_of_equity():
    # 0,0074 + 0,81 · 0,0370 = 0,03737
    assert capm.cost_of_equity(0.0074, 0.81, 0.0370) == pytest.approx(0.03737, abs=1e-9)


def test_unlever_relever_roundtrip_harris_pringle():
    beta_e = 1.0
    d_e = 1.5  # 40/60
    asset = capm.unlever_beta(beta_e, d_e, method=capm.UnleverMethod.HARRIS_PRINGLE)
    back = capm.relever_beta(asset, d_e, method=capm.UnleverMethod.HARRIS_PRINGLE)
    assert back == pytest.approx(beta_e, abs=1e-12)
    assert asset == pytest.approx(1.0 / 2.5, abs=1e-12)


def test_unlever_relever_roundtrip_hamada():
    beta_e, d_e, tax = 1.1, 1.5, 0.23
    asset = capm.unlever_beta(beta_e, d_e, tax, method=capm.UnleverMethod.HAMADA)
    back = capm.relever_beta(asset, d_e, tax, method=capm.UnleverMethod.HAMADA)
    assert back == pytest.approx(beta_e, abs=1e-12)


def test_gearing_helpers():
    assert capm.debt_to_equity_from_gearing(0.60) == pytest.approx(1.5)
    assert capm.equity_share_from_gearing(0.60) == pytest.approx(0.40)


def test_fisher_roundtrip():
    nominal, infl = 0.0666, 0.02
    real = conversions.fisher_real(nominal, infl)
    assert conversions.fisher_nominal(real, infl) == pytest.approx(nominal, abs=1e-12)


def test_tax_gross_up_roundtrip():
    pre = conversions.pre_tax(0.04, 0.23)
    assert conversions.post_tax(pre, 0.23) == pytest.approx(0.04, abs=1e-12)


def test_corporate_tax_with_soli():
    # 15 % KSt + 5,5 % Soli = 15,825 %
    assert conversions.corporate_tax_with_soli(0.15, 0.055) == pytest.approx(0.15825)
