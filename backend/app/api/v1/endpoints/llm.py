from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.core.security import UserPrincipal, get_current_user
from app.llm.client import ollama_client

router = APIRouter()


class GenerateRequest(BaseModel):
    prompt: str
    model: str | None = None
    temperature: float = 0.7


class GenerateResponse(BaseModel):
    prompt: str
    response: str
    model: str


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[ChatMessage]
    model: str | None = None


class ChatResponse(BaseModel):
    response: str


@router.post("/generate", response_model=GenerateResponse)
async def generate_text(
    request: GenerateRequest,
    user: UserPrincipal = Depends(get_current_user),
) -> GenerateResponse:
    """Жергілікті Ollama арқылы мәтін генерациялау (аутентификацияланған пайдаланушыларға)."""
    try:
        result = await ollama_client.generate(
            prompt=request.prompt,
            model=request.model,
            temperature=request.temperature,
        )
        return GenerateResponse(
            prompt=request.prompt,
            response=result,
            model=request.model or ollama_client.default_model,
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Ollama generation error: {str(exc)}")


@router.post("/chat", response_model=ChatResponse)
async def chat_completion(
    request: ChatRequest,
    user: UserPrincipal = Depends(get_current_user),
) -> ChatResponse:
    """Ollama арқылы диалогтік сұраныс өңдеу."""
    try:
        messages = [{"role": m.role, "content": m.content} for m in request.messages]
        result = await ollama_client.chat(messages=messages, model=request.model)
        return ChatResponse(response=result)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Ollama chat error: {str(exc)}")

