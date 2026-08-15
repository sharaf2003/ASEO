from datetime import datetime

from sqlalchemy import (

    Integer,
    Float,
    DateTime,
    JSON,
    String
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from sqlalchemy.sql import func

from app.database.base import Base



class DecisionMemory(Base):

    """
    Permanent memory for successful decisions.

    Stores reusable experiences from previous executions.
    """


    __tablename__ = "decision_memory"



    id: Mapped[int] = mapped_column(

        Integer,

        primary_key=True,

        index=True

    )



    decision_history_id: Mapped[int | None] = mapped_column(

        Integer,

        nullable=True,

        index=True

    )



    agent_name: Mapped[str] = mapped_column(

        String,

        nullable=False

    )



    architecture: Mapped[dict] = mapped_column(

        JSON,

        nullable=False

    )



    similarity_score: Mapped[float] = mapped_column(

        Float,

        nullable=False,

        default=0.0

    )



    success_score: Mapped[float] = mapped_column(

        Float,

        nullable=False,

        default=0.0

    )



    memory_score: Mapped[float] = mapped_column(

        Float,

        nullable=False,

        default=0.0

    )


    adaptive_decision_score: Mapped[float] = mapped_column(

        Float,

        nullable=False,

        default=0.0

    )

    memory_strength = mapped_column(
        Float,
        default=0
    )

    confidence: Mapped[float] = mapped_column(

        Float,

        nullable=False,

        default=0.0

    )

    usage_count: Mapped[int] = mapped_column(

        Integer,

        nullable=False,

        default=0

    )



    extra_data: Mapped[dict | None] = mapped_column(

        JSON,

        nullable=True

    )



    created_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        server_default=func.now()

    )


    updated_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        server_default=func.now(),

        onupdate=func.now()

    )