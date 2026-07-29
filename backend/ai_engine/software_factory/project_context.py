from datetime import datetime
from uuid import uuid4



class ProjectContext:
    """
    ASEO Software Factory Project Context v15
    """



    def __init__(
        self,
        requirement
    ):


        self.id = str(uuid4())


        self.requirement = requirement


        self.architecture = None


        self.files = []


        self.status = "created"


        self.created_at = datetime.now().isoformat()





    def set_architecture(
        self,
        architecture
    ):

        self.architecture = architecture





    def add_file(
        self,
        filename
    ):

        self.files.append(

            filename

        )





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


            "files":

                self.files,


            "status":

                self.status,


            "created_at":

                self.created_at

        }