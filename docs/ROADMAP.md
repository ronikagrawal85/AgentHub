# AgentHub Development Roadmap

This roadmap preserves the eight phases and their sequence from `docs/MASTER_SPEC.md`. A listed task is planned unless `docs/PROGRESS.md` contains confirmed implementation and verification evidence.

## Phase 1 — Project Foundation

**Status:** In progress
**Estimated days:** 1–6

- Finalize requirements.
- Design system architecture.
- Set up Git repositories.
- Set up Python environment.
- Configure FastAPI.
- Configure PostgreSQL.
- Implement SQLAlchemy and Alembic.
- Implement authentication.
- Implement workspace management.
- Implement basic RBAC.
- Establish local Docker infrastructure.

**Deliverable:** Working authenticated backend with multi-tenant workspace management.

## Phase 2 — Advanced RAG

**Status:** Pending
**Estimated days:** 7–17

- Generate initial synthetic documents.
- Implement document ingestion.
- Implement chunking.
- Configure Qdrant.
- Generate embeddings.
- Implement basic RAG baseline.
- Implement hybrid search.
- Implement reranking.
- Implement metadata filtering.
- Implement query rewriting.
- Implement contextual compression.
- Implement corrective retrieval.
- Implement adaptive retrieval.
- Implement answer verification and citations.

**Deliverable:** Working enterprise knowledge assistant with measurable retrieval improvements.

## Phase 3 — MCP Integrations

**Status:** Pending
**Estimated days:** 18–23

- Understand MCP architecture.
- Implement FastMCP servers.
- Implement GitHub integration.
- Implement ticket management integration.
- Implement knowledge base integration.
- Implement tool discovery.
- Implement tool validation and authorization.

**Deliverable:** AI application capable of interacting with authorized external tools.

## Phase 4 — Multi-Agent System

**Status:** Pending
**Estimated days:** 24–31

- Implement Supervisor Agent.
- Implement Knowledge Agent.
- Implement Research Agent.
- Implement Developer Agent.
- Implement Action Agent.
- Implement verification workflow.
- Implement LangGraph subgraphs.
- Implement agent handoffs.
- Implement checkpointing.
- Implement Human-in-the-Loop workflows.

**Deliverable:** Working multi-agent system capable of completing complex business requests.

## Phase 5 — AI Evaluation

**Status:** Pending
**Estimated days:** 32–38

- Create evaluation datasets.
- Implement RAGAS evaluations.
- Implement DeepEval tests.
- Configure LangSmith tracing.
- Implement LLM-as-a-Judge.
- Compare retrieval configurations.
- Measure agent performance.
- Implement regression testing.
- Store evaluation results.

**Deliverable:** Measurable AI quality and reliability with reproducible evaluation experiments.

## Phase 6 — Security and Guardrails

**Status:** Pending
**Estimated days:** 39–44

- Strengthen prompt injection mitigation.
- Implement PII detection and redaction.
- Implement structured output validation.
- Strengthen tool authorization.
- Implement rate limiting.
- Implement audit logs.
- Implement execution limits.
- Test cross-tenant isolation.
- Test unauthorized tool execution.
- Test adversarial document content.

**Deliverable:** Security-tested AI workflows with enforceable authorization and approval controls.

## Phase 7 — Next.js Frontend

**Status:** Pending
**Estimated days:** 45–52

- Configure Next.js.
- Implement authentication pages.
- Implement workspace dashboard.
- Implement streaming AI chat.
- Implement knowledge base interface.
- Implement document management.
- Implement integration settings.
- Implement approval interface.
- Implement evaluation dashboard.
- Implement audit logs.

**Deliverable:** Complete user-facing AI workspace.

## Phase 8 — Testing and Deployment

**Status:** Pending
**Estimated days:** 53–60

- Implement backend integration tests.
- Implement Playwright tests.
- Execute AI regression tests.
- Optimize performance.
- Dockerize services.
- Configure GitHub Actions.
- Deploy a limited public demo.
- Prepare architecture diagrams.
- Prepare technical documentation.
- Prepare GitHub README.
- Prepare project demonstration.

**Deliverable:** Documented, tested and demonstrable portfolio project.

The timeline is an estimate. Prioritize working vertical slices and understanding over completing every feature within an arbitrary deadline.
