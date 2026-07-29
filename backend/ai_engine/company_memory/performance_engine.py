from .agent_profile import (
    AgentProfile
)


from .performance_store import (
    PerformanceStore
)





class AgentPerformanceEngine:
    """
    ASEO Agent Performance Engine v19.2

    Evaluates company agents.
    """



    def __init__(
        self
    ):


        self.store = PerformanceStore()






    def register_agent(
        self,
        name,
        role
    ):


        profile = AgentProfile(

            name,

            role

        )


        self.store.save(

            profile

        )


        return profile.to_dict()






    def record_result(
        self,
        agent,
        success,
        quality
    ):


        profile = self.store.get(

            agent

        )


        if not profile:


            raise Exception(

                "Agent not registered"

            )



        profile.update(

            success,

            quality

        )


        return profile.to_dict()






    def ranking(
        self
    ):


        return sorted(

            self.store.all(),

            key=lambda x:

                x["quality_score"],

            reverse=True

        )