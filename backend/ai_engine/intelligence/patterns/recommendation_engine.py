class PatternRecommendationEngine:
    """
    ASEO Pattern Recommendation Engine v1

    Responsible for:

    Requirement Understanding
    +
    Pattern Discovery
    +
    Knowledge Graph Expansion
    +
    Architecture Recommendation
    """



    def __init__(
        self,
        registry,
        reasoning_engine,
        graph_engine
    ):

        self.registry = registry

        self.reasoning_engine = reasoning_engine

        self.graph_engine = graph_engine






    # =====================================
    # Recommend Architecture
    # =====================================


    def recommend(
        self,
        db,
        requirement
    ):


        matches = self.registry.find(

            requirement

        )



        if not matches:


            return {


                "recommendation":

                    None,


                "confidence":

                    0,


                "reason":

                    "No matching patterns"

            }







        recommendations = []



        total_confidence = 0







        for pattern in matches:



            pattern_name = pattern.get(
                "name"
            )



            analysis = self.reasoning_engine.analyze(

                db,

                pattern.get(
                    "id",
                    0
                )

            )



            confidence = analysis.get(

                "confidence",

                pattern.get(

                    "confidence",

                    0

                )

            )




            total_confidence += confidence




            recommendations.append({


                "pattern":

                    pattern_name,



                "architecture":

                    analysis.get(

                        "inferred_architecture",

                        []

                    ),



                "related":

                    analysis.get(

                        "related_patterns",

                        []

                    ),



                "confidence":

                    confidence


            })








        average_confidence = round(

            total_confidence /

            len(recommendations),

            3

        )







        return {


            "requirement":

                requirement,



            "recommended_patterns":

                recommendations,



            "confidence":

                average_confidence



        }