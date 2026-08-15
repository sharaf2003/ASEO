from app.intelligence.memory.confidence_engine import ConfidenceEngine


engine = ConfidenceEngine()


result = engine.calculate_confidence(

    similarity_score=1.0,

    success_score=1.0,

    usage_count=5,

    memory_score=0.82,

    recency=1

)


print(result)