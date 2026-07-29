from ai_engine.intelligence.reasoning import (
    ReasoningEngine
)



engine = ReasoningEngine()



decision = engine.analyze(

    "Build ecommerce backend system"

)



print(

    decision.to_dict()

)