import pytest

from app.services.document_validator import (
    EmptyDocumentError,
    InvalidPdfError,
    validate_pdf,
)


def test_empty_document_is_rejected() -> None:
    with pytest.raises(
        EmptyDocumentError,
        match="The uploaded file is empty.",
    ):
        validate_pdf(b"")


def test_valid_pdf_is_accepted() -> None:
    validate_pdf(b"%PDF-1.7")


def test_invalid_pdf_signature_is_rejected() -> None:
    with pytest.raises(
        InvalidPdfError,
        match="The uploaded file does not contain a valid PDF signature.",
    ):
        validate_pdf(b"This is not a PDF")