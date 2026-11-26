"""Application middleware for request tracing and observability."""

import logging
from time import perf_counter
from uuid import UUID, uuid4

from starlette.requests import Request
from starlette.types import ASGIApp, Message, Receive, Scope, Send

from app.core.exceptions import unhandled_exception_handler
from app.core.logging import reset_correlation_id, set_correlation_id

CORRELATION_ID_HEADER = "X-Correlation-ID"
logger = logging.getLogger(__name__)


class ExceptionBoundaryMiddleware:
    """Handle unexpected application errors inside observability middleware."""

    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        try:
            await self.app(scope, receive, send)
        except Exception as exception:
            if scope["type"] != "http":
                raise
            request = Request(scope, receive=receive)
            response = await unhandled_exception_handler(request, exception)
            await response(scope, receive, send)


def _correlation_id_from_headers(scope: Scope) -> str:
    for name, value in scope.get("headers", []):
        if name.lower() == b"x-correlation-id":
            candidate = value.decode("latin-1")
            try:
                return str(UUID(candidate))
            except ValueError:
                break
    return str(uuid4())


class CorrelationIdMiddleware:
    """Attach a validated request ID to responses and structured log records."""

    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        correlation_id = _correlation_id_from_headers(scope)
        token = set_correlation_id(correlation_id)
        started_at = perf_counter()
        status_code = 500

        async def send_with_correlation_id(message: Message) -> None:
            nonlocal status_code
            if message["type"] == "http.response.start":
                status_code = message["status"]
                headers = list(message.get("headers", []))
                headers.append(
                    (
                        CORRELATION_ID_HEADER.lower().encode("latin-1"),
                        correlation_id.encode("latin-1"),
                    )
                )
                message["headers"] = headers
            await send(message)

        try:
            await self.app(scope, receive, send_with_correlation_id)
        finally:
            logger.info(
                "HTTP request completed",
                extra={
                    "method": scope["method"],
                    "path": scope["path"],
                    "status_code": status_code,
                    "duration_ms": round((perf_counter() - started_at) * 1000, 2),
                },
            )
            reset_correlation_id(token)
