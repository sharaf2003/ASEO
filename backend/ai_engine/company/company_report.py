from datetime import datetime
from uuid import uuid4




class CompanyReport:
    """
    ASEO Company Report v18.1
    """



    def __init__(
        self,
        request,
        departments
    ):


        self.id = str(uuid4())


        self.request = request


        self.departments = departments


        self.status = "company_ready"


        self.created_at = datetime.now().isoformat()





    def to_dict(
        self
    ):


        return {


            "id":

                self.id,


            "request":

                self.request,


            "status":

                self.status,


            "departments":

                self.departments,


            "created_at":

                self.created_at

        }