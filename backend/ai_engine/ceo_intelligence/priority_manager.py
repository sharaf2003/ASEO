class PriorityManager:
    """
    ASEO Priority Manager v20.5
    """

    def determine(
        self,
        analysis
    ):


        if analysis["status"] == "healthy":

            return {

                "priority":
                    "Scale successful systems",

                "reason":
                    "Company performance is strong"

            }



        return {

            "priority":
                "Improve weak areas",

            "reason":
                "Performance requires optimization"

        }