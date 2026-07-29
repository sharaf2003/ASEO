from datetime import datetime
from uuid import uuid4



class User:
    """
    ASEO User Entity v19.6
    """



    def __init__(
        self,
        email,
        password,
        role,
        customer_id
    ):


        self.id = str(uuid4())

        self.email = email

        self.password = password

        self.role = role

        self.customer_id = customer_id

        self.created_at = datetime.now()



    def to_dict(
        self
    ):


        return {

            "id":
                self.id,

            "email":
                self.email,

            "role":
                self.role,

            "customer_id":
                self.customer_id,

            "created_at":
                self.created_at.isoformat()

        }