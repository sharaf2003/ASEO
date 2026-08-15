from app.intelligence.evolution.evolution_rules import (
    ArchitectureEvolutionRules
)

from app.intelligence.evolution.evolution_result import (
    EvolutionResult
)



class ArchitectureEvolutionEngine:


    def __init__(self):

        self.rules = (
            ArchitectureEvolutionRules()
        )



    def evolve(
        self,
        architecture: dict
    ):


        result = self.rules.analyze(
            architecture
        )


        name = (
            architecture
            .get("backend", {})
            .get("technology")
        )


        return EvolutionResult(

            architecture=name,

            improvements=result[
                "recommendations"
            ],

            risks=result[
                "risks"
            ],

            future_recommendations=result[
                "recommendations"
            ]

        )