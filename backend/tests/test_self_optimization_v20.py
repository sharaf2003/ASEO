from ai_engine.self_optimization import SelfOptimizationEngine


def test_self_optimization_v20():

    engine = SelfOptimizationEngine()

    result = engine.optimize(
        [
            {
                "agent": "backend_engineer",
                "quality_score": 95
            },
            {
                "agent": "database_engineer",
                "quality_score": 88
            },
            {
                "agent": "security_engineer",
                "quality_score": 92
            }
        ],
        95,
        "Build MVP first then scale"
    )

    assert result is not None