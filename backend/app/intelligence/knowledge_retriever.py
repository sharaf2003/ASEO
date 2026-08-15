from app.repositories.knowledge_repository import KnowledgeRepository



class KnowledgeRetriever:

    """
    ASEO Knowledge Retrieval Engine

    Retrieves previous knowledge
    to improve future decisions.

    Responsibilities:

    - Search learned patterns
    - Rank successful knowledge
    - Provide recommendations
    """


    def __init__(

        self,

        db=None

    ):


        self.repository = None


        if db:

            self.repository = KnowledgeRepository(

                db

            )



    # =============================================
    # Retrieve Knowledge
    # =============================================


    def retrieve(

        self,

        category: str | None = None,

        layer: str | None = None,

        limit: int = 10

    ) -> list:


        if not self.repository:

            return []



        patterns = self.repository.get_patterns()



        results = []



        for pattern in patterns:


            context = pattern.context or {}


            pattern_layer = context.get(

                "layer"

            )



            if category:


                if pattern.category != category:

                    continue



            if layer:


                if pattern_layer != layer:

                    continue



            results.append(

                {

                    "id": pattern.id,

                    "name": pattern.name,

                    "category": pattern.category,

                    "success_rate": pattern.success_rate,

                    "usage_count": pattern.usage_count,

                    "layer": pattern_layer,

                    "context": context

                }

            )



        # Sort by learned experience

        results.sort(

            key=lambda item:

            (

                item["success_rate"],

                item["usage_count"]

            ),

            reverse=True

        )


        return results[:limit]



    # =============================================
    # Recommend Technology Stack
    # =============================================


    def recommend_stack(

        self

    ) -> dict:


        return {


            "backend":

                self.retrieve(

                    layer="backend",

                    limit=3

                ),



            "database":

                self.retrieve(

                    layer="database",

                    limit=3

                ),



            "frontend":

                self.retrieve(

                    layer="frontend",

                    limit=3

                ),



            "deployment":

                self.retrieve(

                    layer="deployment",

                    limit=3

                )

        }

    # =============================================
    # Retrieve Architecture Patterns
    # =============================================

    def retrieve_architecture_patterns(

        self,

        request_text: str,

        limit: int = 5

    ) -> list:


        if not self.repository:

            return []


        patterns = self.repository.get_patterns()


        results = []


        request_text = request_text.lower()



        technology_weights = {


            "fastapi": 0.25,

            "react": 0.25,

            "postgresql": 0.15,

            "docker": 0.15,

            "flutter": 0.25,

            "firebase": 0.20,

            "django": 0.20,

            "node": 0.20,

            "angular": 0.20,

            "spring": 0.20

        }



        requested = []


        for tech in technology_weights:


            if tech in request_text:

                requested.append(tech)



        for pattern in patterns:


            if pattern.category != "architecture_pattern":

                continue



            name = pattern.name.lower()



            score = 0


            matched = []



            for tech in requested:


                if tech in name:

                    score += technology_weights[tech]

                    matched.append(tech)



            # Normalize score

            if score > 1:

                score = 1



            results.append({


                "id": pattern.id,


                "name": pattern.name,


                "category": pattern.category,


                "success_rate": pattern.success_rate,


                "usage_count": pattern.usage_count,


                "context": pattern.context,


                "matched_technologies": matched,


                "score": round(

                    score,

                    2

                )


            })



        results.sort(

            key=lambda item:

            (

                item["score"],

                item["success_rate"],

                item["usage_count"]

            ),

            reverse=True

        )



        return results[:limit]