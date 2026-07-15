# Document Processing API

A document-processing REST API built with Python and FastAPI.

The project is being developed as a practical, production-oriented path for learning modern Python backend development, API design, automated testing and software architecture.

> The project is currently under active development.

## English

### Current features

- API health-check endpoint
- Application information endpoint
- PDF upload through `multipart/form-data`
- MIME type validation
- Maximum file-size validation
- PDF signature validation
- Structured responses with Pydantic
- Custom validation exceptions
- Automatic OpenAPI documentation
- Unit tests with pytest
- Modular separation between routes, schemas and services

### Technology stack

- Python 3.13
- FastAPI
- Pydantic
- pytest
- uv

### Project structure

```text
app/
├── api/
│   └── routes/
│       ├── documents.py
│       ├── health.py
│       └── info.py
├── schemas/
│   ├── document.py
│   ├── health.py
│   └── info.py
├── services/
│   └── document_validator.py
└── main.py

tests/
└── test_document_validator.py
```

### Available endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Checks whether the API is available |
| `GET` | `/info` | Returns application name and version |
| `POST` | `/documents` | Uploads and validates a PDF document |

### Run locally

#### Requirements

- Git
- uv

Clone the repository:

```bash
git clone <repository-url>
cd document-processing-api
```

Install the required Python version and synchronize dependencies:

```bash
uv python install 3.13
uv sync
```

Start the development server:

```bash
uv run fastapi dev app/main.py
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Alternative ReDoc documentation:

```text
http://127.0.0.1:8000/redoc
```

### Run the tests

```bash
uv run python -m pytest -v
```

### Example response

A successful PDF upload currently returns:

```json
{
  "id": "2cdf130f-2434-4e44-b0a4-8e81ba53d173",
  "filename": "policy.pdf",
  "content_type": "application/pdf",
  "size_bytes": 124805,
  "status": "uploaded"
}
```

### Current validation

Uploaded documents are checked for:

- `application/pdf` MIME type
- non-empty content
- maximum size of 10 MB
- `%PDF-` binary signature

These checks are an initial validation layer and do not replace complete document integrity checks or malware scanning.

### Roadmap

- Local document persistence
- PDF text extraction
- Structured insurance-document data extraction
- PostgreSQL integration
- Database migrations
- Authentication and authorization
- Background processing
- API integration tests
- Docker support
- Continuous integration with GitHub Actions
- Deployment on AWS
- Logging and monitoring

---

## Italiano

### Descrizione

Document Processing API è un servizio REST sviluppato con Python e FastAPI per il caricamento, la validazione e la futura elaborazione di documenti PDF.

Il progetto nasce come percorso pratico e orientato a un caso reale per approfondire lo sviluppo backend con Python, la progettazione di API, i test automatici e l’architettura software.

> Il progetto è attualmente in fase di sviluppo.

### Funzionalità attuali

- endpoint per verificare lo stato dell’API;
- endpoint con le informazioni dell’applicazione;
- caricamento di PDF tramite `multipart/form-data`;
- validazione del MIME type;
- controllo della dimensione massima;
- verifica della firma binaria del PDF;
- risposte strutturate con Pydantic;
- eccezioni di validazione personalizzate;
- documentazione OpenAPI automatica;
- unit test con pytest;
- separazione modulare tra route, schemi e servizi.

### Endpoint disponibili

| Metodo | Endpoint | Descrizione |
|---|---|---|
| `GET` | `/health` | Verifica che il servizio sia disponibile |
| `GET` | `/info` | Restituisce nome e versione dell’applicazione |
| `POST` | `/documents` | Riceve e valida un documento PDF |

### Avvio locale

Clonare il repository:

```bash
git clone <repository-url>
cd document-processing-api
```

Installare Python e sincronizzare le dipendenze:

```bash
uv python install 3.13
uv sync
```

Avviare il server di sviluppo:

```bash
uv run fastapi dev app/main.py
```

La documentazione interattiva sarà disponibile all’indirizzo:

```text
http://127.0.0.1:8000/docs
```

### Esecuzione dei test

```bash
uv run python -m pytest -v
```

### Obiettivi futuri

Le prossime fasi includeranno:

- salvataggio dei documenti;
- estrazione del testo dai PDF;
- estrazione strutturata dei dati assicurativi;
- integrazione con PostgreSQL;
- autenticazione;
- elaborazione in background;
- test di integrazione;
- Docker e GitHub Actions;
- deploy e monitoraggio su AWS.

## Project status

This project is under active development and is intended for educational and portfolio purposes.