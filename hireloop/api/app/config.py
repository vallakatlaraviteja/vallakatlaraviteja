"""Application configuration loaded from environment via Pydantic Settings."""

from __future__ import annotations

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Strongly-typed environment configuration."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore", case_sensitive=False)

    # --- Owner (single-user mode) ---
    owner_email: str = Field(..., description="Email of the single owner of this instance.")
    owner_name: str = "Owner"
    session_secret: str = Field(..., min_length=16)

    # --- Database ---
    database_url: str
    database_sync_url: str

    # --- Redis ---
    redis_url: str = "redis://redis:6379/0"

    # --- AI providers ---
    anthropic_api_key: str = ""
    anthropic_model: str = "claude-sonnet-4-5-20250929"
    openai_api_key: str = ""
    openai_embed_model: str = "text-embedding-3-large"

    # --- App ---
    environment: str = "local"
    log_level: str = "INFO"
    sentry_dsn: str = ""
    cors_origins: str = "http://localhost:3000"

    @property
    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]


@lru_cache
def get_settings() -> Settings:
    """Cached settings accessor — call from FastAPI deps or modules."""
    return Settings()  # type: ignore[call-arg]
