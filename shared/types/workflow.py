from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class WorkflowDefinition:
    id: str
    name: str
    version: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class WorkflowExecutionRequest:
    workflow_id: str
    payload: dict[str, Any] = field(default_factory=dict)
    correlation_id: str | None = None


@dataclass(slots=True)
class WorkflowExecutionResult:
    workflow_id: str
    execution_id: str
    accepted: bool
    status: str
