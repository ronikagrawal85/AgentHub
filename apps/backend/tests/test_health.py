"""Tests for application configuration and HTTP foundation behavior."""

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from app.core.config import Settings
from app.main import create_app


def test_health_returns_ok(client: TestClient) -> None:
    response = client.get("/api/v1/health")

    assert response.status_code == 200


def test_health_returns_expected_schema(client: TestClient) -> None:
    response = client.get("/api/v1/health")

    assert response.json() == {
        "status": "healthy",
        "service": "AgentHub API",
        "version": "0.1.0",
    }


def test_application_and_health_use_overridden_settings() -> None:
    settings = Settings(
        app_name="Test AgentHub API",
        app_version="9.9.9",
        app_env="test",
        _env_file=None,
    )

    client = TestClient(create_app(settings))
    health_response = client.get("/api/v1/health")
    openapi_response = client.get("/openapi.json")

    assert health_response.json()["service"] == "Test AgentHub API"
    assert health_response.json()["version"] == "9.9.9"
    assert openapi_response.json()["info"]["title"] == "Test AgentHub API"
    assert openapi_response.json()["info"]["version"] == "9.9.9"


def test_openapi_specification_is_available(client: TestClient) -> None:
    response = client.get("/openapi.json")

    assert response.status_code == 200
    assert "/api/v1/health" in response.json()["paths"]


def test_unknown_endpoint_returns_not_found(client: TestClient) -> None:
    response = client.get("/api/v1/unknown")

    assert response.status_code == 404


def test_invalid_application_environment_is_rejected() -> None:
    with pytest.raises(ValidationError):
        Settings(app_env="invalid", _env_file=None)  # type: ignore[arg-type]


def test_environment_can_override_settings_without_env_file(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("APP_NAME", "Environment AgentHub API")
    monkeypatch.setenv("APP_VERSION", "2.0.0")
    monkeypatch.setenv("APP_ENV", "test")

    settings = Settings(_env_file=None)

    assert settings.app_name == "Environment AgentHub API"
    assert settings.app_version == "2.0.0"
    assert settings.app_env == "test"
