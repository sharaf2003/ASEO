from app.database.session import SessionLocal
from app.agents.architect_agent import ArchitectAgent
from app.shared.models.execution import ExecutionContext


db = SessionLocal()


agent = ArchitectAgent(
    db=db
)


context = ExecutionContext(
    id=1,
    metadata={
        "planner_result": {
            "requirements": "Build SaaS platform"
        }
    }
)


result = agent.run(context)


print("\nAgent:")
print(result["agent"])


print("\nKnowledge Used:")
print(result["knowledge_used"])


print("\nArchitecture:")
print(result["architecture"])

print("\nPrevious Architectures:")
print(result.get("previous_architectures"))


print("\nDecisions:")
for decision in result["architecture_decisions"]:
    print(decision)


print("\nDecision Saved:")
print(result.get("decision_saved"))