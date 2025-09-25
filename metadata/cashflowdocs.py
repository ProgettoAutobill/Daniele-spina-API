# descriptions API
cashflow_crunch_detection_desc = "Identifica potenziali crisi di liquidità"
cashflow_accounting_data_desc = "Aggiorna i dati contabili interni"

# parameters API
cashflow_crunch_detection_params = {
    "confidenceThreshold": "Soglia di confidenza (0.0-1.0)",
    "forecastHorizon": "Orizzonte di previsione in giorni"
}

cashflow_accounting_data_params = {
    "dataType": "Tipo di dati (fatture, ordini, prestiti)",
    "data": "Array di oggetti con i dati contabili"
}

# response API
cashflow_crunch_detection_response = "Dettagli sulle potenziali crisi di liquidità con date e probabilità"
cashflow_accounting_data_response = "Conferma di aggiornamento con statistiche"
