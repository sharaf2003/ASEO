from ai_engine.agents.delivery_agent.agent import DeliveryAgent



print("===================")
print("DELIVERY REVIEW ASEO v11")
print("===================")



agent = DeliveryAgent()



result = agent.run(

    "app",

    "ASEO_Project"

)



print(result)