from fastapi import FastAPI

from app.api.routes import documents, health


app = FastAPI(
    title="Document Processing API",
    description="API for uploading and processing structured documents.",
    version="0.1.0",
)

app.include_router(health.router)
app.include_router(documents.router)