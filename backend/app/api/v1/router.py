from fastapi import APIRouter

from app.api.v1.endpoints import auth, health, llm

api_router = APIRouter()

api_router.include_router(health.router, tags=["Health"])
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication & Roles"])
api_router.include_router(llm.router, prefix="/llm", tags=["LLM (Ollama)"])

