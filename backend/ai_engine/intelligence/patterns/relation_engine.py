from datetime import datetime



class RelationEngine:
    """
    ASEO Pattern Relation Engine v2

    Responsible for:

    Pattern Relationship Discovery
    +
    Relation Creation
    +
    Relation Weighting
    +
    Relation Traversal
    +
    Knowledge Graph Intelligence
    """



    def __init__(
        self,
        repository
    ):

        self.repository = repository







    # =====================================
    # Create Relation
    # =====================================


    def create_relation(
        self,
        db,
        source_pattern,
        target_pattern,
        relation_type="extends",
        confidence=0.5
    ):


        if not source_pattern or not target_pattern:

            return None



        if source_pattern.id == target_pattern.id:

            return None






        relation = self.repository.create_pattern_relation(


            db,


            source_id=source_pattern.id,


            target_id=target_pattern.id,


            relation_type=relation_type,


            confidence=confidence,


            usage_count=1,


            extra_data={


                "created_by":

                    "relation_engine",



                "created_at":

                    datetime.utcnow().isoformat()



            }


        )



        return relation







    # =====================================
    # Detect Relation
    # =====================================


    def detect_relation(
        self,
        pattern_a,
        pattern_b
    ):


        score = 0


        reasons = []





        family_a = pattern_a.get(
            "pattern_family",
            ""
        )


        family_b = pattern_b.get(
            "pattern_family",
            ""
        )





        # Same Family

        if family_a and family_a == family_b:


            score += 0.4


            reasons.append(

                "same_pattern_family"

            )







        # Variant similarity


        variant_a = pattern_a.get(
            "variant",
            ""
        )


        variant_b = pattern_b.get(
            "variant",
            ""
        )



        if variant_a and variant_b:


            words_a = set(
                variant_a.lower().split()
            )


            words_b = set(
                variant_b.lower().split()
            )


            intersection = words_a.intersection(
                words_b
            )



            if len(intersection) >= 2:


                score += 0.3


                reasons.append(

                    "shared_variant_components"

                )









        # Category


        category_a = pattern_a.get(
            "category"
        )


        category_b = pattern_b.get(
            "category"
        )


        if category_a == category_b:


            score += 0.2


            reasons.append(

                "same_category"

            )









        # Confidence


        confidence_a = pattern_a.get(
            "confidence",
            pattern_a.get(
                "confidence_score",
                0
            )
        )


        confidence_b = pattern_b.get(
            "confidence",
            pattern_b.get(
                "confidence_score",
                0
            )
        )



        confidence = min(

            confidence_a,

            confidence_b

        )



        score += confidence * 0.1








        score = min(
            score,
            1
        )







        if score >= 0.5:


            return {


                "related": True,


                "relation_type":

                    self.classify_relation(

                        pattern_a,

                        pattern_b

                    ),



                "confidence":

                    round(
                        score,
                        3
                    ),



                "reasons":

                    reasons


            }








        return {


            "related": False,


            "confidence":

                round(
                    score,
                    3
                ),



            "reasons":

                reasons

        }









    # =====================================
    # Classify Relation
    # =====================================


    def classify_relation(
        self,
        pattern_a,
        pattern_b
    ):



        family_a = pattern_a.get(
            "pattern_family"
        )


        family_b = pattern_b.get(
            "pattern_family"
        )




        if family_a == family_b:


            return "variant_of"





        return "extends"









    # =====================================
    # Automatic Relation Discovery
    # =====================================


    def analyze_patterns(
        self,
        db,
        patterns
    ):



        relations = []



        for i in range(len(patterns)):



            for j in range(
                i + 1,
                len(patterns)
            ):



                result = self.detect_relation(


                    patterns[i],


                    patterns[j]


                )





                if result.get(
                    "related"
                ):



                    relation = self.create_relation(


                        db,


                        patterns[i],


                        patterns[j],


                        result.get(
                            "relation_type"
                        ),


                        result.get(
                            "confidence"
                        )

                    )



                    if relation:

                        relations.append(
                            relation
                        )




        return relations







    # =====================================
    # Related Patterns Query
    # =====================================


    def get_related(
        self,
        db,
        pattern_id
    ):



        return self.repository.get_related_patterns(


            db,


            pattern_id


        )