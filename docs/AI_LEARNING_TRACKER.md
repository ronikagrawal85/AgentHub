# AgentHub AI Learning Tracker

This tracker preserves the 31 core AI learning objectives from `docs/MASTER_SPEC.md`. Every objective remains pending until a practical implementation or approved conceptual demonstration exists and its verification criteria are satisfied. A2A may initially be verified conceptually; all other objectives require practical AgentHub evidence.

## Advanced RAG — 11 Topics

| # | Objective | Implementation phase | Status | Practical implementation evidence | Verification criteria |
| ---: | --- | --- | --- | --- | --- |
| 1 | Advanced chunking strategies | Phase 2 | Pending | None; no ingestion pipeline exists. | Implement and compare multiple approved chunking strategies on representative documents; record retrieval results and tests. |
| 2 | Hybrid search | Phase 2 | Pending | None; no retrieval pipeline exists. | Combine dense and sparse retrieval with rank fusion, preserve tenant filters, and verify behavior with retrieval tests and measured evaluation cases. |
| 3 | BM25 sparse retrieval | Phase 2 | Pending | None; no sparse index exists. | Implement BM25-compatible sparse retrieval and verify keyword-sensitive queries against known relevant documents. |
| 4 | Reranking | Phase 2 | Pending | None; no reranker exists. | Apply an approved cross-encoder to retrieved candidates and compare measured ranking quality and latency with the non-reranked baseline. |
| 5 | Metadata filtering | Phase 2; hardened in Phase 6 | Pending | None; no retrieval metadata exists. | Enforce workspace, permission, document, department, and version filters and pass positive and cross-tenant negative tests. |
| 6 | Query rewriting | Phase 2 | Pending | None; no query rewriting exists. | Implement conversational and ambiguous-query rewriting or multi-query retrieval; test that meaning and authorization scope are preserved. |
| 7 | Contextual compression | Phase 2 | Pending | None; no contextual compressor exists. | Remove irrelevant retrieved content while preserving answer-critical evidence and citations; verify on an evaluation set. |
| 8 | Corrective RAG (CRAG) | Phase 2 | Pending | None; no corrective workflow exists. | Implement relevance grading, conditional retry/rewrite, authorized fallback, and abstention; test sufficient- and insufficient-evidence paths. |
| 9 | Self-RAG-inspired verification | Phase 2 | Pending | None; no verification workflow exists. | Implement grounding and unsupported-claim checks with controlled regeneration or abstention; verify against known evidence. |
| 10 | Adaptive RAG and Agentic RAG | Phases 2 and 4 | Pending | None; no adaptive or agentic retrieval exists. | Route representative requests to direct, standard, advanced, external, or action workflows; verify routing, stopping, and evidence decisions. |
| 11 | Qdrant vector database | Phase 2 | Pending | None; Qdrant is not configured. | Configure tenant-aware collections and verify vector creation, filtered search, updates, and deletion through integration tests. |

## Agentic AI and MCP — 7 Topics

| # | Objective | Implementation phase | Status | Practical implementation evidence | Verification criteria |
| ---: | --- | --- | --- | --- | --- |
| 12 | Model Context Protocol (MCP) | Phase 3 | Pending | None; no MCP integration exists. | Demonstrate host/client/server interaction, capability discovery, structured tools or resources, transport behavior, authorization, and error handling. |
| 13 | FastMCP server development | Phase 3 | Pending | None; no FastMCP server exists. | Build and test approved FastMCP servers with typed schemas, independent authorization, safe errors, and at least one working transport. |
| 14 | Multi-agent systems | Phase 4 | Pending | None; no agents exist. | Complete a representative workflow using multiple specialized agents or graph components and verify state, coordination, limits, and output. |
| 15 | Supervisor architecture | Phase 4 | Pending | None; no supervisor exists. | Implement a supervisor that plans or delegates representative requests, consolidates results, and enforces execution budgets; test its decisions. |
| 16 | Agent routing and handoffs | Phase 4 | Pending | None; no routing exists. | Verify expected agent selection, typed handoff state, invalid-route handling, and sequential or parallel transitions on defined scenarios. |
| 17 | LangGraph subgraphs | Phase 4 | Pending | None; no LangGraph graph exists. | Implement reusable subgraphs with explicit state boundaries, checkpoint behavior, and tests for composition and failure paths. |
| 18 | Agent-to-Agent (A2A) protocol concepts | Phase 4 | Pending | None; no conceptual artifact or implementation exists. | Produce a reviewed explanation or design note comparing A2A with MCP, including actors, communication boundaries, use cases, and AgentHub applicability. |

## AI Evaluation — 7 Topics

| # | Objective | Implementation phase | Status | Practical implementation evidence | Verification criteria |
| ---: | --- | --- | --- | --- | --- |
| 19 | LLM evaluation | Phase 5 | Pending | None; no evaluation system exists. | Run reproducible quality evaluations over versioned cases, store actual metrics and configuration, and inspect failures without fabricated results. |
| 20 | Agent evaluation | Phase 5 | Pending | None; no agent evaluation exists. | Measure routing, tool selection, arguments, task completion, approval compliance, recovery, latency, calls, and token use on defined scenarios. |
| 21 | RAGAS | Phase 5 | Pending | None; RAGAS is not configured. | Run approved RAGAS metrics against a versioned dataset using a free/local supported provider and retain reproducible results. |
| 22 | DeepEval | Phase 5 | Pending | None; DeepEval is not configured. | Implement and execute relevant DeepEval tests with documented thresholds, deterministic setup where possible, and retained results. |
| 23 | LangSmith evaluations | Phase 5 | Pending | None; LangSmith is not configured. | Capture authorized traces and run a versioned dataset or experiment within available free limits; document configuration and observed results. |
| 24 | LLM-as-a-Judge | Phase 5 | Pending | None; no judge workflow exists. | Define a structured rubric, validate judge outputs, run repeatable comparisons using an approved provider, and document limitations. |
| 25 | Evaluation datasets and regression testing | Phases 5 and 8 | Pending | None; no evaluation dataset or regression suite exists. | Version representative RAG, agent, authorization, unsupported, and adversarial cases; rerun selected cases after changes and report actual regressions. |

## AI Security — 6 Topics

| # | Objective | Implementation phase | Status | Practical implementation evidence | Verification criteria |
| ---: | --- | --- | --- | --- | --- |
| 26 | AI guardrails | Phases 1 and 6 | Pending | None; no guardrails exist. | Implement layered input, retrieval, execution, and output controls; pass defined normal, malicious, and failure-path tests. |
| 27 | Prompt injection mitigation | Phase 6 | Pending | None; no mitigation exists. | Treat documents and tool output as untrusted, prevent instruction override and restricted access, and pass direct and indirect injection tests. |
| 28 | Hallucination mitigation | Phases 2 and 6 | Pending | None; no grounded-answer system exists. | Require appropriate evidence and citations, grade relevance and grounding, detect unsupported claims, and abstain when evidence is insufficient. |
| 29 | Structured outputs | Phases 3, 4, and 6 | Pending | None; no structured AI output schemas exist. | Validate routing, tool, action, grading, verification, evaluation, and report outputs with typed schemas; test invalid and adversarial payloads. |
| 30 | Tool-level authorization | Phases 3 and 6 | Pending | None; no tools exist. | Enforce least privilege independently of prompts, validate arguments and workspace integration access, require approvals where appropriate, and audit execution. |
| 31 | PII detection and redaction | Phase 6 | Pending | None; no PII controls exist. | Detect and appropriately redact approved synthetic PII categories, verify allowed exceptions, and prevent sensitive values from leaking into logs or responses. |

## Status rules

- **Pending:** No qualifying practical evidence has been verified.
- **In progress:** Implementation has begun, but verification criteria are not fully satisfied.
- **Complete:** Practical evidence is linked or described and all verification criteria have passed.

Status changes must be supported by actual code, artifacts, and command or evaluation evidence recorded in `docs/PROGRESS.md`.
