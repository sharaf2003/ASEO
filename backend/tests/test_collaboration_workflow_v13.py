from ai_engine.collaboration import (
    AgentMessage
)

from ai_engine.collaboration.workflow import (
    CollaborationWorkflow
)



class CodingAgent:


    def execute(
        self,
        data
    ):

        return {

            "files_generated":10,

            "framework":
                data["framework"]

        }




workflow = CollaborationWorkflow()



workflow.register_agent(

    "coding",

    CodingAgent()

)



message = AgentMessage(

    "planning",

    "coding",

    "architecture_ready",

    {
        "framework":"FastAPI"
    }

)



print(

    workflow.process(

        message

    )

)