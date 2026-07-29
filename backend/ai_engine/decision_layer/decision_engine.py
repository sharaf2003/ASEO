from .architecture_selector import (
    ArchitectureSelector
)

from .agent_selector import (
    AgentSelector
)

from .strategy_selector import (
    StrategySelector
)




class ASEODecisionEngine:
    """
    ASEO AI Decision Engine v20.1
    """



    def __init__(
        self
    ):

        self.architecture = ArchitectureSelector()

        self.agents = AgentSelector()

        self.strategy = StrategySelector()





    def decide(
        self,
        requirement
    ):


        architecture = self.architecture.select(

            requirement

        )


        agents = self.agents.select(

            requirement

        )


        strategy = self.strategy.select(

            requirement

        )



        return {


            "requirement":

                requirement,


            "architecture":

                architecture,


            "agents":

                agents,


            "strategy":

                strategy,


            "confidence":

                0.98

        }