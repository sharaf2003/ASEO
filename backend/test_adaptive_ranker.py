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

            "priority_score": 0.55,

            "confidence": 0.87,

            "memory_score": 0.86,

            "recency": 1,

            "failure_penalty": 0

        },


        {

            "id": 2,

            "name": "Django",

            "category": "backend",

            "success_rate": 90,

            "priority_score": 0.30,

            "confidence": 0.60,

            "memory_score": 0.50,

            "recency": 0.8,

            "failure_penalty": 0.05

        },


        {

            "id": 3,

            "name": "Firebase",

            "category": "backend",

            "success_rate": 70,

            "priority_score": 0.40,

            "confidence": 0.50,

            "memory_score": 0.40,

            "recency": 0.5,

            "failure_penalty": 0.1

        }

    ]



    results = ranker.rank(

        patterns

    )



    print("\nAdaptive Ranking Results:\n")



    for result in results:


        print(result)

        print("----------------")




if __name__ == "__main__":

    main()