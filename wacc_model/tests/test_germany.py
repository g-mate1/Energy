"""Validierung: reproduziert das DE-Modell die veröffentlichten EK-Zinssätze?"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest  # noqa: E402

from wacc.cases import de_bnetza  # noqa: E402
from wacc.germany import ek_zinssatz  # noqa: E402

# Mit den dokumentierten, gerundeten Inputs reproduziert das Modell die
# veröffentlichten Werte auf <= 2 Basispunkte (Rundung der Zwischenwerte in
# der BNetzA-Festlegung, v.a. 4. Periode: 5,06 % gerechnet vs. 5,07 % publ.).
TOL = 0.0002


@pytest.mark.parametrize("case", de_bnetza.ALL_CASES, ids=lambda c: c.name)
def test_ek1_reproduces_published(case):
    result = ek_zinssatz(case)
    assert result.ek1_nominal_pretax == pytest.approx(case.published_ek1, abs=TOL)


@pytest.mark.parametrize("case", de_bnetza.ALL_CASES, ids=lambda c: c.name)
def test_ek2_reproduces_published(case):
    result = ek_zinssatz(case)
    assert result.ek2_real_pretax == pytest.approx(case.published_ek2, abs=TOL)


def test_strom_and_gas_parameters_identical_per_period():
    # Innerhalb einer Periode sind Strom- und Gas-Parameter identisch.
    s3, g3 = ek_zinssatz(de_bnetza.DE_P3_STROM), ek_zinssatz(de_bnetza.DE_P3_GAS)
    assert s3.ek1_nominal_pretax == g3.ek1_nominal_pretax
    s4, g4 = ek_zinssatz(de_bnetza.DE_P4_STROM), ek_zinssatz(de_bnetza.DE_P4_GAS)
    assert s4.ek1_nominal_pretax == g4.ek1_nominal_pretax


def test_ek2_is_ek1_minus_inflation():
    for case in de_bnetza.ALL_CASES:
        r = ek_zinssatz(case)
        assert r.ek2_real_pretax == pytest.approx(
            r.ek1_nominal_pretax - case.inflation, abs=1e-12
        )


def test_third_period_surcharge_is_beta_times_mrp():
    # 3. Periode: kein Aufschlag -> Wagniszuschlag = Beta * MRP = 3,15 %.
    r = ek_zinssatz(de_bnetza.DE_P3_STROM)
    assert r.risk_surcharge == pytest.approx(0.83 * 0.0380, abs=1e-12)
    assert r.risk_surcharge == pytest.approx(0.0315, abs=5e-5)
