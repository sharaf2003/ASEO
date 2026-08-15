from app.intelligence.context.context_extractor import (
    ContextExtractor
)

from app.intelligence.reasoning.requirement_analyzer import (
    RequirementAnalyzer
)

from app.intelligence.reasoning.architecture_generator import (
    ArchitectureGenerator
)

from app.intelligence.reasoning.architecture_evaluator import (
    ArchitectureEvaluator
)

from app.intelligence.reasoning.tradeoff_analyzer import (
    TradeoffAnalyzer
)



class ReasoningEngine:
    """
    Main orchestrator for Architecture Reasoning.

    Flow:

    Request
        |
        Context Extraction
        |
        Requirement Analysis
        |
        Candidate Generation
        |
        Architecture Evaluation
        |
        Trade-off Analysis
    """


    def __init__(self):

        self.context_extractor = ContextExtractor()

        self.requirement_analyzer = RequirementAnalyzer()

        self.architecture_generator = ArchitectureGenerator()

        self.architecture_evaluator = ArchitectureEvaluator()

        self.tradeoff_analyzer = TradeoffAnalyzer()



    def reason(

        self,

        request: str

    ) -> dict:


        # =============================================
        # Extract Context
        # =============================================

        context = self.context_extractor.extract(

            request

        )


        # =============================================
        # Analyze Requirements
        # =============================================

        requirements = self.requirement_analyzer.analyze(

            context

        )


        # =============================================
        # Generate Candidates
        # =============================================

        candidates = self.architecture_generator.generate(

            requirements

        )


        # =============================================
        # Evaluate Candidates
        # =============================================

        evaluated = self.architecture_evaluator.evaluate(

            candidates,

            requirements

        )


        # =============================================
        # Analyze Trade-offs
        # =============================================

        tradeoff = self.tradeoff_analyzer.analyze(

            evaluated,

            requirements

        )


        return {

            "context": context,

            "requirements": requirements,

            "candidates": evaluated,

            "recommendation": tradeoff

        }