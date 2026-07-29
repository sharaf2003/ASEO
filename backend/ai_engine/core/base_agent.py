from abc import ABC, abstractmethod
from datetime import datetime



class BaseAgent(ABC):
    """
    Base class for all ASEO AI Agents.

    Every agent must inherit from this class.

    Examples:

    - Document Agent
    - Planning Agent
    - Coding Agent
    - Delivery Agent

    """



    def __init__(
        self,
        name: str,
        description: str
    ):


        self.name = name

        self.description = description

        self.status = "initialized"

        self.created_at = datetime.now()



    # ==================================
    # Execute Agent Task
    # ==================================

    @abstractmethod
    def execute(
        self,
        task
    ):

        """
        Main execution function.

        Every agent must implement it.
        """

        pass



    # ==================================
    # Agent Status
    # ==================================

    def update_status(
        self,
        status
    ):

        self.status = status



    # ==================================
    # Agent Information
    # ==================================

    def info(self):

        return {

            "name":
                self.name,

            "description":
                self.description,

            "status":
                self.status,

            "created_at":
                str(self.created_at)

        }