from abc import ABC, abstractmethod

from shared.types import WorkflowDefinition, WorkflowExecutionRequest, WorkflowExecutionResult


class WorkflowExecutor(ABC):
    @abstractmethod
    async def register(self, workflow: WorkflowDefinition) -> None:
        raise NotImplementedError

    @abstractmethod
    async def execute(self, request: WorkflowExecutionRequest) -> WorkflowExecutionResult:
        raise NotImplementedError

    @abstractmethod
    async def status(self, execution_id: str) -> WorkflowExecutionResult | None:
        raise NotImplementedError
