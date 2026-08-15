from dataclasses import dataclass



@dataclass
class AgentExecutionPlan:

    agents: list

    execution_order: list

    reasons: list