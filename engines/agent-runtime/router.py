from .base_agent import BaseAgent


class GeneralAgent(BaseAgent):
    def run(self, input: dict) -> dict:
        return {}


class LeadIntelligenceAgent(BaseAgent):
    def run(self, input: dict) -> dict:
        return {}


class MarketResearchAgent(BaseAgent):
    def run(self, input: dict) -> dict:
        return {}


class AutomationAgent(BaseAgent):
    def run(self, input: dict) -> dict:
        return {}


class WealthStrategyAgent(BaseAgent):
    def run(self, input: dict) -> dict:
        return {}


def route_task(task_type: str) -> BaseAgent:
    if task_type == "lead_intelligence":
        return LeadIntelligenceAgent()
    if task_type == "market_research":
        return MarketResearchAgent()
    if task_type == "automation":
        return AutomationAgent()
    if task_type == "wealth_strategy":
        return WealthStrategyAgent()
    return GeneralAgent()
