from ai_engine.orchestrator.agent_orchestrator import AgentOrchestrator



print("===================")
print("ASEO FULL PIPELINE v12")
print("===================")



orchestrator = AgentOrchestrator()



result = orchestrator.run(

    "sample_requirement.txt",

    "ASEO Demo Project"

)



print(result)