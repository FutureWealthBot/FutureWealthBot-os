from abc import ABC, abstractmethod
from typing import Any


class WorkflowEngine(ABC):
    @abstractmethod
    def run(self, workflow: dict[str, Any]) -> None:
        raise NotImplementedError
