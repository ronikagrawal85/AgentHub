# AgentHub Backend

The backend is an independent Python 3.12 project managed by `uv`. It exposes the AgentHub HTTP API through FastAPI and will grow as a modular monolith: feature modules share one deployable application while retaining clear boundaries. This foundation contains only configuration, API versioning, and an application liveness check.

## Prerequisites

- Python 3.12.x available to `uv`
- `uv` 0.11.29 or later

Do not replace or modify Ubuntu's system Python. The `.python-version` file asks `uv` to select Python 3.12 for this project.

## Install dependencies

From `apps/backend`:

```bash
uv sync --locked
```

`uv` creates an isolated `.venv` inside this directory. Packages installed there do not alter the operating system Python or packages used by other projects. Runtime dependencies are declared under `[project.dependencies]`; development tools are isolated in the `dev` dependency group. `uv.lock` records exact resolved versions for reproducible installation.

## Environment configuration

The application has safe development defaults. To override them locally:

```bash
cp .env.example .env
```

Supported variables are:

| Variable | Default | Purpose |
| --- | --- | --- |
| `AGENTHUB_APP_NAME` | `AgentHub API` | Service name used in API metadata and health output. |
| `AGENTHUB_APP_VERSION` | `0.1.0` | API version used in metadata and health output. |
| `AGENTHUB_APP_ENV` | `development` | One of `development`, `test`, `staging`, or `production`. |
| `AGENTHUB_DEBUG` | `false` | Enables FastAPI debug behavior when explicitly set. |
| `AGENTHUB_API_V1_PREFIX` | `/api/v1` | Prefix for version 1 API routes. |
| `AGENTHUB_LOG_LEVEL` | `INFO` | Minimum severity emitted by structured application logging. |
| `AGENTHUB_CORS_ALLOWED_ORIGINS` | `["http://localhost:3000"]` | JSON list of browser origins allowed to call the API. |
| `AGENTHUB_CORS_ALLOW_CREDENTIALS` | `true` | Allows credentials for explicitly configured origins. |
| `AGENTHUB_DATABASE_URL` | Required | Async SQLAlchemy PostgreSQL URL; treat its password as a secret. |

The local `.env` file is ignored by Git. `.env.example` contains no secrets and remains tracked.

## Run the development server

```bash
uv run uvicorn app.main:app --reload
```

Invalid configuration is rejected intentionally at startup. Production deployments must explicitly configure their frontend origins rather than using a wildcard with credentials.

Every HTTP response includes an `X-Correlation-ID`. A valid UUID supplied in the same request header is preserved; missing or invalid values are replaced. Application logs are emitted as JSON and include this identifier for request tracing. API failures use a consistent error envelope containing `error` and `correlation_id` fields.

Available endpoints:

- Liveness: `GET http://127.0.0.1:8000/api/v1/health`
- Readiness: `GET http://127.0.0.1:8000/api/v1/ready`
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
- OpenAPI JSON: `http://127.0.0.1:8000/openapi.json`

The liveness endpoint reports whether the API process can respond. The readiness endpoint executes `SELECT 1` and returns success only when PostgreSQL is reachable.

## Database migrations

Alembic reads the same `AGENTHUB_DATABASE_URL` setting as the application. From `apps/backend`:

```bash
uv run alembic upgrade head
uv run alembic downgrade -1
uv run alembic revision --autogenerate -m "describe schema change"
```

The initial revision is an intentionally empty persistence baseline. Business tables are introduced with their owning modules rather than being created prematurely.

## Test and check code quality

```bash
uv run pytest -v
AGENTHUB_TEST_DATABASE_URL="postgresql+asyncpg://..." uv run pytest -m integration -v
uv run ruff check .
uv run ruff format --check .
```

To apply safe automated fixes and formatting during development:

```bash
uv run ruff check --fix .
uv run ruff format .
```

Tests supply explicit settings and do not depend on a developer's `.env`, external services, Docker, network access, or API keys.
