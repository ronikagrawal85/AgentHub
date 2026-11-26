"""Tests for CORS, correlation IDs, and structured logging."""

import json
import logging
from uuid import UUID

from fastapi.testclient import TestClient

from app.core.logging import JsonFormatter, reset_correlation_id, set_correlation_id


def test_response_echoes_valid_correlation_id(client: TestClient) -> None:
    correlation_id = "58e8fa1c-e149-4d5f-bbad-3b0b03fb33d5"

    response = client.get(
        "/api/v1/health",
        headers={"X-Correlation-ID": correlation_id},
    )

    assert response.headers["X-Correlation-ID"] == correlation_id


def test_invalid_correlation_id_is_replaced(client: TestClient) -> None:
    response = client.get(
        "/api/v1/health",
        headers={"X-Correlation-ID": "untrusted-value"},
    )

    generated_id = response.headers["X-Correlation-ID"]
    assert str(UUID(generated_id)) == generated_id


def test_cors_preflight_allows_configured_origin(client: TestClient) -> None:
    response = client.options(
        "/api/v1/health",
        headers={
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "GET",
        },
    )

    assert response.status_code == 200
    assert response.headers["Access-Control-Allow-Origin"] == "http://localhost:3000"
    assert response.headers["Access-Control-Allow-Credentials"] == "true"


def test_cors_preflight_rejects_unconfigured_origin(client: TestClient) -> None:
    response = client.options(
        "/api/v1/health",
        headers={
            "Origin": "https://untrusted.example",
            "Access-Control-Request-Method": "GET",
        },
    )

    assert response.status_code == 400
    assert "Access-Control-Allow-Origin" not in response.headers


def test_json_formatter_includes_correlation_and_request_fields() -> None:
    correlation_id = "62103d47-f80a-4121-aa82-a5048de49d65"
    token = set_correlation_id(correlation_id)
    try:
        record = logging.LogRecord(
            name="agenthub.test",
            level=logging.INFO,
            pathname=__file__,
            lineno=1,
            msg="HTTP request completed",
            args=(),
            exc_info=None,
        )
        record.method = "GET"
        record.path = "/api/v1/health"
        record.status_code = 200
        record.duration_ms = 1.25

        payload = json.loads(JsonFormatter().format(record))
    finally:
        reset_correlation_id(token)

    assert payload["level"] == "INFO"
    assert payload["message"] == "HTTP request completed"
    assert payload["correlation_id"] == correlation_id
    assert payload["method"] == "GET"
    assert payload["path"] == "/api/v1/health"
    assert payload["status_code"] == 200
    assert payload["duration_ms"] == 1.25
