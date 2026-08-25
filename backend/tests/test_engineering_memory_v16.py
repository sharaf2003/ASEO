from ai_engine.engineering_memory import EngineeringMemoryEngine


def test_engineering_memory():

    memory = EngineeringMemoryEngine()


    saved = memory.remember(
        "Ecommerce Backend",
        "FastAPI + PostgreSQL + Layered",
        {
            "score":95,
            "success":True
        }
    )


    retrieved = memory.recall(
        "FastAPI"
    )


    assert saved is not None

    assert len(retrieved) > 0