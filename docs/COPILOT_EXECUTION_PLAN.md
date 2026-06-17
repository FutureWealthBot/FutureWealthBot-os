# FUTUREWEALTHBOT OS — Copilot Execution Plan

## Purpose

This document is the authoritative execution plan for converting the current fragmented FutureWealthBot ecosystem into a unified monorepo system called **FUTUREWEALTHBOT OS**.

This is not a feature roadmap first.

This is an **architecture consolidation directive**.

## Current GitHub Reality

The current ecosystem is fragmented across multiple repositories:

- `API-Factory`
- `API-Factory-2`
- `API-Factory-Administration`
- `FutureWealthBot-GPT`
- `wealth-bot`
- `wealth-bot-djt`
- `mercury-cli`
- `brave-search-mcp-server`
- `SafeNow`

## Critical Problem

There is currently **no unified runtime**.

Multiple repositories are functioning as:
- prototypes
- partial implementations
- forks
- isolated tools
- disconnected control layers

These systems should be consolidated into **one operating system**:

## Target System

**FUTUREWEALTHBOT OS**

The end state must be a single architecture containing:

- API Gateway
- Agent Runtime
- Strategy Engine
- Automation Engine
- Tooling Layer
- Admin Dashboard
- Integrations Layer
- Shared Modules
- Infrastructure Layer
- Database Layer
- Documentation Layer

## Primary Directive

Copilot must treat this repository as the canonical home for the unified operating system.

### Rules

- Do **NOT** create new repositories.
- Do **NOT** duplicate logic across modules.
- Prefer interfaces over implementations.
- Build for modularity and plugin systems.
- Everything must plug into the API Gateway.
- No feature development until architecture is complete.
- Consolidate existing systems before introducing new product behavior.

---

## Phase 1 — Create Monorepo Shell

### Objective
Create the monorepo structure first, before feature work.

### Required structure

```text
futurewealthbot-os/
  api-gateway/
  agent-runtime/
  strategy-engine/
  automation-engine/
  integrations/
  tools/
  admin-dashboard/
  shared/
  infra/
  db/
  docs/
```

### Phase 1 rules

- Folder structure only
- Placeholder documentation allowed
- No business logic
- No feature implementation

---

## Phase 2 — Migration Mapping

### Objective
Map the current repositories into the new monorepo structure.

### Required mapping

| Existing repository | Target location |
|---|---|
| `API-Factory-2` | `apps/api-gateway` + `engines/automation-engine` |
| `API-Factory-Administration` | `apps/admin-dashboard` |
| `FutureWealthBot-GPT` | `engines/agent-engine` |
| `wealth-bot` | `engines/strategy-engine` |
| `wealth-bot-djt` | `engines/strategy-engine` as plugin strategy |
| `mercury-cli` | `tools/mercury-cli` |
| `brave-search-mcp-server` | `integrations/brave-search-mcp` |
| `SafeNow` | `apps/safenow` as isolated module |

### Migration documentation requirements

Create:
- `docs/MIGRATION_MAP.md`

It must include:
- repository-to-module mapping
- duplication notes
- consolidation risks
- isolation notes where needed

---

## Phase 3 — Build the Core Runtime

### Objective
Create the architectural runtime skeleton without business logic.

### Required core runtime elements

1. API Gateway (FastAPI)
2. Agent Runtime Engine
3. Strategy Engine base classes
4. Automation Engine workflow executor
5. Shared types module

### Strict rules

- No business logic
- No product features
- No integration behavior
- Only interfaces, abstract classes, routing layers, and type definitions

### Required conceptual interfaces

#### Agent Base Class

```python
class BaseAgent:
    def run(self, input: dict) -> dict:
        raise NotImplementedError
```

#### Strategy Base Class

```python
class BaseStrategy:
    def evaluate(self, data):
        raise NotImplementedError

    def execute(self, signal):
        raise NotImplementedError
```

#### Automation Workflow Engine

```python
class WorkflowEngine:
    def run(self, workflow: dict):
        pass
```

### Acceptance criteria

- API Gateway starts as a routing shell
- Agent Runtime contains abstract runtime contracts only
- Strategy Engine contains abstract strategy contracts only
- Automation Engine contains abstract workflow contracts only
- Shared module contains common types only

---

## Phase 4 — Integration Layer

### Objective
Create unified adapters for external tools without implementing full integrations.

### Required integration directions

- `mercury-cli` becomes internal command interface
- `brave-search-mcp-server` becomes MCP tool adapter
- Prepare interfaces for:
  - Make.com
  - Stripe
  - Airtable

### Rules

- Adapters only
- Interfaces only
- No production integration behavior yet

---

## Phase 5 — Agent Routing System

### Objective
Create a deterministic, rule-based agent router.

### Supported agents

- `lead_intelligence`
- `market_research`
- `automation`
- `wealth_strategy`
- `general`

### Rule

Routing must be deterministic and rule-based.

No LLM routing yet.

### Example

```python
def route_task(task_type: str):
    if task_type == "lead_intelligence":
        return LeadIntelligenceAgent()
    if task_type == "wealth_strategy":
        return StrategyAgent()
```

### Acceptance criteria

- explicit router module exists
- routing is deterministic
- routing is based on task type only
- no AI inference layer in routing

---

## Phase 6 — Strategy Engine Consolidation

### Objective
Merge strategy forks into one unified strategy engine.

### Required work

Consolidate:
- `wealth-bot`
- `wealth-bot-djt`

### Required components

- `BaseStrategy`
- `StrategyRegistry`
- plugin strategy system

### Rule

Do not preserve `wealth-bot-djt` as a separate engine.

It must become a plugin strategy module.

---

## Phase 7 — Admin Dashboard

### Objective
Create a control-plane frontend that consumes the API Gateway.

### Requirements

Build a Next.js admin dashboard with:

- Agent execution panel
- Workflow viewer
- API key management UI
- Basic analytics dashboard

### Rules

- No backend logic inside frontend
- Frontend must consume APIs only
- No direct business logic in UI modules

---

## Phase 8 — Analytics Pipeline

### Objective
Create a lightweight event system.

### Required events

- `agent_run`
- `workflow_executed`
- `api_request`

### Storage

- PostgreSQL

### Rule

No Kafka or heavy infrastructure yet.

---

## Phase 9 — System Boot Sequence

### Objective
Create a bootstrap path for bringing the OS online in the correct order.

### Required boot sequence

1. Load API Gateway
2. Initialize Agent Registry
3. Register Strategies
4. Load Tools (MCP and CLI adapters)
5. Connect database
6. Start logging system

### Acceptance criteria

A bootstrap script or module exists that documents or orchestrates this order.

---

## Execution Order

Copilot should execute in this order:

1. Monorepo shell
2. Migration map
3. Core runtime skeleton
4. Integration adapters
5. Agent router
6. Strategy consolidation primitives
7. Admin dashboard shell
8. Analytics event skeleton
9. Boot sequence

---

## Architectural End State

The intended end state is:

```text
FutureWealthBot OS
│
├── API Gateway
├── Agent Runtime
├── Strategy Engine
├── Automation Engine
├── Tooling Layer
├── Admin Dashboard
├── Integrations Layer
├── Shared Modules
├── Infrastructure Layer
└── Database Layer
```

## Why this matters

The current system is a set of multiple competing prototypes.

The target system is:

**one operating system for AI business automation**

## Final instruction to Copilot

When uncertain:
- consolidate instead of expanding
- abstract instead of hardcoding
- define interfaces before behavior
- preserve modularity
- avoid feature creep
