from app.intelligence.context.context_extractor import ContextExtractor
from app.intelligence.reasoning.requirement_analyzer import RequirementAnalyzer
from app.intelligence.reasoning.architecture_generator import ArchitectureGenerator



request = """
Build a mobile ecommerce application with Flutter and Firebase
"""


context = ContextExtractor().extract(
    request
)


requirements = RequirementAnalyzer().analyze(
    context
)


generator = ArchitectureGenerator()


candidates = generator.generate(
    requirements
)


print("==============================")
print("ARCHITECTURE CANDIDATES")
print("==============================")


for candidate in candidates:

    print("\n")
    print(candidate["name"])

    print(
        candidate["architecture"]
    )