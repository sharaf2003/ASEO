from ai_engine.database import SessionLocal
from ai_engine.database.repository import DatabaseRepository

from ai_engine.intelligence.patterns.pattern_graph import PatternGraphEngine
from ai_engine.intelligence.reasoning.reasoning_engine import ReasoningEngine



db = SessionLocal()

repo = DatabaseRepository()


graph = PatternGraphEngine(repo)


engine = ReasoningEngine(
    graph
)


result = engine.analyze(
    "Build hospital management system",
    db
)


print(
    result.__dict__
)


db.close()