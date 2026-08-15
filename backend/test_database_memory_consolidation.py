from app.database.connection import SessionLocal

from app.intelligence.memory.database_memory_consolidator import (
    DatabaseMemoryConsolidator
)



def run_test():


    print("\n==============================")
    print("DATABASE MEMORY CONSOLIDATION TEST")
    print("==============================")


    db = SessionLocal()



    consolidator = DatabaseMemoryConsolidator(

        db

    )



    print("\nRUNNING CONSOLIDATION...\n")



    result = consolidator.consolidate()



    print("CONSOLIDATED PATTERNS:")



    for item in result:


        print("\n------------------------------")


        print(

            "Architecture:"

        )


        print(

            item.get(

                "architecture"

            )

        )


        print(

            "Total Usage:",

            item.get(

                "total_usage"

            )

        )


        print(

            "Average Success:",

            item.get(

                "average_success"

            )

        )


        print(

            "Average Confidence:",

            item.get(

                "average_confidence"

            )

        )


        print(

            "Adaptive Score:",

            item.get(

                "average_adaptive_score"

            )

        )


        print(

            "Memory Score:",

            item.get(

                "average_memory_score"

            )

        )


        print(

            "Memory Count:",

            item.get(

                "memory_count"

            )

        )



    print("\n==============================")

    print(

        "TOTAL PATTERNS:",

        len(result)

    )

    print("==============================")



    db.close()



if __name__ == "__main__":

    run_test()