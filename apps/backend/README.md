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
| `APP_NAME` | `AgentHub API` | Service name used in API metadata and health output. |
| `APP_VERSION` | `0.1.0` | API version used in metadata and health output. |
| `APP_ENV` | `development` | One of `development`, `test`, `staging`, or `production`. |
| `DEBUG` | `false` | Enables FastAPI debug behavior when explicitly set. |
| `API_V1_PREFIX` | `/api/v1` | Prefix for version 1 API routes. |

The local `.env` file is ignored by Git. `.env.example` contains no secrets and remains tracked.

## Run the development server

```bash
uv run uvicorn app.main:app --reload
```

If the parent shell already defines an unrelated, non-boolean `DEBUG` value, unset it or start AgentHub explicitly with `DEBUG=false`. Invalid configuration is rejected intentionally at startup.

Available endpoints:

- Liveness: `GET http://127.0.0.1:8000/api/v1/health`
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
- OpenAPI JSON: `http://127.0.0.1:8000/openapi.json`

The health endpoint reports only whether the API process can respond. It does not claim that future databases or external services are ready.

## Test and check code quality

```bash
uv run pytest -v
uv run ruff check .
uv run ruff format --check .
```

To apply safe automated fixes and formatting during development:

```bash
uv run ruff check --fix .
uv run ruff format .
```

Tests supply explicit settings and do not depend on a developer's `.env`, external services, Docker, network access, or API keys.
