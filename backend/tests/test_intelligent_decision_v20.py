from ai_engine.intelligent_decision import (
    IntelligentDecisionEngine
)



engine = IntelligentDecisionEngine()



memories = [

    {

        "project":

        "Ecommerce Platform",


        "decision":

        "FastAPI + PostgreSQL + Layered",


        "result":

        {

            "quality":

            100

        }

    }

]



result = engine.decide(

    "Build ecommerce platform",

    memories

)



print(result)