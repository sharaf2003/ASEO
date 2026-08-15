from datetime import datetime

from sqlalchemy import (
    Integer,
    Float,
    DateTime,
    JSON,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from sqlalchemy.sql import func

from app.database.base import Base





class DecisionHistory(Base):

    """
    Stores previous successful decisions.

    Used for:

    - Architecture experience
    - Agent performance learning
    - Future decision improvement
    """



    __tablename__ = "decision_history"



    id: Mapped[int] = mapped_column(

        Integer,

        primary_key=True,

        index=True

    )



    project_id: Mapped[int | None] = mapped_column(

        Integer,

        nullable=True,

        index=True

    )



    architecture: Mapped[dict] = mapped_column(

        JSON,

        nullable=False

    )



    agents_used: Mapped[list] = mapped_column(

        JSON,

        nullable=False

    )



    success_score: Mapped[float] = mapped_column(

        Float,

        nullable=False,

        default=0.0

    )



    extra_data: Mapped[dict | None] = mapped_column(

        JSON,

        nullable=True

    )


    project_context: Mapped[dict | None] = mapped_column(

        JSON,

        nullable=True

    )

    created_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        server_default=func.now()

    )
