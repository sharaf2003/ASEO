from app.repositories.decision_history_repository import (
    DecisionHistoryRepository
)

from app.intelligence.similarity_engine import SimilarityEngine





class DecisionHistoryRetriever:

    """
    Retrieves previous successful decisions.

    Used for:

    - Architecture reuse
    - Experience based decisions
    - Improving future designs
    """



    def __init__(

        self,

        db=None

    ):


        self.repository = None

        self.similarity_engine = SimilarityEngine()


        if db:

            self.repository = DecisionHistoryRepository(

                db

            )





    # =============================================
    # Retrieve Successful Architectures
    # =============================================


    def retrieve_successful_architectures(

        self,

        limit: int = 5

    ) -> list:


        if not self.repository:

            return []


        decisions = self.repository.get_successful_decisions(

            limit

        )


        results = []


        for decision in decisions:


            results.append(

                {

                    "architecture":
                        decision.architecture,


                    "agents":
                        decision.agents_used,


                    "success_score":
                        decision.success_score,


                    "reason":
                        "Successful previous architecture"

                }

            )


        return results





    # =============================================
    # Get Best Architecture
    # =============================================


    def get_best_architecture(

        self

    ):


        if not self.repository:

            return None



        decisions = self.repository.find_best_architecture(

            limit=1

        )


        if not decisions:

            return None



        decision = decisions[0]


        return {

            "architecture":
                decision.architecture,


            "success_score":
                decision.success_score,


            "reason":
                "Highest successful architecture decision"

        }

    # =============================================
    # Retrieve Similar Decisions
    # =============================================


    def retrieve_similar_decisions(

        self,

        context: dict,

        limit: int = 5

    ):


        if not self.repository:

            return []


        decisions = self.repository.get_by_context(

            context,

            limit

        )


        results = []


        for decision in decisions:


            results.append(

                {

                    "architecture":
                        decision.architecture,


                    "success_score":
                        decision.success_score,


                    "agents":
                        decision.agents_used,


                    "reason":
                        "Similar successful decision"

                }

            )


        return results


    # =============================================
    # Convert Architecture To Text
    # =============================================

    def architecture_to_text(

        self,

        architecture: dict

    ) -> str:


        words = []


        for layer, values in architecture.items():


            if isinstance(values, dict):

                for key, value in values.items():

                    words.append(

                        str(value)

                    )

            else:

                words.append(

                    str(values)

                )


        return " ".join(words)

    # =============================================
    # Retrieve Similar Architectures
    # =============================================


    def retrieve_similar_architectures(

        self,

        current_request: str,

        limit: int = 5

    ):


        if not self.repository:

            return []



        decisions = self.repository.find_best_architecture(

            limit=20

        )



        ranked = []



        for decision in decisions:



            project_context = decision.project_context or {}



            previous_context = self.context_to_text(

                project_context

            )



            if not previous_context:

                continue



            similarity = self.similarity_engine.compare(

                current_request,

                previous_context

            )



            if similarity["related"]:



                ranked.append(

                    {

                        "architecture":

                            decision.architecture,


                        "agents":

                            decision.agents_used,


                        "similarity_score":

                            similarity["similarity_score"],


                        "success_score":

                            decision.success_score,


                        "reason":

                            "Similar successful project decision"

                    }

                )



        ranked.sort(

            key=lambda item:

                item["similarity_score"],

            reverse=True

        )


        return ranked[:limit]


    # =============================================
    # Convert Context To Text
    # =============================================


    def context_to_text(

        self,

        context: dict

    ) -> str:


        result = []



        def extract(value):


            if isinstance(value, dict):

                for item in value.values():

                    extract(item)



            elif isinstance(value, list):

                for item in value:

                    extract(item)



            else:

                result.append(

                    str(value)

                )



        extract(context)



        return " ".join(result)