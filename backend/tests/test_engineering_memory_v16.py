from ai_engine.engineering_memory import (
    EngineeringMemoryEngine
)



memory = EngineeringMemoryEngine()



saved = memory.remember(

    "Ecommerce Backend",

    "FastAPI + PostgreSQL + Layered",

    {
        "score":95,
        "success":True
    }

)



retrieved = memory.recall(

    "FastAPI"

)



print(

    {

        "stored":
            saved,


        "retrieved":
            retrieved,


        "knowledge_used":
            len(retrieved) > 0,


        "recommendation":
            "Use previous successful architecture"

    }

)