from collections.abc import Iterable

from .base import BaseStrategy


class StrategyRegistry:
    def __init__(self) -> None:
        self._strategies: dict[str, BaseStrategy] = {}

    def register(self, strategy: BaseStrategy) -> None:
        self._strategies[strategy.strategy_id] = strategy

    def get(self, strategy_id: str) -> BaseStrategy | None:
        return self._strategies.get(strategy_id)

    def list_ids(self) -> list[str]:
        return sorted(self._strategies.keys())

    def list_strategies(self) -> Iterable[BaseStrategy]:
        return self._strategies.values()
