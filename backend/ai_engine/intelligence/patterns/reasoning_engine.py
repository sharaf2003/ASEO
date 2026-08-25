from datetime import datetime



class PatternReasoningEngine:
    """
    ASEO Pattern Reasoning Engine v1

    Converts Knowledge Graph
    into Engineering Insights.

    Supports:

    Pattern Combination
    +
    Context Reasoning
    +
    Architecture Inference
    +
    Recommendation Generation
    """



    def __init__(
        self,
        repository,
        graph_engine
    ):

        self.repository = repository

        self.graph_engine = graph_engine







    # =====================================
    # Analyze Pattern
    # =====================================


    def analyze(
        self,
        db,
        pattern_id
    ):


        context = self.graph_engine.summarize(

            db,

            pattern_id

        )



        related = context.get(

            "related_patterns",

            []

        )



        if not related:


            return {


                "pattern_id":

                    pattern_id,


                "insight":

                    "No sufficient knowledge relations",


                "confidence":

                    0.0


            }








        architecture_parts = []


        domains = []



        for pattern in related:



            if pattern.get(
                "variant"
            ):


                architecture_parts.append(

                    pattern.get(
                        "variant"
                    )

                )



            if pattern.get(
                "category"
            ):


                domains.append(

                    pattern.get(
                        "category"
                    )

                )








        confidence = self.calculate_confidence(

            related

        )





        return {


            "pattern_id":

                pattern_id,



            "related_patterns":

                [

                    p.get(
                        "name"
                    )

                    for p in related

                ],



            "inferred_architecture":

                list(

                    set(
                        architecture_parts
                    )

                ),



            "domains":

                list(

                    set(
                        domains
                    )

                ),



            "confidence":

                confidence,



            "generated_at":

                datetime.utcnow().isoformat()

        }









    # =====================================
    # Confidence Calculation
    # =====================================


    def calculate_confidence(
        self,
        patterns
    ):


        if not patterns:

            return 0



        scores = []



        for pattern in patterns:


            scores.append(

                pattern.get(

                    "relation_confidence",

                    0

                )

            )



        return round(

            sum(scores)

            /

            len(scores),

            3

        )









    # =====================================
    # Recommend Pattern
    # =====================================


    def recommend(
        self,
        db,
        pattern_id
    ):


        analysis = self.analyze(

            db,

            pattern_id

        )



        confidence = analysis.get(

            "confidence",

            0

        )



        if confidence < 0.5:


            return {


                "recommendation":

                    None,


                "confidence":

                    confidence

            }






        return {


            "recommendation":

                "enterprise_architecture_pattern",



            "based_on":

                analysis.get(

                    "related_patterns"

                ),



            "confidence":

                confidence

        }