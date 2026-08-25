from datetime import datetime




class RecommendationEngine:
    """
    ASEO Recommendation Engine v2

    Converts reasoning results
    into structured engineering plans.

    Supports:

    Architecture Classification
    +
    Security Classification
    +
    Observability Classification
    +
    Module Discovery
    +
    Confidence Propagation
    """



    def __init__(
        self,
        reasoning_engine=None,
        graph_engine=None
    ):

        self.reasoning = reasoning_engine

        self.graph = graph_engine





    # =====================================
    # Recommend
    # =====================================

    def recommend(
        self,
        requirement,
        db=None
    ):


        if not self.reasoning:


            return {

                "requirement":
                    requirement,

                "recommendation":
                    None,

                "confidence":
                    0

            }






        decision = self.reasoning.analyze(

            requirement,

            db

        )





        architecture = decision.action



        if isinstance(
            architecture,
            str
        ):


            architecture = [

                architecture

            ]





        recommendation = {


            "backend":
                None,


            "database":
                None,


            "security":
                [],


            "observability":
                [],


            "infrastructure":
                [],


            "modules":
                []

        }






        self.classify_components(

            architecture,

            recommendation

        )







        if self.graph and db:


            modules = self.discover_modules(

                requirement,

                db

            )


            recommendation["modules"].extend(

                modules

            )







        return {


            "requirement":

                requirement,



            "recommendation":

                recommendation,



            "confidence":

                decision.confidence,



            "reasoning":

                decision.reasoning,



            "generated_at":

                datetime.utcnow()
                .isoformat()

        }









    # =====================================
    # Component Classification
    # =====================================

    def classify_components(
        self,
        components,
        recommendation
    ):


        for component in components:


            item = component.lower()





            if "fastapi" in item:


                recommendation["backend"] = "FastAPI"





            elif "postgresql" in item:


                recommendation["database"] = "PostgreSQL"






            elif (

                "rbac" in item

                or

                "jwt" in item

            ):


                recommendation["security"].append(

                    component

                )







            elif (

                "audit" in item

                or

                "logging" in item

            ):


                recommendation["observability"].append(

                    component

                )







            elif (

                "docker" in item

                or

                "kubernetes" in item

                or

                "redis" in item

            ):


                recommendation["infrastructure"].append(

                    component

                )








            else:


                recommendation["modules"].append(

                    component

                )









    # =====================================
    # Discover Related Modules
    # =====================================

    def discover_modules(
        self,
        requirement,
        db
    ):


        modules = []



        patterns = self.reasoning._find_patterns(

            requirement,

            db

        )



        for pattern in patterns:



            if not self.graph:

                continue





            related = self.graph.neighbors(

                db,

                pattern.id

            )





            for relation in related:



                related_pattern = self.graph.get_pattern(

                    db,

                    relation["id"]

                )



                if not related_pattern:

                    continue





                if related_pattern.pattern_family:



                    modules.append(

                        related_pattern.pattern_family

                    )







        return list(

            dict.fromkeys(

                modules

            )

        )