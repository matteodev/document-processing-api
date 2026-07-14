from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel,Field


class HealthResponse(BaseModel):
    status: Literal["ok"] = Field(
        description="Current availability status of the API.",
        examples=["ok"],
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