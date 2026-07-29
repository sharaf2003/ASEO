from ai_engine.orchestrator.agent_orchestrator import AgentOrchestrator


print("===================")
print("ASEO ORCHESTRATOR v8")
print("===================")


orchestrator = AgentOrchestrator()


result = orchestrator.run(
    "requirements.txt",
    "Clinic Management System"
)


print(result)