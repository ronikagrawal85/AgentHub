"""Shared deterministic test fixtures."""

from os import environ

import pytest
from fastapi.testclient import TestClient

from app.core.config import Settings

# Establish deterministic values before importing the module-level ASGI application.
environ.update(
    {
        "APP_NAME": "AgentHub API",
        "APP_VERSION": "0.1.0",
        "APP_ENV": "test",
        "DEBUG": "false",
        "API_V1_PREFIX": "/api/v1",
    }
)


@pytest.fixture
def test_settings() -> Settings:
    """Create settings without reading a developer's local .env file."""
    return Settings(
        app_name="AgentHub API",
        app_version="0.1.0",
        app_env="test",
        debug=False,
        api_v1_prefix="/api/v1",
        _env_file=None,
    )


@pytest.fixture
def client(test_settings: Settings) -> TestClient:
    """Provide an isolated API client with explicit test settings."""
    from app.main import create_app

    return TestClient(create_app(test_settings))
