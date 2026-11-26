"""Structured JSON logging with request-scoped correlation context."""

import json
import logging
import sys
from contextvars import ContextVar, Token
from datetime import UTC, datetime
from typing import Any

_correlation_id: ContextVar[str | None] = ContextVar(
    "correlation_id",
    default=None,
)


def get_correlation_id() -> str | None:
    """Return the correlation ID associated with the current request context."""
    return _correlation_id.get()


def set_correlation_id(correlation_id: str) -> Token[str | None]:
    """Set correlation context and return the token needed to restore it."""
    return _correlation_id.set(correlation_id)


def reset_correlation_id(token: Token[str | None]) -> None:
    """Restore correlation context after a request completes."""
    _correlation_id.reset(token)


class JsonFormatter(logging.Formatter):
    """Serialize log records as one JSON object per line."""

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, Any] = {
            "timestamp": datetime.fromtimestamp(record.created, tz=UTC).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "correlation_id": get_correlation_id(),
        }

        for field in ("method", "path", "status_code", "duration_ms"):
            value = getattr(record, field, None)
            if value is not None:
                payload[field] = value

        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)

        return json.dumps(payload, default=str)


def configure_structured_logging(log_level: str) -> None:
    """Configure the process root logger without removing host-provided handlers."""
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    for handler in root_logger.handlers:
        if getattr(handler, "_agenthub_structured", False):
            handler.setLevel(log_level)
            return

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(log_level)
    handler.setFormatter(JsonFormatter())
    handler._agenthub_structured = True  # type: ignore[attr-defined]
    root_logger.addHandler(handler)
