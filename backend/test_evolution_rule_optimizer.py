from app.intelligence.self_improvement.evolution_rule_optimizer import (
    EvolutionRuleOptimizer
)


optimizer = EvolutionRuleOptimizer()



learning_result = {

    "success_rate":1.0,

    "confidence":0.9

}



result = optimizer.optimize(

    "Add Cloud Functions",

    learning_result

)



print(result)