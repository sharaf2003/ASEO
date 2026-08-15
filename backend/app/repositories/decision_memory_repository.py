from datetime import datetime

from sqlalchemy.orm import Session

from app.models.decision_memory import DecisionMemory



class DecisionMemoryRepository:


    """
    Repository for permanent decision memory storage.
    """



    def __init__(

        self,

        db: Session

    ):

        self.db = db



    # =============================================
    # Save Memory
    # =============================================


    def save_memory(

        self,

        data: dict

    ) -> DecisionMemory:


        memory = DecisionMemory(

            decision_history_id=data.get(
                "decision_history_id"
            ),


            agent_name=data.get(
                "agent_name",
                "ArchitectAgent"
            ),


            architecture=data.get(
                "architecture",
                {}
            ),


            similarity_score=data.get(
                "similarity_score",
                0
            ),


            success_score=data.get(
                "success_score",
                0
            ),


            memory_score=data.get(
                "memory_score",
                0
            ),

            adaptive_decision_score=data.get(
                "adaptive_decision_score",
                0
            ),

            memory_strength=data.get(
                "memory_strength",
                0
            ),


            usage_count=data.get(
                "usage_count",
                0
            ),


            extra_data=data.get(
                "extra_data",
                {}
            ),

            confidence=data.get(
                "confidence",
                0
            )

        )


        self.db.add(memory)

        self.db.commit()

        self.db.refresh(memory)


        return memory



    # =============================================
    # Get All Memories
    # =============================================


    def get_all_memories(

        self

    ) -> list:


        return (

            self.db.query(

                DecisionMemory

            )

            .order_by(

                DecisionMemory.success_score.desc(),

                DecisionMemory.usage_count.desc(),

                DecisionMemory.memory_score.desc()

            )

            .all()

        )



    # =============================================
    # Get Memory By ID
    # =============================================


    def get_memory(

        self,

        memory_id: int

    ):


        return (

            self.db.query(

                DecisionMemory

            )

            .filter(

                DecisionMemory.id == memory_id

            )

            .first()

        )



    # =============================================
    # Update Usage
    # =============================================


    def increase_usage(

        self,

        memory_id: int

    ):


        memory = self.get_memory(

            memory_id

        )


        if not memory:

            return None



        memory.usage_count += 1

        memory.memory_strength = (
            (memory.confidence * 0.4)
            +
            (memory.memory_score * 0.3)
            +
            (min(memory.usage_count / 50, 1) * 0.2)
            +
            0.1
        )



        if hasattr(

            memory,

            "updated_at"

        ):

            memory.updated_at = datetime.utcnow()



        self.db.commit()

        self.db.refresh(memory)


        return memory



    # =============================================
    # Update Memory Score
    # =============================================


    def update_score(

        self,

        memory_id: int,

        score: float

    ):


        memory = self.get_memory(

            memory_id

        )


        if not memory:

            return None



        memory.memory_score = score



        if hasattr(

            memory,

            "updated_at"

        ):

            memory.updated_at = datetime.utcnow()



        self.db.commit()

        self.db.refresh(memory)


        return memory


    # =============================================
    # Update Confidence
    # =============================================

    def update_confidence(

        self,

        memory_id: int,

        confidence: float

    ):


        memory = self.get_memory(

            memory_id

        )


        if not memory:

            return None



        memory.confidence = confidence



        if hasattr(

            memory,

            "updated_at"

        ):

            memory.updated_at = datetime.utcnow()



        self.db.commit()

        self.db.refresh(memory)


        return memory


    