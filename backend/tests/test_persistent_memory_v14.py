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



print(

    memory.recall_all()

)