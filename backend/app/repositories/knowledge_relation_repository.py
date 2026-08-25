from sqlalchemy.orm import Session

from app.models.knowledge_relation import (
    KnowledgeRelation
)



class KnowledgeRelationRepository:
    """
    Repository for knowledge graph relations.
    """



    def __init__(
        self,
        db: Session
    ):

        self.db = db



    # =====================================================
    # Create Relation
    # =====================================================

    def add_relation(

        self,

        source_id: int,

        target_id: int,

        relation_type: str,

        confidence: float = 0.0,

        extra_data: dict | None = None

    ):


        relation = KnowledgeRelation(

            source_id=source_id,

            target_id=target_id,

            relation_type=relation_type,

            confidence=confidence,

            extra_data=extra_data

        )


        self.db.add(

            relation

        )


        self.db.commit()


        self.db.refresh(

            relation

        )


        return relation