from ai_engine.company_memory import (
    CompanyMemoryEngine
)



memory = CompanyMemoryEngine()



stored = memory.remember(

    "Ecommerce Platform",

    "FastAPI + PostgreSQL + Layered",

    {

        "quality":
        100,

        "success":
        True

    }

)



retrieved = memory.recall(

    "Ecommerce"

)



print({

    "stored":
        stored,

    "retrieved":
        retrieved,

    "knowledge_used":
        len(retrieved) > 0

})