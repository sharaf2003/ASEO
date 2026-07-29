from ai_engine.storage import (
    PersistentMemory
)

from ai_engine.memory_intelligence import (
    MemoryRetriever
)



memory = PersistentMemory()



memory.remember(

    {
        "project":
            "Ecommerce Backend",

        "technology":
            "FastAPI PostgreSQL",

        "score":
            95
    }

)



retriever = MemoryRetriever()



result = retriever.retrieve(

    "Build ecommerce backend"

)



print(result)