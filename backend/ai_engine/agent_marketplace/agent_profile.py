class AgentProfile:
    """
    ASEO Agent Profile v22.7
    """

    def create(
        self,
        name,
        role,
        skills
    ):

        return {

            "agent":
                name,

            "role":
                role,

            "skills":
                skills,

            "status":
                "available"

        }