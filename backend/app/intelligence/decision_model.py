from typing import Any



class DecisionModel:

    """
    ASEO Decision Model v1

    Responsible for making intelligent
    decisions using:

    - Previous knowledge
    - Discovered patterns
    - Similar experiences
    - Agent capabilities

    This will evolve into
    a learned decision system.
    """



    def __init__(

        self,

        knowledge_engine=None,

        pattern_analyzer=None,

        similarity_engine=None

    ):


        self.knowledge_engine = knowledge_engine

        self.pattern_analyzer = pattern_analyzer

        self.similarity_engine = similarity_engine



    # =============================================
    # Analyze Request
    # =============================================


    def analyze(

        self,

        request: str,

        memories: list[Any]

    ) -> dict:


        similar_memories = []



        if self.knowledge_engine and self.similarity_engine:


            similar_memories = (

                self.knowledge_engine.find_relevant(

                    request,

                    memories,

                    self.similarity_engine

                )

            )



        patterns = {}



        if (

            self.pattern_analyzer

            and similar_memories

        ):


            knowledge_items = [

                item["content"]

                for item in similar_memories

                if item["similarity"] > 30

            ]


            patterns = (

                self.pattern_analyzer.analyze_success_patterns(

                    knowledge_items

                )

            )



        return {

            "request": request,

            "similar_experiences": similar_memories[:5],

            "patterns": patterns,

            "confidence": self.calculate_confidence(

                similar_memories

            )

        }



    # =============================================
    # Confidence Calculation
    # =============================================


    def calculate_confidence(

        self,

        results: list

    ) -> float:


        if not results:

            return 0.0



        best_score = results[0].get(

            "similarity",

            0

        )



        return min(

            best_score / 100,

            1.0

        )