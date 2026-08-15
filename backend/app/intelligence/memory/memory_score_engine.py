import math


class MemoryScoreEngine:

    """
    ASEO Memory Score Engine v2

    Responsibilities:

    - Calculate decision memory score
    - Evaluate historical decisions
    - Rank decision memories
    - Reward successful repeated decisions
    """



    def __init__(

        self

    ):

        pass



    # =============================================
    # Calculate Memory Score
    # =============================================


    def calculate_score(

        self,

        similarity_score: float = 0,

        success_score: float = 0,

        usage_count: int = 0,

        confidence: float = 0,

        recency: float = 0

    ) -> float:



        similarity_weight = 0.30

        success_weight = 0.30

        usage_weight = 0.20

        confidence_weight = 0.10

        recency_weight = 0.10



        similarity_score = self.normalize_score(
            similarity_score
        )


        success_score = self.normalize_score(
            success_score
        )


        confidence = self.normalize_score(
            confidence
        )


        recency = self.normalize_score(
            recency
        )



        usage_score = self.calculate_usage_score(
            usage_count
        )



        score = (

            similarity_score *
            similarity_weight

            +

            success_score *
            success_weight

            +

            usage_score *
            usage_weight

            +

            confidence *
            confidence_weight

            +

            recency *
            recency_weight

        )



        return round(

            min(

                max(

                    score,

                    0

                ),

                1

            ),

            2

        )



    # =============================================
    # Usage Score
    # =============================================


    def calculate_usage_score(

        self,

        usage_count: int

    ) -> float:



        if usage_count <= 0:

            return 0



        score = math.log(

            usage_count + 1

        ) / math.log(

            20

        )



        return round(

            min(

                score,

                1

            ),

            2

        )



    # =============================================
    # Recency Score
    # =============================================


    def calculate_recency_score(

        self,

        days_old: int

    ) -> float:



        if days_old <= 0:

            return 1



        decay = math.exp(

            -days_old / 180

        )



        return round(

            decay,

            2

        )



    # =============================================
    # Normalize Score
    # =============================================


    def normalize_score(

        self,

        value

    ):


        if value is None:

            return 0



        try:

            value = float(value)

        except:

            return 0



        if value < 0:

            return 0



        if value > 1:

            value = value / 100



        return round(

            min(

                value,

                1

            ),

            2

        )