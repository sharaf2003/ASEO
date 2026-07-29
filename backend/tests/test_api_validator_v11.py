from ai_engine.agents.api_validator_agent.agent import APIValidatorAgent


print("===================")
print("API VALIDATOR ASEO v11")
print("===================")


agent = APIValidatorAgent()


result = agent.run(
    "app"
)


print(result)