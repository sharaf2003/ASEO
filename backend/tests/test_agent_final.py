from ai_engine.agents.document_agent.pipeline import DocumentPipeline



pipeline = DocumentPipeline()



result = pipeline.process(
    "sample.txt"
)



print("===================")
print("AGENT INFO")
print("===================")

print(
    result.get("agent_info")
)



print("===================")
print("STATUS")
print("===================")

print(
    result.get("status")
)



print("===================")
print("PROCESSING TIME")
print("===================")

print(
    result.get("processing_time")
)



print("===================")
print("SUMMARY")
print("===================")

print(
    result["memory"]
)