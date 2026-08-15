from app.database.connection import SessionLocal
from app.agents.architect_agent import ArchitectAgent
from app.shared.models.execution import ExecutionContext


db = SessionLocal()


agent = ArchitectAgent(
    db=db
)


context = ExecutionContext()


context.metadata["planner_result"] = {

    "request":
    "Build a mobile ecommerce application with Flutter and Firebase"

}


result = agent.run(context)



print("==============================")
print("ARCHITECTURE")
print("==============================")

print(
    result.get(
        "architecture"
    )
)



print("==============================")
print("PREVIOUS ARCHITECTURES")
print("==============================")

print(
    result.get(
        "previous_architectures",
        []
    )
)



print("==============================")
print("ARCHITECTURE DECISION")
print("==============================")

architecture_decision = result.get(
    "architecture_decision",
    {}
)


print(
    architecture_decision
)



print("==============================")
print("MEMORY VALUES USED")
print("==============================")

print(
    "Memory Score:",
    architecture_decision.get(
        "memory_score"
    )
)


print(
    "Historical Success:",
    architecture_decision.get(
        "historical_success"
    )
)


print(
    "Memory Strength:",
    architecture_decision.get(
        "memory_strength"
    )
)


print(
    "Performance Confidence:",
    architecture_decision.get(
        "performance_confidence"
    )
)


print(
    "Adaptive Weights:",
    architecture_decision.get(
        "adaptive_weights"
    )
)



print("==============================")
print("FINAL SCORE")
print("==============================")

print(
    result.get(
        "final_decision_score"
    )
)



print("==============================")
print("ARCHITECTURE EVOLUTION")
print("==============================")

architecture_evolution = result.get(
    "architecture_evolution"
)


print(
    architecture_evolution
)



if architecture_evolution:


    print("==============================")
    print("EVOLUTION IMPROVEMENTS")
    print("==============================")


    print(
        architecture_evolution.get(
            "improvements",
            []
        )
    )


    print("==============================")
    print("EVOLUTION RISKS")
    print("==============================")


    print(
        architecture_evolution.get(
            "risks",
            []
        )
    )


    print("==============================")
    print("FUTURE RECOMMENDATIONS")
    print("==============================")


    print(
        architecture_evolution.get(
            "future_recommendations",
            []
        )
    )



db.close()