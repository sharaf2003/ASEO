from uuid import uuid4



class IncidentManager:
    """
    ASEO Incident Manager v22.3
    """

    def detect(
        self,
        health
    ):

        if health["status"] != "healthy":

            return {

                "id":
                    str(uuid4()),

                "severity":
                    "high",

                "status":
                    "open"

            }


        return {

            "incident":
                None,

            "status":
                "no_incident"

        }