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

MAX_FILE_SIZE = 10 * 1024 * 1024
PDF_SIGNATURE = b"%PDF-"


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

    if not content:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The uploaded file is empty.",
        )

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="The PDF cannot exceed 10 MB.",
        )

    if not content.startswith(PDF_SIGNATURE):
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="The uploaded file does not contain a valid PDF signature.",
        )

    return DocumentResponse(
        id=uuid4(),
        filename=file.filename or "unnamed.pdf",
        content_type=file.content_type,
        size_bytes=len(content),
        status="uploaded",
    )