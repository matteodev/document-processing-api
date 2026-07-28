from fastapi import APIRouter

from app.schemas.info import InfoResponse

router = APIRouter(
    prefix="/info",
    tags=["Info"],
)


@router.get(
    "",
    response_model=InfoResponse,
)
def get_info() -> InfoResponse:
    """
    Get basic information about the API, including its name and version.
    """
    return InfoResponse(
        name="Document Processing API",
        version="0.1.0",
    )
