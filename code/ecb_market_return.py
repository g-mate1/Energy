#!/usr/bin/env python3
"""
Replication of the ECB's derivation of the expected equity *market return*
(implied cost of equity) and the *equity risk premium* (ERP) for the euro area,
using a multi-stage Dividend Discount Model (DDM).

Methodology (as used by the ECB, e.g. ECB Economic Bulletin Article 4/2018,
"Measuring and interpreting the cost of equity in the euro area", and the
recurring DDM boxes in the Financial Stability Review / Economic Bulletin):

    The current equity index price equals the present value of expected future
    (net) dividends, discounted at the required return on equity r.  Expected
    dividend growth passes through THREE horizons:

        Stage 1 (short term)  : grows at the IBES analyst earnings-growth rate
        Stage 2 (transition)  : growth declines LINEARLY from the short-term
                                rate to the long-term rate
        Stage 3 (steady state): grows in perpetuity at long-run nominal GDP
                                growth (from the ECB Survey of Professional
                                Forecasters / Consensus Economics)

    r is the internal rate of return (IRR) that equates the discounted stream
    to the observed price.  r is the expected nominal equity MARKET RETURN
    (the implied cost of equity).  The EQUITY RISK PREMIUM is then

        ERP = r  -  rf

    where rf is the long-term risk-free rate, proxied by the 10-year overnight
    index swap (OIS) rate.

This file implements:
    (A) the full discrete three-stage DDM, solved numerically for r;
    (B) the closed-form Fuller-Hsia (1984) H-model as an analytical
        cross-check; and
    (C) the ECB "term-structure" refinement: instead of a single constant r,
        discount each horizon with the maturity-matched OIS rate plus a
        CONSTANT ERP, and solve for the ERP that matches the price.

No third-party dependencies (standard library only).

All input values are clearly-labelled, June-2026-vintage euro-area figures and
are illustrative: the point of the exercise is to replicate the *derivation*,
not to publish a determination.  Swap in live Refinitiv/IBES/OIS data to refresh.
"""

from dataclasses import dataclass, field
from typing import List, Callable


# --------------------------------------------------------------------------- #
#  Inputs  (euro area, illustrative June-2026 vintage -- see report 05)        #
# --------------------------------------------------------------------------- #

@dataclass
class Inputs:
    # Dividend (net payout) yield D0/P0 of the broad euro-area index.
    # EURO STOXX 50 forward dividend yield ~3.5%; STOXX Europe 600 trailing
    # ~2.5%.  We take 3.2% for the broad euro-area aggregate.  The ECB DDM
    # also adds net buybacks -> a higher "net payout" yield (see buyback case).
    dividend_yield: float = 0.032

    # Stage-1 nominal dividend/earnings growth: IBES near-term consensus EPS
    # growth for the euro area (~8% for 2026).
    g_short: float = 0.080

    # Stage-3 terminal nominal growth = long-run nominal GDP growth:
    #   1.3% real (ECB SPF longer-term, 2030) + 2.0% inflation target = 3.3%.
    g_long: float = 0.033

    # Risk-free rate: 10-year euro OIS (~2.6% mid-2026).
    rf_10y: float = 0.026

    # Horizons (years).
    n_short: int = 5        # Stage-1 length
    n_transition: int = 10  # Stage-2 (linear taper) length


# --------------------------------------------------------------------------- #
#  Core: project the dividend path and price it                               #
# --------------------------------------------------------------------------- #

def dividend_growth_path(inp: Inputs) -> List[float]:
    """Year-by-year nominal dividend growth rate for the explicit horizon.

    Stage 1: constant g_short for n_short years.
    Stage 2: linear decline from g_short to g_long over n_transition years.
    (Stage 3 -- the constant g_long perpetuity -- is handled by the terminal
    value, not the explicit path.)
    """
    path: List[float] = []
    for _ in range(inp.n_short):
        path.append(inp.g_short)
    for k in range(1, inp.n_transition + 1):
        w = k / inp.n_transition            # 0 -> 1 across the transition
        path.append(inp.g_short + w * (inp.g_long - inp.g_short))
    return path


def price_given_r(r: float, inp: Inputs) -> float:
    """Present value (per unit of current price) of the projected dividend
    stream discounted at a single constant rate r.  Price is normalised to 1
    and D0 = dividend_yield, so a fairly-priced index returns ~1.0."""
    if r <= inp.g_long:
        return float("inf")  # terminal Gordon value diverges
    d = inp.dividend_yield                 # D0  (price normalised to 1)
    pv = 0.0
    growth = dividend_growth_path(inp)
    for t, g in enumerate(growth, start=1):
        d *= (1.0 + g)                     # D_t
        pv += d / (1.0 + r) ** t
    # Terminal (Gordon) value at end of explicit horizon T = len(growth)
    T = len(growth)
    d_terminal_next = d * (1.0 + inp.g_long)
    terminal = d_terminal_next / (r - inp.g_long)
    pv += terminal / (1.0 + r) ** T
    return pv


def bisect(f: Callable[[float], float], lo: float, hi: float,
           tol: float = 1e-10, itmax: int = 200) -> float:
    """Plain bisection root-finder (no numpy needed)."""
    flo = f(lo)
    for _ in range(itmax):
        mid = 0.5 * (lo + hi)
        fmid = f(mid)
        if abs(fmid) < tol or (hi - lo) < tol:
            return mid
        if (flo < 0) == (fmid < 0):
            lo, flo = mid, fmid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def implied_cost_of_equity(inp: Inputs) -> float:
    """Solve price_given_r(r) = 1 for r.  r is the expected nominal equity
    market return (implied cost of equity)."""
    return bisect(lambda r: price_given_r(r, inp) - 1.0, inp.g_long + 1e-6, 0.50)


# --------------------------------------------------------------------------- #
#  (B) Closed-form Fuller-Hsia (1984) H-model cross-check                      #
# --------------------------------------------------------------------------- #

def h_model_return(inp: Inputs, H: float | None = None) -> float:
    """H-model: growth starts at g_short and declines LINEARLY to g_long over
    2H years.  Closed-form implied return:

        r = (D0/P0) * [ (1 + g_long) + H * (g_short - g_long) ] + g_long

    Default H matches the explicit model's above-trend window:
    full Stage-1 plus half the transition, H = n_short + n_transition/2.
    """
    if H is None:
        H = inp.n_short + inp.n_transition / 2.0
    d = inp.dividend_yield
    return d * ((1.0 + inp.g_long) + H * (inp.g_short - inp.g_long)) + inp.g_long


# --------------------------------------------------------------------------- #
#  (C) ECB term-structure refinement: solve for a CONSTANT ERP                 #
# --------------------------------------------------------------------------- #

def price_given_erp(erp: float, inp: Inputs, ois_curve: Callable[[int], float]) -> float:
    """Discount each horizon with the maturity-matched OIS rate plus a constant
    ERP (the ECB's preferred specification).  ois_curve(t) returns the t-year
    OIS rate.  With a flat OIS curve this is identical to price_given_r."""
    d = inp.dividend_yield
    pv = 0.0
    growth = dividend_growth_path(inp)
    for t, g in enumerate(growth, start=1):
        d *= (1.0 + g)
        r_t = ois_curve(t) + erp
        pv += d / (1.0 + r_t) ** t
    T = len(growth)
    r_T = ois_curve(T) + erp
    d_terminal_next = d * (1.0 + inp.g_long)
    pv += (d_terminal_next / (r_T - inp.g_long)) / (1.0 + r_T) ** T
    return pv


def implied_erp_termstructure(inp: Inputs, ois_curve: Callable[[int], float]) -> float:
    # Lower bound must keep the terminal discount rate above g_long, else the
    # Gordon terminal value diverges.  Start just above that singularity.
    T = inp.n_short + inp.n_transition
    lo = max(1e-3, inp.g_long - ois_curve(T) + 1e-4)
    return bisect(lambda e: price_given_erp(e, inp, ois_curve) - 1.0, lo, 0.40)


# --------------------------------------------------------------------------- #
#  Reporting                                                                   #
# --------------------------------------------------------------------------- #

def pct(x: float) -> str:
    return f"{100 * x:5.2f}%"


def main() -> None:
    inp = Inputs()

    print("=" * 72)
    print("ECB-style DDM derivation of the euro-area equity market return & ERP")
    print("=" * 72)
    print("\nInputs (illustrative, June-2026 euro area):")
    print(f"  Dividend (net payout) yield D0/P0 ........ {pct(inp.dividend_yield)}")
    print(f"  Stage-1 growth  g_short  (IBES, ~5y) ..... {pct(inp.g_short)}")
    print(f"  Stage-3 growth  g_long   (nominal GDP) ... {pct(inp.g_long)}")
    print(f"  Risk-free rate  rf       (10y OIS) ....... {pct(inp.rf_10y)}")
    print(f"  Stage-1 length / transition length ....... "
          f"{inp.n_short}y / {inp.n_transition}y")

    # (A) Three-stage DDM
    r = implied_cost_of_equity(inp)
    print("\n(A) Three-stage DDM, solved for a single discount rate r")
    print(f"    Implied cost of equity / market return  r = {pct(r)}")
    print(f"    Equity risk premium   ERP = r - rf       = {pct(r - inp.rf_10y)}")

    # (B) H-model closed form
    rh = h_model_return(inp)
    H = inp.n_short + inp.n_transition / 2.0
    print(f"\n(B) Fuller-Hsia H-model (H = {H:.1f}) closed-form cross-check")
    print(f"    Implied market return r_H               = {pct(rh)}")
    print(f"    Equity risk premium   ERP_H              = {pct(rh - inp.rf_10y)}")

    # (C) Term-structure refinement (flat OIS curve here -> matches (A))
    flat = lambda t: inp.rf_10y
    erp_ts = implied_erp_termstructure(inp, flat)
    print("\n(C) ECB term-structure form: solve for constant ERP (flat OIS curve)")
    print(f"    Equity risk premium   ERP                = {pct(erp_ts)}")
    print(f"    Implied long-horizon return rf + ERP     = {pct(inp.rf_10y + erp_ts)}")

    # Buyback / net-payout sensitivity: add ~1pp of net buyback yield.
    inp_bb = Inputs(dividend_yield=inp.dividend_yield + 0.010)
    r_bb = implied_cost_of_equity(inp_bb)
    print("\nNet-payout (dividends + ~1.0pp buybacks) variant")
    print(f"    Net payout yield ......................... {pct(inp_bb.dividend_yield)}")
    print(f"    Implied market return r .................. {pct(r_bb)}")
    print(f"    Equity risk premium ..................... {pct(r_bb - inp.rf_10y)}")

    # ----------------------------------------------------------------------- #
    #  Sensitivity grid: ERP vs dividend yield and short-term growth          #
    # ----------------------------------------------------------------------- #
    print("\nSensitivity of the implied ERP (three-stage DDM), in %:")
    yields = [0.026, 0.029, 0.032, 0.035, 0.038]
    growths = [0.06, 0.07, 0.08, 0.09, 0.10]
    header = "  g_short\\ DY |" + "".join(f"{100*y:7.1f}" for y in yields)
    print(header)
    print("  " + "-" * (len(header) - 2))
    for g in growths:
        row = f"   {100*g:5.1f}%    |"
        for y in yields:
            ip = Inputs(dividend_yield=y, g_short=g)
            erp = implied_cost_of_equity(ip) - ip.rf_10y
            row += f"{100*erp:7.2f}"
        print(row)
    print("\n(Rows: IBES stage-1 growth; columns: dividend yield. rf = 2.6% 10y OIS.)")


if __name__ == "__main__":
    main()
