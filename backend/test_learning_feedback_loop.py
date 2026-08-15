from app.agents.architect_agent import ArchitectAgent
from app.shared.models.execution import ExecutionContext
from app.database.connection import SessionLocal



def run_architecture(request):

    db = SessionLocal()


    try:

        context = ExecutionContext()


        context.metadata = {

            "planner_result": {

                "request": request,

                "requirements": []

            }

        }


        agent = ArchitectAgent(
            db=db
        )


        result = agent.run(
            context
        )


        print("\n==============================")

        print("Request:")

        print(request)


        print("\nArchitecture:")

        print(
            result.get(
                "architecture"
            )
        )


        print("\nDecision Confidence:")

        print(
            result.get(
                "decision_confidence"
            )
        )


        print("\nDecision Memory Saved:")

        print(
            result.get(
                "decision_memory_saved"
            )
        )


        print("\nPrevious Architectures:")

        print(
            result.get(
                "previous_architectures"
            )
        )


        return result


    finally:

        db.close()



def check_memory():


    db = SessionLocal()


    try:

        from app.intelligence.memory.decision_memory import DecisionMemory


        memory = DecisionMemory(
            db=db
        )


        memories = memory.retrieve_memories()


        print("\n==============================")

        print("Stored Memories:")

        print(
            len(memories)
        )


        if memories:

            print("\nLatest Memory:")

            print(
                memories[0]
            )


    finally:

        db.close()



def main():


    request = (
        "Build a mobile ecommerce application "
        "with Flutter and Firebase"
    )


    print("\nFIRST EXECUTION")

    run_architecture(
        request
    )


    check_memory()



    print("\nSECOND EXECUTION")

    run_architecture(
        request
    )


    check_memory()



if __name__ == "__main__":

    main()