class AgentSelector:
    """
    ASEO Agent Selector v22.7
    """

    def select(
        self,
        agents,
        skill
    ):


        for agent in agents:

            if skill in agent["skills"]:

                return {

                    "selected":
                        agent["agent"],

                    "reason":
                        "Skill matched"

                }


        return {

            "selected":
                None,

            "reason":
                "No matching agent"

        }