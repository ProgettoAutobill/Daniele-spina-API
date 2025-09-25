# descriptions API
pos_connect_desc = "Stabilisce una connessione con il sistema POS"
pos_transactions_desc = "Importa le transazioni dal sistema POS"
pos_products_sync_desc = "Sincronizza i dati dei prodotti tra il sistema e il POS"
pos_sales_analysis_desc = "Ottiene analisi delle vendite dal sistema POS"


# parameters API
pos_connect_params = {
    "posType": "Tipo di POS (marca e modello)",
    "connectionParams": "Parametri di connessione",
    "storeId": "ID del negozio"
}

pos_transactions_params = {
    "startDate": "Data di inizio periodo",
    "endDate": "Data di fine periodo",
    "transactionType": "Tipo di transazione (vendita, reso, ecc.)"
}

pos_products_sync_params = {
    "syncDirection": "Direzione della sincronizzazione (import, export, bidirectional)",
    "productCategories": "Categorie di prodotti da sincronizzare"
}

pos_sales_analysis_params = {
    "timeframe": "Periodo di analisi (giornaliero, settimanale, mensile)",
    "productCategory": "Categoria di prodotti (opzionale)",
    "storeId": "ID del negozio (opzionale)"
}

# response API
pos_connect_response = "Stato della connessione e token di autenticazione"
pos_transactions_response = "Dati delle transazioni importate con statistiche"
pos_products_sync_response = "Risultati della sincronizzazione con dettagli"
pos_sales_analysis_response = "Dati di analisi delle vendite con trend e statistiche"


