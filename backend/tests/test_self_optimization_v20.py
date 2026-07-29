from ai_engine.self_optimization import (
    SelfOptimizationEngine
)



engine = SelfOptimizationEngine()



result = engine.optimize(

    [

        {
            "agent":
            "backend_engineer",

            "quality_score":
            95
        },


        {
            "agent":
            "database_engineer",

            "quality_score":
            88
        },


        {
            "agent":
            "security_engineer",

            "quality_score":
            92
        }

    ],

    95,

    "Build MVP first then scale"

)



print(result)