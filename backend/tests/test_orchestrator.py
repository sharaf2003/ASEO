from ai_engine.orchestrator.agent_orchestrator import AgentOrchestrator



print("===================")
print("ASEO ORCHESTRATOR")
print("===================")



orchestrator = AgentOrchestrator()



result = orchestrator.run(
    "requirements.txt"
)



print(result)