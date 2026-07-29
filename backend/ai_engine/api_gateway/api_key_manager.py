from uuid import uuid4


class APIKeyManager:
    """
    ASEO API Key Manager v22.6
    """

    def create(
        self,
        customer
    ):

        return {

            "customer":
                customer,

            "api_key":
                str(uuid4()),

            "status":
                "active"

        }