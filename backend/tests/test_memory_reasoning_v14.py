from ai_engine.memory_reasoning import (
    MemoryReasoner
)


from ai_engine.intelligence.reasoning import (
    ReasoningEngine
)


from ai_engine.storage import (
    PersistentMemory
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



reasoner = MemoryReasoner(

    ReasoningEngine()

)



result = reasoner.analyze(

    "Build ecommerce backend"

)



print(result)