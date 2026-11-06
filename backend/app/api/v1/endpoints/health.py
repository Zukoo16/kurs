from typing import Dict
from fastapi import APIRouter
from app.llm.client import ollama_client

router = APIRouter()


@router.get("/health")
async def health_check() -> Dict[str, str]:
    """Сервер мен негізгі байланыстардың күйін тексеру."""
    ollama_ok = await ollama_client.check_health()
    return {
        "status": "healthy",
        "service": "backend",
        "ollama_available": "yes" if ollama_ok else "no",
    }
