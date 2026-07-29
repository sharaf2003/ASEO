from ai_engine.cfo_intelligence import (
    CFOAgent
)



cfo = CFOAgent()



result = cfo.analyze_project(

    {

        "name":
        "Ecommerce Platform",

        "complexity":
        "high"

    },


    [

        "backend_engineer",

        "database_engineer",

        "security_engineer"

    ]

)



print(result)