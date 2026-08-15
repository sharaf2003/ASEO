from app.intelligence.optimization.adaptive_optimizer import (
    AdaptiveArchitectureOptimizer
)


optimizer = AdaptiveArchitectureOptimizer()


weights = optimizer.calculate_weights(
    performance_confidence=0.97,
    memory_strength=0.89
)


print(weights)