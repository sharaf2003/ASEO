from ai_engine.agents.documentation_agent.agent import DocumentationAgent



print("===================")
print("DOCUMENTATION REVIEW ASEO v11")
print("===================")



agent = DocumentationAgent()



result = agent.run(

    "app",

    "ASEO Project"

)



print(result)