from ai_engine.collaboration import (
    AgentMessage,
    CollaborationManager
)



manager = CollaborationManager()



message = AgentMessage(

    sender="planning",

    receiver="coding",

    message_type="architecture_ready",

    data={

        "framework":
            "FastAPI",

        "database":
            "PostgreSQL"

    }

)



print(

    manager.send(

        message

    )

)



print(

    manager.history()

)