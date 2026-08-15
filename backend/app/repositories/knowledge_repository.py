from sqlalchemy.orm import Session

from app.models.knowledge_pattern import KnowledgePattern





class KnowledgeRepository:

    """
    Repository for persistent ASEO knowledge.

    Handles:

    - Creating patterns
    - Updating knowledge
    - Updating feedback scores
    - Retrieving best patterns
    """



    def __init__(

        self,

        db: Session

    ):

        self.db = db





    # =============================================
    # Add Or Update Knowledge
    # =============================================


    def add_pattern(

        self,

        category: str,

        name: str,

        success: bool = True,

        metadata: dict | None = None,

        context: dict | None = None

    ):



        existing = (

            self.db.query(KnowledgePattern)

            .filter(

                KnowledgePattern.category == category,

                KnowledgePattern.name == name

            )

            .first()

        )



        if existing:



            old_count = existing.usage_count



            existing.usage_count += 1



            if success:


                existing.success_rate = (

                    (

                        existing.success_rate * old_count

                    )

                    +

                    100

                ) / existing.usage_count



            else:


                existing.success_rate = (

                    (

                        existing.success_rate * old_count

                    )

                    +

                    0

                ) / existing.usage_count



            if context:

                existing.context = context



            if metadata:

                existing.extra_data = metadata



            self.db.commit()

            self.db.refresh(existing)


            return existing





        pattern = KnowledgePattern(

            category=category,

            name=name,

            usage_count=1,

            success_rate=100 if success else 0,

            priority_score=0.5,

            extra_data=metadata,

            context=context

        )



        self.db.add(pattern)

        self.db.commit()

        self.db.refresh(pattern)



        return pattern





    # =============================================
    # Feedback Update
    # =============================================


    def update_pattern_score(

        self,

        pattern_id: int,

        success: bool

    ):



        pattern = (

            self.db.query(KnowledgePattern)

            .filter(

                KnowledgePattern.id == pattern_id

            )

            .first()

        )



        if not pattern:

            return None



        old_count = pattern.usage_count



        pattern.usage_count += 1



        score = 100 if success else 0



        pattern.success_rate = (

            (

                pattern.success_rate * old_count

            )

            +

            score

        ) / pattern.usage_count



        self.db.commit()

        self.db.refresh(pattern)



        return pattern





    # =============================================
    # Get Top Knowledge
    # =============================================


    def get_top_patterns(

        self,

        category: str | None = None,

        limit: int = 10

    ):



        query = (

            self.db.query(

                KnowledgePattern

            )

        )



        if category:


            query = query.filter(

                KnowledgePattern.category == category

            )



        return (

            query

            .order_by(

                KnowledgePattern.priority_score.desc(),

                KnowledgePattern.success_rate.desc(),

                KnowledgePattern.usage_count.desc()

            )

            .limit(limit)

            .all()

        )





    # =============================================
    # Get All Knowledge Patterns
    # =============================================


    def get_patterns(

        self,

        category: str | None = None

    ):



        query = (

            self.db.query(

                KnowledgePattern

            )

        )



        if category:


            query = query.filter(

                KnowledgePattern.category == category

            )



        return (

            query

            .order_by(

                KnowledgePattern.success_rate.desc(),

                KnowledgePattern.usage_count.desc()

            )

            .all()

        )
    
    # =============================================
    # Get Pattern By Name
    # =============================================

    def get_pattern_by_name(

        self,

        category: str,

        name: str

    ):


        return (

            self.db.query(KnowledgePattern)

            .filter(

                KnowledgePattern.category == category,

                KnowledgePattern.name == name

            )

            .first()

        )


    # =============================================
    # Update Pattern Priority
    # =============================================

    def update_priority(

        self,

        pattern_id: int,

        new_score: float

    ):


        pattern = (

            self.db.query(

                KnowledgePattern

            )

            .filter(

                KnowledgePattern.id == pattern_id

            )

            .first()

        )


        if not pattern:

            return None



        pattern.priority_score = new_score


        self.db.commit()


        self.db.refresh(pattern)


        return pattern

    # =============================================
    # Get Pattern By ID
    # =============================================

    def get_pattern_by_id(

        self,

        pattern_id: int

    ):


        return (

            self.db.query(

                KnowledgePattern

            )

            .filter(

                KnowledgePattern.id == pattern_id

            )

            .first()

        )