# Methodisches Kapitel: Erweiterungen der Beta-Schätzung und Anwendung impliziter Renditen

*Stand Juni 2026. Dieses Kapitel ist die formale, vertiefende Methoden­darstellung zu [Report 6](06_beta_und_implizite_renditen_methodische_erweiterungen.md) (Überblick) und schließt an [Report 2](02_randl_zechner_peer_groups.md) (Peer-Group-Beta) und [Report 5](05_ecb_market_return_ddm.md) (DDM-Marktrendite) an. Es spezifiziert jede Erweiterung mit Schätzgleichung, statistischen Eigenschaften, Parameterwahl und einem reproduzierbaren Schätzprotokoll. Lauffähige Bausteine: [`../code/beta_tools.py`](../code/beta_tools.py) und [`../code/ddm_engine.py`](../code/ddm_engine.py).*

---

## 1. Gegenstand, Notation und Überblick

Die Eigenkapitalkosten werden im regulatorischen CAPM als

$$k_i = r_f + \beta_i \cdot \mathrm{MRP}, \qquad \mathrm{MRP} = \mathbb{E}[r_m] - r_f$$

bestimmt. Der **Risikofaktor** $\beta_i$ und die **Marktrisikoprämie** (MRP) sind die beiden empirisch umstrittenen Größen. Dieses Kapitel behandelt zwei Stränge:

- **Teil I (Kap. 3–9): Beta-Schätzung.** Ausgehend vom statischen Mehrfenster-OLS (Status quo des Gutachtens) werden das **temporär rollierende Beta**, **zeitvariable/bedingte** Modelle, die Behandlung **temporärer Verzerrungen**, **Mikrostruktur-Korrekturen**, **Adjustierungen** und das **De-/Re-Levering** formal entwickelt.
- **Teil II (Kap. 10): Anwendung impliziter Renditen.** Die DDM-implizite Marktrendite (Report 5) wird als MRP-Quelle, als Basis eines **reverse-CAPM-impliziten Betas** und als Bestandteil eines **zeitkonsistenten Kapitalkosten-Panels** verwendet.

**Notation.** $r_{i,t}$ = (Über-)Rendite des Peers $i$ in Periode $t$; $r_{m,t}$ = Marktrendite (Referenzindex); $r_{f,t}$ = risikofreier Zins; $W$ = Fensterlänge (in Beobachtungen); $T$ = Stichprobenlänge; $D,E$ = Markt­werte von Fremd-/Eigenkapital, $L=D/(D+E)$ = Verschuldungsgrad; $\tau$ = Steuersatz; $\beta_A,\beta_E,\beta_D$ = Asset-, Equity-, Debt-Beta. Renditen werden, sofern nicht anders vermerkt, als **diskrete (einfache) Total-Return-Renditen** verstanden.

---

## 2. Datengrundlage und Renditekonstruktion

Bevor irgendein Beta geschätzt wird, sind fünf Konstruktionsentscheidungen festzulegen, die das Ergebnis materiell beeinflussen:

1. **Total Return vs. Kursrendite.** Betas sind auf **Total-Return-Basis** (inkl. reinvestierter Dividenden) zu schätzen, da das CAPM Gesamt­renditen modelliert. Reine Kursindizes verzerren das Beta dividendenstarker Netzwerte systematisch.
2. **Renditedefinition.** Einfache Rendite $r_t = P_t/P_{t-1}-1$ vs. log-Rendite $\ln(P_t/P_{t-1})$. Für Beta-Regressionen sind beide gebräuchlich; Konsistenz über Peer und Index ist entscheidend.
3. **Frequenz.** Täglich (viele Beobachtungen, aber Mikrostruktur-/Nichthandels­rauschen → Kap. 7), wöchentlich (Rausch­reduktion, Standard im Gutachten), monatlich (geringstes Rauschen, kleinste $T$). Die Frequenz ist eine **Robustheitsachse**, keine Punktentscheidung.
4. **Referenzindex.** Lokal (Heimatindex), regional (Euro Stoxx) oder global (FTSE All-World, so das Gutachten). Die Indexwahl verschiebt das Beta-Niveau; sie ist offenzulegen und zu plausibilisieren.
5. **Synchronisierung/Währung.** Renditen über Märkte hinweg auf eine gemeinsame Handelskalender- und Währungsbasis bringen; asynchrone Schlusskurse erzeugen Scheinkorrelationen (→ Dimson, Kap. 7).

Alle nachfolgenden Schätzer setzen ein sauberes, synchronisiertes Renditepanel $\{r_{i,t}, r_{m,t}\}_{t=1}^{T}$ voraus.

---

## 3. Ausgangspunkt: statisches OLS-Beta (Mehrfenster)

Das Gutachten schätzt je Peer und Fensterlänge $W\in\{1\text{J},3\text{J},5\text{J}\}$ zum Stichtag $T$ das **Roh-Beta** per OLS:

$$\hat\beta_i \;=\; \frac{\sum_{t=T-W+1}^{T}(r_{i,t}-\bar r_i)(r_{m,t}-\bar r_m)}{\sum_{t=T-W+1}^{T}(r_{m,t}-\bar r_m)^2} \;=\; \frac{\widehat{\mathrm{Cov}}(r_i,r_m)}{\widehat{\mathrm{Var}}(r_m)}.$$

Der Standardfehler ist $\mathrm{se}(\hat\beta_i)=\hat\sigma_\varepsilon/\sqrt{\sum (r_{m,t}-\bar r_m)^2}$ mit $\hat\sigma_\varepsilon^2$ = Residualvarianz. **Drei strukturelle Schwächen** motivieren die Erweiterungen (Kap. 4–6): (i) **Stichtagsabhängigkeit** — der Schätzer hängt am Endpunkt $T$; (ii) **Konstanzannahme** — $\beta_i$ wird innerhalb $W$ als konstant unterstellt; (iii) **Rückwärtsgerichtetheit** — Strukturbrüche (z. B. Regulierungs­reform) werden nicht antizipiert.

---

## 4. Das temporär rollierende Beta

### 4.1 Definition

Statt das Beta nur zum Endpunkt $T$ über mehrere $W$ zu schätzen, wird **eine** Fensterlänge $W$ mit Schrittweite $h$ (meist $h=1$) **durch die Zeit geschoben**. Für jeden Endpunkt $t\ge W$ gilt

$$\boxed{\;\hat\beta_t \;=\; \frac{\sum_{s=t-W+1}^{t}(r_{i,s}-\bar r_{i,t})(r_{m,s}-\bar r_{m,t})}{\sum_{s=t-W+1}^{t}(r_{m,s}-\bar r_{m,t})^2}\;,\qquad t=W,W+h,\dots,T\;}$$

mit fensterlokalen Mittelwerten $\bar r_{i,t},\bar r_{m,t}$. Ergebnis ist eine **Beta-Zeitreihe** $\{\hat\beta_t\}$ samt rollierendem Standardfehler $\{\mathrm{se}(\hat\beta_t)\}$ — *nicht* eine einzelne Zahl. „Temporär rollierend" bezeichnet exakt diese wandernde Endpunktschätzung (Umsetzung: `beta_tools.rolling_beta`).

### 4.2 Aggregation zum regulatorischen Punktschätzer

Aus der Trajektorie wird der Festlegungswert abgeleitet — bewusst **nicht** als Endpunktwert $\hat\beta_T$, sondern als Lagemaß über den Referenzzeitraum $\mathcal{T}$:

$$\hat\beta^{\text{roll}} \;=\; \underbrace{\frac{1}{|\mathcal{T}|}\sum_{t\in\mathcal{T}}\hat\beta_t}_{\text{Trailing-Average}} \quad\text{oder}\quad \mathrm{median}_{t\in\mathcal{T}}\,\hat\beta_t \quad\text{oder}\quad \frac{\sum_t w_t\hat\beta_t}{\sum_t w_t}$$

mit z. B. zeitlich abnehmenden Gewichten $w_t$ (jüngere Fenster höher) oder Präzisionsgewichten $w_t=1/\mathrm{se}(\hat\beta_t)^2$. Der **Median** ist robust gegen einzelne Krisen-Spikes; der Trailing-Average ist der in der UK-Praxis übliche Wert (`beta_tools.summarise_rolling`).

### 4.3 Statistische Eigenschaften und Fensterwahl

Die Fensterlänge $W$ steuert einen **Bias-Varianz-Trade-off**. Bei wahrhaft zeitvariablem $\beta_t$ approximiert das rollierende OLS den lokalen Mittelwert; der mittlere quadratische Fehler zerfällt schematisch in

$$\mathrm{MSE}(W) \;\approx\; \underbrace{\Big(\tfrac{1}{W}\!\!\sum_{s\in\text{Fenster}}\!\!(\beta_s-\bar\beta)\Big)^2}_{\text{Glättungs-Bias }\uparrow W} \;+\; \underbrace{\frac{\sigma_\varepsilon^2}{\sum_s (r_{m,s}-\bar r_m)^2}}_{\text{Schätzvarianz }\downarrow W}.$$

- **Kurzes $W$:** reagibel, geringer Bias bei schnellen Niveauwechseln, aber hohe Varianz (verrauschte Reihe).
- **Langes $W$:** glatt, geringe Varianz, aber träge — verschleift echte Strukturbrüche.

Regulatorisch gebräuchlich sind $W\in\{2\text{J},5\text{J}\}$ (wöchentlich: $W\approx104,260$). Die Wahl ist als Sensitivität über mehrere $W$ und Frequenzen darzustellen.

### 4.4 Überlappung und Inferenz

Rollierende Fenster überlappen stark ($h\ll W$); die Reihe $\{\hat\beta_t\}$ ist daher **hoch autokorreliert**. Für Inferenz auf Aggregaten (z. B. Konfidenzband des Trailing-Average) sind HAC-Standardfehler nach **Newey–West** zu verwenden:

$$\hat\sigma^2_{\text{NW}} = \hat\gamma_0 + 2\sum_{j=1}^{q}\Big(1-\tfrac{j}{q+1}\Big)\hat\gamma_j,$$

mit Autokovarianzen $\hat\gamma_j$ der Reihe und Lag-Truncation $q$ (Faustregel $q\approx\lfloor 4(T/100)^{2/9}\rfloor$ oder $q\approx W$). Naive Standardfehler unterschätzen die Unsicherheit massiv.

### 4.5 Bezug zur internationalen Praxis

Die UK-Regulierer (UKRN/Ofgem/Ofwat/CMA) implementieren genau dieses Verfahren als **rolling-OLS-Matrix**: rollierende Regressionen über die Frequenzen {täglich, wöchentlich, monatlich} **gekreuzt** mit Fenstern {1, 2, 5, (10) Jahre} für einen Comparator-Pool; der Punktschätzer ist ein Querschnitts- und Zeit­durchschnitt über diese Matrix [UKRN18][UKRN23]. Der deutsche Mehrfenster-Ansatz ist der Spezialfall mit **einem** Endpunkt.

| | 1 J | 2 J | 5 J | 10 J |
|---|---|---|---|---|
| **täglich** | β̄ | β̄ | β̄ | β̄ |
| **wöchentlich** | β̄ | β̄ | β̄ | β̄ |
| **monatlich** | β̄ | β̄ | β̄ | β̄ |

*Jede Zelle: Trailing-Average der rollierenden Betas; der Festlegungswert ist ein gewichtetes Mittel über die Matrix.*

---

## 5. Zeitvariable und bedingte Beta-Modelle

Das rollierende OLS gewichtet alle Fensterbeobachtungen gleich und unterstellt lokale Konstanz. Die folgenden Modelle modellieren die Zeitvariation **explizit**.

### 5.1 State-Space-/Kalman-Filter (Random-Walk-Beta)

**Mess- und Zustandsgleichung:**

$$\begin{aligned}
\text{Messung:}\quad & r_{i,t} = \alpha_t + \beta_t\, r_{m,t} + \varepsilon_t, & \varepsilon_t &\sim \mathcal N(0,\sigma_\varepsilon^2),\\
\text{Zustand:}\quad & \beta_t = \beta_{t-1} + \eta_t, & \eta_t &\sim \mathcal N(0,\sigma_\eta^2).
\end{aligned}$$

(optional $\alpha_t$ ebenfalls als Random Walk). Die **Filter-Rekursion** liefert die bedingte Beta-Schätzung $\beta_{t|t}$:

$$\begin{aligned}
\text{Prädiktion:}\quad & \beta_{t|t-1}=\beta_{t-1|t-1}, \quad P_{t|t-1}=P_{t-1|t-1}+\sigma_\eta^2,\\
\text{Prognosefehler:}\quad & v_t = r_{i,t}-\alpha-\beta_{t|t-1}r_{m,t}, \quad F_t = r_{m,t}^2 P_{t|t-1}+\sigma_\varepsilon^2,\\
\text{Kalman-Gain:}\quad & K_t = P_{t|t-1}\,r_{m,t}/F_t,\\
\text{Update:}\quad & \beta_{t|t}=\beta_{t|t-1}+K_t v_t, \quad P_{t|t}=(1-K_t r_{m,t})P_{t|t-1}.
\end{aligned}$$

Die Hyperparameter $(\sigma_\varepsilon^2,\sigma_\eta^2)$ — bzw. das **Signal-Rausch-Verhältnis** $q=\sigma_\eta^2/\sigma_\varepsilon^2$, das die Glätte steuert ($q\to0$ ⇒ konstantes Beta) — werden per **Maximum-Likelihood** über die Prediction-Error-Decomposition geschätzt:

$$\ell(\sigma_\varepsilon^2,\sigma_\eta^2) = -\tfrac12\sum_{t}\Big(\ln 2\pi F_t + v_t^2/F_t\Big).$$

Für die *retrospektive* Festlegung ist die **geglättete** Schätzung $\beta_{t|T}$ (Rauch–Tung–Striebel-Smoother) der gefilterten vorzuziehen, da sie die volle Stichprobe nutzt; für *prognostische* Zwecke die gefilterte $\beta_{t|t}$. In Prognosevergleichen dominiert der Kalman-Filter häufig GARCH-Spezifikationen [Zhang17][FaffBrooks].

### 5.2 Bedingtes Beta aus DCC-GARCH

Modelliere die bedingten Varianzen univariat (z. B. GARCH(1,1)) und die bedingte Korrelation dynamisch (Engle 2002):

$$\sigma_{j,t}^2=\omega_j+a_j r_{j,t-1}^2+b_j\sigma_{j,t-1}^2,\quad z_{j,t}=r_{j,t}/\sigma_{j,t},\quad j\in\{i,m\};$$
$$Q_t=(1-a-b)\bar Q + a\,z_{t-1}z_{t-1}^\top + b\,Q_{t-1},\quad R_t=\mathrm{diag}(Q_t)^{-1/2}Q_t\,\mathrm{diag}(Q_t)^{-1/2}.$$

Das **bedingte Beta** ist dann

$$\beta_t \;=\; \frac{\mathrm{Cov}_t(r_i,r_m)}{\mathrm{Var}_t(r_m)} \;=\; \rho_{im,t}\,\frac{\sigma_{i,t}}{\sigma_{m,t}},$$

mit $\rho_{im,t}$ aus $R_t$. Varianten: **BEKK** (direkte Parametrisierung der bedingten Kovarianzmatrix), **DCC-MIDAS** (langfristige Korrelations­komponente). DCC-Betas sind hoch reagibel, aber parameter- und annahmen­intensiv.

### 5.3 Regimewechsel (kurz)

**Markov-Switching-Betas** ($\beta_t=\beta_{S_t}$ mit latentem Zustand $S_t\in\{1,\dots,K\}$ und Übergangsmatrix) modellieren diskrete Regime (Normal vs. Krise) statt glatter Variation — konzeptionell die Brücke zu Kap. 6.

### 5.4 Regulatorische Einordnung

Transparenz und Replizierbarkeit sprechen im Festlegungskontext für das **rollierende OLS als Hauptverfahren**; Kalman/DCC dienen der **Validierung** der Zeitvariation und der Regime-Identifikation. Entscheidend ist die **methodische Konsistenz**: Ein reagibles bedingtes Beta erfordert eine ebenso zeitnah gemessene MRP (Kap. 10.3), sonst entsteht ein Methodenbruch.

---

## 6. Behandlung temporärer (transitorischer) Verzerrungen

Energieversorger-Betas wurden durch **COVID-2020** und die **Energiekrise 2022** vorübergehend verschoben. Die rollierende Reihe macht solche **Spikes** sichtbar; ihre Behandlung muss verzerrungsfrei und regelgebunden erfolgen.

### 6.1 Strukturbruch-Diagnose

- **Chow-Test** auf bekannten Bruchzeitpunkt $t_0$: $F=\frac{(\mathrm{RSS}_r-\mathrm{RSS}_u)/k}{\mathrm{RSS}_u/(T-2k)}$.
- **CUSUM**/CUSUM-of-squares auf rekursiven Residuen für unbekannte Brüche.
- **Bai–Perron** für multiple endogene Bruchpunkte.

### 6.2 Korrekturansätze

1. **Dummy-Variablen-Regression** (transparenteste Variante):
$$r_{i,t}=\alpha+\beta\,r_{m,t}+\gamma\,D_t^{\text{Krise}}+\delta\,(D_t^{\text{Krise}}\!\cdot r_{m,t})+\varepsilon_t,$$
   wobei $\beta$ das „Normalregime"-Beta und $\beta+\delta$ das Krisen-Beta misst; $D_t^{\text{Krise}}$ ist **ex ante** zu definieren.
2. **Regelbasierter Fensterausschluss** der Krisenperiode (`beta_tools.exclude_window`) — nur mit vorab fixierten, symmetrischen Kriterien.
3. **Robuste Schätzung** (Huber-/M-Schätzer, $\beta^{\text{rob}}=\arg\min_\beta\sum_t\rho\big((r_{i,t}-\beta r_{m,t})/\hat s\big)$ mit beschränkter Einflussfunktion $\psi=\rho'$), die Extremtage automatisch herabgewichtet (De-Spiking).
4. **Vasicek-Shrinkage** (Kap. 8.2) dämpft Schätzextreme ohnehin.

### 6.3 Caveat

Jede Krisenbereinigung ist ein manipulationsanfälliger Eingriff. Sie muss **regelgebunden, symmetrisch und vorab dokumentiert** sein — andernfalls droht Ergebnis-Cherry-Picking. Der weite Beurteilungsspielraum der BNetzA (bestätigt durch OLG Düsseldorf/BGH, [Report 3]) erhöht die Anforderung an eine *nachvollziehbare Regel*.

---

## 7. Mikrostruktur-Korrekturen (Nichthandel/asynchroner Handel)

Bei weniger liquiden Peers erzeugt asynchroner Handel ein **nach unten verzerrtes** Beta.

**Dimson (1979), Methode der aggregierten Koeffizienten:** Regression auf zeitversetzte Marktrenditen und Summe der Koeffizienten,

$$r_{i,t}=\alpha+\sum_{k=-n}^{+n}\beta_k\,r_{m,t+k}+\varepsilon_t,\qquad \beta_i^{\text{Dimson}}=\sum_{k=-n}^{+n}\hat\beta_k$$

(Umsetzung: `beta_tools.dimson_beta`). **Scholes–Williams (1977)** als Alternative:

$$\beta_i^{\text{SW}}=\frac{\hat\beta_{-1}+\hat\beta_{0}+\hat\beta_{+1}}{1+2\hat\rho_m},$$

mit $\hat\rho_m$ = Autokorrelation erster Ordnung der Marktrendite. Beide heben die Nichthandels­dämpfung auf; relevant, weil das Liquiditätsfilter des Gutachtens (Report 2, §3) genau solche Verzerrungen vermeiden soll, kleinere TSO-Peers aber betroffen sein können. Höhere Frequenz (täglich) verschärft das Problem; eine Korrektur ist dort am wichtigsten.

---

## 8. Adjustierung Roh → adjustiert

### 8.1 Blume (1971) / Bloomberg-Adjusted

Empirische Mean Reversion der Betas zum Marktwert 1, geschätzt als Querschnitts­regression $\beta_{i,t+1}=a+b\,\beta_{i,t}+u_i$; mit den klassischen Werten $a\approx0{,}33,\,b\approx0{,}67$:

$$\beta_i^{\text{Blume}}=0{,}67\,\hat\beta_i+0{,}33\cdot 1$$

(= Bloomberg-Adjusted-Beta; `beta_tools.blume_adjust`).

### 8.2 Vasicek (1973) — bayesianische Schrumpfung

Optimale **präzisionsgewichtete** Mischung aus Roh-Beta und Prior $\bar\beta$ (Prior­varianz $\sigma_{\bar\beta}^2$):

$$\boxed{\;\beta_i^{\text{Vasicek}} = w_i\,\hat\beta_i + (1-w_i)\,\bar\beta,\qquad w_i=\frac{1/\mathrm{se}(\hat\beta_i)^2}{1/\mathrm{se}(\hat\beta_i)^2+1/\sigma_{\bar\beta}^2}\;}$$

Präzise geschätzte Betas (kleines $\mathrm{se}$) werden **weniger** geschrumpft — der entscheidende Unterschied zu Blumes uniformem Gewicht. Das Gutachten verwendet Vasicek (`beta_tools.vasicek_adjust`). Bei rollierender Schätzung kann $w_t$ und damit die Schrumpfung **je Fenster** variieren.

---

## 9. De-/Re-Levering (Asset-Beta ↔ Equity-Beta)

Equity-Betas werden je Peer auf **Asset-Betas** entschuldet, gemittelt und auf die regulatorische Notional-Struktur wiederverschuldet.

**Mit Steuern und Debt-Beta** (allgemeine Form):

$$\beta_E=\beta_A+(\beta_A-\beta_D)\,(1-\tau)\,\frac{D}{E}\quad\Longleftrightarrow\quad \beta_A=\frac{\beta_E+\beta_D\,(1-\tau)\,\tfrac{D}{E}}{1+(1-\tau)\,\tfrac{D}{E}}.$$

Spezialfälle: **Hamada** mit $\beta_D=0$ ⇒ $\beta_E=\beta_A[1+(1-\tau)D/E]$; **Harris–Pringle** (steuerfrei, $\tau=0$) ⇒ $\beta_E=\beta_A+(\beta_A-\beta_D)D/E$. Die methodisch identischen E-Control-Berichte rechnen **ohne Debt-Beta** ($\beta_D=0$) auf 40 % Eigenkapitalbasis; der Debt-Beta-Ansatz des deutschen Gutachtens ist unbestätigt ([Report 2-Deep-Dive]). **Konsistenz mit der rollierenden Schätzung:** Wird $\beta_{E,t}$ zeitvariabel geschätzt, muss auch der Verschuldungsgrad $D_t/E_t$ (Marktwerte!) zeitvariabel verwendet werden, da das Entschuldungs­ergebnis sonst inkonsistent wird.

---

## 10. Teil II: Anwendung der impliziten Renditen

Report 5 leitet aus dem ECB-Mehrstufen-DDM die **vorwärtsgerichtete** Marktrendite $r_{m}^{\text{impl}}$ (implizite Eigenkapitalrendite des Index) und die implizite Prämie $\mathrm{ERP}^{\text{impl}}=r_m^{\text{impl}}-r_f$ ab. Diese Größen sind **zeitvariabel** und stehen dem historischen MRP (Stehle/DMS, Report 1) gegenüber.

### 10.1 Implizite MRP als Input/Cross-Check

Die implizite MRP plausibilisiert oder ersetzt teilweise den historischen MRP im CAPM. Üblich ist ein **Blending** (Ofgem gewichtet historische und implizite Total-Market-Return-Schätzer etwa gleich, Report 4):

$$\mathrm{MRP}^{\text{reg}}=\lambda\,\mathrm{MRP}^{\text{hist}}+(1-\lambda)\,\mathrm{ERP}^{\text{impl}},\qquad \lambda\in[0,1].$$

Im Kontext der **TMR-Stabilität** dient die implizite Größe primär als Test, *ob* die (bewusst stabil gehaltene) TMR-Annahme noch trägt — nicht als mechanischer Jahres-Input.

### 10.2 Reverse-CAPM-implizites (forward-looking) Beta

Berechne je Peer die DDM-implizite Eigenkapitalrendite $k_i^{\text{impl}}$ (Report 5/`ddm_engine`) und **invertiere das CAPM**:

$$\boxed{\;\beta_i^{\text{impl}}=\frac{k_i^{\text{impl}}-r_f}{r_m^{\text{impl}}-r_f}\;}$$

Das ist ein **preisbasiertes, regressionsunabhängiges** Beta (`beta_tools.implied_beta`). Anwendungen:

- **Cross-Check** zu den (rollierenden) Regressions-Betas: große Abweichungen signalisieren Strukturbruch oder Fehlbewertung.
- **Sektor-implizite Kapitalkosten** (Damodaran): DDM-implizites $k$ auf den **gesamten** Netz-Peer-Index angewandt und allen Netzbetreibern zugewiesen — das Einzel-Beta wird dann nicht benötigt [Dam-impl]. Dies ist die ECB-Logik auf Sektorebene.
- **Aggregation** der peer-impliziten Betas (Mittel/Median) als forward-looking Gegenstück zum 0,81-Equity-Beta.

### 10.3 Zeitkonsistentes Kapitalkosten-Panel

Die anspruchsvollste Anwendung koppelt beide Stränge:

$$k_{i,t}=r_{f,t}+\beta_{i,t}\cdot\mathrm{ERP}_t,$$

mit rollierendem/bedingtem $\beta_{i,t}$ (Teil I) und impliziter $\mathrm{ERP}_t$ (Report 5). **Drei Konsistenzbedingungen:**

1. **Keine Doppelzählung der Zeitvariation.** Steigen in der Krise $\beta_{i,t}$ **und** $\mathrm{ERP}_t$ zugleich, überschießt $k_{i,t}$. Designentscheidung nötig: stabiles Beta × zeitvariable MRP *oder* umgekehrt — nicht beides unreflektiert „voll" zeitvariabel.
2. **Periodenkonsistenz.** Beta-Fenster, MRP-Horizont und $r_{f,t}$ über konsistente Konventionen (Frequenz, Zeitraum, nominal/real).
3. **Zirkularität.** $\beta_i^{\text{impl}}$ und $\mathrm{ERP}^{\text{impl}}$ speisen sich aus Analystenprognosen (IBES) — kein erwartungsunabhängiger Anker; Optimismus-Bias offenlegen (Report 5, §6).

**Prozyklizitäts-Kernvorbehalt.** Voll zeitvariable, marktimplizite zulässige Renditen schwankten mit der Marktstimmung — was Regulierer vermeiden. Daher die **Dämpfungsmechanismen**: gleitende Durchschnitte des risikofreien Zinses (BNetzA: 10-Jahres-Umlaufsrendite), stabiler TMR, Vasicek-Shrinkage, Trailing-Average der rollierenden Betas. Implizite Renditen und reagible Betas sind in der Regulierung primär **Cross-Checks**, nicht der mechanische Festlegungsinput.

---

## 11. Reproduzierbares Schätzprotokoll

Schritt-für-Schritt, mit Verweis auf [`../code/beta_tools.py`](../code/beta_tools.py):

1. **Daten** aufbereiten: Total-Return-Renditen, gewählte Frequenz, synchronisiert, gemeinsame Währung (Kap. 2).
2. **Rollierendes Beta** je Peer über die Frequenz×Fenster-Matrix schätzen → `rolling_beta`; HAC-Inferenz beachten (Kap. 4.4).
3. **Krisenfenster** regelbasiert behandeln (Dummy/Ausschluss/robust) → `exclude_window` (Kap. 6).
4. **Mikrostruktur** prüfen/korrigieren (bei täglichen Daten/illiquiden Peers) → `dimson_beta` (Kap. 7).
5. **Aggregieren** zum Punktschätzer (Trailing-Average/Median) → `summarise_rolling` (Kap. 4.2).
6. **Adjustieren** (Vasicek bevorzugt; Blume als Vergleich) → `vasicek_adjust`/`blume_adjust` (Kap. 8).
7. **De-/Re-Levering** auf Notional-Struktur (Debt-Beta-Annahme explizit) (Kap. 9).
8. **Validieren** mit State-Space/DCC-Beta (Zeitvariation) und mit dem **impliziten Beta** → `implied_beta` (Kap. 5, 10.2).
9. **Kapitalkosten** zusammensetzen, ggf. als Panel $k_{i,t}$ mit Dämpfung (Kap. 10.3).
10. **Sensitivitäten** dokumentieren (Kap. 12).

---

## 12. Sensitivitäts- und Robustheitsachsen

Jede Festlegung sollte über folgende Achsen variiert und tabelliert werden: **Frequenz** (täglich/wöchentlich/monatlich) · **Fensterlänge** $W$ · **Aggregator** (Mittel/Median/gewichtet) · **Krisenbehandlung** (mit/ohne) · **Adjustierung** (roh/Blume/Vasicek) · **Mikrostruktur** (mit/ohne Dimson) · **Referenzindex** (lokal/global) · **Debt-Beta** ($0$/positiv) · **MRP-Quelle** (historisch/implizit/Blend) · **$\lambda$** im Blending. Die Streuung über diese Achsen ist das ehrlichste Maß der Parameter-Unsicherheit.

---

## 13. Grenzen und Fallstricke

- **Überlappungs-Autokorrelation** ⇒ ohne HAC zu enge Konfidenzbänder (Kap. 4.4).
- **Look-ahead-Bias** bei geglätteten (Smoother-)Betas in prognostischen Anwendungen — nur gefilterte Werte verwenden (Kap. 5.1).
- **Krisenbereinigung** ist manipulationsanfällig; nur regelgebunden (Kap. 6.3).
- **Implizite Größen** erben Analysten-Optimismus und Wachstumsannahmen (Kap. 10.3).
- **Prozyklizität** voll zeitvariabler Kapitalkosten — Dämpfung ist Feature, nicht Bug.
- **Debt-Beta- und Gearing-Annahmen** treiben das Re-Levering stark; offenzulegen (Kap. 9).

---

## Quellen

**Rollierende/zeitvariable Beta-Ökonometrie**

[UKRN18] UK Regulators Network, *Estimating the cost of capital for implementation of price controls* (2018) — https://ukrn.org.uk/app/uploads/2018/06/2018-CoE-Study.pdf
[UKRN23] UKRN, *Cost of Capital — guidance* (22.03.2023) — https://ukrn.org.uk/app/uploads/2023/03/CoC-guidance_22.03.23.pdf
[Zhang17] Zhang et al., *Forecasting the Daily Time-Varying Beta … GARCH vs. Kalman Filter*, J. Forecasting (2017) — https://onlinelibrary.wiley.com/doi/10.1002/for.2442
[FaffBrooks] Faff, Hillier & Hillier, *Forecasting the weekly time-varying beta of UK firms: GARCH vs. Kalman filter*, Eur. J. Finance 15(4).
[Engle02] R. Engle, *Dynamic Conditional Correlation*, J. Business & Economic Statistics (2002).
[NW87] Newey & West, *A Simple, Positive Semi-Definite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix*, Econometrica (1987).
[BaiPerron] Bai & Perron, *Estimating and Testing Linear Models with Multiple Structural Changes*, Econometrica (1998).

**Mikrostruktur, Adjustierung, Levering**

[Dimson79] E. Dimson, *Risk measurement when shares are subject to infrequent trading*, J. Financial Economics (1979).
[SW77] Scholes & Williams, *Estimating betas from nonsynchronous data*, J. Financial Economics (1977).
[Blume71] M. Blume, *On the assessment of risk*, J. Finance (1971).
[Vasicek73] O. Vasicek, *A note on using cross-sectional information in Bayesian estimation of security betas*, J. Finance (1973).
[Hamada72] R. Hamada, *The effect of the firm's capital structure on the systematic risk of common stocks*, J. Finance (1972). [HP85] Harris & Pringle (1985).

**Anwendung impliziter Renditen / regulatorischer Kontext**

[Dam-impl] A. Damodaran, *Alternatives to the CAPM, Part 4: Market-Implied cost of equity* — https://aswathdamodaran.blogspot.com/2011/04/alternatives-to-capm-part-4-market.html ; *Equity Risk Premiums (ERP) 2022* — https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/ERP2022Formatted.pdf
[ECB18] EZB, *Measuring and interpreting the cost of equity in the euro area*, Economic Bulletin 4/2018 — https://www.ecb.europa.eu/press/economic-bulletin/articles/2018/html/ecb.ebart201804_02.en.html
[GT] Grant Thornton, *Neue WACC-Berechnung für Netzbetreiber (NEST)* — https://www.grantthornton.de/themen/2025/aktuelle-entwicklungen-zur-eigenkapitalverzinsung-von-netzbetreibern-neue-wacc-berechnung-im-fokus/
[Report 1–6] Berichts-Set dieses Repositoriums (Querverweise im Text).
