# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned

- Document retrieval by UUID
- PDF text extraction
- Persistent document metadata
- API integration tests
- Docker support
- Continuous integration with GitHub Actions

## [0.1.0] - 2026-07-28

Initial public development release of Document Processing API.

### Added

#### API

- FastAPI application with a modular router-based architecture
- `GET /health` endpoint for application health checks
- `GET /info` endpoint for application name and version
- `POST /documents` endpoint for PDF uploads
- Automatic OpenAPI schema generation
- Interactive Swagger UI and ReDoc documentation

#### Document validation

- MIME type validation for PDF uploads
- Empty-document validation
- Maximum upload size of 10 MB
- PDF binary signature validation using the `%PDF-` header
- Custom exceptions for each document-validation failure
- HTTP error mapping for invalid uploads

#### Document storage

- UUID generation for uploaded documents
- Local PDF storage using UUID-based filenames
- Automatic creation of the storage directory
- Separation between validation, storage and HTTP routing
- Exclusion of uploaded documents from Git version control

#### Data models

- Pydantic response models
- Structured document metadata responses
- UUID, filename, MIME type, file size and upload status fields

#### Testing

- Unit tests with pytest
- Tests for empty documents
- Tests for valid PDF signatures
- Tests for invalid PDF signatures
- Tests for documents exceeding the size limit
- Isolated storage tests using pytest temporary directories

#### Developer experience

- Python 3.13 project configuration
- Dependency and virtual-environment management with uv
- Reproducible dependencies through `uv.lock`
- Ruff linting and formatting configuration
- Modern FastAPI parameter declaration using `Annotated`
- Type hints across services, routes and schemas
- Function documentation through Python docstrings

#### Documentation

- English and Italian project documentation
- Local installation and execution instructions
- API endpoint reference
- Testing and code-quality commands
- Current validation limitations
- Project roadmap

[Unreleased]: https://github.com/matteodev/document-processing-api/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/matteodev/document-processing-api/releases/tag/v0.1.0