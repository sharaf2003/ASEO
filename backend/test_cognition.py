from ai_engine.database import SessionLocal

from ai_engine.database.repository import DatabaseRepository

from ai_engine.intelligence.patterns.pattern_graph import PatternGraphEngine


db = SessionLocal()

repo = DatabaseRepository()

graph = PatternGraphEngine(repo)


patterns = repo.get_all_patterns(
    db
)


for pattern in patterns:

    print(
        "PATTERN:",
        pattern.id,
        pattern.name
    )


    print(

        graph.explore(

            db,

            pattern.id

        )

    )


db.close()