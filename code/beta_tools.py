"""
beta_tools.py — methodological extensions to beta estimation and the application
of implied returns (companion to reports/06_*).

Implements, with pandas + the standard library only:

  Part A — beta estimation
    * rolling_beta        : temporally rolling-window OLS beta (a beta TIME SERIES)
    * summarise_rolling   : trailing-average / median point estimate from the series
    * blume_adjust        : Blume (1971) / Bloomberg-adjusted beta
    * vasicek_adjust      : Vasicek (1973) Bayesian shrinkage toward a prior
    * dimson_beta         : Dimson (1979) thin-trading correction (summed lags)
    * exclude_window      : rule-based crisis-window removal (e.g. COVID-2020)

  Part B — application of implied returns
    * implied_beta        : reverse-CAPM forward-looking beta from DDM-implied
                            costs of equity (uses ddm_engine)

A self-contained demo on synthetic data runs under `python3 beta_tools.py`.
"""

from __future__ import annotations

from typing import Iterable, List, Optional, Tuple
import math

import pandas as pd

import ddm_engine as E


# --------------------------------------------------------------------------- #
#  Part A — rolling / time-varying beta                                       #
# --------------------------------------------------------------------------- #

def _ols_beta(y: pd.Series, x: pd.Series) -> Tuple[float, float]:
    """Return (beta, standard_error) of an OLS regression y = a + beta*x + e."""
    df = pd.concat([y, x], axis=1).dropna()
    if len(df) < 3:
        return float("nan"), float("nan")
    yv, xv = df.iloc[:, 0], df.iloc[:, 1]
    xbar, ybar = xv.mean(), yv.mean()
    sxx = ((xv - xbar) ** 2).sum()
    if sxx == 0:
        return float("nan"), float("nan")
    beta = ((xv - xbar) * (yv - ybar)).sum() / sxx
    resid = yv - (ybar - beta * xbar) - beta * xv
    n = len(df)
    sigma2 = (resid ** 2).sum() / (n - 2) if n > 2 else float("nan")
    se = math.sqrt(sigma2 / sxx) if sigma2 == sigma2 else float("nan")
    return beta, se


def rolling_beta(stock_ret: pd.Series, market_ret: pd.Series,
                 window: int) -> pd.DataFrame:
    """Temporally rolling-window OLS beta.

    For each date t the beta is estimated over the window of the last `window`
    observations ending at t, so the window *rolls* through time and you get a
    beta TIME SERIES (plus its rolling standard error), not a single number.
    `window` is in observations (e.g. 104 for 2y weekly, 252 for 1y daily).
    """
    s = pd.concat([stock_ret.rename("y"), market_ret.rename("x")], axis=1).dropna()
    betas, ses, dates = [], [], []
    for end in range(window, len(s) + 1):
        chunk = s.iloc[end - window:end]
        b, se = _ols_beta(chunk["y"], chunk["x"])
        betas.append(b); ses.append(se); dates.append(s.index[end - 1])
    return pd.DataFrame({"beta": betas, "se": ses}, index=pd.Index(dates, name="date"))


def summarise_rolling(roll: pd.DataFrame, how: str = "mean") -> float:
    """Collapse a rolling-beta series to one regulatory point estimate.
    how = 'mean' (trailing average), 'median' (robust), or 'last' (endpoint)."""
    b = roll["beta"].dropna()
    if how == "median":
        return float(b.median())
    if how == "last":
        return float(b.iloc[-1])
    return float(b.mean())


def blume_adjust(beta: float, a: float = 2 / 3, prior: float = 1.0) -> float:
    """Blume (1971) / Bloomberg-adjusted: a*beta + (1-a)*prior."""
    return a * beta + (1 - a) * prior


def vasicek_adjust(beta: float, se: float,
                   prior_mean: float = 1.0, prior_sd: float = 0.25) -> float:
    """Vasicek (1973) Bayesian shrinkage. The shrinkage weight is the estimate's
    precision relative to the prior's — precisely-estimated betas shrink less."""
    if not (se == se) or se <= 0:
        return beta
    w_prior = (1 / prior_sd ** 2)
    w_est = (1 / se ** 2)
    return (w_est * beta + w_prior * prior_mean) / (w_est + w_prior)


def dimson_beta(stock_ret: pd.Series, market_ret: pd.Series, lags: int = 1
                ) -> float:
    """Dimson (1979) thin-trading beta: sum of the coefficients on the
    contemporaneous and `lags` lagged (and led) market returns."""
    df = pd.DataFrame({"y": stock_ret})
    cols = []
    for k in range(-lags, lags + 1):
        c = f"x{k}"
        df[c] = market_ret.shift(k)
        cols.append(c)
    df = df.dropna()
    if len(df) < len(cols) + 2:
        return float("nan")
    # Multivariate OLS via normal equations (small, well-conditioned here).
    X = df[cols].to_numpy() if hasattr(df[cols], "to_numpy") else df[cols].values
    y = df["y"].to_numpy() if hasattr(df["y"], "to_numpy") else df["y"].values
    import numpy as _np  # pandas pulls numpy in; used only here
    Xc = _np.column_stack([_np.ones(len(df)), X])
    coef, *_ = _np.linalg.lstsq(Xc, y, rcond=None)
    return float(coef[1:].sum())  # sum of all market-return coefficients


def exclude_window(returns: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
    """Rule-based removal of a transitory crisis window (e.g. COVID 2020-02..
    2020-06). Must be defined ex ante and symmetrically — see report 06, A.3."""
    mask = (returns.index >= pd.Timestamp(start)) & (returns.index <= pd.Timestamp(end))
    return returns.loc[~mask]


# --------------------------------------------------------------------------- #
#  Part B — application of implied returns: reverse-CAPM implied beta          #
# --------------------------------------------------------------------------- #

def implied_beta(secs: List[E.Security], params: E.Params,
                 market_return: float, rf: float,
                 variant: str = "three_stage") -> pd.DataFrame:
    """Forward-looking beta by inverting the CAPM on DDM-implied costs of equity:

        beta_i = (k_i - rf) / (market_return - rf)

    where k_i is each security's DDM-implied cost of equity (from ddm_engine)
    and `market_return` is the index-level implied return (e.g. from the ECB DDM
    on the whole peer index, report 5). An independent, price-based cross-check
    to the regression betas in Part A.
    """
    rows = []
    denom = market_return - rf
    for s in secs:
        r = E.returns_for_security(s, params, rf_10y=rf).get(variant, float("nan"))
        beta = (r - rf) / denom if denom else float("nan")
        rows.append({"security": s.name, "implied_k": r, "implied_beta": beta})
    return pd.DataFrame(rows)


# --------------------------------------------------------------------------- #
#  Demo (synthetic data)                                                       #
# --------------------------------------------------------------------------- #

def _demo() -> None:
    import random
    random.seed(7)
    n = 520  # ~10y weekly
    idx = pd.date_range("2016-01-08", periods=n, freq="W-FRI")
    mkt, stock = [], []
    true_beta = 0.6
    for i in range(n):
        m = random.gauss(0.0015, 0.02)
        # inject a temporary 2020 beta spike (true_beta ~1.1) for ~20 weeks
        b = 1.1 if pd.Timestamp("2020-02-21") <= idx[i] <= pd.Timestamp("2020-07-10") else true_beta
        s = b * m + random.gauss(0, 0.015)
        mkt.append(m); stock.append(s)
    mkt = pd.Series(mkt, index=idx); stock = pd.Series(stock, index=idx)

    print("=" * 68)
    print("beta_tools demo — temporally rolling beta & implied (reverse-CAPM) beta")
    print("=" * 68)

    roll = rolling_beta(stock, mkt, window=104)  # 2y weekly
    print(f"\nRolling 2y beta: series length {len(roll)}; "
          f"min {roll['beta'].min():.2f}, max {roll['beta'].max():.2f}")
    print(f"  Endpoint beta (stichtag)     : {summarise_rolling(roll, 'last'):.3f}")
    print(f"  Trailing-AVERAGE beta        : {summarise_rolling(roll, 'mean'):.3f}")
    print(f"  Trailing-MEDIAN  beta (robust): {summarise_rolling(roll, 'median'):.3f}")
    print(f"  (true beta = {true_beta}, with a temporary 2020 spike to 1.1)")

    # Crisis-window handling
    rets = pd.concat([stock.rename("stock"), mkt.rename("mkt")], axis=1)
    clean = exclude_window(rets, "2020-02-21", "2020-07-10")
    b_all, se_all = _ols_beta(rets["stock"], rets["mkt"])
    b_cln, se_cln = _ols_beta(clean["stock"], clean["mkt"])
    print(f"\nFull-sample beta            : {b_all:.3f}")
    print(f"Crisis-window-excluded beta : {b_cln:.3f}")
    print(f"Blume-adjusted (full)       : {blume_adjust(b_all):.3f}")
    print(f"Vasicek-adjusted (full)     : {vasicek_adjust(b_all, se_all):.3f}")
    print(f"Dimson (1 lag) beta         : {dimson_beta(stock, mkt, lags=1):.3f}")

    # Implied (reverse-CAPM) beta from DDM-implied costs of equity
    secs = [
        E.Security("Snam",   4.55, g_short=0.05, g_long=0.033, dividend_yield=0.055),
        E.Security("Terna",  8.30, g_short=0.06, g_long=0.033, dividend_yield=0.045),
        E.Security("Enagas", 12.5, g_short=0.02, g_long=0.033, dividend_yield=0.080),
        E.Security("Elia",   95.0, g_short=0.07, g_long=0.033, dividend_yield=0.030),
    ]
    p = E.Params(n_short=5, n_transition=10)
    market_return = 0.09  # e.g. ECB-DDM implied return on the peer index
    ib = implied_beta(secs, p, market_return=market_return, rf=0.026)
    print("\nReverse-CAPM implied beta (market implied return 9.0%, rf 2.6%):")
    for _, r in ib.iterrows():
        print(f"  {r['security']:8s}  implied k={100*r['implied_k']:5.2f}%  "
              f"implied beta={r['implied_beta']:.2f}")
    print(f"  Peer-mean implied beta       : {ib['implied_beta'].mean():.2f}")


if __name__ == "__main__":
    _demo()
