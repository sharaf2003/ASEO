from datetime import datetime
from uuid import uuid4



class RequestManager:
    """
    ASEO Request Manager v20.0
    """

    def create_request(
        self,
        request
    ):

        return {

            "id":
                str(uuid4()),

            "request":
                request,

            "status":
                "received",

            "created_at":
                datetime.now().isoformat()

        }