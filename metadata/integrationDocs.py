# descriptions API
integration_correlate_desc = "Correla i dati provenienti da robot, POS e gestionali"
integration_inventory_impact_desc = "Calcola l'impatto dell'inventario attuale sul flusso di cassa"
integration_inventory_optimization_desc = "Suggerisce ottimizzazioni dell'inventario basate sulle previsioni di flusso di cassa"

# parameters API
integration_correlate_params = {
    "dataSources": "Array di fonti dati da correlare",
    "correlationType": "Tipo di correlazione (inventario-vendite, vendite-flusso di cassa, ecc.)"
}

integration_inventory_impact_params = {
    "timeframe": "Periodo di analisi in giorni"
}

integration_inventory_optimization_params = {
    "cashConstraint": "Vincolo di liquidità",
    "priority": "Priorità (liquidità, vendite, margine)"
}


# response API
integration_correlate_response = "Risultati della correlazione con insights"
integration_inventory_impact_response = "Analisi dell'impatto dell'inventario sul flusso di cassa"
integration_inventory_optimization_response = "Raccomandazioni per l'ottimizzazione delle scorte"
