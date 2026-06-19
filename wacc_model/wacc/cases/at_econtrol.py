"""E-Control-Fälle (Österreich): WACC Strom & Gas (Randl/Zechner-Gutachten).

WICHTIG — DATENLAGE:
In der Bau-Umgebung waren die E-Control-PDFs durch eine Egress-Firewall
gesperrt; die granularen CAPM-Inputs (exaktes Beta, risikoloser Zins, Debt
Premium, Inflationsannahme) liegen NUR in PDF-Tabellen vor und konnten nicht
zellgenau verifiziert werden. Daher gilt:

  * VERIFIZIERT (mehrfach quer-bestätigt): WACC-Formel/-Struktur, Gearing
    40 % EK / 60 % FK, MRP 5,0 % (DMS/historisch), KöSt 24 % (2023) → 23 %
    (ab 2024), die veröffentlichten WACC-Ergebnisse (real, vor Steuern).
  * ZU VERIFIZIEREN (aus den PDFs): risikoloser Zins, Beta, Debt Premium,
    Inflation, CRP.

Statt erfundener Beta-/Zinswerte stellt dieses Modul bereit:
  1. die verifizierten Strukturkonstanten,
  2. die veröffentlichten WACC-Ergebnisse als Referenz (``PUBLISHED``),
  3. einen ``template_case(...)``-Builder, der einen ``AustrianCase`` mit den
     verifizierten Konstanten vorbefüllt — du ergänzt nur r_f, Beta, Debt
     Premium, Inflation aus dem Gutachten,
  4. die Kalibrierung ``implied_equity_beta`` (in ``wacc.austria``), die aus
     einem veröffentlichten WACC das implizite Beta rückrechnet.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..austria import AustrianCase

# --- VERIFIZIERTE Strukturkonstanten (E-Control / Randl-Zechner) ---
MRP_DMS = 0.05            # Marktrisikoprämie (historisch, DMS) — verifiziert
GEARING = 0.60           # Fremdkapitalquote D/V — verifiziert (40/60)
EQUITY_SHARE = 0.40      # Eigenkapitalquote E/V — verifiziert
KOEST = {                # Körperschaftsteuersatz nach Jahr — verifiziert
    2019: 0.25, 2020: 0.25, 2021: 0.25, 2022: 0.25, 2023: 0.24,
    2024: 0.23, 2025: 0.23, 2026: 0.23,
}

# --- PARTIELL bekannte Komponenten (Sekundärquelle, ZU VERIFIZIEREN) ---
# 2024er Aktualisierungsrunde (Stichtag 31.08.): risikoloser EK-Zins ~3,08 %
# (Schnitt AT/NL/FI, 15-j. Laufzeit); Fremdkapitalkosten ~3,99–4,24 %
# (Bloomberg EUR Europe Utilities).
RF_EK_2024_APPROX = 0.0308          # UNSICHER
COD_2024_APPROX_RANGE = (0.0399, 0.0424)  # UNSICHER


@dataclass(frozen=True)
class PublishedWacc:
    """Veröffentlichtes WACC-Ergebnis (real, vor Steuern) als Referenz/Zielwert."""

    sector: str            # "Strom" / "Gas"
    network_level: str     # "Verteilung" / "Übertragung" / "Fernleitung"
    asset_type: str        # "Bestand" / "Neuinvestition"
    year: int              # Bezugsjahr (bei Neuinvest = Stichtagsjahr)
    wacc_real_pretax: float | None       # Punktwert, falls ausgewiesen
    low: float | None = None             # Bandbreite (geom. Mittel)
    high: float | None = None            # Bandbreite (arithm. Mittel)
    source: str = ""

    def label(self) -> str:
        return f"AT {self.sector} {self.network_level} {self.asset_type} {self.year}"


# Veröffentlichte WACC-Ergebnisse (real, vor Steuern). Mehrfach quer-bestätigt.
PUBLISHED: list[PublishedWacc] = [
    # --- Gas-Fernleitung (Randl/Zechner-Gutachten, Bandbreiten geom.–arithm.) ---
    PublishedWacc("Gas", "Fernleitung", "Bestand", 2019, None, 0.0208, 0.0345,
                  "Gutachten Randl/Zechner 2019"),
    PublishedWacc("Gas", "Fernleitung", "Neuinvestition", 2019, None, 0.0362, 0.0480,
                  "Gutachten Randl/Zechner 2019"),
    PublishedWacc("Gas", "Fernleitung", "Bestand", 2024, None, 0.0291, 0.0410,
                  "Aktualisierung 22.03.2024"),
    PublishedWacc("Gas", "Fernleitung", "Neuinvestition", 2024, None, 0.0526, 0.0628,
                  "Aktualisierung 22.03.2024"),
    PublishedWacc("Gas", "Fernleitung", "Neuinvestition", 2026, None, 0.0493, 0.0597,
                  "Aktualisierung Neuinvest 2026"),
    # --- Gas-Verteilung ---
    PublishedWacc("Gas", "Verteilung", "Bestand", 2024, 0.0416, None, None,
                  "02c Annex Regulierungssystematik (Tab. 1.1)"),
    PublishedWacc("Gas", "Verteilung", "Neuinvestition", 2024, 0.0633, None, None,
                  "02c Annex Regulierungssystematik (Tab. 1.1)"),
    # --- Strom-Verteilung (5. Regulierungsperiode 2024–2028) ---
    PublishedWacc("Strom", "Verteilung", "Bestand", 2024, 0.0416, None, None,
                  "Annex kleine VNB / Anlage 4 WACC-Aktualisierung"),
    PublishedWacc("Strom", "Verteilung", "Neuinvestition", 2023, 0.0488, None, None,
                  "FINGREEN-Studie / WACC-Neuinvest"),
    PublishedWacc("Strom", "Verteilung", "Neuinvestition", 2024, 0.0633, None, None,
                  "WACC_Neuinvestitionen_2025.pdf"),
    PublishedWacc("Strom", "Verteilung", "Neuinvestition", 2025, 0.0624, None, None,
                  "WACC_Neuinvestitionen_2025.pdf"),
    PublishedWacc("Strom", "Verteilung", "Neuinvestition", 2026, 0.0570, None, None,
                  "WACC Neuinvest 2026"),
    # --- Strom-Übertragung (APG): Neuinvest-WACC einheitlich mit Verteilung ---
    PublishedWacc("Strom", "Übertragung", "Neuinvestition", 2024, 0.0633, None, None,
                  "WACC_Neuinvestitionen_2025.pdf"),
    PublishedWacc("Strom", "Übertragung", "Neuinvestition", 2025, 0.0624, None, None,
                  "WACC_Neuinvestitionen_2025.pdf"),
    PublishedWacc("Strom", "Übertragung", "Neuinvestition", 2026, 0.0570, None, None,
                  "WACC Neuinvest 2026"),
]


def template_case(
    sector: str,
    network_level: str,
    asset_type: str,
    year: int,
    risk_free: float,
    debt_premium: float,
    inflation: float,
    equity_beta: float | None = None,
    asset_beta: float | None = None,
    country_risk_premium: float = 0.0,
    name: str | None = None,
    source: str = "",
    published_wacc_real_pretax: float | None = None,
) -> AustrianCase:
    """Baut einen ``AustrianCase`` mit den VERIFIZIERTEN E-Control-Konstanten.

    Du ergänzt nur die aus dem Gutachten-PDF zu entnehmenden Werte
    (``risk_free``, ``debt_premium``, ``inflation`` und Beta). MRP, Gearing und
    KöSt werden automatisch aus den verifizierten Konstanten gesetzt.
    """
    return AustrianCase(
        name=name or f"AT {sector} {network_level} {asset_type} {year}",
        sector=sector,
        asset_type=asset_type,
        network_level=network_level,
        year=year,
        risk_free=risk_free,
        mrp=MRP_DMS,
        country_risk_premium=country_risk_premium,
        debt_premium=debt_premium,
        gearing=GEARING,
        tax_rate=KOEST.get(year, 0.23),
        inflation=inflation,
        equity_beta=equity_beta,
        asset_beta=asset_beta,
        source=source,
        published_wacc_real_pretax=published_wacc_real_pretax,
    )
