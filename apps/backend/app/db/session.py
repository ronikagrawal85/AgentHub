"""Asynchronous SQLAlchemy engine, sessions, and FastAPI dependency."""

from collections.abc import AsyncIterator

from fastapi import Request
from pydantic import SecretStr
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

AsyncSessionFactory = async_sessionmaker[AsyncSession]


def create_database_engine(database_url: SecretStr) -> AsyncEngine:
    """Create the application engine without opening a connection eagerly."""
    return create_async_engine(
        database_url.get_secret_value(),
        pool_pre_ping=True,
        hide_parameters=True,
    )


def create_session_factory(engine: AsyncEngine) -> AsyncSessionFactory:
    """Create sessions that retain loaded state after transaction commits."""
    return async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )


async def get_db_session(request: Request) -> AsyncIterator[AsyncSession]:
    """Yield one request-scoped session and roll it back after failures.

    Business services explicitly commit successful units of work. This dependency
    never commits implicitly, which keeps transaction boundaries visible.
    """
    session_factory: AsyncSessionFactory = request.app.state.db_session_factory
    async with session_factory() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
