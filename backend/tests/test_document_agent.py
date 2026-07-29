from ai_engine.agents.document_agent.agent import DocumentAgent


agent = DocumentAgent()


print("========================")
print("AGENT INFORMATION")
print("========================")

print(agent.info())


print("========================")
print("PROCESSING DOCUMENT")
print("========================")


result = agent.execute(
    {
        "file": "sample.txt"
    }
)


print(result)