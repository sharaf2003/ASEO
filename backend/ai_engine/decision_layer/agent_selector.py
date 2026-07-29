class AgentSelector:
    """
    ASEO Agent Selector v20.1
    """

    def select(
        self,
        requirement
    ):


        agents = [

            "backend_engineer",

            "database_engineer",

            "security_engineer",

            "qa_engineer",

            "devops_engineer"

        ]


        return {

            "selected_agents":
                agents,

            "reason":
                "Selected based on project requirements"

        }