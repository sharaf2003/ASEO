from ai_engine.algorithms.document.arabic_requirement_extractor import ArabicRequirementExtractor



# Create extractor

extractor = ArabicRequirementExtractor()



# Arabic document sample

text = """
يمكن للعميل حجز المواعيد.
يقوم المدير بإدارة المستخدمين.
"""



# Extract requirements

result = extractor.extract(
    text
)



# Display result

print(result)