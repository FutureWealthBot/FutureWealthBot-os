from abc import ABC, abstractmethod
from typing import Any


class BaseAgent(ABC):
    @abstractmethod
    def run(self, input: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError
