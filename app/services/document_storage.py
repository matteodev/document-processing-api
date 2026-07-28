from pathlib import Path
from uuid import UUID


PROJECT_ROOT = Path(__file__).resolve().parents[2] # Salgo di due cartelle per arrivare a APP
DOCUMENT_STORAGE_DIRECTORY = PROJECT_ROOT / "storage" / "documents"


def save_document(
    content: bytes,
    document_id: UUID,
    storage_directory: Path = DOCUMENT_STORAGE_DIRECTORY,
) -> Path:
    '''
    Save a document to the specified storage directory.
    If the storage directory does not exist, it will be created.
    The document will be saved with the name "{document_id}.pdf".
    '''
    storage_directory.mkdir(
        parents=True, # Crea anche eventuali cartelle superiori mancanti
        exist_ok=True, # Se esiste non da errori
    )

    document_path = storage_directory / f"{document_id}.pdf"
    document_path.write_bytes(content)

    return document_path