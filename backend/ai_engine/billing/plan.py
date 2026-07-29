from datetime import datetime
from uuid import uuid4



class Plan:
    """
    ASEO Subscription Plan v19.5
    """



    def __init__(
        self,
        name,
        price,
        max_projects,
        max_agents
    ):

        self.id = str(uuid4())

        self.name = name

        self.price = price

        self.max_projects = max_projects

        self.max_agents = max_agents

        self.created_at = datetime.now()



    def to_dict(self):

        return {

            "id":
                self.id,

            "plan":
                self.name,

            "price":
                self.price,

            "max_projects":
                self.max_projects,

            "max_agents":
                self.max_agents

        }