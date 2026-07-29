from ai_engine.orchestrator.v13_orchestrator import (
    ASEOOrchestratorV13
)



class TestAgent:


    def execute(
        self,
        task
    ):

        return {

            "result":
            "done"

        }





orchestrator = ASEOOrchestratorV13()



orchestrator.register_agent(

    "test",

    TestAgent(),

    "1.0"

)



print(

    orchestrator.agents()

)



print(

    orchestrator.run_agent(

        "test",

        {}

    )

)



print(

    orchestrator.events()

)