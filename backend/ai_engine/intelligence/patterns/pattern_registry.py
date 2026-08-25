from datetime import datetime
from copy import deepcopy


from ai_engine.database import (
    SessionLocal,
    DatabaseRepository
)



class PatternRegistry:
    """
    ASEO Pattern Registry v26

    Persistent Engineering Pattern Intelligence

    RAM Cache
    +
    PostgreSQL Storage
    +
    Automatic Recovery
    +
    Feedback Learning
    +
    Pattern Evolution
    +
    Dynamic Rescoring
    +
    Variant Tracking
    +
    Success Tracking
    """



    def __init__(self):

        self.patterns = {}

        self.repository = DatabaseRepository()

        self.load_patterns()





    # =====================================
    # Load Patterns
    # =====================================

    def load_patterns(self):

        db = SessionLocal()

        try:

            records = self.repository.get_all_patterns(
                db
            )


            for record in records:


                pattern = record.extra_data or {}
                
                pattern["id"] = record.id


                if not pattern.get("name"):

                    continue



                pattern["usage_count"] = (
                    record.usage_count or 0
                )


                pattern["success_rate"] = (
                    record.success_rate or 0
                )


                pattern.setdefault(
                    "success_count",
                    0
                )


                pattern.setdefault(
                    "failure_count",
                    0
                )


                pattern.setdefault(
                    "failure_rate",
                    0
                )


                pattern.setdefault(
                    "pattern_family",
                    record.pattern_family
                    or pattern.get("name")
                )


                pattern.setdefault(
                    "variant",
                    record.variant
                    or pattern.get(
                        "architecture",
                        ""
                    )
                )


                pattern.setdefault(
                    "priority_score",
                    record.priority_score
                    or 0.5
                )


                pattern.setdefault(
                    "context",
                    record.context
                    or {}
                )



                self.patterns[
                    pattern["name"]
                ] = pattern



        finally:

            db.close()







    # =====================================
    # Register Pattern
    # =====================================

    def register(
        self,
        pattern
    ):


        name = pattern.get(
            "name"
        )


        if not name:

            return None





        # =====================================
        # Existing Pattern
        # =====================================


        if name in self.patterns:


            existing = self.patterns[name]



            existing["confidence"] = max(

                existing.get(
                    "confidence",
                    0
                ),

                pattern.get(
                    "confidence",
                    0
                )

            )



            existing["pattern_family"] = (

                pattern.get(

                    "pattern_family",

                    existing.get(
                        "pattern_family"
                    )

                )

            )



            existing["variant"] = (

                pattern.get(

                    "variant",

                    existing.get(
                        "variant"
                    )

                )

            )



            existing["priority_score"] = (

                pattern.get(

                    "priority_score",

                    existing.get(
                        "priority_score",
                        0.5
                    )

                )

            )



            existing["context"] = (

                pattern.get(

                    "context",

                    existing.get(
                        "context",
                        {}
                    )

                )

            )



            existing["last_used"] = (
                datetime.utcnow()
            )


            self._persist(
                existing
            )


            return existing







        # =====================================
        # New Pattern
        # =====================================


        stored = deepcopy(
            pattern
        )



        stored["usage_count"] = 0



        stored.setdefault(
            "success_count",
            0
        )


        stored.setdefault(
            "failure_count",
            0
        )


        stored.setdefault(
            "success_rate",
            0
        )


        stored.setdefault(
            "failure_rate",
            0
        )



        stored.setdefault(
            "pattern_family",
            stored.get(
                "name"
            )
        )



        stored.setdefault(
            "variant",
            stored.get(
                "architecture",
                ""
            )
        )



        stored.setdefault(
            "priority_score",
            stored.get(
                "confidence",
                0.5
            )
        )



        stored.setdefault(
            "context",
            {}
        )



        now = datetime.utcnow()



        stored["created_at"] = now

        stored["last_used"] = now



        self.patterns[name] = stored



        self._persist(
            stored
        )


        return stored







    # =====================================
    # Record Feedback Result
    # =====================================

    def record_result(
        self,
        pattern_name,
        success=True
    ):


        pattern = self.patterns.get(
            pattern_name
        )


        if not pattern:

            return None





        if success:


            pattern["success_count"] = (

                pattern.get(
                    "success_count",
                    0
                )

                + 1

            )


            pattern["last_success_at"] = (
                datetime.utcnow()
            )



        else:


            pattern["failure_count"] = (

                pattern.get(
                    "failure_count",
                    0
                )

                + 1

            )






        total = (

            pattern.get(
                "success_count",
                0
            )

            +

            pattern.get(
                "failure_count",
                0
            )

        )



        if total:


            pattern["success_rate"] = round(

                pattern["success_count"]

                /

                total,

                3

            )


            pattern["failure_rate"] = round(

                pattern["failure_count"]

                /

                total,

                3

            )







        # =====================================
        # Dynamic Rescore
        # =====================================


        from ai_engine.intelligence.patterns.pattern_scorer import (
            PatternScorer
        )


        scorer = PatternScorer()


        score_data = scorer.score(
            pattern
        )


        pattern.update(
            score_data
        )




        pattern["last_used"] = (
            datetime.utcnow()
        )



        self.patterns[
            pattern_name
        ] = pattern



        self._persist(
            pattern
        )


        return pattern







    # =====================================
    # Persist
    # =====================================

    def _persist(
        self,
        pattern
    ):


        db = SessionLocal()


        try:

            self.repository.save_or_update_pattern(

                db,

                pattern

            )


        finally:

            db.close()







    # =====================================
    # Get
    # =====================================

    def get(
        self,
        name
    ):

        return self.patterns.get(
            name
        )









    # =====================================
    # Find Pattern
    # =====================================

    def find(
        self,
        keyword
    ):


        results = []


        keyword = keyword.lower()



        for pattern in self.patterns.values():


            text = (

                pattern.get(
                    "name",
                    ""
                )

                +

                " "

                +

                pattern.get(
                    "architecture",
                    ""
                )

                +

                " "

                +

                pattern.get(
                    "pattern_family",
                    ""
                )

                +

                " "

                +

                pattern.get(
                    "variant",
                    ""
                )

            ).lower()



            if keyword in text:


                results.append(
                    pattern
                )



        return results








    # =====================================
    # All Patterns
    # =====================================

    def all(self):

        return list(
            self.patterns.values()
        )