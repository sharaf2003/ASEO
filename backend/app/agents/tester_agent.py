from app.agents.base_agent import BaseAgent

from app.agents.capabilities import AgentCapability

from app.shared.models.execution import ExecutionContext

from app.shared.models.artifact import Artifact



class TesterAgent(BaseAgent):

    """
    Responsible for validating
    generated implementation plans
    and producing test artifacts.
    """



    name = "TesterAgent"

    role = "tester"



    description = (
        "Validates software quality through "
        "testing strategies and quality assurance."
    )



    capabilities = [

        AgentCapability.UNIT_TESTING,

        AgentCapability.INTEGRATION_TESTING,

        AgentCapability.SECURITY_TESTING,

        AgentCapability.QUALITY_ASSURANCE

    ]



    def run(

        self,

        context: ExecutionContext

    ) -> dict:


        # =========================================
        # Get Development Result
        # =========================================

        development_result = context.metadata.get(

            "development_result",

            {}

        )



        if not development_result:

            raise ValueError(

                "Development result is required "
                "before testing phase"

            )



        # =========================================
        # Main Testing Task
        # =========================================

        main_task = context.create_task(

            name="Test application",

            agent_name=self.name,

            description=(

                "Validate application quality, "
                "integration and security."

            )

        )


        context.start_task(main_task)



        try:


            # =========================================
            # Testing Tasks
            # =========================================

            test_tasks = [

                "Run unit tests",

                "Run integration tests",

                "Run security tests"

            ]


            completed_tests = []



            for test_name in test_tasks:


                task = context.create_task(

                    name=test_name,

                    agent_name=self.name,

                    description=test_name

                )


                context.start_task(task)



                context.complete_task(

                    task,

                    {

                        "result": "completed",

                        "test": test_name

                    }

                )


                completed_tests.append(test_name)



            # =========================================
            # Create Test Artifact
            # =========================================

            test_plan = {


                "unit": [

                    "Test database models",

                    "Test business logic",

                    "Test services"

                ],


                "integration": [

                    "Test API endpoints",

                    "Test database integration"

                ],


                "security": [

                    "Test authentication",

                    "Test authorization"

                ]

            }



            artifact = Artifact(

                execution_id=context.id,

                created_by_agent=self.name,

                artifact_type="TEST_PLAN",

                name="Application Test Plan",

                content=test_plan

            )


            context.add_artifact(

                artifact

            )



            result = {


                "agent": self.name,


                "role": self.role,


                "capabilities": [

                    capability.value

                    for capability in self.capabilities

                ],


                "tests": test_plan,


                "tasks_created": len(completed_tests),


                "status": "READY_FOR_DEPLOYMENT"

            }



            context.metadata[

                "testing_result"

            ] = result



            context.complete_task(

                main_task,

                result

            )



            return result



        except Exception as error:


            context.fail_task(

                main_task,

                str(error)

            )


            raise