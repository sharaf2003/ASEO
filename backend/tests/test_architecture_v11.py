from ai_engine.agents.architecture_agent.agent import ArchitectureAgent


print("===================")
print("ARCHITECTURE ASEO v11")
print("===================")


agent = ArchitectureAgent()


result = agent.run(
    "app"
)


print(result)