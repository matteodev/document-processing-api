from pathlib import Path
from uuid import uuid4

from app.services.document_storage import save_document


def test_document_is_saved(tmp_path: Path) -> None:
    """
    Test that a document is saved correctly to the specified storage directory.
    """
    content = b"%PDF-1.7 test content"
    document_id = uuid4()

    saved_path = save_document(
        content=content,
        document_id=document_id,
        storage_directory=tmp_path,
    )

    assert saved_path == tmp_path / f"{document_id}.pdf"
    assert saved_path.exists()
    assert saved_path.read_bytes() == content
