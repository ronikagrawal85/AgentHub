# Learning Note 001: FastAPI Foundation

This note explains the backend pieces introduced in Task 002 and relates them to familiar NestJS concepts where useful.

## FastAPI

FastAPI is a Python framework for building HTTP APIs. It uses Python type annotations to validate input, serialize output, generate an OpenAPI contract, and power interactive documentation. Unlike a complete application platform, it does not prescribe an ORM, job queue, or module system; AgentHub will add only the capabilities each phase requires.

In NestJS terms, a FastAPI application is roughly the root application, while route functions resemble controller handlers. FastAPI uses ordinary functions, type annotations, and explicit routers rather than decorators on controller classes.

## ASGI

ASGI, the Asynchronous Server Gateway Interface, is the standard boundary between an asynchronous Python web server and an application. It supports long-lived and concurrent protocols such as HTTP streaming and WebSockets in addition to normal request/response traffic.

This is conceptually similar to the contract between a Node.js HTTP server adapter and a NestJS application. FastAPI implements the application side of ASGI; it still needs a server to listen on a network port.

## Uvicorn

Uvicorn is the ASGI server used to run FastAPI. It accepts connections, translates network traffic into ASGI messages, invokes the application, and sends responses. The command `uvicorn app.main:app` means: import the `app` object from the `app.main` module.

Uvicorn's `--reload` option watches source files and restarts the development process after changes. It is a development convenience, not a production deployment strategy by itself.

## APIRouter

`APIRouter` groups related route handlers and metadata. Smaller routers can be composed into a version router, which is then included by the application. This keeps endpoint definitions out of the entry point and lets future feature modules own their routes.

An `APIRouter` is closest to a NestJS controller combined with part of a module's routing configuration. It is not a separate server and does not create a microservice.

## API versioning

AgentHub places the current API under `/api/v1`. A stable version prefix makes the public contract explicit and creates room for a future incompatible version without silently breaking existing clients. It does not mean every internal code change requires a new API version.

The prefix comes from typed configuration and is applied once when the v1 router is mounted. Endpoints therefore describe only their resource paths, such as `/health`.

## Application factory

An application factory is a function that constructs and configures a FastAPI instance. `create_app()` makes configuration explicit and allows tests to create isolated applications with controlled settings.

This resembles NestJS testing patterns that build a fresh testing module or application instance. The module-level `app = create_app()` remains the simple ASGI entry point expected by Uvicorn.

## Pydantic models

Pydantic models describe and validate structured data using Python types. `HealthResponse` guarantees that the health handler and generated OpenAPI schema agree on the response fields and types.

They are comparable to NestJS DTO classes used with `class-validator` and `class-transformer`, but validation and serialization behavior comes from Pydantic and Python annotations.

## Pydantic Settings

Pydantic Settings extends typed validation to configuration. Field defaults provide safe local behavior, environment variables can override them, and invalid values fail early. AgentHub restricts `APP_ENV` to known environment names, so a typo cannot silently select an undefined mode.

The optional `.env` file is a local convenience. Production configuration should come from its runtime environment or an approved secret manager; secrets must never be placed in committed configuration.

In NestJS this is similar to combining `ConfigModule` with a validation schema, except the schema is the typed `Settings` class itself.

## Dependency injection

FastAPI dependency injection calls declared providers and passes their results to route handlers. The health endpoint depends on `get_settings`, which keeps configuration lookup out of business logic and lets tests override the provider.

NestJS uses a container with provider tokens and constructor injection. FastAPI's approach is function-oriented: `Depends(get_settings)` declares the dependency at the parameter. Both approaches make dependencies explicit and replaceable in tests.

## Python virtual environments

A virtual environment is an isolated Python installation context for one project. Packages installed in `apps/backend/.venv` do not modify Ubuntu's system Python or another project's dependencies. `uv sync` creates and maintains this environment automatically.

This is related to, but more explicit than, a JavaScript project's local `node_modules`: both isolate dependencies, while a Python virtual environment also supplies project-specific interpreter entry points.

## pyproject.toml

`pyproject.toml` is the standard project metadata and tool-configuration file. It declares the project name, version, supported Python range, direct runtime dependencies, development dependency group, and settings for Pytest and Ruff.

It fills roles commonly spread across `package.json` and tool-specific JavaScript configuration files. It declares acceptable dependency ranges; it is not the complete reproducible resolution.

## uv.lock

`uv.lock` records exact resolved versions and transitive dependencies for supported environments. `uv sync --locked` refuses to re-resolve a stale lockfile, making unexpected dependency drift visible.

This is analogous to `package-lock.json` or `pnpm-lock.yaml`. The lockfile should be committed and changed intentionally when dependencies change.

## Pytest

Pytest discovers test functions, supplies reusable fixtures, and reports assertion failures. AgentHub's `client` fixture creates a fresh FastAPI application with explicit test settings and uses TestClient to make in-process HTTP requests.

These tests exercise routing, serialization, dependency overrides, OpenAPI, and errors without opening a port. This is comparable to using a NestJS testing application with Supertest, although FastAPI TestClient can run the ASGI application directly in the test process.

## Ruff

Ruff is a fast Python linter and formatter. The initial rules catch core Python errors, enforce import ordering, and encourage syntax appropriate for Python 3.12 without introducing an aggressive style burden.

Ruff combines responsibilities often handled by ESLint, Prettier, and import-sorting tools in TypeScript projects. `ruff check` analyzes code; `ruff format --check` verifies formatting without changing files.

## Request flow in this foundation

```text
Uvicorn
  → FastAPI application
  → /api/v1 versioned router
  → /health endpoint
  → Settings dependency
  → validated HealthResponse
  → JSON response
```

This is intentionally a liveness flow only. It does not check a database, Redis, Qdrant, or any external service. Readiness checks belong to later tasks after those dependencies exist.
