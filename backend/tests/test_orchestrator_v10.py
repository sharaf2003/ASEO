from ai_engine.orchestrator.agent_orchestrator import AgentOrchestrator


print("===================")
print("ASEO ORCHESTRATOR v10")
print("===================")



orchestrator = AgentOrchestrator()



result = orchestrator.run(

    "requirements.txt",

    "Clinic Management System"

)



print(result)



print("\n===================")
print("SUMMARY")
print("===================")



print("Status:",
      result.get("status"))



print("Agent:",
      result.get("agent_info"))



print("\nSecurity:")
print(result.get("security"))



print("\nQuality:")
print(result.get("quality"))



print("\nOptimization:")
print(result.get("optimization"))



print("\nSenior Review:")
print(result.get("senior_review"))



print("\nDeployment:")
print(result.get("deployment"))



print("\nDocumentation:")
print(result.get("documentation"))



print("\nDelivery:")
print(result.get("delivery"))