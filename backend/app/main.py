from fastapi import FastAPI

from app.core.config import settings
from app.routers import health

app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

app.include_router(health.router)
