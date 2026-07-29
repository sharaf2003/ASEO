from .quality_analyzer import QualityAnalyzer

from .improvement_engine import ImprovementEngine

from .optimization_tracker import OptimizationTracker




class ImprovementManager:
    """
    ASEO Continuous Improvement Manager v21.5
    """



    def __init__(self):

        self.analyzer = QualityAnalyzer()

        self.engine = ImprovementEngine()

        self.tracker = OptimizationTracker()



    def improve(
        self,
        result,
        old_quality
    ):


        analysis = self.analyzer.analyze(

            result

        )


        suggestions = self.engine.improve(

            analysis

        )


        tracking = self.tracker.track(

            old_quality,

            analysis["quality_score"]

        )


        return {

            "analysis":
                analysis,

            "suggestions":
                suggestions,

            "tracking":
                tracking

        }