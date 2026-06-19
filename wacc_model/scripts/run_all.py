#!/usr/bin/env python3
"""Reproduziert alle Kopfzahlen und gibt Vergleichstabellen aus.

    python -m scripts.run_all           # aus dem Ordner wacc_model/
    python scripts/run_all.py

Deutschland: voller Komponenten-Nachbau, Abgleich gegen veröffentlichte EK I/EK II.
Österreich: veröffentlichte WACC-Referenzwerte + Kalibrierungs-Demo (implizites Beta).
"""

from __future__ import annotations

import sys
from pathlib import Path

# Repo-Wurzel des Modells in den Pfad nehmen (Aufruf ohne Installation).
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from wacc.austria import implied_equity_beta, wacc  # noqa: E402
from wacc.beta import BNETZA_P4, ECONTROL  # noqa: E402
from wacc.capm import UnleverMethod, relever_beta  # noqa: E402
from wacc.cases import at_econtrol, de_bnetza, peer_groups  # noqa: E402
from wacc.germany import ek_zinssatz  # noqa: E402


def pct(x: float | None, nd: int = 2) -> str:
    return "—" if x is None else f"{x * 100:.{nd}f}%"


def germany_table() -> None:
    print("=" * 78)
    print("DEUTSCHLAND — BNetzA kalkulatorischer Eigenkapitalzinssatz")
    print("=" * 78)
    header = (f"{'Fall':<20}{'r_f':>7}{'MRP':>7}{'Beta':>6}{'Wagnis':>8}"
              f"{'EK I':>8}{'(publ.)':>9}{'EK II':>8}{'(publ.)':>9}")
    print(header)
    print("-" * 78)
    for case in de_bnetza.ALL_CASES:
        r = ek_zinssatz(case)
        print(f"{case.name:<20}{pct(case.risk_free):>7}{pct(case.mrp):>7}"
              f"{case.beta:>6.2f}{pct(r.risk_surcharge):>8}"
              f"{pct(r.ek1_nominal_pretax):>8}{pct(case.published_ek1):>9}"
              f"{pct(r.ek2_real_pretax):>8}{pct(case.published_ek2):>9}")
    print("-" * 78)
    print("EK I = (r_f + Wagniszuschlag) · Steuerfaktor 1,225  (nominal, vor KSt)")
    print("EK II = EK I − Ø-Inflation (10-J. VPI)              (real, vor KSt)")
    print()


def austria_published_table() -> None:
    print("=" * 78)
    print("ÖSTERREICH — E-Control WACC (real, vor Steuern), veröffentlichte Werte")
    print("=" * 78)
    print(f"{'Fall':<46}{'Punkt':>9}{'Bandbreite':>18}")
    print("-" * 78)
    for p in at_econtrol.PUBLISHED:
        band = "—"
        if p.low is not None and p.high is not None:
            band = f"{pct(p.low)}–{pct(p.high)}"
        print(f"{p.label():<46}{pct(p.wacc_real_pretax):>9}{band:>18}")
    print("-" * 78)
    print("Verifiziert: Gearing 40/60, MRP 5,0 % (DMS), KöSt 24→23 %.")
    print("Detail-Inputs (Beta, r_f, Debt Premium, Inflation) aus PDFs zu ergänzen.")
    print()


def austria_calibration_demo() -> None:
    print("=" * 78)
    print("ÖSTERREICH — Kalibrierungs-Demo: implizites Beta aus veröffentlichtem WACC")
    print("=" * 78)
    print("Beispiel Gas-Verteilung Neuinvestition 2024, Ziel-WACC real v.St. = 6,33 %.")
    print("Inputs r_f/Debt-Premium aus Sekundärquelle (UNSICHER), Inflation variiert:\n")
    rf = at_econtrol.RF_EK_2024_APPROX                       # ~3,08 % (unsicher)
    cod_mid = sum(at_econtrol.COD_2024_APPROX_RANGE) / 2     # ~4,12 % (unsicher)
    dp = cod_mid - rf
    target = 0.0633
    print(f"  r_f≈{pct(rf)}  CoD≈{pct(cod_mid)}  ⇒ Debt Premium≈{pct(dp)}  "
          f"Gearing 40/60  KöSt 23 %\n")
    print(f"  {'Inflationsannahme':<22}{'implizites Beta (verschuldet)':>30}")
    print("  " + "-" * 52)
    for infl in (0.015, 0.020, 0.025):
        beta = implied_equity_beta(
            target_wacc_real_pretax=target, risk_free=rf, mrp=at_econtrol.MRP_DMS,
            debt_premium=dp, gearing=at_econtrol.GEARING, tax_rate=0.23, inflation=infl,
        )
        print(f"  {pct(infl):<22}{beta:>30.3f}")
    print("  " + "-" * 52)
    print("  → Sobald r_f, Debt Premium und Inflation aus dem Gutachten feststehen,")
    print("    liefert die Kalibrierung das exakte verschuldete Beta (bzw. die")
    print("    Vorwärtsrechnung reproduziert den WACC).")
    print()


def beta_anchor_table() -> None:
    print("=" * 78)
    print("BETA — Re-Levering der dokumentierten Asset-Betas (Validierung)")
    print("=" * 78)
    # E-Control: regulatorisch fixiertes Asset-Beta 0,325 -> Equity-Beta @ 40/60, KöSt.
    ec = relever_beta(peer_groups.ECONTROL_REG_ASSET_BETA, debt_to_equity=1.5, tax_rate=0.23,
                      method=UnleverMethod.HAMADA)
    # BNetzA: Asset-Beta 0,40 -> Equity-Beta @ 40/60, dt. Ertragsteuer ~30 %.
    de = relever_beta(peer_groups.BNETZA_ASSET_BETA, debt_to_equity=1.5, tax_rate=0.30,
                      method=UnleverMethod.HAMADA)
    print(f"{'Regime':<26}{'Asset-β':>9}{'Steuer':>8}{'→ Equity-β':>12}{'(dok.)':>12}")
    print("-" * 78)
    print(f"{'E-Control (reg.)':<26}{peer_groups.ECONTROL_REG_ASSET_BETA:>9.3f}"
          f"{'23%':>8}{ec:>12.3f}{'~0,69–0,70':>12}")
    print(f"{'BNetzA 3. Periode':<26}{peer_groups.BNETZA_ASSET_BETA:>9.3f}"
          f"{'~30%':>8}{de:>12.3f}{'0,83':>12}")
    print(f"{'BNetzA 4. Periode':<26}{peer_groups.BNETZA_ASSET_BETA:>9.3f}"
          f"{'~30%':>8}{de:>12.3f}{'0,81':>12}")
    print("-" * 78)
    print("Modigliani-Miller (Hamada), Debt-Beta 0, Gearing 40/60 (D/E=1,5).")
    print("Veröffentlichte Equity-Betas (0,81–0,83 DE; ~0,69 AT) werden reproduziert.")
    print()


def beta_pipeline_demo() -> None:
    print("=" * 78)
    print("PEER-GROUP-BETA — volle Kette (ILLUSTRATIVE Bloomberg-Werte)")
    print("=" * 78)
    print("Beispiel: E-Control Gas-Fernleitung (BIEGTRDT), Profil Randl/Zechner")
    print("(Modigliani-Miller + Vasicek + Mittelwert). Roh-Betas/SE/Gearing PLATZHALTER.\n")
    group = peer_groups.illustrative_gas_fernleitung()
    est = ECONTROL.estimate(group, target_tax_rate=0.23)
    print(est.summary())
    print(f"\nAsset-Beta Mittelwert={est.extras['asset_beta_mean']:.3f}  "
          f"Median={est.extras['asset_beta_median']:.3f}")

    case = at_econtrol.template_case(
        sector="Gas", network_level="Fernleitung", asset_type="Neuinvestition",
        year=2024, risk_free=0.0308, debt_premium=0.0104, inflation=0.02,
        equity_beta=est.equity_beta,   # fertig re-leveragtes Beta direkt einsetzen
    )
    r = wacc(case)
    print("\nEingesetzt in E-Control-WACC (illustrativ): "
          f"Equity-Beta={r.equity_beta:.3f} -> "
          f"CoE n.St.={pct(r.coe_after_tax)}, WACC real v.St.={pct(r.wacc_real_pretax)}")
    print("(r_f/Debt-Premium/Inflation hier Platzhalter; Beta-Inputs aus Bloomberg.)")
    print()


def main() -> None:
    germany_table()
    austria_published_table()
    austria_calibration_demo()
    beta_anchor_table()
    beta_pipeline_demo()


if __name__ == "__main__":
    main()
