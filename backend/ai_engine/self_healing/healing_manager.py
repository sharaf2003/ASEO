from .error_analyzer import ErrorAnalyzer

from .fix_generator import FixGenerator

from .repair_engine import RepairEngine




class HealingManager:
    """
    ASEO Self Healing Manager v21.4
    """



    def __init__(self):

        self.analyzer = ErrorAnalyzer()

        self.generator = FixGenerator()

        self.repair = RepairEngine()



    def heal(
        self,
        error
    ):


        analysis = self.analyzer.analyze(

            error

        )


        fix = self.generator.generate(

            analysis

        )


        result = self.repair.apply(

            fix

        )


        return {

            "error":
                error,

            "analysis":
                analysis,

            "fix":
                result,

            "status":
                "resolved"

        }