# Schneller Selbsttest des Rechenkerns (Rscript r_app/tests.R).
source("r_app/calc.R")

cat("== DDM: Euro-Aggregat (d0=3.2%, gS=8%, gL=3.3%, 5/10J, H=10) ==\n")
m <- all_models(0.032, 0.08, 0.033, 5, 10, 10)
print(round(100 * m, 2))
stopifnot(abs(m["Dreistufig"] - 0.0801) < 0.001)
stopifnot(abs(m["H-Modell"]   - 0.0811) < 0.001)

cat("\n== Peer-Tabelle + Marktrendite (marktkapitalgewichtet, rf=2.6%) ==\n")
p <- example_peers()
impl <- implied_table(p, 5, 10, 10)
print(round(impl[, -1], 4))
mr <- market_return(impl, p$market_cap)
cat("Marktrendite je Modell:\n"); print(round(100 * mr, 2))

cat("\n== Rollierendes Beta (Snam, 104-Wochen-Fenster) ==\n")
r <- make_example_returns()
roll <- rolling_beta(r$Snam, r$market, 104)
cat(sprintf("Endpunkt %.3f | Mittel %.3f | Median %.3f (wahres Beta 0.55, Spike 2020)\n",
            summarise_rolling(roll, "last"),
            summarise_rolling(roll, "mean"),
            summarise_rolling(roll, "median")))

cat("\n== Adjustierungen / Dimson / implizites Beta ==\n")
b <- ols_beta(r$Snam, r$market)
cat(sprintf("Roh %.3f | Blume %.3f | Vasicek %.3f | Dimson %.3f\n",
            b["beta"], blume_adjust(b["beta"]),
            vasicek_adjust(b["beta"], b["se"]),
            dimson_beta(r$Snam, r$market, 1)))
ib <- implied_beta(impl$Dreistufig, mr["Dreistufig"], 0.026)
cat("Implizite Betas (reverse CAPM):\n"); print(round(setNames(ib, p$name), 2))
cat("\nAlle Tests durchgelaufen.\n")
