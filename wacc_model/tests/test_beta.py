"""Tests der Peer-Group-Beta-Schätzung."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest  # noqa: E402

from wacc.beta import (  # noqa: E402
    Peer,
    PeerGroup,
    UnleverMethod,
    bloomberg_adjust,
    estimate_beta,
)
from wacc.cases import peer_groups  # noqa: E402


def test_bloomberg_adjust():
    assert bloomberg_adjust(1.0) == pytest.approx(1.0)         # 2/3 + 1/3
    assert bloomberg_adjust(0.7) == pytest.approx(0.8)         # 2/3·0,7 + 1/3
    assert bloomberg_adjust(0.4) == pytest.approx(0.6)


def test_single_peer_unlever_relever_harris_pringle():
    # raw_beta 1,0 bei D/E=1,0 -> Asset 0,5; relever auf D/E=1,5 -> 1,25
    pg = PeerGroup("t", (Peer("X", raw_beta=1.0, debt_to_equity=1.0),))
    est = estimate_beta(pg, target_gearing=0.6, method=UnleverMethod.HARRIS_PRINGLE)
    assert est.asset_beta == pytest.approx(0.5)
    assert est.equity_beta == pytest.approx(1.25)   # 0,5·(1+1,5)


def test_median_aggregation():
    pg = PeerGroup("t", (
        Peer("A", raw_beta=0.9, gearing=0.5),   # asset 0,45
        Peer("B", raw_beta=1.0, gearing=0.5),   # asset 0,50
        Peer("C", raw_beta=1.1, gearing=0.5),   # asset 0,55
    ))
    est = estimate_beta(pg, target_gearing=0.5, aggregation="median")
    assert est.asset_beta == pytest.approx(0.50)
    assert est.extras["asset_beta_mean"] == pytest.approx(0.50)


def test_adjusted_changes_result():
    pg = PeerGroup("t", (Peer("X", raw_beta=0.7, debt_to_equity=1.0),))
    raw = estimate_beta(pg, 0.6, adjusted=False)
    adj = estimate_beta(pg, 0.6, adjusted=True)
    assert raw.per_peer[0].equity_beta == pytest.approx(0.7)
    assert adj.per_peer[0].equity_beta == pytest.approx(0.8)
    assert adj.asset_beta > raw.asset_beta


def test_gas_fernleitung_2023_members():
    pg = peer_groups.illustrative_gas_fernleitung_2023()
    assert pg.bloomberg_index == "BIEGTRDT"
    assert len(pg.peers) == 6
    assert "Snam" in pg.names() and "National Grid" in pg.names()
    est = estimate_beta(pg, target_gearing=0.60, adjusted=True)
    # Plausibilität: Asset-Beta regulierter Netze grob 0,3–0,7.
    assert 0.2 < est.asset_beta < 0.8
    assert est.equity_beta > est.asset_beta   # re-leveraged hoch


def test_hamada_uses_tax_shield():
    pg = PeerGroup("t", (Peer("X", raw_beta=1.0, debt_to_equity=1.0, tax_rate=0.25),))
    hp = estimate_beta(pg, 0.6, method=UnleverMethod.HARRIS_PRINGLE)
    ham = estimate_beta(pg, 0.6, target_tax_rate=0.25, method=UnleverMethod.HAMADA)
    # Hamada-Asset-Beta liegt höher (Tax Shield reduziert das Entschulden).
    assert ham.asset_beta > hp.asset_beta
