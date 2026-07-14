from typing import Literal
from uuid import UUID, uuid4

from fastapi import FastAPI, File, HTTPException, UploadFile, status
from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: Literal["ok"]


class DocumentResponse(BaseModel):
    id: UUID
    filename: str
    size_bytes: int
    content_type: str
    status: Literal["uploaded"]

from app.services.document_validator import (
    MAX_FILE_SIZE,
    DocumentTooLargeError,
    EmptyDocumentError,
    InvalidPdfError,
    validate_pdf,
)


app = FastAPI(
    title="Document Processing API",
    description="API for uploading and processing structured documents.",
    version="0.1.0",
)


@app.get(
    "/health",
    response_model=HealthResponse,
    tags=["Health"],
)
def health_check() -> HealthResponse:
    return HealthResponse(status="ok")


@app.post(
    "/documents",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Documents"],
)
async def upload_document(
    file: UploadFile = File(description="PDF document to process"),
) -> DocumentResponse:
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Only PDF documents are supported.",
        )

    content = await file.read(MAX_FILE_SIZE + 1)

    try:
        validate_pdf(content)
    except EmptyDocumentError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error
    except DocumentTooLargeError as error:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=str(error),
        ) from error
    except InvalidPdfError as error:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=str(error),
        ) from error

    return DocumentResponse(
        id=uuid4(),
        filename=file.filename or "unnamed.pdf",
        content_type=file.content_type,
        size_bytes=len(content),
        status="uploaded",
    )