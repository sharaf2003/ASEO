from ai_engine.orchestrator.agent_orchestrator import AgentOrchestrator


print("===================")
print("ASEO ORCHESTRATOR v12")
print("===================")


orchestrator = AgentOrchestrator()


print(orchestrator.agent_info)


print(
    "Registered Agents:"
)

print(
    list(orchestrator.agents.keys())
)