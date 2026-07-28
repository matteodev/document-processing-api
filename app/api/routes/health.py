from fastapi import APIRouter

from app.schemas.health import HealthResponse

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get(
    "",
    response_model=HealthResponse,
)
def health_check() -> HealthResponse:
    """
    Health check endpoint to verify that the API is running.
    """
    return HealthResponse(status="ok")
