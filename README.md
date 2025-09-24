# Backend Python SmartAPI
Backend per la gestione integrata del flusso di cassa (SMARTCASH) e dell'inventario (SMARTINVENTORY): offre API e strumenti per la raccolta, l'analisi e la visualizzazione dei dati finanziari e di magazzino di attività commerciali.

## Requisiti
- Python 3.x (testato con 3.13)
- Docker e Docker Compose
- PostgreSQL (gestito tramite Docker)

## Avvio rapido

### 1. Clona il repository
```bash
git clone <repository-url>
cd module
```

### 2. Setup database e ambiente virtuale
Su Linux/macOS (nel percorso del progetto):
```bash
chmod +x setup_database.sh
./setup_database.sh
```

Su Windows (non testato):
```bash
# Avvia PostgreSQL
docker-compose up -d postgres

# Crea ambiente virtuale
python -m venv venv
venv\Scripts\activate  # Windows

pip install -r requirements.txt

# Crea tabelle database
python python -m database.sessionDB
```

### 3. Avvia il server
Su Linux/macOS:
```bash
# Attiva ambiente virtuale se non già attivo
source /home/$(whoami)/virtualenvs/smartapi/bin/activate
```

Su Windows:
```bash
# Attiva ambiente virtuale se non già attivo
venv\Scripts\activate
```

# Avvia FastAPI server
```bash
python app.py
```

### 4. Popola il database con dati di esempio (opzionale)
```bash
python src/repository/testRepository.py
```

## Funzionalità principali

### Gestione Backend Integrata
- **Autenticazione e Autorizzazione**: Sistema completo per gestione utenti, ruoli e permessi
- **Gestione Entità Business**: Clienti, fornitori, collaboratori con contratti e relazioni
- **Ubicazioni e Sedi**: Gestione di multiple location aziendali con dipendenti associati

### SMARTCASH - Gestione Flusso di Cassa
- **Voci di Entrata**: Ricavi da vendite, entrate finanziarie, rimborsi
- **Voci di Uscita**: Costi operativi, tasse, marketing, utilities, personale, acquisti
- **Transazioni Merci**: Tracking completo di acquisti, vendite e resi con associazione prodotti
- **Analisi Finanziarie**: Reportistica avanzata con filtri temporali e categoriali

### SMARTINVENTORY - Gestione Inventario
- **Catalogo Prodotti**: Gestione completa di prodotti fisici e digitali con attributi estesi
- **Tracciamento Giacenze**: Monitoraggio real-time delle scorte per location
- **Categorie e Classificazioni**: Sistema gerarchico di categorizzazione prodotti
- **Movimenti di Magazzino**: Registrazione automatica di entrate, uscite e trasferimenti

### Integrazione e API
- **API REST**: Endpoints completi per tutte le funzionalità CRUD
- **Frontend Ready**: Integrazione ottimizzata con Svelte e framework moderni
- **Database PostgreSQL**: Persistenza sicura e scalabile con relazioni ottimizzate

### Sviluppo e Testing
- **Generazione Dati Test**: Script automatici per popolamento database di sviluppo
- **Environment Docker**: Setup completo con PostgreSQL containerizzato
- **Documentazione Tecnica**: Specifiche complete di database e API

## Struttura del progetto
- `app.py`: Entry-point backend che espone le API FastAPI e comunica con il front-end
- `src/database/`: Modelli SQLAlchemy e configurazione database PostgreSQL
  - `table.py`: Definizioni di tutte le tabelle e relazioni ORM
  - `create_database.py`: Script per creazione database e tabelle
- `src/repository/`: Repository pattern per accesso dati e script di test
- `src/utils/`: Funzioni di utilità (date, analisi dati, ecc.)
- `docker-compose.yml`: Configurazione servizi Docker (PostgreSQL)
- `DATABASE_STRUCTURE.md`: Documentazione tecnica completa del database
- `setup_database.sh`: Script automatico per setup completo dell'ambiente
- `requirements.txt`: Dipendenze Python del progetto

## Convenzioni per la stesura del codice

### Naming e Stile
- **Lingue**: Nomi di variabili, metodi e classi in inglese. Commenti preferibilmente in inglese (eccezioni per documentazione tecnica/normativa italiana)
- **Visibilità**: Attributi/metodi privati preceduti da underscore (`_`), pubblici senza prefisso
- **Type Annotations**: Sempre utilizzare annotazioni di tipo per parametri e valori di ritorno
- **Nesting**: Evitare nesting delle funzioni per maggiore leggibilità e manutenibilità

### Import e Moduli
- **Percorsi assoluti**: Sempre specificare percorso completo (es. `from src.database.table import Base`)
- **Evitare**: Import relativi (`from .module`) e wildcard (`from module import *`)
- **Ordine import**:
  1. Moduli interni del progetto
  2. Librerie di terze parti (SQLAlchemy, FastAPI, ecc.)
  3. Libreria standard Python
- **Sorting**: Ordine alfabetico all'interno di ogni gruppo

### Dipendenze e Compatibilità
- **Python**: Compatibilità con Python 3.x (testato con 3.13)
- **Database**: PostgreSQL con SQLAlchemy ORM (no MongoDB per dati relazionali)
- **Pandas**: Evitare l'uso di pandas per garantire compatibilità tra versioni Python, ridurre dipendenze esterne e gestire più efficacemente grandi quantità di dati
- **Performance**: Preferire strutture dati native Python (list, dict) e librerie lightweight
- **Portabilità**: Codice funzionante su Linux/macOS/Windows