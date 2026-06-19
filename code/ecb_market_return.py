#!/usr/bin/env python3
"""
Replication of the ECB's derivation of the expected equity *market return*
(implied cost of equity) and the *equity risk premium* (ERP) for the euro area,
using a multi-stage Dividend Discount Model (DDM).  See the write-up in
reports/05_ecb_market_return_ddm.md.

This is the single-aggregate, illustrative replication.  The reusable math lives
in ddm_engine.py (also used by the Streamlit app, code/app.py), so there is one
source of truth.  All inputs are clearly-labelled, June-2026-vintage euro-area
figures and are ILLUSTRATIVE: the point is to replicate the *derivation*, not to
publish a determination.  Swap in live IBES/OIS/index data to refresh.

Methodology (ECB Economic Bulletin 4/2018; FSR/Bulletin DDM boxes): the index
price equals the present value of expected (net) dividends, growing through three
horizons — short-term IBES growth, a linear transition, and a steady state at
long-run nominal GDP growth — discounted at the required return on equity r.
r is the expected nominal market return; ERP = r - rf (rf = 10-year OIS).
"""

from dataclasses import dataclass
import ddm_engine as E


@dataclass
class Inputs:
    dividend_yield: float = 0.032   # broad euro-area net dividend yield
    g_short: float = 0.080          # IBES near-term nominal EPS growth (~5y)
    g_long: float = 0.033           # long-run nominal GDP (1.3% real + 2.0% infl)
    rf_10y: float = 0.026           # 10-year euro OIS
    n_short: int = 5
    n_transition: int = 10


def pct(x: float) -> str:
    return f"{100 * x:5.2f}%"


def main() -> None:
    inp = Inputs()
    p = E.Params(n_short=inp.n_short, n_transition=inp.n_transition)
    d = inp.dividend_yield

    print("=" * 72)
    print("ECB-style DDM derivation of the euro-area equity market return & ERP")
    print("=" * 72)
    print("\nInputs (illustrative, June-2026 euro area):")
    print(f"  Dividend (net payout) yield D0/P0 ........ {pct(d)}")
    print(f"  Stage-1 growth  g_short  (IBES, ~5y) ..... {pct(inp.g_short)}")
    print(f"  Stage-3 growth  g_long   (nominal GDP) ... {pct(inp.g_long)}")
    print(f"  Risk-free rate  rf       (10y OIS) ....... {pct(inp.rf_10y)}")
    print(f"  Stage-1 length / transition length ....... "
          f"{inp.n_short}y / {inp.n_transition}y")

    # (A) Three-stage DDM
    r = E.three_stage_return(d, inp.g_short, inp.g_long, inp.n_short, inp.n_transition)
    print("\n(A) Three-stage DDM, solved for a single discount rate r")
    print(f"    Implied cost of equity / market return  r = {pct(r)}")
    print(f"    Equity risk premium   ERP = r - rf       = {pct(r - inp.rf_10y)}")

    # (B) H-model closed form
    H = p.h()
    rh = E.h_model_return(d, inp.g_short, inp.g_long, H)
    print(f"\n(B) Fuller-Hsia H-model (H = {H:.1f}) closed-form cross-check")
    print(f"    Implied market return r_H               = {pct(rh)}")
    print(f"    Equity risk premium   ERP_H              = {pct(rh - inp.rf_10y)}")

    # (C) Term-structure refinement (flat OIS curve here -> matches (A))
    flat = lambda t: inp.rf_10y
    erp_ts = E.term_structure_erp(d, inp.g_short, inp.g_long,
                                  inp.n_short, inp.n_transition, flat)
    print("\n(C) ECB term-structure form: solve for constant ERP (flat OIS curve)")
    print(f"    Equity risk premium   ERP                = {pct(erp_ts)}")
    print(f"    Implied long-horizon return rf + ERP     = {pct(inp.rf_10y + erp_ts)}")

    # Net-payout (buyback) variant
    d_bb = d + 0.010
    r_bb = E.three_stage_return(d_bb, inp.g_short, inp.g_long,
                                inp.n_short, inp.n_transition)
    print("\nNet-payout (dividends + ~1.0pp buybacks) variant")
    print(f"    Net payout yield ......................... {pct(d_bb)}")
    print(f"    Implied market return r .................. {pct(r_bb)}")
    print(f"    Equity risk premium ..................... {pct(r_bb - inp.rf_10y)}")

    # Sensitivity grid
    print("\nSensitivity of the implied ERP (three-stage DDM), in %:")
    yields = [0.026, 0.029, 0.032, 0.035, 0.038]
    growths = [0.06, 0.07, 0.08, 0.09, 0.10]
    header = "  g_short\\ DY |" + "".join(f"{100*y:7.1f}" for y in yields)
    print(header)
    print("  " + "-" * (len(header) - 2))
    for g in growths:
        row = f"   {100*g:5.1f}%    |"
        for y in yields:
            erp = E.three_stage_return(y, g, inp.g_long,
                                       inp.n_short, inp.n_transition) - inp.rf_10y
            row += f"{100*erp:7.2f}"
        print(row)
    print("\n(Rows: IBES stage-1 growth; columns: dividend yield. rf = 2.6% 10y OIS.)")


if __name__ == "__main__":
    main()
