"""Unit and integration coverage for persistence infrastructure."""

import asyncio
import os
from collections.abc import AsyncIterator
from contextlib import AbstractAsyncContextManager
from pathlib import Path
from types import SimpleNamespace
from typing import Any
from unittest.mock import AsyncMock, MagicMock

import pytest
from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient
from pydantic import SecretStr
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from app.core.config import Settings
from app.db.session import get_db_session
from app.main import create_app

MIGRATION_REVISION = "3333e5fee530"


def _test_database_url() -> str:
    database_url = os.getenv("AGENTHUB_TEST_DATABASE_URL")
    if database_url is None:
        pytest.skip(
            "AGENTHUB_TEST_DATABASE_URL is required for database integration tests"
        )
    return database_url


def test_database_url_is_stored_as_a_secret() -> None:
    settings = Settings(
        database_url="postgresql+asyncpg://user:secret@localhost/database",
        _env_file=None,
    )

    assert isinstance(settings.database_url, SecretStr)
    assert "secret" not in str(settings.database_url)


def test_readiness_reports_reachable_database(test_settings: Settings) -> None:
    application = create_app(test_settings)
    session = AsyncMock(spec=AsyncSession)

    async def override_session() -> AsyncIterator[AsyncSession]:
        yield session

    application.dependency_overrides[get_db_session] = override_session

    with TestClient(application) as client:
        response = client.get("/api/v1/ready")

    assert response.status_code == 200
    assert response.json() == {"status": "ready", "database": "reachable"}
    session.execute.assert_awaited_once()


def test_failed_request_rolls_back_database_session() -> None:
    session = AsyncMock(spec=AsyncSession)
    session_context = MagicMock(spec=AbstractAsyncContextManager)
    session_context.__aenter__ = AsyncMock(return_value=session)
    session_context.__aexit__ = AsyncMock(return_value=None)
    session_factory = MagicMock(return_value=session_context)
    request = SimpleNamespace(
        app=SimpleNamespace(
            state=SimpleNamespace(db_session_factory=session_factory),
        )
    )

    async def exercise_dependency() -> None:
        dependency = get_db_session(request)  # type: ignore[arg-type]
        assert await anext(dependency) is session
        with pytest.raises(RuntimeError, match="force rollback"):
            await dependency.athrow(RuntimeError("force rollback"))

    asyncio.run(exercise_dependency())

    session.rollback.assert_awaited_once_with()


@pytest.mark.integration
def test_database_connectivity() -> None:
    settings = Settings(
        app_env="test",
        database_url=_test_database_url(),
        _env_file=None,
    )

    with TestClient(create_app(settings)) as client:
        response = client.get("/api/v1/ready")

    assert response.status_code == 200
    assert response.json() == {"status": "ready", "database": "reachable"}


@pytest.mark.integration
def test_migration_upgrade_and_downgrade(monkeypatch: pytest.MonkeyPatch) -> None:
    database_url = _test_database_url()
    monkeypatch.setenv("AGENTHUB_DATABASE_URL", database_url)
    alembic_config = Config(Path(__file__).parents[1] / "alembic.ini")

    async def current_revision() -> Any:
        engine = create_async_engine(database_url)
        try:
            async with engine.connect() as connection:
                return await connection.scalar(
                    text("SELECT version_num FROM alembic_version")
                )
        finally:
            await engine.dispose()

    command.downgrade(alembic_config, "base")
    command.upgrade(alembic_config, "head")
    assert asyncio.run(current_revision()) == MIGRATION_REVISION

    command.downgrade(alembic_config, "base")
    assert asyncio.run(current_revision()) is None

    # Restore the development database to the latest revision for subsequent work.
    command.upgrade(alembic_config, "head")
