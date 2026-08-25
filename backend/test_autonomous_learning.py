from ai_engine.autonomous_learning import AutonomousLearningEngine


engine = AutonomousLearningEngine()


print("===== FIRST RUN =====")

result1 = engine.learn_build_project(
    "Build hospital management system"
)

print(result1)


print("\n===== SECOND RUN =====")

result2 = engine.learn_build_project(
    "Build hospital management system"
)

print(result2)