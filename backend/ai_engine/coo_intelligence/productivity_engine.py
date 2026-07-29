class ProductivityEngine:
    """
    ASEO Productivity Engine v20.8
    """

    def measure(
        self,
        team
    ):


        productivity = (

            team["completed"]

            /

            team["total"]

        ) * 100



        return {

            "productivity":
                round(productivity,2),

            "team_status":
                "productive"
                if productivity >= 80
                else
                "needs_improvement"

        }