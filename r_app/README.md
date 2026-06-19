# R-Shiny-App: Beta-Varianten & implizite Marktrenditen

Interaktive App zu den Methoden aus [Report 5](../reports/05_ecb_market_return_ddm.md)
(implizite Marktrendite per DDM) und [Report 6](../reports/06_beta_und_implizite_renditen_deep-dive.md)
(Beta-Varianten). Läuft sofort mit Beispieldaten.

## Starten

```r
install.packages(c("shiny", "ggplot2"))   # einmalig
shiny::runApp("r_app")                     # aus dem Repo-Wurzelverzeichnis
```

oder in RStudio `r_app/app.R` öffnen und **Run App** klicken.

## Inhalt

**Tab „Implizite Marktrendite"** – die vier Modellansätze auf Basis von Kurs +
Analystenschätzungen:

1. **Gordon** (einstufig)
2. **Zweistufig**
3. **Dreistufig** (ECB-Standard)
4. **H-Modell** (Fuller/Hsia)

Je Wertpapier und als markt­gewichtete Aggregat-Marktrendite, inkl. ERP gegen den
risikofreien Zins. Stufenlängen, H, rf, Buyback-Berücksichtigung und Gewichtung
(Marktkapitalisierung/gleich) sind einstellbar; eigene Peers per CSV ladbar.

**Tab „Beta-Varianten"** – für einen wählbaren Netzbetreiber:

- **temporär rollierendes Beta** (Mittel / Median / Endpunkt des rollierenden
  Fensters) mit Zeitreihen-Plot,
- OLS über den Vollzeitraum und **krisenbereinigt** (ausschließbares Krisenfenster),
- **Blume**- und **Vasicek**-Adjustierung,
- **Dimson**-Beta (Mikrostruktur-Korrektur).

**Tab „Daten & Methodik"** – Beispieldaten und Methodenhinweise.

## Dateien

| Datei | Zweck |
|---|---|
| `app.R` | UI + Server (Shiny) |
| `calc.R` | Rechenkern (ohne Shiny-Abhängigkeit, einzeln testbar) |
| `tests.R` | Selbsttest des Rechenkerns: `Rscript r_app/tests.R` |
| `data/peers_example.csv` | Beispiel-Peers im Upload-Format (Raten als Dezimalzahl) |

## Daten-Format (CSV-Upload)

Spalten: `name, price, dividend_yield, g_short, g_long, buyback_yield, market_cap`.
Renditen/Wachstumsraten als **Dezimalzahl** (0.03 = 3 %). `g_long` und
`buyback_yield` sind optional (Default 0.033 bzw. 0). Die Beta-Renditen sind
synthetisch erzeugt (reproduzierbar via `set.seed`), mit einem temporären
Beta-Sprung im Frühjahr 2020, um die Krisenbehandlung zu demonstrieren.

## Hinweis

Illustrative Beispieldaten – kein Festlegungsinput. Implizite Renditen und
reagible Betas erben Annahmen (Analystenwachstum, Fensterwahl) und sind
regulatorisch als Cross-Check zu verstehen (siehe Report 6, Kap. 10).
