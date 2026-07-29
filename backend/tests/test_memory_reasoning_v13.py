from ai_engine.intelligence.memory import (
    MemoryManager
)

from ai_engine.intelligence.reasoning import (
    MemoryReasoningEngine
)



memory = MemoryManager()



memory.remember(

    "database_choice",

    "Use PostgreSQL for scalable backend",

    "architecture",

    0.95

)



engine = MemoryReasoningEngine(

    memory

)



result = engine.analyze(

    "Build ecommerce backend system"

)



print(result)