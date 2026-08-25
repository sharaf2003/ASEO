from datetime import datetime

from .decision import Decision





class ReasoningEngine:
    """
    ASEO Reasoning Engine v15

    Knowledge Graph Based Engineering Reasoning

    Responsibilities:

    Pattern Discovery
    +
    Graph Expansion
    +
    Architecture Normalization
    +
    Decision Generation
    """



    def __init__(
        self,
        graph_engine=None
    ):

        self.graph = graph_engine





    # =====================================
    # Analyze Requirement
    # =====================================

    def analyze(
        self,
        requirement,
        db=None
    ):


        if not self.graph or not db:


            return Decision(

                action=[
                    "Layered FastAPI Architecture"
                ],

                confidence=0.5,

                reasoning=
                "No knowledge graph available."

            )





        patterns = self._find_patterns(

            requirement,

            db

        )



        if not patterns:


            return Decision(

                action=[
                    "Layered FastAPI Architecture"
                ],

                confidence=0.6,

                reasoning=
                "No matching engineering patterns."

            )







        architectures = []

        confidence_scores = []

        evidence = []






        for pattern in patterns:



            result = self.reason_pattern(

                db,

                pattern.id

            )



            architectures.extend(

                result.get(
                    "inferred_architecture",
                    []
                )

            )



            confidence_scores.append(

                result.get(
                    "confidence",
                    0
                )

            )



            evidence.append(

                pattern.name

            )







        normalized = self.normalize_architecture(

            architectures

        )





        confidence = 0



        if confidence_scores:


            confidence = round(

                sum(confidence_scores)

                /

                len(confidence_scores),

                3

            )






        return Decision(


            action=normalized,


            confidence=confidence,


            reasoning=

            "Architecture inferred from knowledge graph patterns: "

            +

            ", ".join(evidence)

        )









    # =====================================
    # Find Matching Patterns
    # =====================================

    def _find_patterns(
        self,
        requirement,
        db
    ):


        text = requirement.lower()


        patterns = []



        records = self.graph.repository.get_all_patterns(

            db

        )



        for pattern in records:



            family = (

                pattern.pattern_family

                or ""

            ).lower()



            name = (

                pattern.name

                or ""

            ).lower()



            if (

                family in text

                or

                name.replace(
                    "_pattern",
                    ""
                )
                in text

            ):


                patterns.append(
                    pattern
                )



        return patterns







    # =====================================
    # Reason Single Pattern
    # =====================================

    def reason_pattern(
        self,
        db,
        pattern_id
    ):


        pattern = self.graph.get_pattern(

            db,

            pattern_id

        )



        if not pattern:


            return {}





        graph = self.graph.explore(

            db,

            pattern_id

        )



        architectures = []


        scores = []






        if pattern.variant:


            architectures.append(

                pattern.variant

            )


            scores.append(

                pattern.confidence_score

                or

                0

            )







        related = []





        for edge in graph:



            target = self.graph.get_pattern(

                db,

                edge["target"]

            )



            if not target:

                continue




            related.append(

                target.name

            )



            if target.variant:


                architectures.append(

                    target.variant

                )



            scores.append(

                edge.get(
                    "confidence",
                    0
                )

            )







        confidence = 0



        if scores:


            confidence = round(

                sum(scores)

                /

                len(scores),

                3

            )







        return {


            "pattern":

                pattern.name,


            "related_patterns":

                related,


            "inferred_architecture":

                architectures,


            "confidence":

                confidence

        }









    # =====================================
    # Architecture Normalizer
    # =====================================

    def normalize_architecture(
        self,
        architectures
    ):


        components = []



        known_components = [

            "FastAPI",

            "PostgreSQL",

            "RBAC",

            "JWT",

            "Audit Logging",

            "Redis",

            "Docker",

            "Kubernetes",

            "Inventory",

            "Microservices"

        ]




        text = " ".join(

            architectures

        ).lower()






        for component in known_components:


            if component.lower() in text:


                components.append(

                    component

                )





        if not components:


            return list(

                dict.fromkeys(

                    architectures

                )

            )




        return components







    # =====================================
    # Compare Patterns
    # =====================================

    def compare(
        self,
        db,
        pattern_a,
        pattern_b
    ):


        return self.graph.find_path(

            db,

            pattern_a,

            pattern_b

        )