from app.intelligence.reasoning.reasoning_engine import (
    ReasoningEngine
)



request = """
Build a mobile ecommerce application with Flutter and Firebase
"""


engine = ReasoningEngine()


result = engine.reason(

    request

)


print("==============================")
print("REASONING ENGINE RESULT")
print("==============================")


print("\nCONTEXT")
print(
    result["context"]
)


print("\nREQUIREMENTS")
print(
    result["requirements"]
)


print("\nCANDIDATES")


for item in result["candidates"]:

    print(
        item["name"],
        item["final_score"]
    )


print("\nRECOMMENDATION")

print(
    result["recommendation"]
)