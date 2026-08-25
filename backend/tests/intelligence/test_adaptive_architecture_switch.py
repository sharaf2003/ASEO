import pytest

from app.database.connection import SessionLocal

from app.intelligence.self_improvement.evolution_learning_engine import (
    EvolutionLearningEngine
)

from app.intelligence.self_improvement.evolution_feedback import (
    EvolutionFeedback
)

from app.models.evolution_memory import EvolutionMemory

from app.agents.architect_agent import ArchitectAgent

from app.shared.models.execution import ExecutionContext


FIREBASE_RECOMMENDATION = "Add Cloud Functions"
FASTAPI_RECOMMENDATION = "Use FastAPI Enterprise"
NODE_RECOMMENDATION = "Use Node Mongo Stack"


@pytest.fixture
def db():

    session = SessionLocal()

    yield session

    session.close()



def reset_memory(db):

    db.query(
        EvolutionMemory
    ).filter(
        EvolutionMemory.recommendation.in_(
            [
                FIREBASE_RECOMMENDATION,
                FASTAPI_RECOMMENDATION,
                NODE_RECOMMENDATION,
                "Consider PostgreSQL"
            ]
        )
    ).delete(
        synchronize_session=False
    )

    db.commit()



def add_feedback(
    engine,
    architecture,
    recommendation,
    success,
    count
):

    for _ in range(count):

        feedback = EvolutionFeedback(

            architecture=architecture,

            recommendation=recommendation,

            success=success

        )

        engine.record_feedback(
            feedback
        )



def run_architect(db):

    agent = ArchitectAgent(
        db=db
    )

    context = ExecutionContext()

    context.metadata["planner_result"] = {

        "request":

        "Build a mobile ecommerce application"

    }

    return agent.run(
        context
    )



def get_decision(result):

    decision = result.get(
        "architecture_decision"
    )

    return decision.get(
        "architecture"
    )



def test_firebase_should_win(db):

    reset_memory(db)

    engine = EvolutionLearningEngine(
        db
    )


    add_feedback(
        engine,
        "Firebase",
        FIREBASE_RECOMMENDATION,
        True,
        20
    )


    add_feedback(
        engine,
        "FastAPI",
        FASTAPI_RECOMMENDATION,
        False,
        10
    )


    add_feedback(
        engine,
        "Node Mongo",
        NODE_RECOMMENDATION,
        False,
        10
    )


    result = run_architect(db)




    assert get_decision(result) == "Firebase Serverless"



def test_fastapi_should_win(db):

    reset_memory(db)

    engine = EvolutionLearningEngine(
        db
    )


    add_feedback(
        engine,
        "Firebase",
        FIREBASE_RECOMMENDATION,
        False,
        10
    )


    add_feedback(
        engine,
        "FastAPI",
        FASTAPI_RECOMMENDATION,
        True,
        20
    )

    print("==============================")
    print("MEMORY AFTER FASTAPI INSERT")
    print("==============================")

    for item in db.query(EvolutionMemory).all():
        print(item.__dict__)


    add_feedback(
        engine,
        "Node Mongo",
        NODE_RECOMMENDATION,
        False,
        10
    )


    result = run_architect(db)

    print(
        result.get(
            "architecture_decision"
        )
    )


    assert get_decision(result) == "FastAPI Enterprise"



def test_node_should_win(db):

    reset_memory(db)

    engine = EvolutionLearningEngine(
        db
    )


    add_feedback(
        engine,
        "Firebase",
        FIREBASE_RECOMMENDATION,
        False,
        10
    )


    add_feedback(
        engine,
        "FastAPI",
        FASTAPI_RECOMMENDATION,
        False,
        10
    )


    add_feedback(
        engine,
        "Node Mongo",
        NODE_RECOMMENDATION,
        True,
        20
    )

    print("==============================")
    print("MEMORY AFTER NODE INSERT")
    print("==============================")

    for item in db.query(EvolutionMemory).all():
        print(item.__dict__)


    result = run_architect(db)


    assert get_decision(result) == "Node Mongo Stack"