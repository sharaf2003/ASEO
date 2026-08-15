from app.intelligence.context.context_extractor import ContextExtractor
from app.intelligence.reasoning.requirement_analyzer import RequirementAnalyzer



request = """
Build a mobile ecommerce application with Flutter and Firebase
"""


extractor = ContextExtractor()

context = extractor.extract(
    request
)


analyzer = RequirementAnalyzer()

result = analyzer.analyze(
    context
)


print("==============================")
print("CONTEXT")
print(context)

print("==============================")
print("REASONING RESULT")
print(result)