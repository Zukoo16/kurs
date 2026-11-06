from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.config import settings


def create_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        version="1.0.0",
        description="FastAPI + PostgreSQL + SQLAlchemy 2 + Alembic + Keycloak OIDC + Ollama + Redis + RabbitMQ",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    # CORS баптаулары
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Негізгі API маршруттарын қосу
    application.include_router(api_router, prefix="/api/v1")

    @application.get("/", tags=["Root"])
    async def root():
        return {
            "project": settings.PROJECT_NAME,
            "status": "online",
            "docs": "/docs",
        }

    return application


app = create_application()

