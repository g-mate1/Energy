"""Peer-Group-Beta-Schätzung (Randl/Zechner-Methodik) mit Bloomberg-Inputs.

Randl/Zechner leiten den Beta-Faktor nicht aus einem Einzelwert ab, sondern aus
einer **Peer Group** börsennotierter Vergleichsnetzbetreiber. Der Ablauf:

    1. Roh-Beta je Peer aus Bloomberg (Regression gegen einen Marktindex).
    2. Optional Adjustment (Bloomberg/Blume:  β_adj = 2/3·β_raw + 1/3).
    3. Unlevering je Peer auf das Asset-Beta beim individuellen Verschuldungsgrad
       (und ggf. lokalen Steuersatz).
    4. Aggregation der Asset-Betas über die Peers (i.d.R. Median).
    5. Re-Levering des aggregierten Asset-Betas auf den regulatorischen
       Verschuldungsgrad (E-Control: 40/60).

Dieses Modul implementiert genau diese Kette. Die Roh-Betas und Verschuldungs-
grade je Peer stammen aus Bloomberg und werden vom Nutzer eingetragen; das
Unlevering/Re-Levering nutzt ``wacc.capm``.

Hinweis zum Unlevering-Verfahren: regulatorisch wird häufig **Harris/Pringle**
(ohne Tax Shield, kontinuierliches Rebalancing) verwendet; ``UnleverMethod``
erlaubt den Wechsel zu Hamada (mit Tax Shield). Das im jeweiligen Gutachten
tatsächlich verwendete Verfahren ist zu prüfen (siehe SOURCES.md).
"""

from __future__ import annotations

import statistics
from dataclasses import dataclass, field

from .capm import (
    UnleverMethod,
    debt_to_equity_from_gearing,
    relever_beta,
    unlever_beta,
)


def bloomberg_adjust(raw_beta: float) -> float:
    """Bloomberg/Blume-Adjustment:  β_adj = 2/3·β_raw + 1/3·1."""
    return (2.0 / 3.0) * raw_beta + (1.0 / 3.0)


@dataclass(frozen=True)
class Peer:
    """Ein börsennotiertes Vergleichsunternehmen der Peer Group.

    Beta-Input: entweder ``raw_beta`` (Bloomberg-Rohbeta, ggf. mit Adjustment)
    ODER ``adjusted_beta`` (bereits adjustiert, hat Vorrang).
    Verschuldungsgrad: entweder ``debt_to_equity`` (D/E) ODER ``gearing`` (D/V).
    """

    name: str
    country: str = ""
    ticker: str = ""
    raw_beta: float | None = None
    adjusted_beta: float | None = None
    debt_to_equity: float | None = None
    gearing: float | None = None          # D/V
    tax_rate: float = 0.0                  # lokaler Steuersatz (nur Hamada)

    def equity_beta(self, *, adjust: bool) -> float:
        """Verschuldetes Beta des Peers (adjustiert je nach ``adjust``)."""
        if self.adjusted_beta is not None:
            return self.adjusted_beta
        if self.raw_beta is None:
            raise ValueError(f"{self.name}: weder raw_beta noch adjusted_beta gesetzt.")
        return bloomberg_adjust(self.raw_beta) if adjust else self.raw_beta

    def de(self) -> float:
        """Verschuldungsgrad D/E des Peers."""
        if self.debt_to_equity is not None:
            return self.debt_to_equity
        if self.gearing is not None:
            return debt_to_equity_from_gearing(self.gearing)
        raise ValueError(f"{self.name}: weder debt_to_equity noch gearing gesetzt.")


@dataclass(frozen=True)
class PeerGroup:
    name: str
    peers: tuple[Peer, ...]
    source: str = ""
    bloomberg_index: str = ""

    def names(self) -> list[str]:
        return [p.name for p in self.peers]


@dataclass(frozen=True)
class PeerBeta:
    peer: Peer
    equity_beta: float       # nach Adjustment-Wahl
    asset_beta: float        # unverschuldet


@dataclass(frozen=True)
class BetaEstimate:
    """Ergebnis der Peer-Group-Beta-Schätzung inkl. Zerlegung je Peer."""

    group_name: str
    method: UnleverMethod
    adjusted: bool
    aggregation: str
    per_peer: tuple[PeerBeta, ...]
    asset_beta: float        # aggregiert
    target_gearing: float
    target_tax_rate: float
    equity_beta: float       # re-leveraged auf regulatorisches Gearing
    extras: dict = field(default_factory=dict)

    def summary(self) -> str:
        lines = [
            f"Peer Group: {self.group_name}  "
            f"(Verfahren {self.method.value}, "
            f"{'adjustiert' if self.adjusted else 'roh'}, {self.aggregation})",
            f"{'Peer':<22}{'β_equity':>10}{'D/E':>8}{'β_asset':>10}",
        ]
        for pb in self.per_peer:
            lines.append(
                f"{pb.peer.name:<22}{pb.equity_beta:>10.3f}"
                f"{pb.peer.de():>8.2f}{pb.asset_beta:>10.3f}"
            )
        lines.append("-" * 50)
        lines.append(f"{'Asset-Beta (aggr.)':<22}{self.asset_beta:>10.3f}")
        lines.append(
            f"{'Equity-Beta @ ' + format(self.target_gearing, '.0%'):<22}"
            f"{self.equity_beta:>10.3f}"
        )
        return "\n".join(lines)


def _aggregate(values: list[float], how: str) -> float:
    if how == "median":
        return statistics.median(values)
    if how in ("mean", "average", "arithmetic"):
        return statistics.fmean(values)
    raise ValueError(f"Unbekannte Aggregation: {how!r} (median|mean)")


def estimate_beta(
    group: PeerGroup,
    target_gearing: float,
    target_tax_rate: float = 0.0,
    *,
    method: UnleverMethod = UnleverMethod.HARRIS_PRINGLE,
    adjusted: bool = False,
    aggregation: str = "median",
    debt_beta: float = 0.0,
) -> BetaEstimate:
    """Schätzt das verschuldete Beta für das regulatorische Gearing aus einer Peer Group.

    Args:
        group: Peer Group mit Roh-/Adjusted-Betas und Verschuldungsgraden.
        target_gearing: Regulatorisches D/V (z.B. 0.60 für E-Control).
        target_tax_rate: Steuersatz für das Re-Levering (nur Hamada relevant).
        method: Un-/Relevering-Verfahren (Harris/Pringle oder Hamada).
        adjusted: Bloomberg/Blume-Adjustment auf die Roh-Betas anwenden?
        aggregation: "median" (Standard) oder "mean".
        debt_beta: Beta des Fremdkapitals (i.d.R. 0).
    """
    per_peer: list[PeerBeta] = []
    for p in group.peers:
        beta_e = p.equity_beta(adjust=adjusted)
        beta_a = unlever_beta(beta_e, p.de(), p.tax_rate, debt_beta, method)
        per_peer.append(PeerBeta(peer=p, equity_beta=beta_e, asset_beta=beta_a))

    asset_beta = _aggregate([pb.asset_beta for pb in per_peer], aggregation)
    d_e = debt_to_equity_from_gearing(target_gearing)
    equity_beta = relever_beta(asset_beta, d_e, target_tax_rate, debt_beta, method)

    return BetaEstimate(
        group_name=group.name,
        method=method,
        adjusted=adjusted,
        aggregation=aggregation,
        per_peer=tuple(per_peer),
        asset_beta=asset_beta,
        target_gearing=target_gearing,
        target_tax_rate=target_tax_rate,
        equity_beta=equity_beta,
        extras={
            "asset_beta_mean": _aggregate([pb.asset_beta for pb in per_peer], "mean"),
            "asset_beta_median": _aggregate([pb.asset_beta for pb in per_peer], "median"),
        },
    )
