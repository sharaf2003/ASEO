from ai_engine.agents.delivery_agent.agent import DeliveryAgent



print("===================")

print("DELIVERY AGENT")

print("===================")



agent = DeliveryAgent()



result = agent.run(

    "generated_project",

    "Clinic_Management_System"

)



print(result)