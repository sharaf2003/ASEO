class SkillManager:
    """
    ASEO Skill Manager v22.7
    """

    def match(
        self,
        agent,
        required_skill
    ):

        return {

            "agent":
                agent["agent"],

            "skill":
                required_skill,

            "matched":
                required_skill in agent["skills"]

        }