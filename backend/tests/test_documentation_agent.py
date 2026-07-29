from ai_engine.agents.documentation_agent.agent import DocumentationAgent



agent=DocumentationAgent()



result=agent.run(

    "generated_project",

    "Clinic Management System"

)



print("===================")

print("DOCUMENTATION AGENT")

print("===================")


print(result)