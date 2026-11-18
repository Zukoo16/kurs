from pydantic import BaseModel


class HealthRead(BaseModel):
    """GET /api/health жауабының пішімі (7-сабақ)."""

    status: str
    environment: str
