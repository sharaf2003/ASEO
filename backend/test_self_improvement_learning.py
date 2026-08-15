from app.database.connection import SessionLocal
from app.agents.architect_agent import ArchitectAgent
from app.shared.models.execution import ExecutionContext



def run_test():

    print("\n==============================")
    print("SELF IMPROVEMENT LEARNING TEST")
    print("==============================")


    db = SessionLocal()


    context = ExecutionContext()


    context.metadata = {

        "planner_result": {

            "request":
                "Build a mobile ecommerce application with Flutter and Firebase",

            "requirements": []

        }

    }



    agent = ArchitectAgent(

        db=db

    )


    print("\nRUNNING DECISION...")


    result = agent.run(

        context

    )


    print("\nPROJECT CONTEXT")

    print(

        result.get(

            "project_context"

        )

    )


    print("\nSELECTED ARCHITECTURE")

    print(

        result.get(

            "architecture"

        )

    )


    print("\nDECISION CONFIDENCE")

    print(

        result.get(

            "decision_confidence"

        )

    )


    print("\nMEMORY USED")

    print(

        result.get(

            "previous_architectures"

        )

    )


    db.close()



if __name__ == "__main__":

    run_test()