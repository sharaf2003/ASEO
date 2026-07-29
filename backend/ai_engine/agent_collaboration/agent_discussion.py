class AgentDiscussion:
    """
    ASEO Agent Discussion Engine v22.8
    """

    def discuss(
        self,
        task,
        agents
    ):

        opinions = []


        for agent in agents:

            opinions.append(

                {

                    "agent":
                        agent,

                    "opinion":
                        f"{agent} recommends solution"

                }

            )


        return {

            "task":
                task,

            "opinions":
                opinions

        }