class HealthMonitor:
    """
    ASEO Company Health Monitor v20.9
    """

    def calculate(
        self,
        data
    ):

        scores = []


        for value in data.values():

            if isinstance(value, (int, float)):

                scores.append(value)



        health = (
            sum(scores) / len(scores)
            if scores
            else 0
        )


        return {

            "company_health":
                round(health, 2),

            "status":
                "healthy"
                if health >= 80
                else
                "needs_attention"

        }