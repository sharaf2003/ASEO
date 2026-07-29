from ai_engine.agents.quality_agent.agent import QualityAgent



print("===================")
print("QUALITY AGENT v1.1")
print("===================")



agent = QualityAgent()



result = agent.run(

    "generated_project"

)



print(result)