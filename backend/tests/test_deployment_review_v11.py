from ai_engine.agents.deployment_agent.agent import DeploymentAgent



print("===================")
print("DEPLOYMENT REVIEW ASEO v11")
print("===================")



agent = DeploymentAgent()



result = agent.run(

    "app"

)



print(result)