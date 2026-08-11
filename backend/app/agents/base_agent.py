from abc import ABC, abstractmethod

from app.shared.models.execution import ExecutionContext



class BaseAgent(ABC):

    """
    Base class for all ASEO autonomous agents.

    Provides a unified execution contract
    for Planner, Architect, Developer,
    Tester and Deployment agents.
    """



    name: str = "BaseAgent"

    role: str = "generic"



    def execute(

        self,

        context: ExecutionContext

    ) -> dict:

        """
        Standard agent execution wrapper.
        """


        self.validate_context(

            context

        )


        result = self.run(

            context

        )


        return result



    def validate_context(

        self,

        context: ExecutionContext

    ):

        """
        Validate execution context.
        """


        if not context:

            raise ValueError(

                "Execution context is required"

            )



    @abstractmethod
    def run(

        self,

        context: ExecutionContext

    ) -> dict:

        """
        Agent implementation logic.

        Must be implemented by every agent.
        """

        pass