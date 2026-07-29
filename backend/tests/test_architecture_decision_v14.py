from ai_engine.storage import (
    PersistentMemory
)

from ai_engine.architecture_intelligence import (
    ArchitectureDecisionEngine
)



memory = PersistentMemory()



memory.remember(

    {

        "project":
            "Ecommerce Backend",

        "decision":
            "FastAPI + PostgreSQL",

        "score":
            95

    }

)



engine = ArchitectureDecisionEngine()



result = engine.decide(

    "Build ecommerce platform"

)



print(result)