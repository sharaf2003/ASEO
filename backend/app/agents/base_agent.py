from abc import ABC, abstractmethod



class BaseAgent(ABC):

    """
    Base class for all ASEO agents.
    """


    @abstractmethod
    def run(
        self,
        context: dict
    ) -> dict:

        pass