from app.intelligence.decision.adaptive_ranker import (
    AdaptiveDecisionRanker
)


def main():

    ranker = AdaptiveDecisionRanker()


    patterns = [

        {
            "id": 1,
            "name": "FastAPI",
            "category": "backend",
            "success_rate": 100,
            "priority_score": 0.8,
            "confidence": 0.9,
            "memory_score": 0.85,
            "recency": 1,
            "failure_penalty": 0,
            "adaptive_decision_score": 0.8
        },


        {
            "id": 2,
            "name": "Django",
            "category": "backend",
            "success_rate": 90,
            "priority_score": 0.7,
            "confidence": 0.7,
            "memory_score": 0.6,
            "recency": 0.8,
            "failure_penalty": 0.05,
            "adaptive_decision_score": 0.5
        },


        {
            "id": 3,
            "name": "Firebase",
            "category": "backend",
            "success_rate": 70,
            "priority_score": 0.5,
            "confidence": 0.5,
            "memory_score": 0.4,
            "recency": 0.5,
            "failure_penalty": 0.1,
            "adaptive_decision_score": 0.3
        }

    ]


    results = ranker.rank(
        patterns
    )


    print("\nPattern Competition Results:\n")


    for result in results:

        print({
            "name": result.get("name"),
            "decision_score": result.get(
                "decision_score"
            ),
            "adaptive_decision_score": result.get(
                "adaptive_decision_score"
            )
        })

        print("----------------")


    print("\nWinner:")

    print(
        results[0].get("name")
    )



if __name__ == "__main__":

    main()