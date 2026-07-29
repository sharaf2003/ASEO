from uuid import uuid4


class CustomerManager:
    """
    ASEO Customer Manager v22.5
    """

    def create(
        self,
        company
    ):

        return {

            "id":
                str(uuid4()),

            "company":
                company,

            "status":
                "active"

        }