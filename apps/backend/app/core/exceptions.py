"""Centralized exception handling for the AgentHub API."""

import logging
from http import HTTPStatus
from typing import Any

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException

logger = logging.getLogger(__name__)


class ErrorDetail(BaseModel):
    """Stable error envelope returned by every exception handler."""

    code: str
    message: str
    details: Any | None = None


class ErrorResponse(BaseModel):
    """Public API error response."""

    error: ErrorDetail


def _error_response(
    *,
    status_code: int,
    code: str,
    message: str,
    details: Any | None = None,
    headers: dict[str, str] | None = None,
) -> JSONResponse:
    response = ErrorResponse(
        error=ErrorDetail(code=code, message=message, details=details)
    )
    return JSONResponse(
        status_code=status_code,
        content=jsonable_encoder(response),
        headers=headers,
    )


async def http_exception_handler(
    request: Request,
    exception: StarletteHTTPException,
) -> JSONResponse:
    """Convert framework HTTP errors into the public error envelope."""
    del request
    try:
        default_message = HTTPStatus(exception.status_code).phrase
    except ValueError:
        default_message = "HTTP error"
    message = exception.detail if isinstance(exception.detail, str) else default_message

    return _error_response(
        status_code=exception.status_code,
        code=f"http_{exception.status_code}",
        message=message,
        headers=exception.headers,
    )


async def validation_exception_handler(
    request: Request,
    exception: RequestValidationError,
) -> JSONResponse:
    """Return safe, structured information for invalid request data."""
    del request
    return _error_response(
        status_code=422,
        code="request_validation_error",
        message="Request validation failed",
        details=exception.errors(),
    )


async def unhandled_exception_handler(
    request: Request,
    exception: Exception,
) -> JSONResponse:
    """Log unexpected failures and avoid exposing internal implementation details."""
    logger.exception(
        "Unhandled API exception",
        exc_info=(type(exception), exception, exception.__traceback__),
        extra={"method": request.method, "path": request.url.path},
    )
    return _error_response(
        status_code=500,
        code="internal_server_error",
        message="An unexpected error occurred",
    )


def register_exception_handlers(application: FastAPI) -> None:
    """Register all global API exception handlers on an application instance."""
    application.add_exception_handler(
        StarletteHTTPException,
        http_exception_handler,
    )
    application.add_exception_handler(
        RequestValidationError,
        validation_exception_handler,
    )
    application.add_exception_handler(Exception, unhandled_exception_handler)
