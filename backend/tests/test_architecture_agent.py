from ai_engine.agents.architecture_agent.agent import ArchitectureAgent



print("===================")
print("ARCHITECTURE AGENT")
print("===================")



agent = ArchitectureAgent()



result = agent.run(

    "generated_project"

)



print(result)