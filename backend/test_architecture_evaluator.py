from app.intelligence.context.context_extractor import ContextExtractor
from app.intelligence.reasoning.requirement_analyzer import RequirementAnalyzer
from app.intelligence.reasoning.architecture_generator import ArchitectureGenerator
from app.intelligence.reasoning.architecture_evaluator import ArchitectureEvaluator



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


results = ArchitectureEvaluator().evaluate(
    candidates,
    requirements
)



print("==============================")
print("ARCHITECTURE EVALUATION")
print("==============================")


for result in results:

    print("\n")
    print(
        result["name"]
    )

    print(
        "Score:",
        result["final_score"]
    )

    print(
        result["scores"]
    )