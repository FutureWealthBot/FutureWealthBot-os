# Migration Map

This document locks the repository consolidation plan for **FUTUREWEALTHBOT OS** into the codebase.

## Objective

Consolidate the current FutureWealthBot repository ecosystem into a single architecture-first monorepo.

## Canonical Target Repository

- `FutureWealthBot/FutureWealthBot-os`

This repository is the canonical destination for shared runtime architecture, orchestration contracts, and future module consolidation.

## Repository-to-Module Mapping

| Existing repository | Target module/location | Notes |
|---|---|---|
| `FutureWealthBot/api-factory` | `apps/api-gateway/`, `shared/`, `docs/` | Source for API factory patterns, OpenAPI workflows, SDK generation concepts, and roadmap alignment. |
| `FutureWealthBot/FutureWealthBot-GPT` | `engines/agent-runtime/` | Source for agent behavior, orchestration contracts, and GPT-facing abstractions. |
| `FutureWealthBot/wealth-bot` | `engines/strategy-engine/` | Primary source for wealth strategy engine consolidation. |
| `FutureWealthBot/wealth-bot-djt` | `engines/strategy-engine/plugins/` | Must be preserved as a plugin strategy module, not a separate engine. |
| `FutureWealthBot/SafeNow` | `apps/safenow/` | Isolated application module pending integration boundary review. |

## Target Monorepo Zones

```text
apps/
  api-gateway/
  admin-dashboard/
  safenow/

engines/
  agent-runtime/
  strategy-engine/
  automation-engine/

integrations/
  brave-search-mcp/

tools/
  mercury-cli/

shared/
infra/
db/
docs/
```

## Consolidation Rules

1. Do not create new repositories for core runtime work.
2. Consolidate shared abstractions before migrating business logic.
3. Prefer base classes, registries, interfaces, and schemas before implementations.
4. All future engines must integrate through the API Gateway boundary.
5. Strategy forks must converge under one strategy engine with plugin support.
6. App-specific modules may remain isolated temporarily, but their contracts must be documented here.

## Duplication Notes

Current duplication risk areas include:

- agent/task orchestration logic spread across GPT-oriented repositories
- strategy evaluation logic spread across `wealth-bot` and `wealth-bot-djt`
- API-generation patterns that may overlap between API factory and future gateway scaffolding
- analytics, automation, and control-plane concepts that may reappear in multiple repos under different names

## Consolidation Risks

### 1. Naming drift

Different repositories may describe similar concepts with different names:
- agents
- automations
- workflows
- strategies
- operators

Mitigation:
- normalize naming in `shared/` first
- adopt canonical contracts before code migration

### 2. Runtime coupling

Some existing projects may mix UI, logic, and orchestration.

Mitigation:
- extract interfaces first
- isolate transport layers from execution logic
- route cross-module behavior through the API Gateway boundary

### 3. Fork preservation pressure

There may be pressure to keep `wealth-bot-djt` as a standalone subsystem.

Mitigation:
- preserve identity as a plugin, not a runtime root
- move unique behavior into plugin modules under `engines/strategy-engine/plugins/`

### 4. Premature feature migration

Migrating features before contracts can recreate fragmentation inside the monorepo.

Mitigation:
- move documentation and abstractions first
- delay business logic until architecture and boundaries are stable

## Isolation Notes

### SafeNow

`SafeNow` should remain isolated during initial consolidation until:
- its integration boundaries are documented
- its dependencies are mapped
- its coupling to the shared runtime is understood

Target state:
- keep it under `apps/safenow/`
- expose integration via documented interfaces only

## Migration Sequence

1. lock architectural directives in `docs/`
2. establish shared types and base interfaces
3. establish deterministic routing and registries
4. create plugin and adapter boundaries
5. document boot/runtime initialization order
6. begin controlled repo-by-repo migration into target modules
7. migrate business logic only after contracts stabilize

## Definition of Success

The consolidation is successful when:

- runtime boundaries are centralized in `FutureWealthBot-os`
- strategy systems are unified under one engine
- agent orchestration lives under one runtime contract model
- external tools are adapters, not parallel control planes
- new development happens inside the monorepo instead of new fragmented repositories
