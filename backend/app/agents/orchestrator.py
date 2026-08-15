from app.agents.decision_engine import AgentDecisionEngine

from app.intelligence.learning_engine import LearningEngine

from app.shared.models.execution import ExecutionContext





class AgentOrchestrator:

    """
    Controls execution flow between ASEO agents.

    Supports:

    - Dynamic agent selection
    - Agent memory
    - Intelligence decision system
    - Learning from executions
    """



    def __init__(

        self,

        db=None,

        project_id: int | None = None,

        organization_id: int | None = None

    ):


        self.db = db

        self.project_id = project_id

        self.organization_id = organization_id



        self.decision_engine = AgentDecisionEngine(

            db=self.db,

            project_id=self.project_id,

            organization_id=self.organization_id

        )


        # =============================================
        # Intelligence Learning
        # =============================================


        self.learning_engine = LearningEngine(
                db=self.db

        )





    # =====================================================
    # Agent Execution
    # =====================================================


    def execute_agent(

        self,

        agent,

        context

    ):


        try:


            result = agent.execute(

                context

            )


            # Learn from successful execution

            lesson = self.learning_engine.learn_from_execution(

                {

                    "agent": agent.name,

                    "status": "SUCCESS",

                    **(
                        result
                        if isinstance(result, dict)
                        else {}
                    )

                }

            )


            context.metadata.setdefault(

                "learning",

                []

            ).append(

                lesson

            )


            return result



        except Exception as error:



            lesson = self.learning_engine.learn_from_execution(

                {

                    "agent": agent.name,

                    "status": "FAILED",

                    "error": str(error),

                    "solutions": [],

                    "problems": [
                        str(error)
                    ]

                }

            )


            context.metadata.setdefault(

                "learning",

                []

            ).append(

                lesson

            )


            raise error





    # =====================================================
    # Main Execution Flow
    # =====================================================


    def run(

        self,

        request: str,

        project_id: int | None = None,

        organization_id: int | None = None,

        execution_id: int | None = None

    ) -> dict:



        context = ExecutionContext(

            id=execution_id,

            project_id=project_id,

            organization_id=organization_id,

            metadata={

                "request": request

            }

        )



        executed_agents = []



        try:


            selected_agents = self.decision_engine.select_agents(

                request

            )



            for agent in selected_agents:


                context.current_agent = agent.name



                context.start(

                    agent.name

                )



                self.execute_agent(

                    agent,

                    context

                )



                executed_agents.append(

                    agent.name

                )



            context.complete()



        except Exception as error:



            context.fail(

                str(error)

            )


            raise



        # =============================================
        # Final Learning Evaluation
        # =============================================


        final_lesson = self.learning_engine.learn_from_execution(

            {

                "status": context.status.value,


                "agents": executed_agents,

                "request": request,
                
                "technologies": context.metadata.get(
                    "technologies",
                    []
                ),

                "solutions": context.metadata.get(
                    "solutions",
                    []
                ),

                "problems": context.metadata.get(
                    "problems",
                    []
                )
                
            }

        )


        context.metadata.setdefault(

            "learning",

            []

        ).append(

            final_lesson

        )



        return {


            "execution_status":

                context.status.value,


            "project_id":

                context.project_id,


            "organization_id":

                context.organization_id,


            "agents_executed":

                executed_agents,


            "tasks": [

                {

                    "name": task.name,

                    "agent": task.agent_name,

                    "status": task.status.value

                }

                for task in context.tasks

            ],


            "artifacts": [

                {

                    "name": artifact.name,

                    "type": artifact.artifact_type,

                    "agent": artifact.created_by_agent

                }

                for artifact in context.artifacts

            ],


            "metadata":

                context.metadata

        }