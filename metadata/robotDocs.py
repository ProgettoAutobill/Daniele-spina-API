# descriptions API
robot_control_desc = "Invia comandi di controllo al robot"
robot_images_desc = "Riceve le immagini catturate dalla telecamera del robot"
robot_recognition_desc = "Elabora le immagini per riconoscere i prodotti"
robot_status_desc = "Ottiene lo stato attuale del robot"
robot_schedule_desc = "Configura la pianificazione delle scansioni automatiche"

# parameters API
robot_control_params = {
    "command": "Tipo di comando (start_scan, stop_scan, return_to_base)",
    "zoneId": "ID della zona da scansionare",
    "priority": "Priorità del comando (alta, media, bassa)"
}

robot_images_params = {
    "imageData": "Dati dell'immagine (base64 o URL)",
    "timestamp": "Data e ora dell'acquisizione",
    "location": "Posizione del robot al momento dell'acquisizione",
    "metadata": "Metadati aggiuntivi (risoluzione, formato, ecc.)"
}

robot_recognition_params = {
    "imageId": "ID dell'immagine da elaborare",
    "recognitionMode": "Modalità di riconoscimento (rapida, accurata)"
}

robot_status_params = {
    "detailsLevel": "Livello di dettaglio (base, completo)"
}

robot_schedule_params = {
    "schedule": "Array di oggetti con orari e zone da scansionare",
    "priorityZones": "Zone con priorità di scansione più alta"
}

# response API
robot_control_response = "Conferma di ricezione del comando e stato del robot"
robot_images_response = "ID dell'immagine e stato dell'elaborazione"
robot_recognition_response = "Lista dei prodotti riconosciuti con quantità e livello di confidenza"
robot_status_response = "Stato del robot, posizione, livello batteria, attività corrente"
robot_schedule_response = "Conferma della pianificazione con prossime scansioni programmate"
