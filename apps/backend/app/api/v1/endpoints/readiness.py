"""Database-backed application readiness endpoint."""

import logging
from typing import Annotated, Literal

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db_session

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/ready", tags=["health"])


class ReadinessResponse(BaseModel):
    """Public readiness state for required application dependencies."""

    status: Literal["ready"]
    database: Literal["reachable"]


@router.get("", response_model=ReadinessResponse)
async def readiness_check(
    session: Annotated[AsyncSession, Depends(get_db_session)],
) -> ReadinessResponse:
    """Report readiness only when PostgreSQL accepts a simple query."""
    try:
        await session.execute(text("SELECT 1"))
    except SQLAlchemyError as exception:
        logger.warning("Database readiness check failed", exc_info=exception)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database is unavailable",
        ) from exception
    return ReadinessResponse(status="ready", database="reachable")
