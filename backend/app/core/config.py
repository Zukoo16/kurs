import os

try:
    from pydantic_settings import BaseSettings, SettingsConfigDict

    class Settings(BaseSettings):
        PROJECT_NAME: str = "AIDD Platform"
        ENVIRONMENT: str = "development"
        SECRET_KEY: str = "supersecret_default_key"

        # Database (PostgreSQL)
        POSTGRES_SERVER: str = "localhost"
        POSTGRES_PORT: int = 5432
        POSTGRES_DB: str = "app_db"
        POSTGRES_USER: str = "app_user"
        POSTGRES_PASSWORD: str = "app_secure_password"
        DATABASE_URL: str = "postgresql+asyncpg://app_user:app_secure_password@localhost:5432/app_db"

        # Keycloak (OIDC)
        KEYCLOAK_URL: str = "http://localhost:8080"
        KEYCLOAK_REALM: str = "aidd-realm"
        KEYCLOAK_CLIENT_ID: str = "aidd-backend"
        KEYCLOAK_CLIENT_SECRET: str = "client_secret"

        # Ollama (Local LLM)
        OLLAMA_BASE_URL: str = "http://localhost:11434"
        OLLAMA_MODEL: str = "llama3.2"

        # Redis Cache
        REDIS_URL: str = "redis://localhost:6379/0"

        # RabbitMQ
        RABBITMQ_HOST: str = "localhost"
        RABBITMQ_PORT: int = 5672
        RABBITMQ_USER: str = "guest"
        RABBITMQ_PASSWORD: str = "guest"
        RABBITMQ_QUEUE: str = "aidd_tasks"

        # CORS
        CORS_ORIGINS: list[str] = ["*"]

        model_config = SettingsConfigDict(
            env_file=".env",
            env_file_encoding="utf-8",
            extra="ignore",
        )

except ImportError:
    # Python standard library fallback (пакеттер толық орнатылмаған жеңіл орта үшін)
    from dataclasses import dataclass, field

    @dataclass
    class Settings:
        PROJECT_NAME: str = os.getenv("PROJECT_NAME", "AIDD Platform")
        ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
        SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecret_default_key")

        POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
        POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", "5432"))
        POSTGRES_DB: str = os.getenv("POSTGRES_DB", "app_db")
        POSTGRES_USER: str = os.getenv("POSTGRES_USER", "app_user")
        POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "app_secure_password")
        DATABASE_URL: str = os.getenv(
            "DATABASE_URL",
            "postgresql+asyncpg://app_user:app_secure_password@localhost:5432/app_db",
        )

        KEYCLOAK_URL: str = os.getenv("KEYCLOAK_URL", "http://localhost:8080")
        KEYCLOAK_REALM: str = os.getenv("KEYCLOAK_REALM", "aidd-realm")
        KEYCLOAK_CLIENT_ID: str = os.getenv("KEYCLOAK_CLIENT_ID", "aidd-backend")
        KEYCLOAK_CLIENT_SECRET: str = os.getenv("KEYCLOAK_CLIENT_SECRET", "client_secret")

        OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama3.2")

        REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")

        RABBITMQ_HOST: str = os.getenv("RABBITMQ_HOST", "localhost")
        RABBITMQ_PORT: int = int(os.getenv("RABBITMQ_PORT", "5672"))
        RABBITMQ_USER: str = os.getenv("RABBITMQ_USER", "guest")
        RABBITMQ_PASSWORD: str = os.getenv("RABBITMQ_PASSWORD", "guest")
        RABBITMQ_QUEUE: str = os.getenv("RABBITMQ_QUEUE", "aidd_tasks")

        CORS_ORIGINS: list[str] = field(default_factory=lambda: ["*"])


settings = Settings()
