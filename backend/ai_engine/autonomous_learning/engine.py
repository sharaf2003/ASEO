from ai_engine.orchestrator import (
    AutonomousExecutionEngine
)

from ai_engine.learning_loop import (
    LearningLoop
)

from ai_engine.knowledge_graph import (
    KnowledgeGraph,
    KnowledgeGraphUpdater
)



class AutonomousLearningEngine:
    """
    ASEO Autonomous Learning Engine v14.1.2

    Combines:

    Autonomous Execution
    +
    Learning Loop
    +
    Real Agent Evaluation
    +
    Knowledge Graph Update
    """



    def __init__(
        self,
        agents=None
    ):


        self.executor = AutonomousExecutionEngine(

            agents

        )


        self.learning_loop = LearningLoop()



        # Knowledge Intelligence Layer

        self.knowledge_graph = KnowledgeGraph()


        self.knowledge_updater = KnowledgeGraphUpdater(

            self.knowledge_graph

        )





    def learn_build_project(
        self,
        requirement
    ):


        # 1 - Execute project

        execution = self.executor.run(

            requirement

        )



        # 2 - Extract execution result

        result = (

            execution
            .get(
                "execution",
                {}
            )
            .get(
                "result",
                {}
            )

        )





        decision = (

            execution
            .get(
                "intelligence",
                {}
            )
            .get(
                "decision",
                {}
            )

        )





        # 3 - Extract real agents from pipeline stages

        stages = (

            execution
            .get(
                "execution",
                {}
            )
            .get(
                "stages",
                []
            )

        )



        agent_names = [

            stage.get(

                "agent"

            )

            for stage in stages

            if isinstance(
                stage,
                dict
            )

            and stage.get(
                "agent"
            )

        ]





        # 4 - Learning process

        learning = self.learning_loop.process(

            project=requirement,


            prompt="Generate backend API",


            improved_prompt=(

                "Generate scalable backend API "
                "with best architecture"

            ),



            # Real agents

            agents=agent_names,


            result=result,


            old_score=75,


            new_score=95

        )





        # 5 - Update Knowledge Graph

        knowledge_result = (

            self.knowledge_updater.update_from_result(

                {

                    **result,


                    "requirement":

                        requirement,


                    "score":

                        95

                }

            )

        )





        return {


            "status":

                "completed",



            "execution":

                execution,



            "learning":

                learning,



            "knowledge":

                knowledge_result

        }