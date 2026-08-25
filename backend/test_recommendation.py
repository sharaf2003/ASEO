from ai_engine.database import SessionLocal

from ai_engine.database.repository import DatabaseRepository

from ai_engine.intelligence.patterns.pattern_graph import PatternGraphEngine

from ai_engine.intelligence.reasoning.reasoning_engine import ReasoningEngine

from ai_engine.intelligence.recommendation.recommendation_engine import RecommendationEngine



db = SessionLocal()


repo = DatabaseRepository()


graph = PatternGraphEngine(
    repo
)


reasoning = ReasoningEngine(
    graph
)


recommendation = RecommendationEngine(
    reasoning
)



result = recommendation.recommend(

    "Build hospital management system",

    db

)



print(result)



db.close()