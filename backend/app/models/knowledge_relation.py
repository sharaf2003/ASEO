from datetime import datetime


from sqlalchemy import (
    String,
    Integer,
    DateTime,
    JSON,
    ForeignKey
)


from sqlalchemy.orm import (
    Mapped,
    mapped_column
)


from sqlalchemy.sql import func


from app.database.base import Base





class KnowledgeRelation(Base):

    """
    Stores relationships between
    learned knowledge patterns.

    Examples:

    FastAPI -> works_with -> PostgreSQL

    React -> frontend_type -> SPA

    Docker -> deploys -> FastAPI
    """



    __tablename__ = "knowledge_relations"



    id: Mapped[int] = mapped_column(

        primary_key=True,

        index=True

    )



    source_id: Mapped[int] = mapped_column(

        ForeignKey(

            "knowledge_patterns.id",

            ondelete="CASCADE"

        ),

        nullable=False,

        index=True

    )



    target_id: Mapped[int] = mapped_column(

        ForeignKey(

            "knowledge_patterns.id",

            ondelete="CASCADE"

        ),

        nullable=False,

        index=True

    )



    relation_type: Mapped[str] = mapped_column(

        String(100),

        nullable=False,

        index=True

    )



    confidence: Mapped[float] = mapped_column(

        default=0.0,

        nullable=False

    )



    usage_count: Mapped[int] = mapped_column(

        Integer,

        default=1,

        nullable=False

    )



    extra_data: Mapped[dict | None] = mapped_column(

        JSON,

        nullable=True

    )



    created_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        server_default=func.now()

    )