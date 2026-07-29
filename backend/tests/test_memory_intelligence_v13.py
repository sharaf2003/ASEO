from ai_engine.intelligence.memory import (
    MemoryManager
)



memory = MemoryManager()



memory.remember(

    "database_choice",

    "Use PostgreSQL for scalable backend",

    "architecture",

    0.95

)



memory.remember(

    "authentication",

    "Use JWT authentication",

    "security",

    0.90

)



print(

    memory.recall(

        "PostgreSQL"

    )

)



print(

    memory.memories()

)