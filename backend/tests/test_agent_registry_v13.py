from ai_engine.registry import (
    AgentRegistry,
    AgentInfo
)



class SecurityAgent:
    pass



registry = AgentRegistry()



registry.register(

    AgentInfo(
        "security",
        SecurityAgent(),
        "1.0"
    )

)



print(

    registry.list_agents()

)