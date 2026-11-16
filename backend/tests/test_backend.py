from app.core.config import settings
from app.core.security import UserPrincipal, extract_roles_from_token
from app.llm.client import OllamaClient


def test_settings_load():
    assert settings.PROJECT_NAME == "AIDD Platform"
    assert settings.OLLAMA_MODEL is not None
    assert "postgresql" in settings.DATABASE_URL


def test_extract_roles_from_token():
    mock_claims = {
        "realm_access": {"roles": ["student", "default-roles-aidd"]},
        "resource_access": {
            settings.KEYCLOAK_CLIENT_ID: {"roles": ["teacher"]}
        },
    }
    roles = extract_roles_from_token(mock_claims)
    assert "student" in roles
    assert "teacher" in roles


def test_user_principal_has_role():
    user = UserPrincipal(
        user_id="user-123",
        username="alibek",
        email="alibek@example.com",
        roles=["student"],
    )
    assert user.has_role("student") is True
    assert user.has_role("admin") is False


def test_ollama_client_init():
    client = OllamaClient(base_url="http://localhost:11434", default_model="llama3.2")
    assert client.base_url == "http://localhost:11434"
    assert client.default_model == "llama3.2"

