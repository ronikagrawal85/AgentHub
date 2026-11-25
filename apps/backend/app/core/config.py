"""Typed application configuration loaded from environment variables."""

from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

AppEnvironment = Literal["development", "test", "staging", "production"]


class Settings(BaseSettings):
    """AgentHub API settings with safe, non-secret defaults."""

    app_name: str = "AgentHub API"
    app_version: str = "0.1.0"
    app_env: AppEnvironment = "development"
    debug: bool = False
    api_v1_prefix: str = "/api/v1"

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
