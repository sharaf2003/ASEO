from ai_engine.database import SessionLocal
from ai_engine.database.repository import DatabaseRepository
from ai_engine.intelligence.patterns.pattern_graph import PatternGraphEngine


db = SessionLocal()

repo = DatabaseRepository()

graph = PatternGraphEngine(repo)


print(
    graph.find_path(
        db,
        21,
        22
    )
)


print(
    graph.find_path(
        db,
        22,
        21
    )
)


db.close()