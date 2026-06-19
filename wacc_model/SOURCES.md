# Quellen — WACC-Replikationsmodell

Primärquellen für die im Modell hinterlegten Parameter. **In der Bau-Umgebung
waren alle Behörden-/Gerichts-Hosts durch eine Egress-Firewall gesperrt
(HTTP 403)** — die Werte stammen daher aus quer-verifizierten WebSearch-Index-
inhalten dieser Dokumente. Zur finalen Verifikation die PDFs auf einem Rechner
ohne Egress-Beschränkung öffnen (bzw. `e-control.at`/`bundesnetzagentur.de` in
der Netzwerk-Policy der Umgebung freischalten).

## Deutschland — BNetzA

**Festlegungen (Aktenzeichen):**
- 3. Periode: BK4-16-160 (Strom), BK4-16-161 (Gas), Festlegung 05.10.2016
- 4. Periode: BK4-21-0055 (Strom), BK4-21-0056 (Gas), Festlegung 12.10.2021
- Übersicht EK-Zins: https://www.bundesnetzagentur.de/DE/Beschlusskammern/BK04/BK4_74_EK_Zins/BK4_Beschl_EK_Zins.html
- Pressemitteilung 20.10.2021: https://www.bundesnetzagentur.de/SharedDocs/Pressemitteilungen/DE/2021/20211020_EKZins.html

**Randl/Zechner/Frontier-Gutachten (MRP & Wagniszuschläge, Juli 2021):**
- https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Energie/Unternehmen_Institutionen/Netzentgelte/Anreizregulierung/Gutachten/GutachtenZuschlägeWagnisse.pdf
- Stehle MRP-Gutachten (April 2016, 3. Periode): https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Telekommunikation/Unternehmen_Institutionen/Marktregulierung/Massstaebe_Methoden/Kapitalkostensatz/Stehle_MRP-Gutachten_April_2016.pdf

**Gerichtsentscheidungen:**
- BGH-Pressemitteilung 09.07.2019 (3. Periode, EnVR 41/18 u. a.): https://www.bundesgerichtshof.de/SharedDocs/Pressemitteilungen/DE/2019/2019094.html
- OLG Düsseldorf 3 Kart 311/21 (30.08.2023, Gas): https://nrwe.justiz.nrw.de/olgs/duesseldorf/j2023/3_Kart_311_21_Beschluss_20230830.html
- OLG Düsseldorf 3 Kart 689/21 (30.08.2023, Strom): https://nrwe.justiz.nrw.de/olgs/duesseldorf/j2023/3_Kart_689_21_Beschluss_20230830.html

**Sekundär (Parameter im Klartext tabelliert):**
- NERA, Internationaler Vergleich EK-Zins (BDEW): https://www.bdew.de/media/documents/NERA_Internationaler_Vergleich_EK_Zins_Festlegungen.pdf
- BET/Seidel, Berechnung EK I/EK II (Formel-Detail): http://files.enreg.eu/2017/17_06_29_Workshop%20Energierecht/170629_BET_Vortrag_Berlin_EK_Zinsfestlegung__Seidel.pdf

## Österreich — E-Control (tokenisierte URLs; die bloßen `…/0/Datei.pdf` liefern 403)

**Gas-Fernleitung (Randl/Zechner):**
- 2019: https://www.e-control.at/documents/1785851/0/GutachtenRandlZechner20191103_KapitalkostenGasfernleitungsbetreiber+(3).pdf
- 2023: https://www.e-control.at/documents/1785851/1811582/Gutachten_WACC_Gas-Fernleitungsnetzbetreiber_RandlZechner_20231111.cleaned.pdf

**Kern-Gutachten & WACC-Updates (enthalten Beta, Peer Group, r_f, Debt Premium):**
- 02_3 Gutachten WACC (Core-Peer-Group, Asset-/Equity-Beta, MRP-Herleitung): https://www.e-control.at/documents/1785851/1811582/02_3_Gutachten+WACC+(1).pdf/d63ecd59-4f58-a87c-8bc0-50d5b038f4af?t=1668673987435
- RandlZechner Aktualisierung Stromübertragung (APG), 04.10.2022: https://www.e-control.at/documents/1785851/0/RandlZechner_AktualisierungGutachten_Stromübertragungsnetzbetreiber_20221004.pdf/62a9a8d4-b5f6-324c-d14e-6857e1a013c2?t=1670920549435
- Anlage 4 — WACC-Aktualisierung Strom-Verteilung (volle Parametertabelle): https://www.e-control.at/documents/1785851/0/Anlage_4_WACC_Aktualisierung.pdf/8d8f0d2c-418f-d2d6-eb23-d5c6946a5ae0?t=1699525703120
- WACC Neuinvestitionen 2025: https://www.e-control.at/documents/1785851/0/WACC_Neuinvestitionen_2025.pdf/8849f847-ca33-6622-7348-d80779b811cc?t=1732175305088
- 02c Annex Regulierungssystematik — WACC Neuinvestitionen 2024: https://www.e-control.at/documents/1785851/0/02c_Annex_zur_Regulierungssystematik_-_WACC_Neuinvestitionen24.pdf/d588479e-319d-fd85-be73-4a46713407e6?t=1701332279132
- Annex kleine VNB (5. RP): https://www.e-control.at/documents/1785851/0/Annex_kleine_VNB.pdf/2f49730b-9275-72b6-e951-b42d13a6e34a?t=1732175438275
- WACC Neuinvestitionen 2026 (Gas-/Stromverteiler + Stromübertragung): https://www.e-control.at/documents/1785851/1811582/20250903_Gasverteiler_Stromverteiler_Stromübertragung_WACC_Neuinvest.pdf

**Sekundär (AT-Parameter im Klartext):**
- AK FINGREEN-Studie (08.07.2025): https://wien.arbeiterkammer.at/interessenvertretung/wirtschaft/klimadialog/FINGREEN_Studie_20250708.pdf
- NERA WACC für Stromnetzbetreiber (VSE, 19.06.2024): https://www.strom.ch/de/media/14927/download
- Rödl & Partner, Neuer Regulierungsrahmen: https://www.roedl.com/insights/neuer-regulierungsrahmen-fuer-strom-und-gasnetzbetreiber/

## Zuordnung: welcher Wert aus welcher Tabelle

| Fehlender AT-Parameter | Dokument (s. o.) |
|---|---|
| Roh-/Asset-/Equity-Beta, Peer Group | 02_3 Gutachten WACC; Gas-FL 2019/2023 |
| risikoloser Zins (Bestand / Neuinvest je Jahr) | Anlage 4; WACC Neuinvestitionen 2025 |
| Debt Premium / FK-Kosten-Zerlegung | Anlage 4; WACC Neuinvestitionen 2025 |
| Inflationsannahme | Anlage 4; 02c Annex |
| Strom-Übertragung (APG) Detailwerte | RandlZechner Stromübertragung 04.10.2022 |
