# calc.R -----------------------------------------------------------------
# Rechenkern fuer die Shiny-App: Beta-Varianten und implizite Marktrenditen.
# Bewusst frei von Shiny-Abhaengigkeiten, damit man die Funktionen auch per
# Rscript testen kann (siehe tests.R). Methodik: Reports 5 und 6 im Repo.

# == Teil 1: DDM / implizite Marktrendite =================================
# Konvention: Preis auf 1 normiert, d0 = Dividenden-(Netto-Auszahlungs-)Rendite
# D0/P0. Gesucht ist die interne Verzinsung r (= erwartete nominale Rendite).

# Jaehrlicher Dividendenwachstumspfad: g_short ueber n_short Jahre, danach
# linearer Uebergang auf g_long ueber n_trans Jahre. Die g_long-Perpetuitaet
# steckt im Terminal Value, nicht im Pfad.
growth_path <- function(g_short, g_long, n_short, n_trans) {
  short <- rep(g_short, n_short)
  trans <- if (n_trans > 0) {
    w <- seq_len(n_trans) / n_trans
    g_short + w * (g_long - g_short)
  } else numeric(0)
  c(short, trans)
}

# Barwert des Dividendenstroms inkl. Gordon-Terminalwert.
ddm_price <- function(r, d0, g_path, g_long) {
  if (r <= g_long) return(Inf)
  tt <- seq_along(g_path)
  d  <- d0 * cumprod(1 + g_path)          # D_1 ... D_T
  pv <- sum(d / (1 + r)^tt)
  T  <- length(g_path)
  term <- d[T] * (1 + g_long) / (r - g_long)
  pv + term / (1 + r)^T
}

# Die vier Modellherangehensweisen ---------------------------------------
# 1) Gordon (einstufig): r = D1/P0 + g
gordon_return <- function(d0, g_long) d0 * (1 + g_long) + g_long

# Hilfsfunktion: loese ddm_price(r) = 1 numerisch nach r.
solve_ddm <- function(d0, g_short, g_long, n_short, n_trans) {
  gp <- growth_path(g_short, g_long, n_short, n_trans)
  f  <- function(r) ddm_price(r, d0, gp, g_long) - 1
  out <- try(uniroot(f, c(g_long + 1e-6, 0.6), tol = 1e-8)$root, silent = TRUE)
  if (inherits(out, "try-error")) NA_real_ else out
}

# 2) Zweistufig: Hochwachstum, dann direkter Sprung auf g_long
two_stage_return <- function(d0, g_short, g_long, n_short)
  solve_ddm(d0, g_short, g_long, n_short, 0)

# 3) Dreistufig (ECB-Standard): Hochwachstum + linearer Uebergang + Steady State
three_stage_return <- function(d0, g_short, g_long, n_short, n_trans)
  solve_ddm(d0, g_short, g_long, n_short, n_trans)

# 4) H-Modell (Fuller/Hsia, geschlossene Form), H = halbe Uebergangsdauer
h_model_return <- function(d0, g_short, g_long, H)
  d0 * ((1 + g_long) + H * (g_short - g_long)) + g_long

# Alle vier auf einmal, als benannter Vektor (in Prozentpunkten der Rendite).
all_models <- function(d0, g_short, g_long, n_short, n_trans, H) {
  c("Gordon"      = gordon_return(d0, g_long),
    "Zweistufig"  = two_stage_return(d0, g_short, g_long, n_short),
    "Dreistufig"  = three_stage_return(d0, g_short, g_long, n_short, n_trans),
    "H-Modell"    = h_model_return(d0, g_short, g_long, H))
}

# Implizite Rendite je Wertpapier in einer Peer-Tabelle (ERP wird im UI aus rf
# gebildet). peers: data.frame mit dividend_yield, g_short, g_long,
# buyback_yield, name. Renditen/Wachstum in Dezimalform.
implied_table <- function(peers, n_short, n_trans, H, use_buybacks = TRUE) {
  d0 <- peers$dividend_yield + if (use_buybacks) peers$buyback_yield else 0
  res <- t(mapply(function(d, gs, gl)
    all_models(d, gs, gl, n_short, n_trans, H),
    d0, peers$g_short, peers$g_long))
  out <- data.frame(Name = peers$name, NettoRendite = d0, res,
                    check.names = FALSE)
  out
}

# Marktrendite = gewichteter Schnitt der Einzelrenditen je Modell.
# weights: numerischer Vektor (wird normiert); NA-Zellen fallen heraus.
market_return <- function(impl, weights) {
  models <- c("Gordon", "Zweistufig", "Dreistufig", "H-Modell")
  w <- weights / sum(weights)
  vapply(models, function(m) {
    v <- impl[[m]]
    ok <- is.finite(v)
    sum(w[ok] * v[ok]) / sum(w[ok])
  }, numeric(1))
}

# == Teil 2: Beta-Varianten ==============================================

# Einfaches OLS-Beta mit Standardfehler.
ols_beta <- function(y, x) {
  ok <- is.finite(y) & is.finite(x)
  y <- y[ok]; x <- x[ok]
  if (length(x) < 3 || var(x) == 0) return(c(beta = NA_real_, se = NA_real_))
  fit <- lm(y ~ x)
  s <- summary(fit)$coefficients
  c(beta = s[2, 1], se = s[2, 2])
}

# Temporaer rollierendes Beta: festes Fenster, das durch die Zeit wandert.
# window in Beobachtungen. Gibt je Endpunkt beta und se zurueck.
rolling_beta <- function(stock, market, window) {
  n <- length(stock)
  if (n < window) return(data.frame(t = integer(0), beta = numeric(0), se = numeric(0)))
  ends <- window:n
  m <- t(vapply(ends, function(e) {
    idx <- (e - window + 1):e
    ols_beta(stock[idx], market[idx])
  }, numeric(2)))
  data.frame(t = ends, beta = m[, 1], se = m[, 2])
}

# Punktschaetzer aus der rollierenden Reihe.
summarise_rolling <- function(roll, how = c("mean", "median", "last")) {
  how <- match.arg(how)
  b <- roll$beta[is.finite(roll$beta)]
  switch(how, mean = mean(b), median = median(b), last = b[length(b)])
}

# Blume / Bloomberg-Adjustierung
blume_adjust <- function(beta, a = 2/3, prior = 1) a * beta + (1 - a) * prior

# Vasicek-Shrinkage: praezise geschaetzte Betas werden weniger geschrumpft.
vasicek_adjust <- function(beta, se, prior_mean = 1, prior_sd = 0.25) {
  if (!is.finite(se) || se <= 0) return(beta)
  wp <- 1 / prior_sd^2; we <- 1 / se^2
  (we * beta + wp * prior_mean) / (we + wp)
}

# Verschiebt x um k Positionen: k>0 = Vergangenheit (Lag), k<0 = Zukunft (Lead).
shift_vec <- function(x, k) {
  n <- length(x); out <- rep(NA_real_, n)
  if (k == 0) return(x)
  if (k > 0) out[(k + 1):n] <- x[1:(n - k)]
  else { kk <- -k; out[1:(n - kk)] <- x[(kk + 1):n] }
  out
}

# Dimson-Beta (1979): Regression auf zeitversetzte Marktrenditen, Summe der
# Koeffizienten -- korrigiert Verzerrung durch asynchronen Handel.
dimson_beta <- function(stock, market, lags = 1) {
  cols <- lapply(-lags:lags, function(k) shift_vec(market, k))
  X <- as.data.frame(cols)
  names(X) <- paste0("m", -lags:lags)
  df <- cbind(y = stock, X)
  fit <- lm(y ~ ., data = df)
  sum(coef(fit)[-1], na.rm = TRUE)
}

# Reverse-CAPM: implizites (forward-looking) Beta aus impliziten Kapitalkosten.
implied_beta <- function(k_i, r_market, rf) (k_i - rf) / (r_market - rf)

# == Beispieldaten ========================================================

# Synthetische Wochenrenditen: Markt + mehrere Netzbetreiber mit unterschied-
# lichem "wahrem" Beta und einem temporaeren Beta-Sprung 2020 (Corona).
make_example_returns <- function(seed = 7) {
  set.seed(seed)
  dates <- seq(as.Date("2016-01-08"), by = "week", length.out = 520)
  mkt <- rnorm(length(dates), 0.0015, 0.020)
  betas <- c(Snam = 0.55, Terna = 0.60, Enagas = 0.50,
             Elia = 0.65, NationalGrid = 0.58)
  crisis <- dates >= as.Date("2020-02-21") & dates <= as.Date("2020-07-10")
  cols <- lapply(betas, function(b) {
    bt <- ifelse(crisis, b + 0.5, b)          # temporaerer Spike
    bt * mkt + rnorm(length(dates), 0, 0.015)
  })
  data.frame(date = dates, market = mkt, as.data.frame(cols), check.names = FALSE)
}

# Beispiel-Analystenschaetzungen (europaeische Netz-Peergroup, illustrativ).
example_peers <- function() {
  data.frame(
    name           = c("E.ON","Elia","Enagas","National Grid","Redeia",
                       "REN","Snam","Terna"),
    price          = c(13.20, 95.00, 12.50, 10.80, 16.40, 2.65, 4.55, 8.30),
    dividend_yield = c(0.040, 0.030, 0.080, 0.055, 0.060, 0.065, 0.055, 0.045),
    g_short        = c(0.060, 0.070, 0.020, 0.050, 0.030, 0.030, 0.050, 0.060),
    g_long         = rep(0.033, 8),
    buyback_yield  = c(0.000, 0.000, 0.000, 0.005, 0.000, 0.000, 0.003, 0.005),
    market_cap     = c(34000, 8000, 4000, 45000, 9000, 1800, 15000, 17000),
    stringsAsFactors = FALSE)
}
