from datetime import datetime
from uuid import uuid4



class ProjectBlueprint:
    """
    ASEO Project Blueprint v17.1
    """



    def __init__(
        self,
        name,
        architecture,
        framework,
        database,
        modules
    ):


        self.id = str(uuid4())


        self.name = name


        self.architecture = architecture


        self.framework = framework


        self.database = database


        self.modules = modules


        self.created_at = datetime.now().isoformat()





    def to_dict(
        self
    ):

        return {


            "id":
                self.id,


            "project":
                self.name,


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