from ai_engine.self_improvement import (
    SelfImprovementEngine
)



engine = SelfImprovementEngine()



result = engine.improve(

    "Generate backend API",

    "Generate scalable FastAPI backend API with JWT authentication",

    75,

    95

)



print(result)



print(

    engine.history()

)