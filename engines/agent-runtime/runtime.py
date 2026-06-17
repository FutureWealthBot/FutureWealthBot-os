from abc import ABC, abstractmethod

from shared.types import AgentTask


class AgentRuntime(ABC):
    @abstractmethod
    async def submit_task(self, task: AgentTask) -> str:
        raise NotImplementedError

    @abstractmethod
    async def get_task(self, task_id: str) -> AgentTask | None:
        raise NotImplementedError

    @abstractmethod
    async def cancel_task(self, task_id: str) -> bool:
        raise NotImplementedError
