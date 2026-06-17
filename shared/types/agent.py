from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class AgentTaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass(slots=True)
class AgentTask:
    id: str
    agent_name: str
    status: AgentTaskStatus = AgentTaskStatus.PENDING
    input_payload: dict[str, Any] = field(default_factory=dict)
