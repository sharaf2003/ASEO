from ai_engine.agents.quality_agent.agent import QualityAgent



print("===================")
print("QUALITY REVIEW ASEO v11")
print("===================")



agent = QualityAgent()



result = agent.run(

    "app"

)



print(result)