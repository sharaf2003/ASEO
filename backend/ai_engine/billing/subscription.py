from datetime import datetime
from uuid import uuid4



class Subscription:
    """
    ASEO Customer Subscription v19.5
    """



    def __init__(
        self,
        customer_id,
        plan
    ):


        self.id = str(uuid4())

        self.customer_id = customer_id

        self.plan = plan

        self.status = "active"

        self.created_at = datetime.now()



    def to_dict(self):

        return {


            "id":
                self.id,


            "customer_id":
                self.customer_id,


            "plan":
                self.plan.name,


            "status":
                self.status,


            "created_at":
                self.created_at.isoformat()

        }