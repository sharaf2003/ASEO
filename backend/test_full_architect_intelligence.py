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



result = agent.run(
    context
)



print("==============================")
print("FINAL ARCHITECT RESULT")
print("==============================")


print(
    result
)



print("==============================")
print("ARCHITECTURE")
print("==============================")


print(
    result.get(
        "architecture"
    )
)



print("==============================")
print("DECISION SCORE")
print("==============================")


print(
    result.get(
        "final_decision_score"
    )
)



print("==============================")
print("EVOLUTION")
print("==============================")


print(
    result.get(
        "architecture_evolution"
    )
)



print("==============================")
print("MEMORY")
print("==============================")


print(
    result.get(
        "previous_architectures"
    )
)



db.close()