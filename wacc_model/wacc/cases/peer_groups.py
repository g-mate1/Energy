"""Peer Groups der Randl/Zechner-Gutachten + Bloomberg-Befüll-Builder.

Die Mitglieder (Firmennamen) sind dokumentiert; die Roh-Betas und Verschuldungs-
grade je Peer trägst du aus **Bloomberg** ein (genau so, wie die Gutachten sie
ableiten). ``estimate_beta`` (in ``wacc.beta``) macht daraus Asset-Beta und das
auf das regulatorische Gearing re-leveragte Equity-Beta.

Status der Peer-Listen:
  * VERIFIZIERT: E-Control Gas-Fernleitung 2023 (Bloomberg-Index BIEGTRDT).
  * weitere Gruppen (Strom-Übertragung/-Verteilung, BNetzA) werden ergänzt,
    sobald die Namen aus den Gutachten bestätigt sind (siehe SOURCES.md).
"""

from __future__ import annotations

from ..beta import Peer, PeerGroup

# ---------------------------------------------------------------------------
# E-Control Gas-Fernleitung 2023 — Peer Group (Bloomberg-Index BIEGTRDT)
# Quelle: Gutachten WACC Gas-Fernleitungsnetzbetreiber, Randl/Zechner 2023.
# (Name, Land, Bloomberg-Ticker [zu prüfen])
# ---------------------------------------------------------------------------
GAS_FERNLEITUNG_2023_MEMBERS: list[tuple[str, str, str]] = [
    ("Snam", "IT", "SRG IM"),
    ("Enagás", "ES", "ENG SM"),
    ("Italgas", "IT", "IG IM"),
    ("Fluxys Belgium", "BE", "FLUX BB"),
    ("National Grid", "GB", "NG/ LN"),
    ("REN", "PT", "RENE PL"),
]


def gas_fernleitung_2023(bloomberg: dict[str, dict]) -> PeerGroup:
    """Baut die Gas-Fernleitungs-Peer-Group 2023 aus Bloomberg-Werten.

    Args:
        bloomberg: Mapping ``{Peer-Name: {...}}`` mit je optional
            ``raw_beta``/``adjusted_beta`` und ``gearing`` (D/V) bzw.
            ``debt_to_equity`` sowie optional ``tax_rate``.

    Beispiel::

        pg = gas_fernleitung_2023({
            "Snam":            {"raw_beta": 0.62, "gearing": 0.58, "tax_rate": 0.24},
            "Enagás":          {"raw_beta": 0.70, "gearing": 0.55, "tax_rate": 0.25},
            ...
        })
    """
    peers = []
    for name, country, ticker in GAS_FERNLEITUNG_2023_MEMBERS:
        d = bloomberg.get(name, {})
        peers.append(
            Peer(
                name=name,
                country=country,
                ticker=ticker,
                raw_beta=d.get("raw_beta"),
                adjusted_beta=d.get("adjusted_beta"),
                gearing=d.get("gearing"),
                debt_to_equity=d.get("debt_to_equity"),
                tax_rate=d.get("tax_rate", 0.0),
            )
        )
    return PeerGroup(
        name="AT Gas-Fernleitung 2023",
        peers=tuple(peers),
        source="Gutachten WACC Gas-Fernleitungsnetzbetreiber, Randl/Zechner 2023",
        bloomberg_index="BIEGTRDT",
    )


# ---------------------------------------------------------------------------
# ILLUSTRATIVES Beispiel — PLATZHALTER-Betas (NICHT aus dem Gutachten!).
# Nur zur Demonstration der Berechnungskette. Durch echte Bloomberg-Werte
# ersetzen. Werte grob an europäischen regulierten Netzbetreibern orientiert.
# ---------------------------------------------------------------------------
ILLUSTRATIVE_BLOOMBERG: dict[str, dict] = {
    "Snam":            {"raw_beta": 0.62, "gearing": 0.58, "tax_rate": 0.24},
    "Enagás":          {"raw_beta": 0.70, "gearing": 0.55, "tax_rate": 0.25},
    "Italgas":         {"raw_beta": 0.66, "gearing": 0.60, "tax_rate": 0.24},
    "Fluxys Belgium":  {"raw_beta": 0.55, "gearing": 0.50, "tax_rate": 0.25},
    "National Grid":   {"raw_beta": 0.64, "gearing": 0.52, "tax_rate": 0.19},
    "REN":             {"raw_beta": 0.60, "gearing": 0.62, "tax_rate": 0.21},
}


def illustrative_gas_fernleitung_2023() -> PeerGroup:
    """Gas-Fernleitungs-Peer-Group mit ILLUSTRATIVEN Platzhalter-Betas."""
    return gas_fernleitung_2023(ILLUSTRATIVE_BLOOMBERG)
