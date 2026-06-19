# Shiny-App: Beta-Varianten & implizite Marktrenditen ---------------------
# Start:  in R/RStudio das Verzeichnis oeffnen und "Run App", oder
#         shiny::runApp("r_app")
# Pakete: install.packages(c("shiny", "ggplot2"))
#
# Der Rechenkern liegt in calc.R; diese Datei kuemmert sich nur um UI/Server.

library(shiny)
library(ggplot2)

source("calc.R", local = TRUE)   # relativ zum App-Verzeichnis

# Beispieldaten einmal beim Start erzeugen.
returns0 <- make_example_returns()
peers0   <- example_peers()

pct  <- function(x, d = 2) ifelse(is.finite(x), sprintf(paste0("%.", d, "f%%"), 100 * x), "-")
peer_cols <- function(df) setdiff(names(df), c("date", "market"))

# --- UI ------------------------------------------------------------------
ui <- fluidPage(
  titlePanel("Eigenkapitalkosten: Beta-Varianten & implizite Marktrenditen"),
  p("Demo mit Beispieldaten (europaeische Netz-Peergroup). Methodik: Reports 5 und 6 im Repo."),

  tabsetPanel(
    # ---- Tab 1: implizite Marktrendite ----
    tabPanel(
      "Implizite Marktrendite",
      sidebarLayout(
        sidebarPanel(
          width = 3,
          helpText("Vier Modellansaetze auf Basis von Kurs + Analystenschaetzungen."),
          sliderInput("n_short", "Stufe 1 (Hochwachstum), Jahre", 1, 15, 5),
          sliderInput("n_trans", "Stufe 2 (Uebergang), Jahre", 0, 20, 10),
          numericInput("H", "H-Modell: H (halbe Uebergangsdauer)", 10, 0.5, 30, 0.5),
          numericInput("rf", "Risikofreier Zins (10J), %", 2.6, 0, 10, 0.1),
          radioButtons("weighting", "Marktgewichtung",
                       c("Marktkapitalisierung", "Gleichgewichtung")),
          checkboxInput("buybacks", "Buybacks in Netto-Auszahlungsrendite", TRUE),
          tags$hr(),
          fileInput("peerfile", "Eigene Peers (CSV) laden", accept = ".csv"),
          helpText("Spalten: name, price, dividend_yield, g_short, g_long,",
                   "buyback_yield, market_cap. Raten als Dezimalzahl (0.03 = 3%).")
        ),
        mainPanel(
          h4("Marktrendite je Modellansatz"),
          tableOutput("mkt_table"),
          plotOutput("mkt_plot", height = "320px"),
          h4("Implizite Rendite je Wertpapier"),
          tableOutput("peer_table")
        )
      )
    ),

    # ---- Tab 2: Beta-Varianten ----
    tabPanel(
      "Beta-Varianten",
      sidebarLayout(
        sidebarPanel(
          width = 3,
          selectInput("peer", "Netzbetreiber", peer_cols(returns0)),
          sliderInput("window", "Rollierendes Fenster (Wochen)", 26, 312, 104, step = 13),
          radioButtons("aggr", "Punktschaetzer der Reihe",
                       c("Mittelwert" = "mean", "Median" = "median", "Endpunkt" = "last")),
          tags$hr(),
          checkboxInput("excl", "Krisenfenster ausschliessen", FALSE),
          dateRangeInput("crisis", "Krisenfenster",
                         start = "2020-02-21", end = "2020-07-10"),
          numericInput("lags", "Dimson-Lags", 1, 0, 5),
          numericInput("prior_sd", "Vasicek-Prior-SD", 0.25, 0.05, 1, 0.05)
        ),
        mainPanel(
          h4("Beta-Varianten im Vergleich"),
          tableOutput("beta_table"),
          h4("Temporaer rollierendes Beta"),
          plotOutput("beta_plot", height = "360px"),
          helpText("Graue Flaeche = Krisenfenster; rote Linie = gewaehlter Punktschaetzer.")
        )
      )
    ),

    # ---- Tab 3: Daten & Methodik ----
    tabPanel(
      "Daten & Methodik",
      fluidRow(
        column(6,
          h4("Beispiel-Peers (Analystenschaetzungen)"),
          tableOutput("rawpeers")),
        column(6,
          h4("Beispiel-Renditen (Auszug)"),
          tableOutput("rawret"),
          br(),
          p(strong("Modellansaetze (implizite Marktrendite):"),
            "Gordon (einstufig), zweistufig, dreistufig (ECB-Standard), H-Modell."),
          p(strong("Beta-Varianten:"),
            "rollierendes OLS (Mittel/Median/Endpunkt), Vollzeitraum-OLS,",
            "krisenbereinigt, Blume, Vasicek, Dimson, implizites (reverse-CAPM) Beta."),
          p("Details: reports/05_ecb_market_return_ddm.md und",
            "reports/06_beta_und_implizite_renditen_deep-dive.md.")
        )
      )
    )
  )
)

# --- Server --------------------------------------------------------------
server <- function(input, output, session) {

  # Peers aus Upload oder Beispiel.
  peers <- reactive({
    if (is.null(input$peerfile)) return(peers0)
    df <- tryCatch(read.csv(input$peerfile$datapath, stringsAsFactors = FALSE),
                   error = function(e) NULL)
    validate(need(!is.null(df), "CSV konnte nicht gelesen werden."))
    if (is.null(df$g_long)) df$g_long <- 0.033
    if (is.null(df$buyback_yield)) df$buyback_yield <- 0
    df
  })

  impl <- reactive({
    implied_table(peers(), input$n_short, input$n_trans, input$H,
                  use_buybacks = input$buybacks)
  })

  weights <- reactive({
    if (input$weighting == "Gleichgewichtung")
      rep(1, nrow(peers())) else peers()$market_cap
  })

  mkt <- reactive(market_return(impl(), weights()))

  # Marktrendite-Tabelle (Rendite + ERP je Modell).
  output$mkt_table <- renderTable({
    rf <- input$rf / 100
    data.frame(
      Modell = names(mkt()),
      `Marktrendite` = pct(mkt()),
      `ERP (r - rf)` = pct(mkt() - rf),
      check.names = FALSE)
  }, striped = TRUE)

  output$mkt_plot <- renderPlot({
    rf <- input$rf / 100
    d <- data.frame(Modell = factor(names(mkt()), levels = names(mkt())),
                    r = as.numeric(mkt()))
    ggplot(d, aes(Modell, r, fill = Modell)) +
      geom_col(width = 0.65, show.legend = FALSE) +
      geom_hline(yintercept = rf, linetype = "dashed") +
      annotate("text", x = 0.7, y = rf, label = "rf", vjust = -0.5, size = 3.5) +
      geom_text(aes(label = pct(r)), vjust = -0.4, size = 4) +
      scale_y_continuous(labels = function(x) paste0(100 * x, "%")) +
      labs(x = NULL, y = "implizite Marktrendite") +
      theme_minimal(base_size = 13)
  })

  output$peer_table <- renderTable({
    t <- impl()
    data.frame(
      Name = t$Name,
      `Netto-Rendite` = pct(t$NettoRendite),
      Gordon = pct(t$Gordon), Zweistufig = pct(t$Zweistufig),
      Dreistufig = pct(t$Dreistufig), `H-Modell` = pct(t$`H-Modell`),
      check.names = FALSE)
  }, striped = TRUE)

  # ---- Beta-Tab ----
  ret <- reactive(returns0)   # (Upload liesse sich hier analog ergaenzen)

  beta_series <- reactive({
    df <- ret()
    roll <- rolling_beta(df[[input$peer]], df$market, input$window)
    roll$date <- df$date[roll$t]
    roll
  })

  output$beta_table <- renderTable({
    df <- ret()
    s  <- df[[input$peer]]; m <- df$market
    roll <- beta_series()

    # ggf. krisenbereinigt
    keep <- rep(TRUE, nrow(df))
    if (isTRUE(input$excl))
      keep <- !(df$date >= input$crisis[1] & df$date <= input$crisis[2])
    full <- ols_beta(s, m)
    excl <- ols_beta(s[keep], m[keep])

    data.frame(
      Variante = c("Rollierend (Mittel)", "Rollierend (Median)", "Rollierend (Endpunkt)",
                   "OLS Vollzeitraum", "OLS krisenbereinigt",
                   "Blume", "Vasicek", "Dimson"),
      Beta = sprintf("%.3f", c(
        summarise_rolling(roll, "mean"),
        summarise_rolling(roll, "median"),
        summarise_rolling(roll, "last"),
        full["beta"],
        excl["beta"],
        blume_adjust(full["beta"]),
        vasicek_adjust(full["beta"], full["se"], prior_sd = input$prior_sd),
        dimson_beta(s, m, input$lags))),
      check.names = FALSE)
  }, striped = TRUE)

  output$beta_plot <- renderPlot({
    roll <- beta_series()
    point <- summarise_rolling(roll, input$aggr)
    g <- ggplot(roll, aes(date, beta)) +
      geom_line(colour = "steelblue") +
      geom_hline(yintercept = point, colour = "firebrick", linetype = "dashed") +
      labs(x = NULL, y = paste0("rollierendes Beta (", input$window, " Wochen)")) +
      theme_minimal(base_size = 13)
    if (isTRUE(input$excl))
      g <- g + annotate("rect", xmin = input$crisis[1], xmax = input$crisis[2],
                        ymin = -Inf, ymax = Inf, alpha = 0.15)
    g
  })

  output$rawpeers <- renderTable(peers())
  output$rawret   <- renderTable(head(returns0, 8))
}

shinyApp(ui, server)
