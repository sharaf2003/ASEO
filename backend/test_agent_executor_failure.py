from app.database.connection import SessionLocal

from app.agents.execution.agent_executor import AgentExecutor



class FakeFailAgent:


    name = "ArchitectAgent"


    def run(self, context):


        return {

            "agent": "ArchitectAgent",

            "success": False,


            "error": "Docker deployment failed",


            "architecture_decisions": [

                {

                    "id": 7,

                    "layer": "deployment",

                    "pattern": "Docker",

                    "category": "technology"

                }

            ]

        }



def main():


    db = SessionLocal()


    try:


        executor = AgentExecutor(

            db=db

        )


        class FakePlan:

            agents = [

                FakeFailAgent()

            ]



        class FakeContext:


            metadata = {}



        result = executor.execute(

            FakePlan(),

            FakeContext()

        )


        print("\nExecution Result:\n")

        print(result)



        print("\nMetadata:\n")

        print(FakeContext.metadata)



    finally:


        db.close()



if __name__ == "__main__":

    main()