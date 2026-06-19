"""Tests der Peer-Group-Beta-Schätzung."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest  # noqa: E402

from wacc.beta import (  # noqa: E402
    BNETZA_P4,
    ECONTROL,
    Adjustment,
    Peer,
    PeerGroup,
    UnleverMethod,
    blume_adjust,
    estimate_beta,
    vasicek_adjust,
)
from wacc.capm import relever_beta  # noqa: E402
from wacc.cases import peer_groups  # noqa: E402


def test_blume_adjust():
    assert blume_adjust(1.0) == pytest.approx(1.0)         # 2/3 + 1/3
    assert blume_adjust(0.7) == pytest.approx(0.8)
    assert blume_adjust(0.4) == pytest.approx(0.6)


def test_vasicek_shrinks_toward_prior():
    # Hoher Standardfehler -> stärkere Schrumpfung Richtung Prior.
    adj = vasicek_adjust([0.5, 1.5], [0.3, 0.3], prior=1.0)
    assert adj[0] > 0.5 and adj[1] < 1.5         # beide Richtung 1,0 gezogen
    # Symmetrisch um den Prior bei gleichem SE.
    assert (adj[0] + adj[1]) / 2 == pytest.approx(1.0, abs=1e-9)


def test_vasicek_requires_std_error():
    pg = PeerGroup("t", (Peer("X", raw_beta=0.8),))
    with pytest.raises(ValueError):
        estimate_beta(pg, 0.6, adjustment=Adjustment.VASICEK)


def test_single_peer_unlever_relever_harris_pringle():
    # raw_beta 1,0 bei D/E=1,0 -> Asset 0,5; relever auf D/E=1,5 -> 1,25
    pg = PeerGroup("t", (Peer("X", raw_beta=1.0, debt_to_equity=1.0),))
    est = estimate_beta(pg, target_gearing=0.6, method=UnleverMethod.HARRIS_PRINGLE)
    assert est.asset_beta == pytest.approx(0.5)
    assert est.equity_beta == pytest.approx(1.25)   # 0,5·(1+1,5)


def test_mean_vs_median_aggregation():
    pg = PeerGroup("t", (
        Peer("A", raw_beta=0.9, gearing=0.5),   # asset 0,45
        Peer("B", raw_beta=1.0, gearing=0.5),   # asset 0,50
        Peer("C", raw_beta=1.6, gearing=0.5),   # asset 0,80
    ))
    med = estimate_beta(pg, 0.5, aggregation="median")
    mean = estimate_beta(pg, 0.5, aggregation="mean")
    assert med.asset_beta == pytest.approx(0.50)
    assert mean.asset_beta == pytest.approx((0.45 + 0.50 + 0.80) / 3)


def test_blume_changes_result():
    pg = PeerGroup("t", (Peer("X", raw_beta=0.7, debt_to_equity=1.0),))
    raw = estimate_beta(pg, 0.6, adjustment=Adjustment.NONE)
    adj = estimate_beta(pg, 0.6, adjustment=Adjustment.BLUME)
    assert raw.per_peer[0].equity_beta == pytest.approx(0.7)
    assert adj.per_peer[0].equity_beta == pytest.approx(0.8)


# --- Validierung gegen dokumentierte regulatorische Anker-Betas ---
def test_econtrol_anchor_asset_to_equity_beta():
    # Asset-Beta 0,325 -> Equity-Beta @ 40/60, KöSt 23 %, Modigliani-Miller.
    beta_e = relever_beta(peer_groups.ECONTROL_REG_ASSET_BETA, debt_to_equity=1.5,
                          tax_rate=0.23, method=UnleverMethod.HAMADA)
    assert beta_e == pytest.approx(0.70, abs=0.02)   # dokumentiert ~0,69–0,70


def test_bnetza_anchor_asset_to_equity_beta():
    # Asset-Beta 0,40 -> Equity-Beta @ 40/60, dt. Ertragsteuer ~30 %.
    beta_e = relever_beta(peer_groups.BNETZA_ASSET_BETA, debt_to_equity=1.5,
                          tax_rate=0.30, method=UnleverMethod.HAMADA)
    # Reproduziert die veröffentlichten 0,81 (4. P.) / 0,83 (3. P.) im Rahmen.
    assert beta_e == pytest.approx(0.82, abs=0.02)
    assert peer_groups.BNETZA_EQUITY_BETA_P4 == 0.81
    assert peer_groups.BNETZA_EQUITY_BETA_P3 == 0.83


def test_peer_group_rosters():
    # E-Control Gas-Fernleitung: 7 Kern-Peers inkl. A2A; BIEGTRDT.
    pg = peer_groups.illustrative_gas_fernleitung()
    assert pg.bloomberg_index == "BIEGTRDT"
    assert len(pg.peers) == 7
    assert {"Snam", "Enagás", "A2A"} <= set(pg.names())
    # BNetzA-Kern: 7 europäische Netzbetreiber, A2A NICHT enthalten.
    de_names = {m[0] for m in peer_groups.BNETZA_CORE}
    assert {"Terna", "Elia", "Red Eléctrica (Redeia)"} <= de_names
    assert "A2A" not in de_names


def test_regime_profiles_distinct():
    # DE: Mittelwert; AT: ebenfalls Mittelwert (operativ), beide Hamada+Vasicek.
    assert BNETZA_P4.method is UnleverMethod.HAMADA
    assert BNETZA_P4.adjustment is Adjustment.VASICEK
    assert BNETZA_P4.aggregation == "mean"
    assert ECONTROL.method is UnleverMethod.HAMADA
    assert ECONTROL.target_gearing == 0.60


def test_regime_profile_estimate_runs():
    pg = peer_groups.illustrative_gas_fernleitung()
    est = ECONTROL.estimate(pg, target_tax_rate=0.23)
    assert 0.2 < est.asset_beta < 0.8
    assert est.equity_beta > est.asset_beta
