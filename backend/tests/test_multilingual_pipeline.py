from ai_engine.agents.document_agent.pipeline import DocumentPipeline



pipeline = DocumentPipeline()



result = pipeline.process(
    "sample.txt"
)



print(result)