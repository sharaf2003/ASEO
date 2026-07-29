from ai_engine.company_memory import (
    AgentPerformanceEngine
)



engine = AgentPerformanceEngine()



engine.register_agent(

    "backend_engineer",

    "Backend Developer"

)



engine.record_result(

    "backend_engineer",

    True,

    95

)



engine.record_result(

    "backend_engineer",

    True,

    98

)



engine.record_result(

    "backend_engineer",

    False,

    60

)



print({

    "profile":

        engine.store.get(

            "backend_engineer"

        ).to_dict(),


    "ranking":

        engine.ranking()

})