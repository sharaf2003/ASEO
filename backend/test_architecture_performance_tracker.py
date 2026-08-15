from app.intelligence.optimization.architecture_performance_tracker import (
    ArchitecturePerformanceTracker
)


tracker = ArchitecturePerformanceTracker()


tracker.record_result(
    "Firebase Serverless",
    0.93,
    True
)


tracker.record_result(
    "Firebase Serverless",
    0.90,
    True
)


result = tracker.get_metrics(
    "Firebase Serverless"
)


print(result)