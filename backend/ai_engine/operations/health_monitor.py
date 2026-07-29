class HealthMonitor:
    """
    ASEO Health Monitor v22.3
    """

    def check(
        self,
        system
    ):

        return {

            "system":
                system,

            "status":
                "healthy",

            "availability":
                99.9

        }