from sqlalchemy.orm import Session

from app.models.decision_history import DecisionHistory





class DecisionHistoryRepository:

    """
    Repository for storing and retrieving
    previous AI decisions.

    Used for:

    - Architecture learning
    - Decision improvement
    - Experience reuse
    """



    def __init__(

        self,

        db: Session

    ):

        self.db = db





    # =============================================
    # Save Decision
    # =============================================


    def save_decision(

        self,

        architecture: dict,

        agents_used: list,

        success_score: float,

        project_id: int | None = None,

        extra_data: dict | None = None,

        project_context: dict | None = None

    ) -> DecisionHistory:



        decision = DecisionHistory(

            project_id=project_id,

            architecture=architecture,

            agents_used=agents_used,

            success_score=success_score,

            extra_data=extra_data,

            project_context=project_context,

        )


        self.db.add(

            decision

        )


        self.db.commit()


        self.db.refresh(

            decision

        )


        return decision





    # =============================================
    # Get Successful Decisions
    # =============================================


    def get_successful_decisions(

        self,

        limit: int = 10

    ) -> list[DecisionHistory]:


        return (

            self.db.query(

                DecisionHistory

            )

            .filter(

                DecisionHistory.success_score >= 0.8

            )

            .order_by(

                DecisionHistory.success_score.desc()

            )

            .limit(

                limit

            )

            .all()

        )





    # =============================================
    # Find Best Architecture
    # =============================================


    def find_best_architecture(

        self,

        limit: int = 1

    ) -> list[DecisionHistory]:


        return (

            self.db.query(

                DecisionHistory

            )

            .order_by(

                DecisionHistory.success_score.desc()

            )

            .limit(

                limit

            )

            .all()

        )





    # =============================================
    # Count Decisions
    # =============================================


    def count_decisions(

        self

    ) -> int:


        return (

            self.db.query(

                DecisionHistory

            )

            .count()

        )

    # =============================================
    # Get Decisions By Context
    # =============================================


    def get_by_context(

        self,

        context: dict,

        limit: int = 5

    ):


        decisions = (

            self.db.query(

                DecisionHistory

            )

            .order_by(

                DecisionHistory.success_score.desc()

            )

            .limit(

                limit

            )

            .all()

        )


        return decisions