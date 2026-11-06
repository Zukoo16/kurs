from typing import Any, Dict, List, Optional

from app.core.config import settings


class OllamaClient:
    """Жергілікті Ollama LLM серверімен өзара әрекеттесу клиенті."""

    def __init__(self, base_url: Optional[str] = None, default_model: Optional[str] = None):
        self.base_url = (base_url or settings.OLLAMA_BASE_URL).rstrip("/")
        self.default_model = default_model or settings.OLLAMA_MODEL

    async def generate(self, prompt: str, model: Optional[str] = None, temperature: float = 0.7) -> str:
        """Мәтіндік генерация жасау (/api/generate)."""
        import httpx

        target_model = model or self.default_model
        payload = {
            "model": target_model,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": temperature},
        }

        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(f"{self.base_url}/api/generate", json=payload)
            response.raise_for_status()
            data = response.json()
            return data.get("response", "")

    async def chat(self, messages: List[Dict[str, str]], model: Optional[str] = None) -> str:
        """Чат форматында сұраныс жолдау (/api/chat)."""
        import httpx

        target_model = model or self.default_model
        payload = {
            "model": target_model,
            "messages": messages,
            "stream": False,
        }

        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(f"{self.base_url}/api/chat", json=payload)
            response.raise_for_status()
            data = response.json()
            message = data.get("message", {})
            return message.get("content", "")

    async def check_health(self) -> bool:
        """Ollama серверінің қолжетімділігін тексеру."""
        try:
            import httpx

            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get(f"{self.base_url}/api/tags")
                return response.status_code == 200
        except Exception:
            return False


ollama_client = OllamaClient()
