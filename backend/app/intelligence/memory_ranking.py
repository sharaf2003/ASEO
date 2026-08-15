from datetime import datetime, timezone



class MemoryRankingEngine:

    """
    ASEO Memory Ranking Engine v1

    Ranks memories using:

    - Similarity
    - Success score
    - Usage frequency
    - Recent usage

    """



    def __init__(self):

        pass



    # =============================================
    # Calculate Memory Score
    # =============================================


    def calculate_score(

        self,

        memory,

        similarity: float

    ) -> float:


        success_score = (

            memory.success_score or 0

        )



        usage_count = (

            memory.usage_count or 0

        )



        recency_score = self.calculate_recency(

            memory.last_used

        )



        final_score = (

            similarity * 0.5

            +

            success_score * 0.3

            +

            min(

                usage_count * 5,

                100

            ) * 0.1

            +

            recency_score * 0.1

        )



        return round(

            final_score,

            2

        )



    # =============================================
    # Recency
    # =============================================


    def calculate_recency(

        self,

        last_used

    ) -> float:


        if not last_used:

            return 0



        now = datetime.now(

            timezone.utc

        )



        days = (

            now - last_used

        ).days



        if days <= 1:

            return 100



        if days <= 7:

            return 70



        if days <= 30:

            return 40



        return 10



    # =============================================
    # Rank Memories
    # =============================================


    def rank(

        self,

        memories: list,

        similarity_scores: dict

    ) -> list:


        ranked = []



        for memory in memories:


            similarity = similarity_scores.get(

                memory.id,

                0

            )



            score = self.calculate_score(

                memory,

                similarity

            )



            ranked.append(

                {

                    "memory": memory,

                    "ranking_score": score

                }

            )



        return sorted(

            ranked,

            key=lambda x: x["ranking_score"],

            reverse=True

        )