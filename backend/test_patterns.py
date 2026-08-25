from ai_engine.intelligence.patterns import PatternAnalyzer


analyzer = PatternAnalyzer()


memory = [

    {
        "key":
        "hospital management system",

        "value":
        "FastAPI PostgreSQL RBAC Audit Logging",

        "category":
        "architecture",

        "confidence":
        0.94
    }

]


result = analyzer.analyze(memory)


print(result)