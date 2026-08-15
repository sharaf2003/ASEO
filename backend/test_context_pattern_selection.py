from app.intelligence.decision.adaptive_ranker import (
    AdaptiveDecisionRanker
)


def run_test(context_name, patterns):

    ranker = AdaptiveDecisionRanker()


    results = ranker.rank(
        patterns
    )


    print("\nContext:")
    print(context_name)

    print("\nResults:")

    for item in results:

        print({
            "pattern": item.get("name"),
            "score": item.get("decision_score"),
            "category": item.get("category"),
            "adaptive_score": item.get(
                "adaptive_decision_score",
                0
            )
        })

        print("----------------")


    print(
        "Winner:",
        results[0].get("name")
    )



def main():


    web_patterns = [

        {
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


    mobile_patterns = [

        {
            "name": "Flutter",
            "category": "mobile",
            "success_rate": 100,
            "priority_score": 0.9,
            "confidence": 0.9,
            "memory_score": 0.9,
            "recency": 1,
            "failure_penalty": 0,
            "adaptive_decision_score": 0.85
        },


        {
            "name": "React",
            "category": "web",
            "success_rate": 95,
            "priority_score": 0.7,
            "confidence": 0.7,
            "memory_score": 0.6,
            "recency": 0.8,
            "failure_penalty": 0.05,
            "adaptive_decision_score": 0.5
        }

    ]


    run_test(
        "SaaS Web Application",
        web_patterns
    )


    run_test(
        "Mobile Application",
        mobile_patterns
    )



if __name__ == "__main__":

    main()