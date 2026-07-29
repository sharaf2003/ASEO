from ai_engine.orchestrator.agent_orchestrator import AgentOrchestrator



print("===================")
print("ASEO ORCHESTRATOR v11")
print("===================")



orchestrator = AgentOrchestrator()



result = orchestrator.run(

    "requirements.txt",

    "Clinic Management System"

)



print(result)



print("\n===================")
print("V11 SUMMARY")
print("===================")



print("\nStatus:")
print(result.get("status"))



print("\nAgent Info:")
print(result.get("agent_info"))



print("\nArchitecture Review:")
print(result.get("architecture"))



print("\nDatabase Review:")
print(result.get("database_review"))



print("\nAPI Validation:")
print(result.get("api_validation"))



print("\nSenior Review:")
print(result.get("senior_review"))



print("\nDeployment:")
print(result.get("deployment"))