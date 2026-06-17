from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class StrategyContext:
    strategy_id: str
    execution_id: str
    parameters: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class StrategySignal:
    signal_type: str
    payload: dict[str, Any] = field(default_factory=dict)
