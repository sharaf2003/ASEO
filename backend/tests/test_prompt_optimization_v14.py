from ai_engine.optimization import (
    PromptOptimizer
)



optimizer = PromptOptimizer()



result = optimizer.optimize(

    "Generate backend API",

    "Add authentication"

)



print(result)



print(

    optimizer.history()

)