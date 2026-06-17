from abc import ABC, abstractmethod

from shared.types import StrategyContext, StrategySignal


class BaseStrategy(ABC):
    def __init__(self, strategy_id: str) -> None:
        self.strategy_id = strategy_id

    @abstractmethod
    async def initialize(self, context: StrategyContext) -> None:
        raise NotImplementedError

    @abstractmethod
    async def evaluate(self, context: StrategyContext) -> list[StrategySignal]:
        raise NotImplementedError

    @abstractmethod
    async def shutdown(self, context: StrategyContext) -> None:
        raise NotImplementedError
