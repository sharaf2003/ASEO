from ai_engine.intelligence.patterns import PatternScorer


scorer = PatternScorer()


pattern = {

    "name":
    "Healthcare Backend Pattern",

    "confidence":
    0.94
}



result = scorer.score(

    pattern,

    usage_count=200,

    success_rate=0.95,

    failure_rate=0.05

)


print(result)