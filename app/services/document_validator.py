MAX_FILE_SIZE = 10 * 1024 * 1024
PDF_SIGNATURE = b"%PDF-"


class EmptyDocumentError(Exception):
    pass


class DocumentTooLargeError(Exception):
    pass


class InvalidPdfError(Exception):
    pass


def validate_pdf(content: bytes) -> None:
    if not content:
        raise EmptyDocumentError("The uploaded file is empty.")

    if len(content) > MAX_FILE_SIZE:
        raise DocumentTooLargeError("The PDF cannot exceed 10 MB.")

    if not content.startswith(PDF_SIGNATURE):
        raise InvalidPdfError(
            "The uploaded file does not contain a valid PDF signature."
        )