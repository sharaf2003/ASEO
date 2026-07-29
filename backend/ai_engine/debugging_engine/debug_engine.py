from .error_analyzer import (
    ErrorAnalyzer
)

from .fixer import (
    CodeFixer
)



class SelfDebuggingEngine:
    """
    ASEO Self Debugging Engine v16
    """



    def __init__(
        self
    ):


        self.analyzer = ErrorAnalyzer()


        self.fixer = CodeFixer()





    def debug(
        self,
        error
    ):


        analysis = self.analyzer.analyze(

            error

        )


        fix = self.fixer.fix(

            analysis

        )



        return {

            "error_detected":
                True,


            "analysis":
                analysis,


            "fix":
                fix,


            "status":
                "resolved"

        }