from ai_engine.coo_intelligence import (
    COOAgent
)



coo = COOAgent()



result = coo.analyze_operations(

    {

        "completed_tasks":
            20,

        "pending_tasks":
            5

    },


    {

        "completed":
            25,

        "total":
            30

    }

)



print(result)