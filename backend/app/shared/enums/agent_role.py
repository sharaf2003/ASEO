from enum import Enum


class AgentRole(str, Enum):
    """
    Roles of autonomous ASEO agents.
    """

    PLANNER = "PLANNER"

    ARCHITECT = "ARCHITECT"

    DEVELOPER = "DEVELOPER"

    TESTER = "TESTER"

    DEPLOYMENT = "DEPLOYMENT"