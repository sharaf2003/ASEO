from ai_engine.learning import (
    LearningEngine
)

from ai_engine.evaluation import (
    AgentEvaluator
)

from ai_engine.optimization import (
    PromptOptimizer
)

from ai_engine.self_improvement import (
    SelfImprovementEngine
)

from .result_analyzer import (
    ResultAnalyzer
)

from .knowledge_updater import (
    KnowledgeUpdater
)

from .improvement_tracker import (
    ImprovementTracker
)

from ai_engine.intelligence.patterns import (
    PatternLearning
)

from ai_engine.intelligence.memory import (
    MemoryManager
)



class LearningLoop:
    """
    ASEO Learning Loop v21

    Connects:

    Experience Memory
    +
    Pattern Evolution
    +
    Knowledge Graph
    +
    Evaluation
    +
    Optimization
    +
    Self Improvement
    """



    def __init__(
        self,
        memory=None,
        knowledge=None
    ):


        self.learning = LearningEngine()


        self.evaluator = AgentEvaluator()


        self.optimizer = PromptOptimizer()


        self.improver = SelfImprovementEngine()


        self.pattern_learning = PatternLearning()



        self.memory = (

            memory

            if memory

            else MemoryManager()

        )



        self.analyzer = ResultAnalyzer()



        # Shared Knowledge Layer

        self.knowledge = (

            knowledge

            if knowledge

            else KnowledgeUpdater()

        )



        self.tracker = ImprovementTracker()






    def process(
        self,
        project,
        prompt,
        improved_prompt,
        agents,
        result,
        old_score,
        new_score,
        pattern=None
    ):



        # 1 - Save experience


        experience = self.learning.learn(

            project,

            result.get(
                "decision",
                {}
            ),

            result,

            True,

            new_score

        )





        decision = result.get(
            "decision",
            {}
        )


        if isinstance(decision, str):

            decision = {
                "action": decision
            }



        architecture = decision.get(
            "action",
            ""
        )



        # 2 - Create memory from successful decision


        if architecture:


            self.memory.remember(

                project,

                architecture,

                "architecture",

                new_score / 100

            )





        # 3 - Update pattern intelligence


        pattern_update = None



        if pattern:


            pattern_update = self.pattern_learning.update(

                pattern,

                True,

                new_score

            )





        # 4 - Analyze result


        analysis = self.analyzer.analyze(

            result

        )





        # 5 - Update knowledge


        knowledge = self.knowledge.update(

            project,

            decision,

            analysis

        )






        # 6 - Evaluate agents


        evaluations = {}



        for agent in agents:


            evaluations[agent] = self.evaluator.evaluate(

                agent,

                True,

                new_score

            )






        # 7 - Prompt optimization


        optimized = self.optimizer.optimize(

            prompt

        )






        # 8 - Improvement


        improvement = self.improver.improve(

            prompt,

            improved_prompt,

            old_score,

            new_score

        )






        # 9 - Track progress


        learning_progress = self.tracker.track(

            old_score,

            new_score

        )






        return {


            "experience":

                experience,



            "result_analysis":

                analysis,



            "knowledge":

                knowledge,



            "evaluation":

                evaluations,



            "optimized_prompt":

                optimized,



            "improvement":

                improvement,



            "learning_progress":

                learning_progress,



            "pattern_update":

                pattern_update

        }