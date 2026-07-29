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




class LearningLoop:
    """
    ASEO Learning Loop v20.3

    Connects:

    Learning +
    Evaluation +
    Optimization +
    Self Improvement +
    Result Analysis +
    Knowledge Update +
    Improvement Tracking
    """



    def __init__(self):


        # Previous intelligence

        self.learning = LearningEngine()

        self.evaluator = AgentEvaluator()

        self.optimizer = PromptOptimizer()

        self.improver = SelfImprovementEngine()



        # v20.3 intelligence

        self.analyzer = ResultAnalyzer()

        self.knowledge = KnowledgeUpdater()

        self.tracker = ImprovementTracker()





    def process(
        self,
        project,
        prompt,
        improved_prompt,
        agents,
        result,
        old_score,
        new_score
    ):


        # 1 - Save engineering experience

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





        # 2 - Analyze result

        analysis = self.analyzer.analyze(

            result

        )





        # 3 - Update company knowledge

        knowledge = self.knowledge.update(

            project,

            result.get(
                "decision",
                {}
            ),

            analysis

        )





        # 4 - Evaluate agents

        evaluations = {}



        for agent in agents:


            evaluations[agent] = (

                self.evaluator.evaluate(

                    agent,

                    True,

                    new_score

                )

            )





        # 5 - Optimize prompt

        optimized = self.optimizer.optimize(

            prompt

        )





        # 6 - Compare improvement

        improvement = self.improver.improve(

            prompt,

            improved_prompt,

            old_score,

            new_score

        )





        # 7 - Track learning improvement

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

                learning_progress

        }