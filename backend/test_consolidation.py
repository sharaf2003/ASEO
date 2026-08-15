from app.intelligence.memory.memory_consolidation import (
    MemoryConsolidationEngine
)



engine = MemoryConsolidationEngine()



memories = [

    {
        "architecture":{
            "backend":{
                "technology":"FastAPI"
            },
            "frontend":{
                "technology":"React"
            }
        },

        "usage_count":5,

        "success_score":1

    },


    {
        "architecture":{
            "backend":{
                "technology":"FastAPI"
            },
            "frontend":{
                "technology":"React"
            }
        },

        "usage_count":3,

        "success_score":1

    }

]



result = engine.consolidate(
    memories
)


print(result)