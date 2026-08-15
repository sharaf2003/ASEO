from app.intelligence.decision_intelligence.architecture_decision_engine import (
    ArchitectureDecisionEngine
)



reasoning = {

    "recommendation": {

        "recommended_architecture":
            "Firebase Serverless",

        "score":
            0.85

    }

}



memory = {

    "memory_score":0.97,

    "success_score":1.0,

    "memory_strength":0.87

}



engine = ArchitectureDecisionEngine()


result = engine.decide(

    reasoning,

    memory,

    feedback_score=0.95

)



print("==============================")
print("ARCHITECTURE DECISION")
print("==============================")


print(result)