from datetime import datetime
from uuid import uuid4



class ArchitectureBlueprint:
    """
    ASEO Architecture Blueprint v15
    """



    def __init__(
        self,
        requirement
    ):


        self.id = str(uuid4())


        self.requirement = requirement


        self.architecture = None


        self.framework = None


        self.database = None


        self.modules = []


        self.created_at = datetime.now().isoformat()





    def to_dict(
        self
    ):

        return {

            "id":

                self.id,


            "requirement":

                self.requirement,


            "architecture":

                self.architecture,


            "framework":

                self.framework,


            "database":

                self.database,


            "modules":

                self.modules,


            "created_at":

                self.created_at

        }