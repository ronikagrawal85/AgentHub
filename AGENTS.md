# AgentHub Repository Instructions

## Purpose and architecture

AgentHub is an enterprise, multi-tenant AI workspace for private knowledge retrieval, specialized agent collaboration, authorized tool execution, human approval, and AI quality evaluation. Treat `docs/MASTER_SPEC.md` as the authoritative requirements source.

Build the system incrementally as a modular monolith. Use a FastAPI backend and a Next.js App Router frontend. Keep background workers and MCP servers independently runnable without introducing premature microservices.

## Core technology

- Use Python 3.12 and `uv` for Python dependency and environment management.
- Use TypeScript for the Next.js frontend.
- Use PostgreSQL for relational data, Redis for caching and job coordination, and Qdrant for vectors and retrieval metadata.
- Use LangChain for AI application components, LangGraph for stateful agent workflows, and FastMCP for MCP servers.
- Prefer free, open-source, local, or free-tier technology. Do not introduce paid services or infrastructure without explicit approval.
- Add dependencies only when they solve an approved requirement.

## Engineering rules

- Implement only the explicitly requested feature or phase. Do not build future phases prematurely.
- Preserve the modular boundaries defined in the master specification.
- Keep code clean, typed, maintainable, and appropriately documented. Prefer clear solutions over unnecessary abstraction.
- Maintain strict tenant isolation. Derive workspace access from authenticated membership; never trust a user-supplied tenant identifier by itself.
- Enforce RBAC and authorization at API, retrieval, data-access, and tool-execution boundaries.
- Treat retrieved documents and external tool output as untrusted input.
- Never hardcode secrets, commit credentials, or access company repositories or confidential data. Use synthetic or properly licensed public data only.
- Preserve existing files unless an approved change requires modifying them.
- Do not automatically commit, push, deploy, or provision infrastructure.

## Testing and verification

- Add automated tests appropriate to each implementation, including tenant-isolation and authorization tests for security-sensitive work.
- Run relevant formatting, linting, type checking, tests, and integrity checks before reporting completion.
- Never fabricate test results, benchmarks, evaluation scores, or implementation status.
- Mark work complete only after it is implemented and successfully verified. Record failed or unavailable verification honestly.

## Documentation and progress

- After every implementation, update `docs/PROGRESS.md` with completed work, pending work, blockers, and actual verification evidence.
- Update `docs/ROADMAP.md` only when roadmap status or an approved architectural decision changes.
- Update `docs/AI_LEARNING_TRACKER.md` only when an objective has practical implementation evidence and its verification criteria have been satisfied.
- Keep documentation consistent with `docs/MASTER_SPEC.md`; do not modify the master specification unless explicitly requested.

## Git conventions

Use Conventional Commits with a focused scope when helpful, for example:

- `feat(auth): add workspace-aware login`
- `fix(retrieval): enforce tenant metadata filter`
- `docs(progress): record foundation verification`
- `test(auth): cover cross-tenant access denial`
- `chore(deps): update approved backend dependencies`

Keep commits small and cohesive. Do not commit generated artifacts, local data, secrets, or credentials.
