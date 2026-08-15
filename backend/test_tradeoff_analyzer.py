from app.intelligence.context.context_extractor import ContextExtractor
from app.intelligence.reasoning.requirement_analyzer import RequirementAnalyzer
from app.intelligence.reasoning.architecture_generator import ArchitectureGenerator
from app.intelligence.reasoning.architecture_evaluator import ArchitectureEvaluator
from app.intelligence.reasoning.tradeoff_analyzer import TradeoffAnalyzer



request = """
Build a mobile ecommerce application with Flutter and Firebase
"""


context = ContextExtractor().extract(
    request
)


requirements = RequirementAnalyzer().analyze(
    context
)


candidates = ArchitectureGenerator().generate(
    requirements
)


evaluated = ArchitectureEvaluator().evaluate(
    candidates,
    requirements
)


result = TradeoffAnalyzer().analyze(
    evaluated,
    requirements
)


print("==============================")
print("TRADEOFF ANALYSIS")
print("==============================")


print(result)