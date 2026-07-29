from ai_engine.continuous_improvement import (
    ImprovementManager
)



manager = ImprovementManager()



result = manager.improve(

    {

        "quality":
            96

    },

    85

)



print(result)