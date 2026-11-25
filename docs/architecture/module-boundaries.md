# AgentHub — Module Boundaries and Responsibilities

## Architecture Style

AgentHub uses a modular monolith for the core FastAPI backend, with independently executable Celery workers and MCP servers.

The architecture separates business logic, persistence, HTTP interfaces, AI engineering and external integrations.

## Core Infrastructure

### core

Responsibilities:

- Application configuration
- Security utilities
- Structured logging
- Exception handling
- Middleware
- Correlation IDs

### db

Responsibilities:

- SQLAlchemy async engine
- Database session management
- Declarative ORM base
- Database connectivity

### api

Responsibilities:

- API versioning
- Router aggregation
- Infrastructure endpoints
- Liveness and readiness endpoints

## Business Modules

### Auth

Owns authentication, registration orchestration, password verification, JWT generation, refresh token rotation, session management and logout.

Owned entities: Session, RefreshToken.

### Users

Owns user identity, user profile management and account lifecycle.

Owned entity: User.

### Workspaces

Owns workspace creation, workspace configuration, workspace updates and workspace lifecycle.

Owned entity: Workspace.

### Memberships

Owns workspace membership, invitations, role management, permission enforcement and authorized workspace context.

Owned entities: WorkspaceMember, Invitation.

### Documents

Owns document upload, metadata, storage, document versioning, document permissions and document lifecycle.

Owned entities: Document, DocumentVersion, DocumentPermission.

### Ingestion

Owns document parsing, chunking, embedding generation, vector indexing, ingestion status and retry handling.

Owned entities: IngestionJob, DocumentChunk.

### Conversations

Owns conversation creation, message persistence, conversation history, ownership and workspace isolation.

Owned entities: Conversation, Message.

### Agents

Owns agent execution lifecycle, orchestration requests, execution budgets, run persistence and execution event generation.

Owned entities: AgentRun, ToolExecution.

### Integrations

Owns workspace integration configuration, MCP server registration, connection management, tool discovery and integration permissions.

Owned entity: Integration.

### Tickets

Owns internal ticket creation, ticket assignment, ticket updates, status management and ticket retrieval.

Owned entity: Ticket.

### Approvals

Owns human approval requests, approval decisions, immutable action proposals, approval expiration and execution authorization.

Owned entity: ApprovalRequest.

### Evaluations

Owns evaluation datasets, test cases, evaluation execution, experiment tracking, metric persistence and regression comparisons.

Owned entities: EvaluationDataset, EvaluationTestCase, EvaluationRun, EvaluationResult.

### Audit

Owns security event persistence, business activity logging, tool execution audit records and authorized audit retrieval.

Owned entities: AuditLog, GuardrailEvent.

## AI Engineering Layer

### Providers

Provides configurable interfaces for LLM and embedding providers.

### Embeddings

Handles document and query embedding generation.

### Chunking

Implements configurable document chunking strategies.

### Retrieval

Implements dense search, sparse search, hybrid search, metadata filtering and retrieval orchestration.

### Reranking

Implements relevance scoring and cross-encoder reranking.

### RAG

Implements baseline RAG, query rewriting, contextual compression, corrective retrieval, evidence verification, adaptive retrieval and agentic retrieval.

### Agents and Graphs

Implements supervisor orchestration, specialized agents, routing, handoffs, LangGraph subgraphs and workflow execution.

### Tools

Provides authorized tools for agent workflows and MCP integration.

### Memory

Provides conversation context management and LangGraph checkpoint integration.

### Evaluation

Provides evaluation metrics, judge models, RAGAS, DeepEval and LangSmith evaluation adapters.

### Guardrails

Provides AI input validation, output validation, prompt injection mitigation, PII detection, structured output validation and safety policies.

## Background Workers

Celery workers execute asynchronous document ingestion and other explicitly defined background jobs.

Workers must preserve tenant context, support bounded retries and implement idempotency.

## MCP Servers

Independent MCP servers:

- GitHub MCP Server
- Ticket Management MCP Server
- Knowledge Base MCP Server

MCP servers must enforce authentication, authorization, resource permissions and workspace isolation independently.

## Module Dependency Rules

- HTTP routers delegate business logic to services.
- Services coordinate business rules and persistence.
- Repositories handle database access.
- Modules own their respective database entities.
- Cross-module operations use explicit service interfaces.
- Avoid circular module dependencies.
- AI components must not bypass business authorization.
- MCP tools must not bypass application authorization.
- Tenant context must propagate through API requests, background jobs, retrieval and agent execution.
- Shared infrastructure must not contain unrelated business logic.
- Database transactions must cover atomic business operations.
- Create abstractions only when justified by actual requirements.

## Implementation Strategy

Implement modules incrementally according to the project roadmap.

Do not create empty implementations for future modules.

Each module must include appropriate validation, error handling, authorization, tests and documentation before being marked complete.