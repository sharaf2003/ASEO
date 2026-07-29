from ai_engine.agents.security_agent.agent import SecurityAgent



print("===================")
print("SECURITY REVIEW ASEO v11")
print("===================")



agent = SecurityAgent()



result = agent.run(

    "app"

)



print(result)