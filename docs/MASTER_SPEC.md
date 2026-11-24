# AgentHub — Enterprise Multi-Agent AI Workspace

## 1. Developer Background and Learning Objectives

I am a Full Stack Software Engineer with 3.5+ years of professional software development experience.

My existing technical skills include:

- JavaScript, TypeScript and Python
- React.js, Node.js, NestJS and Express.js
- PostgreSQL, Redis and TypeORM
- REST APIs, WebSockets and Socket.IO
- Microservices, CQRS and event-driven architecture
- JWT, OAuth 2.0, RBAC and refresh token rotation
- Docker, GitHub Actions, CI/CD and AWS EC2
- Playwright automation testing

I currently work at eSparkBiz Technologies on ChainIT (Black Ink Technologies), an enterprise identity verification and trusted-transactions platform. My professional experience includes Pactvera digital agreements and electronic signatures, KYC/KYB, organization onboarding, Progressive Web Applications and enterprise frontend and backend development within a distributed microservices ecosystem.

I have already built a personal project called VenueFlow, a real-time event ticket booking platform covering database transactions, pessimistic locking, concurrency control, Redis caching, WebSockets, authentication, ticket generation and cloud deployment.

I have also developed a foundational Agentic AI Chatbot using Python, LangChain, LangGraph and Streamlit, covering:

- LLM integration
- LangGraph state and graph workflows
- Conditional routing
- Tool calling
- Tavily web search
- Basic Retrieval-Augmented Generation (RAG)
- Embeddings and vector search
- Short-term and long-term memory
- Persistent conversations and threads
- Human-in-the-Loop workflows
- LangSmith tracing and observability
- Docker and CI/CD deployment

I do not want to restart these foundational concepts unnecessarily.

My objective is to become a strong Full Stack AI Engineer, Generative AI Engineer and Agentic AI Engineer while retaining my existing full-stack and backend engineering expertise.

I want to learn advanced AI application engineering through one comprehensive, practical, production-oriented portfolio project.

---

## 2. Project Overview

**Project Name:** AgentHub

**Full Name:** AgentHub — Enterprise Multi-Agent AI Workspace

**Category:** Enterprise SaaS, Generative AI, Agentic AI and Business Automation

**Application Type:** Multi-tenant full-stack AI application

**Target Users:** Organizations, employees, developers, managers, HR teams, security teams and administrators.

**Development Budget:** ₹0 wherever possible.

**Estimated Timeline:** Approximately 45–60 days of focused development, with additional time if required.

AgentHub is an enterprise AI workspace that allows organizations to manage internal knowledge, retrieve information from private documents, integrate external applications, automate business operations and delegate complex tasks to specialized AI agents.

The platform should combine selected capabilities inspired by:

- ChatGPT — conversational AI, memory and tool execution.
- Glean — enterprise knowledge retrieval and search.
- Microsoft Copilot — workplace productivity and enterprise assistance.
- n8n — external integrations and workflow automation.

The objective is not to clone these products completely. The objective is to build a focused application that demonstrates modern AI engineering, system design, security, evaluation and full-stack development.

Unlike a traditional chatbot, AgentHub should be capable of understanding user intent, planning tasks, retrieving information, selecting tools, coordinating specialized agents, verifying responses, requesting human approval and executing authorized business operations.

---

## 3. Business Problem

Organizations maintain large amounts of information across multiple systems:

- Internal documents
- Employee handbooks
- HR policies
- Engineering documentation
- Security policies
- GitHub repositories
- Project management tickets
- Vendor agreements
- Financial policies
- Standard operating procedures

Employees frequently spend time searching through documents, asking colleagues for information, comparing policies, creating tickets and manually collecting information from different applications.

Traditional search systems primarily return matching documents. Basic AI chatbots may generate answers but can hallucinate, lack access controls, fail to verify information and cannot reliably execute business operations.

AgentHub addresses these problems through:

- Centralized enterprise knowledge retrieval
- Evidence-grounded AI responses
- Advanced hybrid search
- Specialized AI agents
- MCP-based external integrations
- Secure tool execution
- Human-approved business operations
- Automated AI quality evaluation
- Multi-tenant data isolation
- Persistent conversations and workflows

---

## 4. Practical Business Use Cases

### Use Case 1: Enterprise Knowledge Assistant

An employee asks:

"What is our annual leave policy, and how many unused leaves can be carried forward?"

The system should:

1. Identify the user's intent.
2. Determine the user's organization and permissions.
3. Search authorized company documents.
4. Combine semantic and keyword-based retrieval.
5. Rerank relevant document chunks.
6. Verify whether sufficient evidence exists.
7. Generate a grounded answer.
8. Return document citations and relevant page or section references.

This use case covers Advanced RAG, hybrid search, embeddings, metadata filtering, reranking, contextual compression and hallucination mitigation.

### Use Case 2: Multi-Document Analysis

A legal team member asks:

"Compare these three vendor agreements and identify differences in payment terms, termination clauses and liability."

The system should retrieve relevant sections from multiple documents, compare information, identify differences and produce a structured comparison with citations.

This covers advanced chunking, multi-document retrieval, structured outputs and evidence verification.

### Use Case 3: Developer Productivity Assistant

A developer asks:

"Find all open authentication-related GitHub issues and summarize the common problems."

The system should:

- Route the request to a Developer Agent.
- Retrieve GitHub issues using an MCP integration.
- Analyze issue descriptions.
- Retrieve relevant internal engineering documentation when required.
- Generate a technical summary with references.

This covers MCP, FastMCP, tool calling, agent routing and external API integration.

### Use Case 4: Automated Ticket Creation

An employee asks:

"Create a high-priority bug ticket for the login failure."

The system should:

1. Understand the requested action.
2. Prepare the ticket title, description and priority.
3. Validate the structured output.
4. Check the user's permissions.
5. Pause execution and request human approval.
6. Resume the workflow after approval.
7. Create the ticket through an MCP tool.
8. Return the created ticket information.
9. Record the action in the audit log.

This covers Human-in-the-Loop, LangGraph interrupts, checkpointing, tool authorization and secure action execution.

### Use Case 5: Research and Recommendation

A manager asks:

"Research Kubernetes and AWS ECS, compare them against our internal deployment requirements and recommend a suitable approach."

The system should coordinate a Research Agent and Knowledge Agent, retrieve public and private information, verify supporting evidence and generate a recommendation.

This covers multi-agent orchestration, supervisor architecture, web search, parallel execution and agent handoffs.

### Use Case 6: Complex Multi-Agent Workflow

A developer asks:

"Analyze open authentication issues in VenueFlow, compare them with our internal security policies, identify potential violations and create a remediation ticket."

The workflow should involve:

- Supervisor Agent for planning and routing.
- Developer Agent for GitHub issue retrieval.
- Knowledge Agent for security policy retrieval.
- Verification Agent for evidence validation.
- Action Agent for ticket preparation.
- Human approval before ticket creation.
- Audit logging after execution.

This should become one of the flagship demonstrations of AgentHub.

### Use Case 7: AI Quality Evaluation

An administrator wants to determine whether changing the embedding model or retrieval strategy has reduced answer quality.

The system should execute a predefined evaluation dataset, compare results between configurations and display metrics such as faithfulness, retrieval quality, tool-call accuracy, latency and token consumption.

This covers RAGAS, DeepEval, LangSmith, LLM-as-a-Judge and AI regression testing.

### Use Case 8: Unauthorized Data Access

A regular employee asks:

"Show me confidential employee salary records."

The system should enforce organization and document-level permissions before retrieval and prevent unauthorized information disclosure.

This covers RBAC, tenant isolation, metadata filtering, PII protection and AI guardrails.

---

## 5. High-Level System Architecture

The application should use a modular architecture rather than unnecessary microservices.

The main components are:

1. Next.js frontend.
2. FastAPI backend.
3. Authentication and authorization layer.
4. LangGraph agent orchestration layer.
5. Advanced RAG pipeline.
6. MCP integration layer.
7. PostgreSQL relational database.
8. Qdrant vector database.
9. Redis caching and background job coordination.
10. Celery background workers.
11. Document storage.
12. AI evaluation and observability layer.
13. Security and guardrail layer.

The general request lifecycle is:

User Request → FastAPI → Authentication and Authorization → Input Guardrails → Supervisor Agent → Specialized Agent or Retrieval Pipeline → MCP Tools if Required → Human Approval if Required → Output Verification → Response Streaming → Persistence and Audit Logging.

Authorization must also be enforced inside retrieval operations and tool execution. It must not rely solely on the initial API authentication or an LLM prompt.

The backend should initially be a modular monolith with independently runnable background workers and MCP servers.

Avoid introducing microservices or Kubernetes simply to increase the technology count.

---

## 6. Authentication and Multi-Tenant Workspace Management

Implement the foundation of an enterprise SaaS application.

Features:

- User registration and login
- JWT authentication
- Access and refresh tokens
- Secure session management
- Organization creation
- Organization invitations
- Workspace switching
- User membership management
- Role-Based Access Control
- Document-level access permissions
- Tenant-level data isolation
- Protected API endpoints
- Logout and session revocation

Initial roles:

- Owner
- Administrator
- Member

Every document, conversation, integration, agent execution and evaluation dataset must belong to an authorized workspace.

Organization identifiers and permissions must be derived from authenticated membership rather than trusting arbitrary user-supplied identifiers.

Technologies:

FastAPI, Pydantic, PostgreSQL, SQLAlchemy, Alembic, JWT and Next.js.

---

## 7. Enterprise Knowledge Base

Organizations should be able to upload, manage and search internal documents.

Supported file types:

- PDF
- DOCX
- TXT
- Markdown
- Selected CSV files

Features:

- Document upload
- File validation
- Document parsing
- Text extraction
- Metadata extraction
- Background ingestion
- Document chunking
- Embedding generation
- Vector indexing
- Document versioning
- Department classification
- Document access permissions
- Document search
- Reindexing
- Document deletion
- Duplicate document detection
- Failed ingestion retries

Document statuses:

- Pending
- Processing
- Indexed
- Failed

Store document metadata in PostgreSQL, vectors and retrieval metadata in Qdrant, and original files in local or object storage.

Document ingestion should support asynchronous processing using Celery and Redis when the core ingestion pipeline is stable.

Deleting or replacing a document should also update its corresponding vector index.

---

## 8. Advanced RAG Implementation

Advanced RAG is one of the most important learning objectives of this project.

Implement and understand the following techniques.

### Advanced Chunking

- Recursive character-based chunking
- Semantic chunking
- Parent-child chunking
- Chunk overlap
- Document structure-aware chunking
- Chunk size experimentation

Compare how different chunking strategies affect retrieval quality.

### Embeddings

Use freely available local embedding models initially.

Preferred starting model:

BAAI/bge-small-en-v1.5

Understand:

- Embedding dimensions
- Semantic similarity
- Cosine similarity
- Dense vectors
- Sparse vectors
- Embedding model selection
- Embedding normalization
- Embedding quality evaluation

### Vector Database

Use Qdrant.

Learn:

- Collections
- Vector indexing
- Payload metadata
- Similarity search
- Dense vector search
- Sparse vector search
- Metadata filtering
- Hybrid retrieval
- Vector deletion and updates
- Tenant-aware retrieval

### Hybrid Search

Combine:

- Dense semantic retrieval
- BM25-compatible sparse retrieval
- Reciprocal Rank Fusion (RRF)

Understand when keyword search performs better than semantic search and vice versa.

### Reranking

Use a suitable BGE cross-encoder reranking model.

Learn:

- Bi-encoders versus cross-encoders
- Candidate retrieval
- Relevance scoring
- Top-K selection
- Retrieval precision
- Reranking latency trade-offs

### Query Rewriting

Implement:

- Conversational query rewriting
- Ambiguous query clarification
- Search query optimization
- Multi-query retrieval

### Contextual Compression

Reduce irrelevant retrieved information before passing context to the LLM.

Preserve source references and avoid removing information necessary for answering the question.

### Corrective RAG (CRAG)

Implement a corrective retrieval workflow:

1. Retrieve documents.
2. Grade document relevance.
3. Determine whether evidence is sufficient.
4. Rewrite the query when required.
5. Retrieve again.
6. Use an authorized alternative source when appropriate.
7. Generate an answer or abstain if evidence remains insufficient.

### Self-RAG-Inspired Workflow

Implement a practical workflow inspired by Self-RAG concepts:

- Retrieval relevance grading
- Answer grounding checks
- Evidence verification
- Unsupported claim detection
- Controlled answer regeneration

This is a Self-RAG-inspired application workflow, not training or reproducing the original Self-RAG model.

### Adaptive RAG

Select retrieval strategy based on query complexity.

- General questions: Direct LLM response.
- Simple enterprise questions: Standard RAG.
- Complex enterprise questions: Advanced or multi-step RAG.
- External information requests: Research tools.
- Business operations: Agentic workflows.

### Agentic RAG

Allow an agent to determine:

- Whether retrieval is required.
- Which authorized knowledge source to use.
- Whether additional retrieval is necessary.
- Whether retrieved evidence is sufficient.
- When to stop searching.
- When to abstain from answering.

### Complete Retrieval Pipeline

User Query → Intent Classification → Query Rewriting → Permission-Aware Hybrid Retrieval → Rank Fusion → Reranking → Contextual Compression → Relevance Grading → Corrective Retrieval if Required → Answer Generation → Evidence Verification → Source Citations.

Implement the basic pipeline first and introduce advanced techniques incrementally.

Do not execute every advanced retrieval stage for every request unnecessarily.

Benchmark each meaningful improvement against a basic RAG baseline.

---

## 9. Multi-Agent Architecture

Use LangGraph to implement specialized AI agents.

### Supervisor Agent

Responsibilities:

- Understand user intent.
- Determine request complexity.
- Select appropriate agents.
- Break complex requests into subtasks.
- Coordinate sequential and parallel execution.
- Manage agent routing and handoffs.
- Consolidate results.
- Enforce execution limits.

### Knowledge Agent

Responsibilities:

- Retrieve internal documents.
- Execute Advanced RAG.
- Perform multi-document analysis.
- Generate evidence-grounded answers.
- Return source citations.

### Research Agent

Responsibilities:

- Search public information using Tavily.
- Analyze multiple sources.
- Compare external information.
- Generate research summaries.
- Provide source references.

### Developer Agent

Responsibilities:

- Retrieve GitHub issues.
- Retrieve pull request information.
- Access authorized repository metadata.
- Analyze technical problems.
- Combine GitHub information with internal engineering documentation.

### Action Agent

Responsibilities:

- Prepare business operations.
- Generate structured action payloads.
- Validate tool arguments.
- Request human approval for sensitive actions.
- Execute authorized tools.
- Return execution results.

### Verification Agent

Responsibilities:

- Validate generated answers against evidence.
- Identify unsupported claims.
- Check whether requested tasks were completed.
- Verify citation references.
- Request controlled regeneration when required.

The Verification Agent may be implemented as a dedicated graph node or subgraph rather than a separate autonomous agent when that is more efficient.

### Multi-Agent Concepts

Cover:

- Supervisor architecture
- Agent routing
- Agent handoffs
- LangGraph subgraphs
- Shared state
- Conditional edges
- Sequential execution
- Parallel execution
- Tool selection
- Checkpointing
- Persistent memory
- Human-in-the-Loop
- Retry limits
- Execution timeouts
- Token and iteration budgets
- Agent failure recovery

Study the Agent-to-Agent (A2A) protocol conceptually and understand its differences from MCP.

Full A2A protocol implementation is optional.

---

## 10. Model Context Protocol (MCP)

Implement MCP as a standardized integration layer for connecting AI agents with external tools and data sources.

Understand:

- MCP Host
- MCP Client
- MCP Server
- Tools
- Resources
- Prompts
- Capability discovery
- Tool schemas
- Structured tool arguments
- STDIO transport
- Streamable HTTP transport
- Authentication and authorization
- Error handling

Use FastMCP to build custom MCP servers.

### GitHub MCP Server

Tools:

- List repositories
- Search issues
- Retrieve issue details
- List pull requests
- Retrieve pull request details
- Retrieve repository information

Use my personal GitHub repositories, including VenueFlow, for practical demonstrations.

Never use confidential company repositories.

### Ticket Management MCP Server

Tools:

- Search tickets
- Retrieve ticket details
- Create tickets
- Update ticket status
- Assign tickets

Initially implement a lightweight internal ticket management system backed by PostgreSQL or use GitHub Issues in a dedicated demo repository.

Do not require a paid Jira account.

### Knowledge Base MCP Server

Tools:

- Search authorized documents
- Retrieve document metadata
- Retrieve relevant document sections
- Retrieve source references

Every MCP tool must enforce authorization independently of the LLM.

Treat external tool responses as untrusted data.

For write operations, validate the action and require approval where appropriate.

Additional Slack, email and calendar integrations are optional future enhancements.

---

## 11. Human-in-the-Loop Workflows

Implement human approval for sensitive or externally visible actions.

Examples:

- Creating tickets
- Updating tickets
- Assigning tickets
- Sending messages
- Modifying external application data

The workflow should:

1. Prepare the proposed action.
2. Validate its arguments.
3. Check user permissions.
4. Save the proposed action.
5. Interrupt the LangGraph workflow.
6. Display an approval request in the frontend.
7. Allow an authorized user to approve or reject it.
8. Resume the workflow after approval.
9. Revalidate authorization and the approved payload.
10. Execute the action.
11. Record the result in the audit log.

Use checkpointing to resume interrupted workflows.

Implement idempotency to reduce duplicate actions caused by retries or repeated approval requests.

The agent must not silently modify an approved payload before execution.

---

## 12. Conversation Management and Memory

Implement persistent conversations similar to modern AI assistants.

Features:

- Create conversation
- List conversation threads
- Retrieve chat history
- Rename conversation
- Delete conversation
- Continue previous conversations
- Short-term conversational memory
- Authorized long-term memory
- Conversation summarization
- Context window management
- Persistent agent state
- Checkpoint recovery
- Memory deletion

Technologies:

- LangGraph PostgreSQL checkpointer
- PostgreSQL
- Redis where useful
- LLM-based conversation summarization

Conversation history and memory must be isolated by user and workspace.

---

## 13. LLM Evaluation and Agent Evaluation

AI evaluation is a core feature, not an optional addition.

The application should demonstrate how AI systems are measured, tested and improved.

### Evaluation Frameworks

Use:

- RAGAS
- DeepEval
- LangSmith
- LLM-as-a-Judge
- Pytest

Understand the differences between deterministic tests, model-based evaluations, retrieval evaluations and end-to-end agent evaluations.

### RAG Evaluation Metrics

- Faithfulness
- Answer relevancy
- Context precision
- Context recall
- Retrieval relevance
- Recall@K
- Precision@K
- Mean Reciprocal Rank
- Citation correctness
- Unsupported claim rate

### Agent Evaluation Metrics

- Tool selection accuracy
- Tool argument correctness
- Task completion
- Agent routing accuracy
- Approval compliance
- Unauthorized action prevention
- Failure recovery
- Execution latency
- Number of LLM calls
- Token consumption

### Evaluation Datasets

Create datasets containing:

- User question
- Expected answer
- Expected source documents
- Expected retrieved information
- Expected tool selection
- Expected tool arguments
- Expected authorization outcome
- Evaluation category

Include factual questions, complex multi-document questions, unsupported questions, malicious instructions and tool execution scenarios.

### Evaluation Experiments

Compare:

- Basic RAG versus Hybrid RAG
- Hybrid RAG versus Reranked RAG
- Different chunk sizes
- Different embedding models
- Different Top-K values
- Query rewriting enabled versus disabled
- Corrective retrieval enabled versus disabled
- Different LLM configurations

Store actual evaluation results and compare configurations.

Use LangSmith for traces, datasets, debugging and evaluation experiments.

### Regression Testing

When prompts, models, retrieval strategies or agent workflows change, rerun selected evaluation datasets.

Include deterministic security tests and lightweight evaluation smoke tests in CI/CD.

Run larger LLM evaluation suites manually or within free-tier quotas.

Do not fabricate evaluation scores or performance improvements.

---

## 14. AI Security and Guardrails

Implement practical security controls throughout the application.

### Prompt Injection Mitigation

Handle:

- Direct prompt injection
- Indirect prompt injection through documents
- Malicious external tool responses
- Attempts to override system instructions
- Attempts to retrieve restricted information
- Attempts to execute unauthorized tools

Treat retrieved documents and external tool responses as untrusted data, not executable instructions.

Do not rely solely on system prompts for security.

### Hallucination Mitigation

Implement:

- Evidence-grounded answers
- Source citations
- Retrieval relevance grading
- Answer verification
- Controlled regeneration
- Abstention when evidence is insufficient

### PII Detection and Redaction

Use Microsoft Presidio or an equivalent suitable library.

Detect and redact sensitive information where appropriate, including:

- Email addresses
- Phone numbers
- Personal identifiers
- Sensitive employee information

Use synthetic personal data for testing.

### Structured Outputs

Use Pydantic schemas for:

- Agent routing decisions
- Tool arguments
- Ticket creation payloads
- Evaluation results
- Relevance grading
- Verification responses
- Structured reports

### Tool Authorization

Implement:

- Tool-level permissions
- Workspace-specific integrations
- Least-privilege credentials
- Argument validation
- Human approval
- Audit logging
- Execution limits

### Additional Security

- Rate limiting
- Secure credential storage
- Input validation
- Output validation
- File upload restrictions
- Tenant isolation
- Cross-tenant retrieval tests
- Request timeouts
- Agent iteration limits
- Sensitive log redaction
- Protection against duplicate action execution

Security should be integrated from the beginning and strengthened during development.

---

## 15. Synthetic Enterprise Dataset

Do not use confidential ChainIT documents, company source code, customer information or real employee data.

Create a fictional enterprise organization named NexaTech Solutions.

The organization should contain six departments.

### Human Resources

Sample documents:

- Employee handbook
- Leave policy
- Remote work policy
- Employee onboarding guide
- Attendance policy
- Performance review policy

### Engineering

Sample documents:

- System architecture
- API documentation
- Coding standards
- Deployment guides
- Git workflow
- Incident management
- Database guidelines

### IT and Security

Sample documents:

- Security policy
- Access control policy
- Password policy
- Incident response procedure
- Production access guidelines
- Data retention policy

### Finance

Sample documents:

- Expense policy
- Reimbursement guidelines
- Travel policy
- Budget approval policy

### Legal

Sample documents:

- NDA templates
- Vendor agreements
- Service agreements
- Privacy policies
- Data processing agreements

### Operations

Sample documents:

- Standard operating procedures
- Approval workflows
- Escalation policies
- Support processes

Generate realistic synthetic documents in PDF, DOCX, Markdown, TXT and CSV formats.

Start with approximately 10–15 carefully designed documents.

Expand gradually toward:

- 90 synthetic enterprise documents
- 100 selected public technical documents
- 50 fictional employee records
- 100 sample project tickets
- 100 RAG evaluation questions
- 30 agent evaluation scenarios
- 30 security and adversarial test cases

These are target quantities, not prerequisites for starting development.

Use publicly available documentation from FastAPI, PostgreSQL, Docker, Redis, LangChain, LangGraph, GitHub and OWASP where licensing and usage terms permit.

Maintain source attribution and applicable licenses.

Create a canonical source-of-truth dataset containing known policy values and expected answers.

Example fictional policies:

- Annual paid leave: 24 days.
- Maximum leave carry-forward: 10 days.
- Remote working allowance: 3 days per week.
- Expenses above ₹10,000 require department head approval.
- Production access requires MFA and manager approval.

Include multiple document versions, conflicting policies, outdated documents, irrelevant information and missing information to test advanced retrieval.

Create at least two fictional workspaces to verify tenant isolation.

---

## 16. Frontend Application

Use Next.js with TypeScript.

Build a professional enterprise SaaS interface.

### Application Pages

1. Login
2. Registration
3. Workspace dashboard
4. AI chat
5. Conversation history
6. Knowledge base
7. Document upload and ingestion status
8. Agent execution activity
9. MCP integrations
10. Ticket management
11. Pending approvals
12. Evaluation dashboard
13. Audit logs
14. Workspace settings
15. Member and role management

### AI Chat Features

- Streaming responses
- Markdown rendering
- Code block rendering
- Document citations
- File attachments
- Conversation history
- Agent execution status
- Tool execution status
- Human approval requests
- Error handling
- Stop generation where supported
- Retry response

Display meaningful execution summaries and tool activity, not private model reasoning or hidden chain-of-thought.

### Evaluation Dashboard

Display:

- Evaluation runs
- Retrieval strategy comparisons
- Faithfulness scores
- Answer relevancy
- Tool-call accuracy
- Latency
- Token usage
- Failed evaluation cases
- Historical evaluation results

Use actual measured data.

### Frontend Technologies

- Next.js App Router
- React
- TypeScript
- Tailwind CSS
- shadcn/ui
- TanStack Query
- React Hook Form
- Zod
- Recharts

Learn Next.js concepts including layouts, nested routes, server components, client components, dynamic routing, loading states, error boundaries and authenticated application flows.

---

## 17. FastAPI Backend

Build a clean, modular Python backend.

Main modules:

- Authentication
- Users
- Workspaces
- Memberships
- Documents
- Document ingestion
- Retrieval
- Conversations
- Agents
- MCP integrations
- Tickets
- Approvals
- Evaluations
- Audit logs
- Security

Learn and implement:

- FastAPI routers
- Pydantic models
- Dependency injection
- Async/await
- SQLAlchemy ORM
- Alembic migrations
- Database transactions
- Request validation
- Response serialization
- Global exception handling
- Middleware
- Structured logging
- Correlation IDs
- Pagination
- Filtering
- Background processing
- REST APIs
- Server-Sent Events (SSE)
- OpenAPI documentation
- Health checks
- Unit testing
- Integration testing

Use clear separation between API routes, business services, repositories, schemas and AI workflows.

Avoid unnecessary abstractions.

Relate FastAPI concepts to my existing NestJS knowledge whenever helpful.

---

## 18. Database Architecture

### PostgreSQL

Store:

- Users
- Organizations
- Organization members
- Sessions
- Refresh tokens
- Documents
- Document versions
- Document chunk references
- Conversations
- Messages
- Agent runs
- Tool executions
- Approval requests
- Integrations
- Tickets
- Evaluation datasets
- Evaluation test cases
- Evaluation runs
- Evaluation results
- Audit logs

### Qdrant

Store:

- Dense embeddings
- Sparse vectors
- Document chunks
- Organization identifiers
- Document identifiers
- Department metadata
- Document version metadata
- Retrieval permission metadata
- Page and section references

### Redis

Use for:

- Caching
- Rate limiting
- Background job coordination
- Celery message broker
- Temporary execution state where appropriate

### Document Storage

Use local filesystem storage during development.

Introduce an S3-compatible storage abstraction when required.

Use free-tier object storage or AWS S3 only when available within the intended budget.

---

## 19. Complete Technology Stack

### Programming Languages

- Python
- TypeScript
- JavaScript
- SQL

### Frontend

- Next.js
- React
- Tailwind CSS
- shadcn/ui
- TanStack Query
- React Hook Form
- Zod
- Recharts

### Backend

- FastAPI
- Pydantic
- SQLAlchemy
- Alembic
- Uvicorn
- REST APIs
- SSE

### Databases and Infrastructure

- PostgreSQL
- Qdrant
- Redis
- Celery
- Local or S3-compatible document storage

### Generative AI

- LangChain
- LangGraph
- Groq
- Ollama as an optional local LLM provider
- Sentence Transformers
- BGE embeddings
- BGE cross-encoder reranking
- BM25-compatible sparse retrieval
- Hybrid search
- Advanced RAG
- Agentic RAG

### Agentic AI

- MCP SDK
- FastMCP
- Multi-agent systems
- Supervisor architecture
- LangGraph subgraphs
- Agent routing
- Tool calling
- Human-in-the-Loop
- Checkpointing
- Persistent memory

### AI Evaluation

- RAGAS
- DeepEval
- LangSmith
- LLM-as-a-Judge

### Security

- Microsoft Presidio
- Pydantic structured outputs
- JWT
- OAuth 2.0 where required
- RBAC
- Custom guardrails
- Tool authorization

### External Integrations

- Tavily
- GitHub APIs
- Internal ticket management APIs

### Document Processing

- PyMuPDF
- python-docx
- LangChain document loaders

### Testing

- Pytest
- FastAPI integration testing
- Playwright
- AI evaluation datasets
- Regression testing

### DevOps

- Docker
- Docker Compose
- Git
- GitHub
- GitHub Actions
- GitHub Container Registry or Docker Hub
- Nginx where required
- AWS EC2, ECR and S3 as optional cloud learning exercises

---

## 20. Free Development and Deployment Strategy

The project must prioritize a zero-cost development approach.

Use:

- Groq free-tier LLM inference within available limits.
- Ollama for optional local inference.
- Local Sentence Transformers embeddings.
- Local BGE reranking.
- Local Qdrant using Docker.
- Local PostgreSQL using Docker.
- Local Redis using Docker.
- Local Celery workers.
- Tavily free-tier usage within available limits.
- LangSmith developer plan within available limits.
- Open-source evaluation frameworks.
- Synthetic and licensed public documents.
- GitHub for source control.
- GitHub Actions within available free quotas.

Do not require a paid OpenAI API subscription.

Configure evaluation frameworks to use supported free or local model providers instead of automatically using paid model defaults.

### Local Development

Run the complete application locally using Docker Compose where appropriate.

Use local models for embeddings and reranking.

Avoid running resource-intensive services unnecessarily.

### Public Demo Deployment

Preferred free-tier deployment options, subject to current availability:

- Next.js: Vercel Hobby
- FastAPI: Render
- PostgreSQL: Neon
- Qdrant: Qdrant Cloud
- Redis: Upstash
- Source control: GitHub
- CI/CD: GitHub Actions

Free hosting may have sleeping instances, memory limitations, request limits and storage restrictions.

The full local application is the primary implementation. The public demo may use pre-indexed documents and reduced workloads to remain within free hosting limits.

Heavy document ingestion, reranking and evaluation workloads may run locally if free cloud infrastructure cannot support them.

AWS deployment is optional and should only be performed after checking available credits and potential charges.

Do not provision paid infrastructure without my explicit approval.

Verify current pricing and free-tier limits before selecting external services.

---

## 21. All 31 Core AI Learning Objectives

### Advanced RAG — 11 Topics

1. Advanced chunking strategies
2. Hybrid search
3. BM25 sparse retrieval
4. Reranking
5. Metadata filtering
6. Query rewriting
7. Contextual compression
8. Corrective RAG (CRAG)
9. Self-RAG-inspired verification
10. Adaptive RAG and Agentic RAG
11. Qdrant vector database

### Agentic AI and MCP — 7 Topics

12. Model Context Protocol (MCP)
13. FastMCP server development
14. Multi-agent systems
15. Supervisor architecture
16. Agent routing and handoffs
17. LangGraph subgraphs
18. Agent-to-Agent (A2A) protocol concepts

### AI Evaluation — 7 Topics

19. LLM evaluation
20. Agent evaluation
21. RAGAS
22. DeepEval
23. LangSmith evaluations
24. LLM-as-a-Judge
25. Evaluation datasets and regression testing

### AI Security — 6 Topics

26. AI guardrails
27. Prompt injection mitigation
28. Hallucination mitigation
29. Structured outputs
30. Tool-level authorization
31. PII detection and redaction

Additional engineering learning objectives:

- FastAPI
- Pydantic
- SQLAlchemy
- Alembic
- Next.js
- Celery
- SSE streaming
- Multi-tenant architecture
- Docker Compose
- Cloud deployment
- Automated testing

All core AI concepts should have a practical implementation or demonstration within AgentHub, except A2A, which can initially be covered conceptually.

---

## 22. Development Roadmap

### Phase 1 — Project Foundation

Estimated days: 1–6

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

Deliverable: Working authenticated backend with multi-tenant workspace management.

### Phase 2 — Advanced RAG

Estimated days: 7–17

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

Deliverable: Working enterprise knowledge assistant with measurable retrieval improvements.

### Phase 3 — MCP Integrations

Estimated days: 18–23

- Understand MCP architecture.
- Implement FastMCP servers.
- Implement GitHub integration.
- Implement ticket management integration.
- Implement knowledge base integration.
- Implement tool discovery.
- Implement tool validation and authorization.

Deliverable: AI application capable of interacting with authorized external tools.

### Phase 4 — Multi-Agent System

Estimated days: 24–31

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

Deliverable: Working multi-agent system capable of completing complex business requests.

### Phase 5 — AI Evaluation

Estimated days: 32–38

- Create evaluation datasets.
- Implement RAGAS evaluations.
- Implement DeepEval tests.
- Configure LangSmith tracing.
- Implement LLM-as-a-Judge.
- Compare retrieval configurations.
- Measure agent performance.
- Implement regression testing.
- Store evaluation results.

Deliverable: Measurable AI quality and reliability with reproducible evaluation experiments.

### Phase 6 — Security and Guardrails

Estimated days: 39–44

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

Deliverable: Security-tested AI workflows with enforceable authorization and approval controls.

### Phase 7 — Next.js Frontend

Estimated days: 45–52

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

Deliverable: Complete user-facing AI workspace.

### Phase 8 — Testing and Deployment

Estimated days: 53–60

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

Deliverable: Documented, tested and demonstrable portfolio project.

The timeline is an estimate. Prioritize working vertical slices and understanding over completing every feature within an arbitrary deadline.

---

## 23. Testing Requirements

Implement conventional software testing and AI-specific testing.

### Backend Testing

- Authentication
- Authorization
- Workspace isolation
- Database operations
- Document ingestion
- API validation
- Error handling
- Approval workflows
- Idempotent action execution

### Frontend Testing

Use Playwright for:

- Login
- Workspace switching
- Document upload
- AI chat
- Conversation history
- Approval and rejection
- Ticket creation
- Evaluation dashboard
- Permission restrictions

### AI Testing

- Retrieval quality
- Citation accuracy
- Answer grounding
- Agent routing
- Tool selection
- Tool arguments
- Multi-agent task completion
- Unsupported questions
- Prompt injection
- Unauthorized data access
- Agent failure recovery

Create deterministic mocks for external services so that normal automated tests do not require paid LLM calls.

---

## 24. Performance and Cost Optimization

Implement:

- Embedding caching where appropriate
- Document deduplication
- Incremental indexing
- Controlled Top-K retrieval
- Conditional reranking
- Query complexity classification
- Limited agent iterations
- Smaller models for simple classification
- LLM request timeouts
- Bounded retries
- Token budget management
- Conversation summarization
- Asynchronous document processing
- Batched evaluation execution
- Database indexing
- API pagination

Do not use multi-agent workflows when a simpler deterministic operation or standard RAG pipeline is sufficient.

Measure latency and quality trade-offs instead of assuming that adding more AI techniques always improves results.

---

## 25. Project Completion Criteria

The project should be considered complete when it contains:

- Working full-stack AI application.
- Multi-tenant workspaces.
- Authentication and RBAC.
- Enterprise document knowledge base.
- Synthetic enterprise demo dataset.
- Advanced RAG pipeline.
- Hybrid retrieval and reranking.
- Adaptive and corrective retrieval workflows.
- Supervisor-based multi-agent orchestration.
- Specialized AI agents.
- Three practical MCP integrations.
- Persistent conversations.
- LangGraph checkpointing.
- Human-in-the-Loop approvals.
- Secure tool execution.
- AI guardrails.
- PII detection and redaction.
- Audit logs.
- RAGAS and DeepEval evaluations.
- LangSmith observability.
- Measured evaluation results.
- Backend automated tests.
- Playwright end-to-end tests.
- Dockerized local infrastructure.
- GitHub Actions CI/CD.
- Working local demonstration.
- Limited public deployment where feasible.
- Comprehensive GitHub README.
- System architecture diagrams.
- Technical design documentation.
- Demonstration video or screenshots.
- Interview-ready explanations of major engineering decisions.

---

## 26. Project Scope Restrictions

The objective is AI application engineering, not AI model research.

The following are not mandatory:

- Training LLMs from scratch
- Fine-tuning large models
- PyTorch model development
- TensorFlow
- GPU infrastructure
- Kubernetes
- AWS EKS
- Complex distributed microservices
- Fully autonomous browser automation
- Paid enterprise integrations
- Custom foundation models
- Complete A2A protocol implementation

These can be explored later if required.

Avoid scope creep.

Do not introduce additional frameworks unless they solve a genuine project requirement.

---

## 27. Instructions for ChatGPT Throughout Development

Act as my Senior AI Engineer, Software Architect, Technical Mentor and Project Development Partner.

Your responsibility is to help me build AgentHub from scratch while ensuring that I understand the engineering concepts and implementation decisions.

Follow these instructions throughout the project:

1. Use this document as the master project specification.
2. Maintain continuity with previously completed project work.
3. Do not restart completed modules unnecessarily.
4. Develop the application incrementally, one feature at a time.
5. Explain the purpose of each feature before implementation.
6. Explain the underlying concepts in detail.
7. Explain why a technology or architectural pattern is selected.
8. Explain alternative approaches and relevant trade-offs.
9. Relate new Python and FastAPI concepts to my existing NestJS and TypeScript knowledge.
10. Provide practical, maintainable and production-oriented implementations.
11. Explain important code sections rather than providing unexplained code dumps.
12. Provide exact installation commands and required dependencies when implementation begins.
13. Specify the file paths and folder structure for every implementation.
14. Prefer clear naming, type safety and modular design.
15. Include error handling, validation and security.
16. Explain how to test each feature.
17. Define acceptance criteria before considering a feature complete.
18. Help debug errors using actual logs and code rather than assumptions.
19. Review existing code before suggesting major architectural changes.
20. Avoid unnecessary overengineering.
21. Prefer free and open-source technologies.
22. Verify current library documentation and compatibility when necessary.
23. Do not introduce paid services without my approval.
24. Maintain a project progress tracker.
25. Track which of the 31 AI concepts have been practically implemented.
26. Identify dependencies between features.
27. Provide suitable Git commit messages after completing features.
28. Keep project documentation updated.
29. Provide relevant interview questions after completing important modules.
30. Help me understand how each implementation relates to real enterprise applications.
31. Never claim that an implementation is complete unless it has actually been implemented and tested.
32. Do not invent evaluation metrics, performance improvements or project achievements.
33. Distinguish completed work from planned work.
34. Keep the project focused on becoming a job-ready Full Stack AI Engineer.
35. Use synthetic or publicly licensed data only.
36. Prioritize security, reliability and maintainability over impressive-looking technology lists.
37. Ask for missing environment details only when they materially affect implementation.
38. Update the project plan when architectural decisions change.
39. At the end of each development session, summarize completed work, pending tasks, concepts learned, testing status and the next development step.
40. Help me become capable of explaining and defending every major project decision independently during interviews.

When starting a new module, use the following approach:

- Business requirement
- Conceptual explanation
- Practical use case
- Architecture and design
- Technology selection
- Implementation plan
- Step-by-step implementation
- Testing
- Common errors
- Security and performance considerations
- Interview questions
- Completion checklist

Do not attempt to implement the entire application in one response.

---

## 28. Career and Portfolio Objectives

AgentHub should strengthen my profile for the following roles:

- Full Stack Software Engineer
- Software Development Engineer II
- Full Stack AI Engineer
- Generative AI Engineer
- Agentic AI Engineer
- Applied AI Engineer
- LLM Application Engineer
- Python Backend Engineer
- AI Evaluation Engineer
- Forward Deployed Engineer

My portfolio should ultimately contain three complementary flagship projects:

**ChainIT:** Professional enterprise software engineering experience covering Pactvera, KYC/KYB, PWA, organization onboarding and distributed microservices.

**VenueFlow:** Backend engineering and system design covering concurrency control, database transactions, real-time systems and authentication.

**AgentHub:** Advanced AI application engineering covering Advanced RAG, MCP, multi-agent systems, LLM evaluations, AI guardrails, FastAPI and Next.js.

The final objective is to demonstrate that I can design, build, evaluate, secure, deploy and maintain reliable AI-powered software applications.

---

## 29. Current Project Status

AgentHub is currently in the planning stage.

No AgentHub features should be assumed to have been implemented yet.

The architecture, business use cases, learning objectives, technology stack and development roadmap have been defined.

My existing foundational Agentic AI Chatbot and VenueFlow projects can be used as references, but AgentHub should be developed as a separate, comprehensive application.

---

## 30. First Task

When I begin development, start by helping me finalize the MVP scope, architecture, repository structure, local development environment and implementation sequence.

Explain what we will build first, why it is the correct starting point and how it connects to the remaining modules.

Do not immediately generate the entire application.

We will build AgentHub step by step, understand every important concept, test every major feature and maintain a clear record of our progress.