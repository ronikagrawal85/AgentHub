# AgentHub

AgentHub is an enterprise multi-agent AI workspace being built as a production-oriented, multi-tenant SaaS application. It will combine private knowledge retrieval, specialized AI agents, authorized integrations, human approvals, and measurable AI evaluation.

The project is implemented incrementally as a modular monolith. The initial repository layout separates deployable applications, MCP servers, datasets, infrastructure, scripts, and technical documentation while keeping them in one versioned repository.

## Repository layout

```text
apps/backend/          FastAPI backend and its tests
apps/frontend/         Future Next.js application
mcp-servers/           Future independently runnable MCP servers
datasets/              Synthetic, public, evaluation, and adversarial data
infrastructure/        Local and future deployment infrastructure
scripts/               Repository automation and maintenance scripts
docs/                  Architecture, decisions, learning notes, and trackers
```

The FastAPI foundation and local PostgreSQL Compose configuration are implemented. Database integration, authentication, AI workflows, MCP servers, the frontend, and deployment infrastructure belong to later tasks.

## Local PostgreSQL

Docker Engine with the Compose plugin is required. The Compose service binds PostgreSQL only to the local machine and stores its data in a named Docker volume.

```bash
cp .env.example .env
# Replace POSTGRES_PASSWORD in .env, then run:
docker compose up -d postgres
docker compose ps
```

When Docker Desktop is not running but the system Docker Engine is available, select it with `docker context use default` or run the commands with `docker --context default compose ...`.

PostgreSQL is available at `127.0.0.1:5432` by default. Stop the container with `docker compose stop postgres`; remove the container with `docker compose down`. Neither command deletes the named database volume. Deliberately deleting the volume requires `docker compose down --volumes` and destroys the local database data.

## Backend quick start

Python 3.12 and [uv](https://docs.astral.sh/uv/) are required.

```bash
cd apps/backend
uv sync --locked
uv run uvicorn app.main:app --reload
```

The API is then available at `http://127.0.0.1:8000`, with documentation at `/docs` and `/redoc`. See [`apps/backend/README.md`](apps/backend/README.md) for complete backend instructions.

## Project documentation

- [`docs/MASTER_SPEC.md`](docs/MASTER_SPEC.md) — authoritative project requirements.
- [`docs/ROADMAP.md`](docs/ROADMAP.md) — the eight-phase delivery sequence.
- [`docs/PROGRESS.md`](docs/PROGRESS.md) — verified implementation status and evidence.
- [`docs/AI_LEARNING_TRACKER.md`](docs/AI_LEARNING_TRACKER.md) — the 31 core AI learning objectives.

Do not commit secrets or local `.env` files. Copy the root `.env.example` for Docker Compose settings and `apps/backend/.env.example` for backend overrides.
