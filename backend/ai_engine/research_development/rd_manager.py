from .idea_generator import IdeaGenerator

from .market_analyzer import MarketAnalyzer

from .innovation_engine import InnovationEngine




class RDManager:
    """
    ASEO R&D Manager v21.7
    """

    def __init__(self):

        self.generator = IdeaGenerator()

        self.market = MarketAnalyzer()

        self.engine = InnovationEngine()



    def research(
        self,
        context
    ):


        ideas = self.generator.generate(

            context

        )


        results = []


        for idea in ideas:


            market = self.market.analyze(

                idea

            )


            innovation = self.engine.evaluate(

                market

            )


            results.append(

                innovation

            )


        return {

            "ideas_analyzed":
                len(results),

            "results":
                results,

            "status":
                "completed"

        }