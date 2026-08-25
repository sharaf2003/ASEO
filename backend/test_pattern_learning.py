from ai_engine.intelligence.patterns import PatternLearning


learner = PatternLearning()


pattern = {

    "name":
    "Healthcare Backend Pattern",

    "usage_count":
    10,

    "success_count":
    9,

    "failure_count":
    1
}


updated = learner.update(
    pattern,
    True
)


print(updated)