"""Typed application configuration loaded from environment variables."""

from functools import lru_cache
from typing import Literal

from pydantic import Field, SecretStr, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

AppEnvironment = Literal["development", "test", "staging", "production"]


class Settings(BaseSettings):
    """AgentHub API settings with safe, non-secret defaults."""

    app_name: str = "AgentHub API"
    app_version: str = "0.1.0"
    app_env: AppEnvironment = "development"
    debug: bool = False
    api_v1_prefix: str = "/api/v1"
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"
    cors_allowed_origins: list[str] = Field(
        default_factory=lambda: ["http://localhost:3000"]
    )
    cors_allow_credentials: bool = True
    database_url: SecretStr

    @model_validator(mode="after")
    def validate_cors_configuration(self) -> "Settings":
        """Prevent credentialed browser access from using a wildcard origin."""
        if self.cors_allow_credentials and "*" in self.cors_allowed_origins:
            raise ValueError(
                "CORS wildcard origins cannot be used when credentials are enabled"
            )
        return self

    model_config = SettingsConfigDict(
        env_prefix="AGENTHUB_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        frozen=True,
    )


@lru_cache
def get_settings() -> Settings:
    """Return a cached settings instance per process."""
    return Settings()
