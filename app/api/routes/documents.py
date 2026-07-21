from uuid import uuid4

from fastapi import APIRouter, File, HTTPException, UploadFile, status

from app.schemas.document import DocumentResponse

from app.services.document_storage import save_document

from app.services.document_validator import (
    MAX_FILE_SIZE,
    DocumentTooLargeError,
    EmptyDocumentError,
    InvalidPdfError,
    validate_pdf,
)


router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post(
    "",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED,
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
    
    # Salvataggio
    document_id = uuid4()
    save_document(content, document_id)

    return DocumentResponse(
        id=document_id,
        filename=file.filename or "unnamed.pdf",
        content_type=file.content_type,
        size_bytes=len(content),
        status="uploaded",
    )