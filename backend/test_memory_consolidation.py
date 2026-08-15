from app.intelligence.memory.memory_consolidation import MemoryConsolidationEngine



def run_test():


    print("\n==============================")
    print("MEMORY CONSOLIDATION TEST")
    print("==============================")


    memories = [


        {

            "id": 75,

            "architecture": {

                "backend": {

                    "technology": "Firebase",

                    "architecture": "Serverless Backend"

                },

                "database": {

                    "technology": "Firebase Firestore"

                },

                "frontend": {

                    "technology": "Flutter"

                },

                "deployment": {

                    "technology": "Firebase"

                }

            },

            "success_score": 1.0,

            "confidence": 0.92,

            "adaptive_decision_score": 0.20,

            "memory_score": 0.90,

            "usage_count": 10

        },


        {

            "id": 80,

            "architecture": {

                "backend": {

                    "technology": "Firebase",

                    "architecture": "Serverless Backend"

                },

                "database": {

                    "technology": "Firebase Firestore"

                },

                "frontend": {

                    "technology": "Flutter"

                },

                "deployment": {

                    "technology": "Firebase"

                }

            },

            "success_score": 0.95,

            "confidence": 0.84,

            "adaptive_decision_score": 0.10,

            "memory_score": 0.85,

            "usage_count": 5

        }

    ]



    engine = MemoryConsolidationEngine()



    result = engine.consolidate(

        memories

    )



    print("\nCONSOLIDATED RESULT")

    print(result)



    print("\nCOUNT")

    print(

        len(result)

    )



if __name__ == "__main__":

    run_test()