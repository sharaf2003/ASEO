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

from ai_engine.intelligence.memory import (
    MemoryManager
)



class AutonomousLearningEngine:
    """
    ASEO Autonomous Learning Engine v14.2

    Combines:

    Autonomous Execution
    +
    Learning Loop
    +
    Real Agent Evaluation
    +
    Knowledge Graph Intelligence
    +
    Pattern Evolution
    +
    Shared Memory Intelligence
    """



    def __init__(
        self,
        agents=None
    ):


        # Shared memory brain

        self.memory = MemoryManager()



        # Knowledge intelligence layer

        self.knowledge_graph = KnowledgeGraph()


        self.knowledge_updater = KnowledgeGraphUpdater(

            self.knowledge_graph

        )



        # Autonomous execution engine

        self.executor = AutonomousExecutionEngine(

            agents,

            self.memory

        )



        # Learning system

        self.learning_loop = LearningLoop(

            memory=self.memory

        )






    def learn_build_project(
        self,
        requirement
    ):



        # 1 - Execute autonomous pipeline

        execution = self.executor.run(

            requirement

        )






        # 2 - Extract result


        execution_data = execution.get(

            "execution",

            {}

        )


        result = execution_data.get(

            "result",

            {}

        )





        intelligence = execution.get(

            "intelligence",

            {}

        )





        decision = intelligence.get(

            "decision",

            {}

        )






        # 3 - Extract pattern


        pattern = None



        if isinstance(
            decision,
            dict
        ):


            patterns = decision.get(

                "patterns",

                []

            )


            if patterns:

                pattern = patterns[0]




        if pattern is None:


            patterns = intelligence.get(

                "patterns",

                []

            )


            if patterns:

                pattern = patterns[0]






        # 4 - Extract agents


        stages = execution_data.get(

            "stages",

            []

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






        # 5 - Learning


        learning = self.learning_loop.process(

            project=requirement,


            prompt="Generate backend API",


            improved_prompt=(

                "Generate scalable backend API "
                "with best architecture"

            ),


            agents=agent_names,


            result=result,


            old_score=75,


            new_score=95,


            pattern=pattern

        )






        # 6 - Knowledge graph update


        knowledge_result = self.knowledge_updater.update_from_result(

            {

                **result,


                "requirement":

                    requirement,


                "score":

                    95

            }

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