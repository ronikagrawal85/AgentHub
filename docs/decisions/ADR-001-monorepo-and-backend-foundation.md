# ADR-001: Monorepo and FastAPI Foundation

- **Status:** Accepted
- **Date:** 2026-11-24
- **Phase:** 1 — Project Foundation

## Context

AgentHub will eventually contain a browser application, an HTTP backend, independently runnable MCP servers, datasets, infrastructure definitions, scripts, and technical documentation. These components will evolve together and share product concepts, API contracts, security requirements, and delivery milestones.

The first executable component is a small Python API foundation. It needs reproducible dependency management, typed configuration, API versioning, tests, and code-quality checks without introducing databases, authentication, AI frameworks, or deployment machinery before those capabilities are requested.

## Decision

Use a single monorepo with explicit top-level boundaries for applications, MCP servers, datasets, infrastructure, scripts, and documentation.

Implement the backend as an independent Python 3.12 project under `apps/backend`, using:

- FastAPI for the HTTP application.
- Uvicorn as the ASGI server.
- Pydantic Settings for typed environment configuration.
- `uv` for interpreter selection, virtual environments, dependency resolution, and locking.
- Pytest and FastAPI's TestClient for deterministic tests.
- Ruff for linting, import ordering, and formatting.

Begin the backend as a modular monolith. The current foundation separates core configuration, versioned API routing, endpoints, and tests, but does not add feature layers before real business behavior requires them.

## Why a monorepo

- Product-wide changes can update API code, frontend consumers, documentation, datasets, and tests atomically.
- One repository makes architectural rules, progress evidence, and security expectations visible to every component.
- It reduces coordination and versioning overhead for one developer during incremental development.
- Top-level boundaries still allow applications and future MCP servers to have independent dependencies and execution commands.

## Why FastAPI

- Python is required for AgentHub's future AI ecosystem.
- FastAPI provides typed request and response validation, dependency injection, async support, automatic OpenAPI generation, Swagger UI, and ReDoc with little framework ceremony.
- Its router and dependency patterns support a modular monolith without requiring premature service or repository abstractions.
- For a NestJS developer, FastAPI routers are similar to controllers, dependencies serve many provider/guard use cases, and Pydantic models play a role similar to validated DTOs.

## Why uv

- `uv` manages Python selection, isolated environments, dependencies, commands, and a cross-platform lockfile in one fast tool.
- `uv.lock` records the complete resolution, while `pyproject.toml` describes direct runtime and development requirements.
- A project-local `.venv` protects the operating system Python and other projects.

## Why Python 3.12

- Python 3.12 is the project baseline specified for AgentHub.
- It provides current typing and language features while retaining broad support across FastAPI and the planned AI ecosystem.
- Constraining compatibility to `>=3.12,<3.13` prevents an unnoticed interpreter upgrade from changing behavior before compatibility is intentionally verified.

## Alternatives considered

### Separate repositories

Separate frontend, backend, MCP, and data repositories offer stronger independent ownership and release boundaries. They would add coordination, contract-versioning, and documentation overhead that does not benefit the current single-product, single-developer phase.

### Poetry, pip-tools, or pip with requirements files

Each can produce viable Python environments. Poetry introduces a second project workflow, pip-tools focuses primarily on locking, and raw pip requires more manual interpreter and environment management. `uv` satisfies all current needs with fewer tools.

### Django or Flask

Django includes a mature ORM and administration system but adds features not needed for this API-first foundation. Flask is flexible and lightweight but requires more choices and packages for validation, dependency patterns, and OpenAPI documentation. FastAPI matches the typed API and future AI-service requirements directly.

### Microservices from the start

Microservices could isolate scaling and deployment concerns, but would immediately add network contracts, distributed tracing, service discovery, and operational overhead. The master specification explicitly favors a modular monolith until concrete scaling or ownership needs justify separation.

## Consequences and trade-offs

- Repository-wide checks may eventually need path-aware execution as more applications are added.
- The monorepo can grow large when datasets and generated artifacts appear; `.gitignore`, licensing rules, and dataset curation must remain disciplined.
- The FastAPI application and settings dependency are easy to test and override, but module boundaries must be maintained as features accumulate.
- Lockfile updates must be reviewed alongside dependency declarations.
- Python 3.12 compatibility is deliberate; adopting a newer interpreter will require an explicit decision and verification.
- This decision does not select persistence, authentication, background jobs, AI frameworks, or deployment infrastructure.
