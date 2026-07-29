from ai_engine.autonomous_decision import (
    AutonomousDecisionEngine
)



engine = AutonomousDecisionEngine()



result = engine.decide(

    "Build ecommerce platform",


    [

        "memory",

        "agents",

        "brain",

        "improvement"

    ]

)



print(result)