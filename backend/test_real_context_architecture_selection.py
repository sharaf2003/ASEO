from app.agents.architect_agent import ArchitectAgent
from app.shared.models.execution import ExecutionContext
from app.database.connection import SessionLocal



def run_test(request):

    print("\n==============================")
    print("Request:")
    print(request)


    context = ExecutionContext()


    context.metadata = {

        "planner_result": {

            "request": request,

            "requirements": []

        }

    }


    db = SessionLocal()


    try:

        agent = ArchitectAgent(
            db=db
        )


        result = agent.run(
            context
        )


        print("\nProject Context:")

        print(
            result.get(
                "project_context"
            )
        )


        print("\nArchitecture:")

        print(
            result.get(
                "architecture"
            )
        )


        print("\nDecisions:")

        for decision in result.get(
            "architecture_decisions",
            []
        ):

            print({

                "layer": decision.get(
                    "layer"
                ),

                "pattern": decision.get(
                    "pattern"
                ),

                "score": decision.get(
                    "score"
                )

            })


    finally:

        db.close()



def main():


    tests = [

        "Build a mobile ecommerce application with Flutter and Firebase",

        "Create a SaaS web platform with FastAPI backend and React frontend",

        "Build an AI system using machine learning and database"

    ]


    for test in tests:

        run_test(
            test
        )



if __name__ == "__main__":

    main()