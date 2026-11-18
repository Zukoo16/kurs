from fastapi import APIRouter

from app.core.config import settings
from app.schemas.health import HealthRead

router = APIRouter(prefix="/api")


@router.get("/health", response_model=HealthRead)
def health() -> HealthRead:
    """Бірінші endpoint: сервер істеп тұрғанын көрсетеді (7-сабақ)."""
    return HealthRead(
        status="ok",
        environment=settings.ENVIRONMENT,
    )
