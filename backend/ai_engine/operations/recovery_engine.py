class RecoveryEngine:
    """
    ASEO Recovery Engine v22.3
    """

    def recover(
        self,
        incident
    ):

        if incident.get(
            "incident"
        ):

            return {

                "action":
                    "restart_service",

                "status":
                    "recovered"

            }


        return {

            "action":
                "none",

            "status":
                "stable"

        }