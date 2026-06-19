"""Peer Groups der Randl/Zechner-Gutachten + Bloomberg-Befüll-Builder.

Die Mitglieder (Firmennamen) sind recherchiert und mit Konfidenz markiert; die
Roh-Betas, Standardfehler (für Vasicek) und Verschuldungsgrade je Peer trägst du
aus **Bloomberg** ein. ``estimate_beta`` (in ``wacc.beta``) macht daraus das
Asset-Beta und das auf das regulatorische Gearing re-leveragte Equity-Beta.

KONFIDENZ der Peer-Listen (Recherche, Firewall-bedingt aus Index-Snippets):
  * BESTÄTIGT: E-Control Gas-Fernleitung (BIEGTRDT) — 7 Kern-Peers.
  * BESTÄTIGT (Kern): BNetzA 3./4. Periode — 7 europäische Kern-Peers.
  * UNSICHER: E-Control Strom-Übertragung "Core"; BNetzA-Randpeers (Italgas,
    Fluxys, Duet Group).

DOKUMENTIERTE ANKER-BETAS (zur Validierung der Re-Levering-Kette):
  * E-Control: regulatorisch fixiertes **unverschuldetes Beta = 0,325**
    (illustratives Asset-Beta im Gutachten 0,41) → Equity-Beta ≈ 0,69–0,70.
  * BNetzA: Asset-Beta **0,40** → Equity-Beta 0,83 (3. P.) / 0,81 (4. P.).
"""

from __future__ import annotations

from ..beta import Peer, PeerGroup

# --- Dokumentierte regulatorische Anker-Betas (Quelle: Gutachten, s. SOURCES.md) ---
ECONTROL_REG_ASSET_BETA = 0.325       # E-Control: fixiertes unverschuldetes Beta
ECONTROL_ILLUSTRATIVE_ASSET_BETA = 0.41  # illustratives Beispiel im 02_3-Gutachten
BNETZA_ASSET_BETA = 0.40              # BNetzA Asset-Beta (beide Perioden)
BNETZA_EQUITY_BETA_P3 = 0.83
BNETZA_EQUITY_BETA_P4 = 0.81

# ---------------------------------------------------------------------------
# Peer-Group-Mitglieder (Name, Land, Bloomberg-Ticker [zu prüfen], Konfidenz)
# ---------------------------------------------------------------------------
# E-Control Gas-Fernleitung 2019 & 2023 (Bloomberg-Vergleichsgruppe BIEGTRDT).
ECONTROL_GAS_FERNLEITUNG: list[tuple[str, str, str]] = [
    ("Snam", "IT", "SRG IM"),
    ("Enagás", "ES", "ENG SM"),
    ("Italgas", "IT", "IG IM"),
    ("Fluxys Belgium", "BE", "FLUX BB"),
    ("National Grid", "GB", "NG/ LN"),
    ("REN", "PT", "RENE PL"),
    ("A2A", "IT", "A2A IM"),
]
# Erweiterte Gruppe (im 2023-Gutachten genannt, Zuordnung UNSICHER):
ECONTROL_GAS_FERNLEITUNG_EXTENDED = ECONTROL_GAS_FERNLEITUNG + [
    ("Ascopiave", "IT", "ASC IM"),
    ("Centrica", "GB", "CNA LN"),
]

# E-Control Strom-Übertragung (APG-Gutachten 2022) — "Core" (UNSICHER).
ECONTROL_STROM_UEBERTRAGUNG: list[tuple[str, str, str]] = [
    ("Terna", "IT", "TRN IM"),
    ("Red Eléctrica (Redeia)", "ES", "RED SM"),
    ("Elia", "BE", "ELI BB"),
    ("National Grid", "GB", "NG/ LN"),
    ("REN", "PT", "RENE PL"),
    ("Snam", "IT", "SRG IM"),
]

# BNetzA 3. & 4. Regulierungsperiode — 7 europäische Kern-Peers (BESTÄTIGT).
BNETZA_CORE: list[tuple[str, str, str]] = [
    ("Snam", "IT", "SRG IM"),
    ("Terna", "IT", "TRN IM"),
    ("Enagás", "ES", "ENG SM"),
    ("Red Eléctrica (Redeia)", "ES", "RED SM"),
    ("National Grid", "GB", "NG/ LN"),
    ("REN", "PT", "RENE PL"),
    ("Elia", "BE", "ELI BB"),
]
# 4. Periode: Beta = arithm. Mittel von 11 Vergleichsunternehmen. Wahrscheinliche
# Ergänzungen (UNSICHER): Italgas, Fluxys Belgium. 3. Periode zusätzlich Duet
# Group (AU). Achtung: A2A/Ascopiave gehören zu E-Control (AT), NICHT zu BNetzA.
BNETZA_P4_LIKELY = BNETZA_CORE + [
    ("Italgas", "IT", "IG IM"),
    ("Fluxys Belgium", "BE", "FLUX BB"),
]


def build_peer_group(
    name: str,
    members: list[tuple[str, str, str]],
    bloomberg: dict[str, dict],
    source: str = "",
    bloomberg_index: str = "",
) -> PeerGroup:
    """Baut eine ``PeerGroup`` aus Mitgliederliste + Bloomberg-Werten.

    ``bloomberg`` ist ein Mapping ``{Peer-Name: {...}}`` mit je optional
    ``raw_beta``/``adjusted_beta``, ``beta_std_error`` (für Vasicek) und
    ``gearing`` (D/V) bzw. ``debt_to_equity`` sowie optional ``tax_rate``.
    Fehlt ein Peer im Mapping, wird er mit leeren Feldern angelegt (zu ergänzen).
    """
    peers = []
    for nm, country, ticker in members:
        d = bloomberg.get(nm, {})
        peers.append(
            Peer(
                name=nm,
                country=country,
                ticker=ticker,
                raw_beta=d.get("raw_beta"),
                adjusted_beta=d.get("adjusted_beta"),
                beta_std_error=d.get("beta_std_error"),
                gearing=d.get("gearing"),
                debt_to_equity=d.get("debt_to_equity"),
                tax_rate=d.get("tax_rate", 0.0),
            )
        )
    return PeerGroup(name=name, peers=tuple(peers), source=source,
                     bloomberg_index=bloomberg_index)


def gas_fernleitung(bloomberg: dict[str, dict], year: int = 2023) -> PeerGroup:
    """E-Control Gas-Fernleitungs-Peer-Group (BIEGTRDT) aus Bloomberg-Werten."""
    return build_peer_group(
        name=f"AT Gas-Fernleitung {year}",
        members=ECONTROL_GAS_FERNLEITUNG,
        bloomberg=bloomberg,
        source=f"Gutachten WACC Gas-Fernleitungsnetzbetreiber, Randl/Zechner {year}",
        bloomberg_index="BIEGTRDT",
    )


# ---------------------------------------------------------------------------
# ILLUSTRATIVES Beispiel — PLATZHALTER (NICHT aus dem Gutachten!).
# Nur zur Demonstration der Kette. raw_beta/beta_std_error/gearing durch echte
# Bloomberg-Werte ersetzen. Std.-Fehler werden für das Vasicek-Adjustment genutzt.
# ---------------------------------------------------------------------------
ILLUSTRATIVE_BLOOMBERG: dict[str, dict] = {
    "Snam":           {"raw_beta": 0.62, "beta_std_error": 0.07, "gearing": 0.58, "tax_rate": 0.24},
    "Enagás":         {"raw_beta": 0.70, "beta_std_error": 0.08, "gearing": 0.55, "tax_rate": 0.25},
    "Italgas":        {"raw_beta": 0.66, "beta_std_error": 0.07, "gearing": 0.60, "tax_rate": 0.24},
    "Fluxys Belgium": {"raw_beta": 0.55, "beta_std_error": 0.10, "gearing": 0.50, "tax_rate": 0.25},
    "National Grid":  {"raw_beta": 0.64, "beta_std_error": 0.06, "gearing": 0.52, "tax_rate": 0.19},
    "REN":            {"raw_beta": 0.60, "beta_std_error": 0.09, "gearing": 0.62, "tax_rate": 0.21},
    "A2A":            {"raw_beta": 0.72, "beta_std_error": 0.08, "gearing": 0.56, "tax_rate": 0.24},
}


def illustrative_gas_fernleitung() -> PeerGroup:
    """Gas-Fernleitungs-Peer-Group mit ILLUSTRATIVEN Platzhalter-Betas."""
    return gas_fernleitung(ILLUSTRATIVE_BLOOMBERG, year=2023)
