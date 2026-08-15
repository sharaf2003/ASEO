from app.agents.base_agent import BaseAgent

from app.agents.capabilities import AgentCapability

from app.shared.models.execution import ExecutionContext



class PlannerAgent(BaseAgent):

    """
    Responsible for analyzing user requirements
    and creating the initial execution plan.
    """


    name = "PlannerAgent"

    role = "planner"


    description = (
        "Analyzes requirements and creates "
        "initial project execution plans."
    )


    capabilities = [

        AgentCapability.REQUIREMENT_ANALYSIS,

        AgentCapability.PROJECT_PLANNING

    ]



    # =====================================================
    # Run Planner
    # =====================================================


    def run(

        self,

        context: ExecutionContext

    ) -> dict:


        """
        Analyze execution request and create
        initial planning result.
        """



        task = context.create_task(

            name="Analyze requirements",

            agent_name=self.name,

            description=(

                "Analyze the user request and "
                "identify functional and technical "
                "requirements."

            )

        )



        context.start_task(task)



        try:


            request = context.metadata.get(

                "request"

            )



            if not request:

                raise ValueError(

                    "Execution request is required "
                    "for PlannerAgent"

                )



            # =============================================
            # Planner Logic
            # =============================================


            result = {


                "agent": self.name,


                "role": self.role,


                "capabilities": [

                    capability.value

                    for capability in self.capabilities

                ],


                "request": request,


                "requirements": [

                    "Analyze user requirements",

                    "Identify technical constraints",

                    "Prepare execution plan"

                ]

            }



            context.complete_task(

                task,

                result

            )



            context.metadata[

                "planner_result"

            ] = result



            return result



        except Exception as error:


            context.fail_task(

                task,

                str(error)

            )


            raise