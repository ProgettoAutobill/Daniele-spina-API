# descriptions API
erp_connect_desc = "Stabilisce una connessione con il gestionale aziendale"
erp_accounting_desc = "Importa dati contabili dal gestionale"
erp_import_inventory_desc = "Importa dati di inventario dal gestionale"
erp_sync_desc = "Sincronizza i dati tra il sistema di previsione e il gestionale"
erp_mapping_desc = "Configura la mappatura tra i campi del gestionale e quelli del sistema"
erp_import_entities_desc = "Importa dati su clienti e fornitori dal gestionale"
erp_sync_status_desc = "Monitora lo stato delle sincronizzazioni con i gestionali"

# parameters API
erp_connect_params = {
    "erpType": "Tipo di gestionale (SAP, Oracle, Zucchetti, ecc.)",
    "connectionParams": "Parametri di connessione (URL, credenziali, ecc.)",
    "syncFrequency": "Frequenza di sincronizzazione dei dati"
}

erp_accounting_params = {
    "dataType": "Tipo di dati (fatture, ordini, pagamenti)",
    "startDate": "Data di inizio periodo",
    "endDate": "Data di fine periodo"
}

erp_import_inventory_params = {
    "warehouseId": "ID del magazzino (opzionale)",
    "product_Category": "Categoria di prodotti (opzionale)"
}

erp_sync_params = {
    "syncDirection": "Direzione della sincronizzazione (import, export, bidirectional)",
    "dataModules": "Array di moduli da sincronizzare"
}

erp_mapping_params = {
    "erpType": "Tipo di gestionale",
    "entityType": "Tipo di entità (cliente, fornitore, prodotto, ecc.)",
    "fieldMappings": "Oggetto con le mappature dei campi"
}

erp_import_entities_params = {
    "entityType": "Tipo di entità (cliente, fornitore)",
    "status": "Stato (attivo, inattivo)"
}

erp_sync_status_params = {
    "syncId": "ID della sincronizzazione (opzionale)",
    "status": "Filtra per stato (in corso, completato, fallito)"
}

# response API
erp_connect_response = "Stato della connessione e token di autenticazione"
erp_accounting_response = "Dati contabili importati e statistiche di sincronizzazione"
erp_import_inventory_response = "Dati di inventario importati e statistiche"
erp_sync_response = "Risultati della sincronizzazione con dettagli per ogni modulo"
erp_mapping_response = "Stato della configurazione della mappatura"
erp_import_entities_response = "Dati delle entità importate con statistiche di pagamento"
erp_sync_status_response = "Stato dettagliato delle sincronizzazioni con timestamp e log"
