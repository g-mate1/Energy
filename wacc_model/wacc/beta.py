"""Peer-Group-Beta-Schätzung (Randl/Zechner-Methodik) mit Bloomberg-Inputs.

Randl/Zechner leiten den Beta-Faktor aus einer **Peer Group** börsennotierter
Vergleichsnetzbetreiber ab. Der Ablauf:

    1. Roh-Beta je Peer aus Bloomberg (Regression gegen einen Marktindex).
    2. Adjustment (optional): Blume/Bloomberg (2/3·β+1/3) ODER Vasicek (Bayes-
       Shrinkage, gewichtet mit dem Standardfehler je Peer).
    3. Unlevering je Peer auf das Asset-Beta beim individuellen (Markt-)D/E.
    4. Aggregation über die Peers: Median ODER arithmetisches Mittel.
    5. Re-Levering des aggregierten Asset-Betas auf das regulatorische Gearing.

WICHTIG — die beiden Regime unterscheiden sich (siehe ``regime_profiles``):

    * **BNetzA (DE):** wöchentliche Renditen (2 & 3 J.), lokaler Heimatmarkt-
      Index, **Vasicek**-Adjustment (4. Periode; 3. Periode roh), Unlevering
      nach **Modigliani-Miller mit Steuer (Hamada)** mit Debt-Beta 0,
      **arithmetisches Mittel** über die Peers, Re-Levering auf 40/60 mit dem
      Steuersatz des Festlegungsjahres. Asset-Beta ≈ 0,40 → Equity-Beta ≈ 0,81–0,83.
    * **E-Control (AT):** tägliche Renditen (5/3/1 J.), **Median** über die
      Peers, Praktikermethode (Harris/Pringle), Re-Levering auf 40/60.

Die Roh-Betas, Standardfehler und Verschuldungsgrade je Peer stammen aus
Bloomberg und werden vom Nutzer eingetragen.
"""

from __future__ import annotations

import statistics
from dataclasses import dataclass, field
from enum import Enum

from .capm import (
    UnleverMethod,
    debt_to_equity_from_gearing,
    relever_beta,
    unlever_beta,
)


class Adjustment(str, Enum):
    """Verfahren zur Beta-Adjustierung der Roh-Betas."""

    NONE = "none"        # Roh-Betas (OLS) unverändert
    BLUME = "blume"      # Blume/Bloomberg:  β_adj = 2/3·β_raw + 1/3
    VASICEK = "vasicek"  # Vasicek-Bayes-Shrinkage (braucht Standardfehler)


def blume_adjust(raw_beta: float) -> float:
    """Blume/Bloomberg-Adjustment:  β_adj = 2/3·β_raw + 1/3·1."""
    return (2.0 / 3.0) * raw_beta + (1.0 / 3.0)


def vasicek_adjust(
    raw_betas: list[float],
    std_errors: list[float | None],
    prior: float | None = None,
) -> list[float]:
    """Vasicek (1973): Bayes-Shrinkage Richtung Querschnitts-Prior.

        β_adj_i = w_i·β_raw_i + (1−w_i)·β̄
        w_i     = σ²_quer / (σ²_quer + se_i²)

    σ²_quer = Querschnittsvarianz der Roh-Betas, se_i = Standardfehler des
    Beta-Schätzers je Peer (aus Bloomberg), β̄ = Prior (Default:
    Querschnittsmittel der Roh-Betas).
    """
    if prior is None:
        prior = statistics.fmean(raw_betas)
    cross_var = statistics.pvariance(raw_betas)
    out: list[float] = []
    for b, se in zip(raw_betas, std_errors):
        if se is None:
            raise ValueError(
                "Vasicek-Adjustment benötigt einen Standardfehler (beta_std_error) "
                "je Peer."
            )
        w = cross_var / (cross_var + se * se)
        out.append(w * b + (1.0 - w) * prior)
    return out


@dataclass(frozen=True)
class Peer:
    """Ein börsennotiertes Vergleichsunternehmen der Peer Group.

    Beta-Input: ``raw_beta`` (Bloomberg-Rohbeta; nötig für Blume/Vasicek) und/oder
    ``adjusted_beta`` (direkt vorgegeben, überschreibt das Adjustment).
    ``beta_std_error`` wird für Vasicek benötigt.
    Verschuldungsgrad: ``debt_to_equity`` (D/E) ODER ``gearing`` (D/V).
    """

    name: str
    country: str = ""
    ticker: str = ""
    raw_beta: float | None = None
    adjusted_beta: float | None = None
    beta_std_error: float | None = None
    debt_to_equity: float | None = None
    gearing: float | None = None          # D/V
    tax_rate: float = 0.0                  # lokaler Steuersatz (nur Hamada)

    def de(self) -> float:
        """Verschuldungsgrad D/E des Peers (Marktwerte)."""
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
    equity_beta: float       # nach Adjustment-Wahl (Input ins Unlevering)
    asset_beta: float        # unverschuldet


@dataclass(frozen=True)
class BetaEstimate:
    """Ergebnis der Peer-Group-Beta-Schätzung inkl. Zerlegung je Peer."""

    group_name: str
    method: UnleverMethod
    adjustment: Adjustment
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
            f"(Unlevering {self.method.value}, Adjustment {self.adjustment.value}, "
            f"Aggregation {self.aggregation})",
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


def _input_equity_betas(group: PeerGroup, adjustment: Adjustment,
                        vasicek_prior: float | None) -> list[float]:
    """Liefert je Peer das (ggf. adjustierte) verschuldete Beta als Unlevering-Input."""
    if adjustment is Adjustment.NONE:
        betas = []
        for p in group.peers:
            if p.adjusted_beta is not None:
                betas.append(p.adjusted_beta)
            elif p.raw_beta is not None:
                betas.append(p.raw_beta)
            else:
                raise ValueError(f"{p.name}: weder raw_beta noch adjusted_beta gesetzt.")
        return betas

    raws = []
    for p in group.peers:
        if p.raw_beta is None:
            raise ValueError(f"{p.name}: raw_beta für {adjustment.value}-Adjustment nötig.")
        raws.append(p.raw_beta)

    if adjustment is Adjustment.BLUME:
        return [blume_adjust(b) for b in raws]
    # VASICEK
    return vasicek_adjust(raws, [p.beta_std_error for p in group.peers], vasicek_prior)


def estimate_beta(
    group: PeerGroup,
    target_gearing: float,
    target_tax_rate: float = 0.0,
    *,
    method: UnleverMethod = UnleverMethod.HARRIS_PRINGLE,
    adjustment: Adjustment = Adjustment.NONE,
    aggregation: str = "median",
    debt_beta: float = 0.0,
    vasicek_prior: float | None = None,
) -> BetaEstimate:
    """Schätzt das verschuldete Beta für das regulatorische Gearing aus einer Peer Group.

    Args:
        group: Peer Group mit Roh-Betas, Standardfehlern und Verschuldungsgraden.
        target_gearing: Regulatorisches D/V (z.B. 0.60).
        target_tax_rate: Steuersatz für das Re-Levering (nur Hamada relevant).
        method: Un-/Relevering-Verfahren (Harris/Pringle [AT] oder Hamada [DE]).
        adjustment: Roh / Blume / Vasicek.
        aggregation: "median" (AT) oder "mean" (DE).
        debt_beta: Beta des Fremdkapitals (i.d.R. 0).
        vasicek_prior: Prior-Beta für Vasicek (Default: Querschnittsmittel).
    """
    input_betas = _input_equity_betas(group, adjustment, vasicek_prior)

    per_peer: list[PeerBeta] = []
    for p, beta_e in zip(group.peers, input_betas):
        beta_a = unlever_beta(beta_e, p.de(), p.tax_rate, debt_beta, method)
        per_peer.append(PeerBeta(peer=p, equity_beta=beta_e, asset_beta=beta_a))

    asset_beta = _aggregate([pb.asset_beta for pb in per_peer], aggregation)
    d_e = debt_to_equity_from_gearing(target_gearing)
    equity_beta = relever_beta(asset_beta, d_e, target_tax_rate, debt_beta, method)

    return BetaEstimate(
        group_name=group.name,
        method=method,
        adjustment=adjustment,
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


# ---------------------------------------------------------------------------
# Dokumentierte Methodik-Profile je Regime (als Default-Schalter für estimate_beta).
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class RegimeProfile:
    """Dokumentierte Beta-Methodik eines Regimes (Quelle: Gutachten, s. SOURCES.md)."""

    name: str
    method: UnleverMethod
    adjustment: Adjustment
    aggregation: str
    target_gearing: float
    estimation: str          # Frequenz/Fenster (informativ)
    reference_index: str     # Marktportfolio (informativ)
    debt_beta: float = 0.0

    def estimate(self, group: PeerGroup, target_tax_rate: float = 0.0,
                 vasicek_prior: float | None = None) -> BetaEstimate:
        return estimate_beta(
            group, self.target_gearing, target_tax_rate,
            method=self.method, adjustment=self.adjustment,
            aggregation=self.aggregation, debt_beta=self.debt_beta,
            vasicek_prior=vasicek_prior,
        )


# BNetzA 4. Regulierungsperiode (Randl/Zechner 2021).
BNETZA_P4 = RegimeProfile(
    name="BNetzA 4. Periode (Randl/Zechner)",
    method=UnleverMethod.HAMADA,          # Modigliani-Miller mit Steuer, Debt-Beta 0
    adjustment=Adjustment.VASICEK,
    aggregation="mean",                    # ungewichtetes arithm. Mittel (11 Peers)
    target_gearing=0.60,                   # 40 % EK / 60 % FK
    estimation="wöchentliche Renditen, 2- & 3-Jahres-Fenster",
    reference_index="lokaler Heimatmarkt-Index je Peer (konsistent zur MRP)",
)

# BNetzA 3. Regulierungsperiode (Frontier 2016).
BNETZA_P3 = RegimeProfile(
    name="BNetzA 3. Periode (Frontier)",
    method=UnleverMethod.HAMADA,
    adjustment=Adjustment.NONE,            # rohe OLS-Betas
    aggregation="mean",
    target_gearing=0.60,
    estimation="1-, 3- & 5-Jahres-Fenster",
    reference_index="lokaler Index (Sektor-Cross-Check: DJ EuroStoxx Utilities, CDAX Utilities)",
)

# E-Control (Randl/Zechner, ab 2019).
# Hinweis: Quellenlage deutet auf Modigliani-Miller (Hamada) + Vasicek + Median.
# Eine ältere E-Control/Frontier-Generation nutzte die Praktikermethode
# (Harris/Pringle, tägliche Daten, Mittelwert) — bei Bedarf method/adjustment/
# aggregation entsprechend umstellen (siehe SOURCES.md).
# Gutachten nennt "Mittelwert oder Median"; operativ Mittelwert (mit dem
# Broad-Sample-Mittel als Vasicek-Prior). Für Median: aggregation="median".
ECONTROL = RegimeProfile(
    name="E-Control (Randl/Zechner)",
    method=UnleverMethod.HAMADA,           # Modigliani-Miller mit Steuer, Debt-Beta 0
    adjustment=Adjustment.VASICEK,
    aggregation="mean",
    target_gearing=0.60,
    estimation="wöchentliche Renditen, 5-/3-/1-Jahres-Fenster (Basis 5 J.)",
    reference_index="MSCI World (USD); Varianten MSCI ACWI / MSCI World EUR",
)
