from datetime import datetime

from sqlalchemy import (
    String,
    Integer,
    Float,
    DateTime,
    JSON
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from sqlalchemy.sql import func

from app.database.base import Base



class KnowledgePattern(Base):

    """
    Persistent knowledge extracted
    from thousands of projects.

    Stores:

    - Technologies
    - Architectures
    - Solutions
    - Problems
    - Success patterns
    """



    __tablename__ = "knowledge_patterns"



    id: Mapped[int] = mapped_column(

        primary_key=True,

        index=True

    )



    category: Mapped[str] = mapped_column(

        String(100),

        nullable=False,

        index=True

    )



    name: Mapped[str] = mapped_column(

        String(255),

        nullable=False,

        index=True

    )



    usage_count: Mapped[int] = mapped_column(

        Integer,

        nullable=False,

        default=1

    )



    success_rate: Mapped[float] = mapped_column(

        Float,

        nullable=False,

        default=0.0

    )

    priority_score: Mapped[float] = mapped_column(

        Float,

        nullable=False,

        default=0.5

    )



    extra_data: Mapped[dict | None] = mapped_column(

        JSON,

        nullable=True

    )

    context: Mapped[dict | None] = mapped_column(

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
