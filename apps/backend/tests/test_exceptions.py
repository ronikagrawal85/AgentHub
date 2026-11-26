"""Tests for the API's global exception handling contract."""

import pytest
from fastapi import Query
from fastapi.testclient import TestClient

from app.core.config import Settings
from app.main import create_app


def test_http_exception_uses_standard_error_envelope(client: TestClient) -> None:
    response = client.get("/api/v1/unknown")

    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "http_404",
            "message": "Not Found",
            "details": None,
        }
    }


def test_request_validation_error_includes_structured_details() -> None:
    application = create_app(Settings(app_env="test", _env_file=None))

    @application.get("/test-validation")
    def validation_endpoint(limit: int = Query(ge=1)) -> dict[str, int]:
        return {"limit": limit}

    client = TestClient(application)
    response = client.get("/test-validation", params={"limit": 0})

    assert response.status_code == 422
    body = response.json()
    assert body["error"]["code"] == "request_validation_error"
    assert body["error"]["message"] == "Request validation failed"
    assert body["error"]["details"][0]["loc"] == ["query", "limit"]


def test_unhandled_exception_returns_safe_error_and_is_logged(
    caplog: pytest.LogCaptureFixture,
) -> None:
    application = create_app(Settings(app_env="test", _env_file=None))

    @application.get("/test-failure")
    def failure_endpoint() -> None:
        raise RuntimeError("sensitive internal failure")

    client = TestClient(application, raise_server_exceptions=False)

    with caplog.at_level("ERROR", logger="app.core.exceptions"):
        response = client.get("/test-failure")

    assert response.status_code == 500
    assert response.json() == {
        "error": {
            "code": "internal_server_error",
            "message": "An unexpected error occurred",
            "details": None,
        }
    }
    assert "sensitive internal failure" not in response.text
    assert "Unhandled API exception" in caplog.text
