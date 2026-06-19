# Methodische Erweiterungen: Beta-Berechnung und Anwendung impliziter Renditen

*Stand Juni 2026. Dieser Bericht ist die methodische Vertiefung zu **Report 2** (Peer-Group-Beta nach Randl/Zechner) und **Report 5** (ECB-DDM-Herleitung der Marktrendite). Er behandelt – wie erbeten – **getrennt** (A) die methodischen Erweiterungen der Beta-Schätzung, mit Schwerpunkt auf dem **temporär rollierenden Beta**, und (B) die Anwendung der **impliziten Renditen**. Eine lauffähige Umsetzung liegt unter [`../code/beta_tools.py`](../code/beta_tools.py); die DDM-Engine unter [`../code/ddm_engine.py`](../code/ddm_engine.py). Die **formale, detaillierte Methodendarstellung** (Modellgleichungen, Schätzer, Schätzprotokoll) findet sich im begleitenden Methodenkapitel [`06_beta_und_implizite_renditen_deep-dive.md`](06_beta_und_implizite_renditen_deep-dive.md).*

---

## Ausgangspunkt (Status quo aus Report 2)

Das Frontier/Zechner/Randl-Gutachten (BK4-21-0055) schätzt das Beta **statisch über mehrere feste Fenster** zu **einem** Stichtag (31.12.2020): Roh-Betas aus täglichen/wöchentlichen Renditen über **1-, 3- und 5-Jahres-Fenster**, **Vasicek-adjustiert**, **MM-entschuldet/wiederverschuldet** (Debt-Beta in der Schwesterstudie E-Control = 0), Marktindex **FTSE All-World**; Ergebnis: Equity-Beta ≈ **0,81**, Asset-Beta ≈ **0,34–0,42** [Report 2]. Dieser Ansatz ist transparent und replizierbar, hat aber drei bekannte Schwächen: **Stichtagsabhängigkeit** (das Ergebnis hängt am gewählten Endpunkt), **Annahme der Beta-Konstanz** innerhalb des Fensters und **Rückwärtsgerichtetheit** (historische Betas antizipieren keine Strukturbrüche, etwa die NEST/WACC-Reform ab der 5. Periode [GT]). Die folgenden Erweiterungen setzen genau hier an.

---

# Teil A — Methodische Erweiterungen der Beta-Berechnung

## A.1 Das temporär rollierende Beta (rolling-window-Beta)

**Idee.** Statt das Beta nur an *einem* Stichtag über mehrere Fensterlängen zu schätzen, wird ein **fester Fensterlänge W** (z. B. 2 Jahre wöchentlich) **durch die Zeit geschoben**: Für jeden Handelstag *t* wird

```
β_t = Cov(r_i, r_m | Fenster [t−W, t]) / Var(r_m | Fenster [t−W, t])
```

geschätzt. Man erhält keine einzelne Zahl, sondern eine **Beta-Zeitreihe** `{β_t}`. „Temporär rollierend" meint genau dies: der Schätzzeitraum *rolliert temporal*, der Endpunkt wandert. Aus der Trajektorie wird der regulatorische Punktschätzer abgeleitet – typischerweise als **Mittelwert/Median der rollierenden Betas über den Referenzzeitraum** (ein „trailing average" der Betas), nicht als einzelner Endpunktwert.

**Warum das eine echte Erweiterung ist.**
- **Reduktion der Stichtagsabhängigkeit.** Der Endpunkt-Bias des statischen Ansatzes wird gemittelt; ein einzelner Krisen- oder Erholungstag dominiert das Ergebnis nicht mehr.
- **Sichtbarkeit der Instabilität.** Die Zeitreihe macht Niveauverschiebungen, Trends und Krisen-Spikes explizit – Grundlage für Stabilitäts- und Strukturbruchtests (Chow, CUSUM) und für die bewusste Behandlung temporärer Verzerrungen (A.3).
- **Anschluss an die internationale Praxis.** Die UK-Regulierer (UKRN/Ofgem/Ofwat/CMA) verwenden genau diesen **rolling-OLS-Ansatz**: rollierende Regressionen über **mehrere Frequenzen** (täglich/wöchentlich/monatlich) und **mehrere Fenster** (1/2/5/10 Jahre) für einen Pool von Vergleichsunternehmen, mit aktuellen Equity-Beta-Spannen von rund **0,77–1,03** [UKRN18][UKRN23][UKRN25]. Der deutsche Multi-Fenster-Ansatz ist faktisch ein *Spezialfall mit nur einem Endpunkt*.

**Designparameter und Trade-offs** (alle in `beta_tools.py` umgesetzt):
- **Fensterlänge W:** kurz = reagibel, aber verrauscht; lang = glatt, aber träge. Regulatorisch üblich 2–5 Jahre.
- **Frequenz:** täglich (viele Beobachtungen, aber Mikrostruktur-/Nichthandels-Rauschen), wöchentlich/monatlich (weniger Rauschen, weniger Beobachtungen). Mehrere Frequenzen parallel = Robustheitscheck.
- **Überlappung:** rollierende Fenster sind stark überlappend → die β_t-Reihe ist autokorreliert; bei Inferenz auf der Reihe (z. B. Konfidenzbändern für den Mittelwert) zu berücksichtigen.
- **Aggregation:** Mittelwert vs. Median (robuster) vs. zeitlich gewichteter (jüngere Fenster höher gewichtet) Durchschnitt.

## A.2 Zeitvariable/bedingte Beta-Modelle (über das rollierende OLS hinaus)

Das rollierende OLS unterstellt **innerhalb** des Fensters Konstanz und gewichtet alle Fensterbeobachtungen gleich. Ökonometrisch sauberere Erweiterungen modellieren die Zeitvariation **direkt**:

- **State-Space / Kalman-Filter.** Das Beta wird als latenter Zustand mit **Random-Walk-Dynamik** modelliert (`β_t = β_{t−1} + η_t`); der Kalman-Filter liefert die optimale **gefilterte** (nur Vergangenheit) bzw. **geglättete** (Voll-Sample) Schätzung samt Konfidenzbändern. In Prognosevergleichen schneidet der Kalman-Filter oft **am besten** ab und dominiert GARCH-Varianten [Zhang17][FaffBrooks].
- **Bedingtes Beta aus (DCC-)GARCH.** `β_t = ρ_{im,t} · σ_{i,t} / σ_{m,t}` aus der bedingten Kovarianzmatrix (DCC-/BEKK-GARCH). Passt sich Volatilitätsregimen an; reagibel, aber parameter- und annahmenintensiv [DCC].

**Regulatorische Abwägung.** Transparenz und Replizierbarkeit sprechen im Festlegungskontext für das **rollierende OLS** als Hauptverfahren; Kalman/GARCH eignen sich als **Validierung** der Zeitvariation und zur Identifikation von Regimen. Wichtig ist die Konsistenz: Wer ein reagibles, bedingtes Beta verwendet, muss es mit einer ebenso zeitnah gemessenen Marktrisikoprämie kombinieren (siehe Teil B.3) – sonst entsteht ein Methodenbruch.

## A.3 Behandlung **temporärer** Verzerrungen (Krisenfenster)

Der Begriff „temporär" hat eine zweite, ökonomisch zentrale Lesart: der Umgang mit **transitorischen Schocks**, die das Beta vorübergehend verzerren. Die Energieversorger-Betas wurden durch die **COVID-Krise 2020** und die **Energiekrise 2022** (Gaspreis-Spike nach Februar 2022) temporär verschoben – defensive Netzwerte korrelierten und schwankten anders als im Normalregime. Eine rollierende Beta-Reihe macht solche **Spikes** sichtbar; die Frage ist, wie man sie behandelt, ohne das Ergebnis zu verzerren:

- **Regelbasierter Fensterausschluss / Down-Weighting** der Krisenperiode (ex ante definierte Kriterien, nicht ex post „cherry-picking").
- **Dummy-/Ereignisvariablen** in der Regression, die den Krisenzeitraum separat auffangen.
- **De-Spiking / robuste Regression** (z. B. Huber-Schätzer), die Extremtage herabgewichtet.
- **Längere Fenster**, die einen Schock verdünnen – auf Kosten der Reagibilität.
- **Vasicek-Shrinkage** (bereits im Status quo) dämpft Schätzextreme ohnehin Richtung Prior.

**Caveat.** Jede Krisenbereinigung ist ein Eingriff mit Manipulationspotenzial; sie muss **regelgebunden, symmetrisch und vorab** dokumentiert sein. Die Gerichte (OLG Düsseldorf, BGH) haben der BNetzA hier weiten Beurteilungsspielraum zugestanden [Report 2/3], was die Anforderung an eine *nachvollziehbare* Regel eher erhöht als senkt.

## A.4 Mikrostruktur- und Adjustierungsfragen (frequenz- und liquiditätsbezogen)

- **Nichthandels-/Thin-Trading-Korrektur.** Bei weniger liquiden Peers erzeugt asynchroner Handel ein nach unten verzerrtes Beta. **Dimson (1979)** (Summe der Koeffizienten auf verzögerte Marktrenditen) bzw. **Scholes–Williams (1977)** korrigieren dies – relevant, weil das Liquiditätskriterium (Report 2, §3) genau solche Verzerrungen vermeiden soll, kleinere TSO-Peers aber betroffen sein können.
- **Adjustierung Roh→adjustiert.** **Blume (1971):** `β_adj = 0,67·β_raw + 0,33·1` (Mean Reversion; = Bloomberg-Adjusted-Beta). **Vasicek (1973):** bayesianische Schrumpfung zum Prior mit *peer-spezifischem* Gewicht (präziser geschätzte Betas werden weniger geschrumpft) – das im deutschen Gutachten gewählte Verfahren. Beide sind in `beta_tools.py` enthalten, um die Sensitivität sichtbar zu machen.
- **Referenzindex.** Lokal vs. global: das Gutachten nutzt den globalen FTSE All-World; ein engerer Euro-/Heimatindex liefert i. d. R. ein anderes Beta-Niveau (Report 2, §4). Der Indexwahl-Effekt sollte als Sensitivität ausgewiesen werden.

---

# Teil B — Anwendung der impliziten Renditen

Report 5 leitet aus dem ECB-Mehrstufen-DDM eine **vorausschauende, marktimplizite** Renditegröße ab: die implizite Eigenkapitalrendite `r_impl` (= erwartete nominale Marktrendite) und die implizite Risikoprämie `ERP_impl = r_impl − rf`. Diese Größen sind **zeitvariabel** und stehen dem **historischen** MRP (Stehle/DMS; Report 1) gegenüber, auf den die BNetzA primär abstellt. Die Anwendungen:

## B.1 Implizite MRP als Input bzw. Cross-Check zum historischen MRP

Die naheliegendste Anwendung: die DDM-implizite MRP als **vorwärtsgerichtete Alternative oder Plausibilisierung** der historischen MRP im CAPM. Praktisch relevant, weil der historische MRP (3,70 % im Gutachten) der zweite große Werthebel neben dem Beta ist. Die implizite MRP bewegt sich mit Kursen und Zinsen; ein **Blending** historischer und impliziter Schätzer (wie es Ofgem beim Total Market Return mit etwa gleicher Gewichtung praktiziert [Report 4]) ist die gängige Brücke. Wichtig für die Anwendung ist die **TMR-Stabilitätsdebatte**: UK-Regulierer halten den realen TMR bewusst stabil und lassen den risikofreien Zins wandern – implizite Renditen dienen dann als Test, *ob* die TMR-Annahme noch trägt, nicht als mechanischer Jahres-Input.

## B.2 Implizites / forward-looking Beta (Reverse-CAPM)

Die zweite, weniger triviale Anwendung verbindet Teil A und B. Man berechnet das DDM-implizite Kapitalkostenniveau **je Peer** (`k_i`, aus Preis + Analystenschätzungen jedes Unternehmens, Report 5/`app.py`) und **invertiert das CAPM**:

```
β_i,impl = (k_i − rf) / (r_impl − rf)
```

Das ergibt ein **preisbasiertes, vorwärtsgerichtetes Beta**, das *unabhängig* von der Regressionsmechanik ist [Dam-impl]. Anwendungen:
- **Cross-Check** zu den Regressions-Betas (rollierend/statisch) der Peer-Group: weichen implizites und historisches Beta stark ab, ist das ein Warnsignal für Strukturbruch oder Fehlbewertung.
- **Sektor-implizite Eigenkapitalkosten** (Damodaran): Statt firmenweiser Betas berechnet man das DDM-implizite `k` für den **gesamten Netz-Peer-Index** und weist es als Sektor-Kapitalkostensatz allen Netzbetreibern zu – das Beta wird dann gar nicht erst einzeln benötigt [Dam-impl]. Das ist methodisch genau die ECB-Logik auf Sektorebene.
- **Aggregation** der peer-impliziten Betas (Mittel/Median) als forward-looking Gegenstück zum 0,81-Equity-Beta.

`beta_tools.implied_beta()` setzt diese Inversion um und nutzt dafür die `ddm_engine`-Renditen.

## B.3 Konsistente Kopplung: zeitvariable MRP × rollierendes Beta

Die anspruchsvollste Anwendung ist die **gemeinsame** Verwendung beider Erweiterungen zu einem zeitkonsistenten Eigenkapitalkosten-Panel:

```
k_{i,t} = rf_t + β_{i,t} · ERP_impl,t
```

mit rollierendem/bedingtem `β_{i,t}` (Teil A) und DDM-impliziter `ERP_impl,t` (Report 5). Das ist maximal vorwärtsgerichtet und regimesensitiv – birgt aber drei **Konsistenzfallen**, die in der Anwendung beachtet werden müssen:

1. **Doppelzählung der Zeitvariation.** Steigen in einer Krise *zugleich* Beta und implizite MRP, kann `k_{i,t}` überschießen. Bewusste Designentscheidung nötig: entweder stabiles Beta × zeitvariable MRP, oder umgekehrt – nicht unreflektiert beides „voll" zeitvariabel.
2. **Periodenkonsistenz.** Beta-Fenster, MRP-Horizont und risikofreier Zins müssen über konsistente Konventionen (Frequenz, Zeitraum, nominal/real) gemessen werden.
3. **Zirkularität/Erwartungsabhängigkeit.** Das implizite Beta speist sich aus impliziten Marktrenditen, die wiederum auf Analystenprognosen (IBES) beruhen – kein von Erwartungen unabhängiger Anker. Transparenz über die Inputs ist Pflicht (vgl. Optimismus-Bias der Analysten, Report 5, §6).

**Regulatorischer Kernvorbehalt – Prozyklizität.** Voll zeitvariable, marktimplizite zulässige Renditen würden mit der Marktstimmung schwanken. Genau das wollen Regulierer vermeiden; daher die **Dämpfungsmechanismen** (gleitende Durchschnitte beim risikofreien Zins – die BNetzA nutzt den 10-Jahres-Schnitt der Umlaufsrendite –, stabiler TMR, Vasicek-Shrinkage, Trailing-Average der rollierenden Betas). Implizite Renditen und reagible Betas sind deshalb in der Regulierung primär **Cross-Checks und Plausibilisierungen**, nicht der mechanische Festlegungsinput – konsistent mit der Botschaft aus Report 5.

## B.4 Weitere Anwendungen impliziter Renditen

- **ECB-Dekomposition.** Zerlegung von Kursbewegungen in Cashflow-, Zins- und Risikoprämienbeitrag (Report 5) – nützlich, um zu verstehen, *warum* sich eine implizite MRP/ein implizites Beta bewegt.
- **Cross-Checks der zulässigen Rendite.** Market-to-Asset-Ratio (MAR/RAB-Prämie), Investierbarkeit/Finanzierbarkeit, „Aiming up" (Report 4) – implizite Eigenkapitalkosten sind ein Maßstab dafür, ob die festgelegte Rendite mit dem Marktpreis vereinbar ist.

---

## Verzahnung und Empfehlung

| Dimension | Status quo (Report 2/Gutachten) | Erweiterung (dieser Bericht) |
|---|---|---|
| Beta-Schätzung | feste 1/3/5-J-Fenster, ein Stichtag | **temporär rollierend** (β_t-Reihe, Trailing-Average); optional Kalman/DCC |
| Endpunkt-Bias | hoch | gemittelt/reduziert |
| Krisenbehandlung | implizit via Vasicek | regelbasierter Fensterausschluss/Dummy/De-Spiking |
| Mikrostruktur | Liquiditätsfilter | + Dimson/Scholes-Williams |
| MRP | historisch (Stehle 3,70 %) | + DDM-implizit (Report 5) als Cross-Check/Blend |
| Beta-Validierung | nur Regression | + **implizites Beta** (Reverse-CAPM) |
| Zeitkonsistenz | statisch | optionales Panel `k_{i,t}=rf_t+β_{i,t}·ERP_impl,t` |

**Empfehlung für die praktische Anwendung:** das rollierende Beta als **transparentes Hauptverfahren** (Trailing-Average über mehrere Frequenzen/Fenster, regelbasierte Krisenbehandlung), flankiert von **state-space**-Schätzungen zur Stabilitätsprüfung; die impliziten Renditen/Betas als **vorwärtsgerichteter Cross-Check** zur historischen MRP und zum Regressions-Beta – mit expliziter Dämpfung gegen Prozyklizität. Alle Verfahren sind in [`../code/beta_tools.py`](../code/beta_tools.py) lauffähig hinterlegt.

---

## Quellen

**Beta-Methodik (rollierend / zeitvariabel / Adjustierung)**

[UKRN18] UK Regulators Network, *Estimating the cost of capital for implementation of price controls by UK Regulators* (2018) — https://ukrn.org.uk/app/uploads/2018/06/2018-CoE-Study.pdf
[UKRN23] UKRN, *Cost of Capital — guidance* (22.03.2023; rolling-OLS, Frequenzen/Fenster) — https://ukrn.org.uk/app/uploads/2023/03/CoC-guidance_22.03.23.pdf
[UKRN25] UKRN, *Annual Cost of Capital Report 2025* — https://ukrn.org.uk/app/uploads/2025/12/UKRN-Annual-Cost-of-Capital-Report-2025-edition-final-Dec-2025.pdf
[Zhang17] Y. Zhang et al., *Forecasting the Daily Time-Varying Beta of European Banks: GARCH Models vs. the Kalman Filter*, Journal of Forecasting (2017) — https://onlinelibrary.wiley.com/doi/10.1002/for.2442
[FaffBrooks] Faff, Hillier & Hillier, *Forecasting the weekly time-varying beta of UK firms: GARCH vs. Kalman filter*, European Journal of Finance 15(4) — https://www.tandfonline.com/doi/abs/10.1080/13518470802604499
[DCC] R. Beeli, *Modeling conditional betas with DCC-GARCH* (Bali/Engle/Tang-Konstrukt) — https://github.com/rbeeli/dynamic_conditional_beta
[Dimson] E. Dimson, *Risk measurement when shares are subject to infrequent trading*, J. Financial Economics (1979).
[Blume] M. Blume, *On the assessment of risk*, Journal of Finance (1971). [Vasicek] O. Vasicek, *A note on using cross-sectional information in Bayesian estimation of security betas*, Journal of Finance (1973).

**Anwendung impliziter Renditen**

[Dam-impl] A. Damodaran, *Alternatives to the CAPM, Part 4: Market-Implied cost of equity* (Reverse-CAPM, Sektor-implizite Kapitalkosten) — https://aswathdamodaran.blogspot.com/2011/04/alternatives-to-capm-part-4-market.html ; *Equity Risk Premiums (ERP): Determinants, Estimation and Implications* — https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/ERP2022Formatted.pdf
[ECB18] EZB, *Measuring and interpreting the cost of equity in the euro area*, Economic Bulletin 4/2018 — https://www.ecb.europa.eu/press/economic-bulletin/articles/2018/html/ecb.ebart201804_02.en.html

**Regulatorischer Kontext (DE)**

[GT] Grant Thornton, *Neue WACC-Berechnung für Netzbetreiber* (NEST, 5. Periode) — https://www.grantthornton.de/themen/2025/aktuelle-entwicklungen-zur-eigenkapitalverzinsung-von-netzbetreibern-neue-wacc-berechnung-im-fokus/
[50H] *Wissenschaftliches Gutachten Methodik Eigenkapitalzinssatz Netzbetreiber* (50Hertz) — https://www.50hertz.com/xspProxy/api/staticfiles/50hertz-client/dokumente/transparenz/gutachten/wissenschaftliches_gutachten_methodik_eigenkapitalzinssatz_netzbetreiber.pdf
[Report 2] Report 2 dieses Sets (Randl/Zechner Peer-Group-Beta) · [Report 5] Report 5 (ECB-DDM-Marktrendite) · [Report 1] Report 1 (DMS) · [Report 4] Report 4 (Methodenvergleich).
