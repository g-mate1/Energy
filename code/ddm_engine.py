"""
ddm_engine.py — shared Dividend-Discount-Model engine.

Canonical, dependency-free (standard library only) implementation of the
methodological variants used to back the *implied cost of equity* (expected
nominal return) and the *equity risk premium* (ERP) out of share prices and
analyst estimates, following the ECB's multi-stage DDM approach
(see reports/05_ecb_market_return_ddm.md).

Variants implemented, per security:
    1. Gordon (one-stage)           gordon_return
    2. Two-stage DDM                two_stage_return   (= three-stage, no taper)
    3. Three-stage DDM              three_stage_return (ECB primary)
    4. Fuller-Hsia H-model          h_model_return
    5. Term-structure / constant-ERP solve  term_structure_erp / _return

Plus weighted aggregation of per-security results into a market return & ERP.

Both code/ecb_market_return.py (the standalone replication) and code/app.py
(the Streamlit app) import from here, so the math has a single source of truth.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, List, Optional
import math

NaN = float("nan")


# --------------------------------------------------------------------------- #
#  Security container                                                          #
# --------------------------------------------------------------------------- #

@dataclass
class Security:
    """One share's inputs.  Provide either `dividend` (D0, currency per share)
    or `dividend_yield` (D0/P0).  `buyback_yield` (net buyback / market cap) is
    added to the dividend yield to form the *net payout* yield used by the ECB
    DDM.  `weight` is the market-return weight (if None, derived from
    `market_cap`, else equal-weighted)."""
    name: str
    price: float
    g_short: float
    g_long: float
    dividend: Optional[float] = None
    dividend_yield: Optional[float] = None
    buyback_yield: float = 0.0
    weight: Optional[float] = None
    market_cap: Optional[float] = None

    def net_payout_yield(self, include_buybacks: bool = True) -> float:
        if self.dividend_yield is not None:
            dy = self.dividend_yield
        elif self.dividend is not None and self.price:
            dy = self.dividend / self.price
        else:
            raise ValueError(f"{self.name}: need dividend or dividend_yield")
        return dy + (self.buyback_yield if include_buybacks else 0.0)


# --------------------------------------------------------------------------- #
#  Numerics                                                                    #
# --------------------------------------------------------------------------- #

def _bisect(f: Callable[[float], float], lo: float, hi: float,
            tol: float = 1e-10, itmax: int = 200) -> float:
    """Sign-bracketed bisection.  Returns NaN if the interval is not bracketed."""
    flo, fhi = f(lo), f(hi)
    if math.isnan(flo) or math.isnan(fhi) or (flo > 0) == (fhi > 0):
        return NaN
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


def growth_path(g_short: float, g_long: float,
                n_short: int, n_transition: int) -> List[float]:
    """Year-by-year growth: constant g_short for n_short years, then a LINEAR
    taper to g_long over n_transition years.  The g_long perpetuity that
    follows is handled by the terminal value, not this explicit path."""
    path = [g_short] * n_short
    for k in range(1, n_transition + 1):
        w = k / n_transition if n_transition else 1.0
        path.append(g_short + w * (g_long - g_short))
    return path


# --------------------------------------------------------------------------- #
#  Pricing kernels                                                             #
# --------------------------------------------------------------------------- #

def _price_constant_r(r: float, d0: float, growth: List[float],
                      g_long: float) -> float:
    """PV (per unit price) of the dividend stream discounted at constant r.
    d0 is the current net-payout yield (price normalised to 1)."""
    if r <= g_long:
        return float("inf")
    d, pv = d0, 0.0
    for t, g in enumerate(growth, start=1):
        d *= (1.0 + g)
        pv += d / (1.0 + r) ** t
    T = len(growth)
    pv += (d * (1.0 + g_long) / (r - g_long)) / (1.0 + r) ** T
    return pv


def _price_curve(erp: float, d0: float, growth: List[float], g_long: float,
                 ois_curve: Callable[[int], float]) -> float:
    """PV discounting each horizon at the maturity-matched curve rate + ERP."""
    d, pv = d0, 0.0
    for t, g in enumerate(growth, start=1):
        d *= (1.0 + g)
        r_t = ois_curve(t) + erp
        pv += d / (1.0 + r_t) ** t
    T = len(growth)
    r_T = ois_curve(T) + erp
    if r_T <= g_long:
        return float("inf")
    pv += (d * (1.0 + g_long) / (r_T - g_long)) / (1.0 + r_T) ** T
    return pv


# --------------------------------------------------------------------------- #
#  The five variants (single security)                                        #
# --------------------------------------------------------------------------- #

def gordon_return(d0: float, g_long: float) -> float:
    """One-stage Gordon growth: r = D1/P0 + g = d0*(1+g) + g."""
    return d0 * (1.0 + g_long) + g_long


def three_stage_return(d0: float, g_short: float, g_long: float,
                       n_short: int, n_transition: int) -> float:
    """ECB primary: solve P0=1 for the single discount rate r."""
    growth = growth_path(g_short, g_long, n_short, n_transition)
    return _bisect(lambda r: _price_constant_r(r, d0, growth, g_long) - 1.0,
                   g_long + 1e-6, 0.60)


def two_stage_return(d0: float, g_short: float, g_long: float,
                     n_short: int) -> float:
    """Two-stage = three-stage with no transition (immediate step to g_long)."""
    return three_stage_return(d0, g_short, g_long, n_short, 0)


def h_model_return(d0: float, g_short: float, g_long: float, H: float) -> float:
    """Fuller-Hsia (1984) closed form.  Growth declines linearly from g_short
    to g_long over 2H years.  r = d0*[(1+g_long) + H*(g_short-g_long)] + g_long."""
    return d0 * ((1.0 + g_long) + H * (g_short - g_long)) + g_long


def term_structure_erp(d0: float, g_short: float, g_long: float,
                       n_short: int, n_transition: int,
                       ois_curve: Callable[[int], float]) -> float:
    """ECB term-structure form: solve for the constant ERP that prices P0=1
    when each horizon is discounted at ois_curve(t)+ERP."""
    growth = growth_path(g_short, g_long, n_short, n_transition)
    T = n_short + n_transition
    lo = max(1e-3, g_long - ois_curve(T) + 1e-4)
    return _bisect(lambda e: _price_curve(e, d0, growth, g_long, ois_curve) - 1.0,
                   lo, 0.40)


def term_structure_return(d0: float, g_short: float, g_long: float,
                          n_short: int, n_transition: int,
                          ois_curve: Callable[[int], float]) -> float:
    """Long-horizon implied return = curve(T) + implied constant ERP."""
    erp = term_structure_erp(d0, g_short, g_long, n_short, n_transition, ois_curve)
    if math.isnan(erp):
        return NaN
    return ois_curve(n_short + n_transition) + erp


# --------------------------------------------------------------------------- #
#  Driver: all variants for one security                                      #
# --------------------------------------------------------------------------- #

@dataclass
class Params:
    n_short: int = 5
    n_transition: int = 10
    include_buybacks: bool = True
    H: Optional[float] = None  # default n_short + n_transition/2

    def h(self) -> float:
        return self.H if self.H is not None else self.n_short + self.n_transition / 2.0


def returns_for_security(sec: Security, p: Params,
                         ois_curve: Optional[Callable[[int], float]] = None,
                         rf_10y: Optional[float] = None) -> dict:
    """Compute every variant's implied return for one security.  ERP uses the
    10y point of the curve (or rf_10y) as the risk-free rate."""
    d0 = sec.net_payout_yield(p.include_buybacks)
    g_s = sec.g_short
    g_l = sec.g_long
    if rf_10y is None and ois_curve is not None:
        rf_10y = ois_curve(10)

    out = {
        "net_payout_yield": d0,
        "gordon": gordon_return(d0, g_l),
        "two_stage": two_stage_return(d0, g_s, g_l, p.n_short),
        "three_stage": three_stage_return(d0, g_s, g_l, p.n_short, p.n_transition),
        "h_model": h_model_return(d0, g_s, g_l, p.h()),
    }
    if ois_curve is not None:
        out["term_structure"] = term_structure_return(
            d0, g_s, g_l, p.n_short, p.n_transition, ois_curve)
    if rf_10y is not None:
        for k in list(out):
            if k == "net_payout_yield":
                continue
            r = out[k]
            out[k + "_erp"] = (r - rf_10y) if not math.isnan(r) else NaN
    return out


# --------------------------------------------------------------------------- #
#  Aggregation to a market return                                             #
# --------------------------------------------------------------------------- #

def normalised_weights(secs: List[Security]) -> List[float]:
    """Weights from explicit `weight`, else `market_cap`, else equal-weight."""
    if all(s.weight is not None for s in secs):
        raw = [float(s.weight) for s in secs]
    elif all(s.market_cap is not None for s in secs):
        raw = [float(s.market_cap) for s in secs]
    else:
        raw = [1.0] * len(secs)
    tot = sum(raw)
    return [w / tot for w in raw] if tot else [1.0 / len(secs)] * len(secs)


def aggregate_market(secs: List[Security], p: Params,
                     ois_curve: Optional[Callable[[int], float]] = None,
                     rf_10y: Optional[float] = None) -> dict:
    """Weighted-average each variant's implied return across securities.
    NaN cells are dropped from their column's weight base."""
    w = normalised_weights(secs)
    per = [returns_for_security(s, p, ois_curve, rf_10y) for s in secs]
    keys = set().union(*[set(d) for d in per])
    agg = {}
    for k in keys:
        num, den = 0.0, 0.0
        for wi, d in zip(w, per):
            v = d.get(k, NaN)
            if v is not None and not math.isnan(v):
                num += wi * v
                den += wi
        agg[k] = num / den if den else NaN
    return {"weights": w, "per_security": per, "market": agg}
