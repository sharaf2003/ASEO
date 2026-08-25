from ai_engine.self_improvement import SelfImprovementEngine


def test_self_improvement_v14():

    engine = SelfImprovementEngine()

    result = engine.improve(
        "Generate backend API",
        "Generate scalable FastAPI backend API with JWT authentication",
        75,
        95
    )

    assert result is not None

    history = engine.history()

    assert len(history) > 0