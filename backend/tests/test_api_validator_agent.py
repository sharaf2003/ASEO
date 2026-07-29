from ai_engine.agents.api_validator_agent.agent import APIValidatorAgent



print("===================")
print("API VALIDATOR AGENT")
print("===================")



agent = APIValidatorAgent()



result = agent.run(

    "generated_project"

)



print(result)