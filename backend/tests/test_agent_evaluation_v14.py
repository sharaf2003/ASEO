from ai_engine.evaluation import (
    AgentEvaluator
)



evaluator = AgentEvaluator()



print(

    evaluator.evaluate(

        "coding",

        True,

        95

    )

)



print(

    evaluator.evaluate(

        "coding",

        True,

        98

    )

)



print(

    evaluator.evaluate(

        "security",

        False,

        60

    )

)



print(

    evaluator.report()

)