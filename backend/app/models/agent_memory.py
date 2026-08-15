from datetime import datetime

from pgvector.sqlalchemy import Vector

from sqlalchemy import (
    String,
    DateTime,
    JSON,
    ForeignKey,
    Integer,
    Float
)


from sqlalchemy.orm import (
    Mapped,
    mapped_column
)


from sqlalchemy.sql import func


from app.database.base import Base



class AgentMemory(Base):

    """
    Persistent memory storage for ASEO agents.

    Stores:

    - Agent experiences
    - Successful executions
    - Failed attempts
    - Learned patterns
    - Memory ranking data
    """



    __tablename__ = "agent_memories"



    id: Mapped[int] = mapped_column(

        primary_key=True,

        index=True

    )



    agent_name: Mapped[str] = mapped_column(

        String(100),

        nullable=False,

        index=True

    )



    memory_type: Mapped[str] = mapped_column(

        String(50),

        nullable=False,

        index=True

    )



    content: Mapped[dict | None] = mapped_column(

        JSON,

        nullable=True

    )



    # =============================================
    # Memory Ranking Fields
    # =============================================


    success_score: Mapped[float] = mapped_column(

        Float,

        nullable=False,

        default=0.0

    )



    usage_count: Mapped[int] = mapped_column(

        Integer,

        nullable=False,

        default=0

    )



    last_used: Mapped[datetime | None] = mapped_column(

        DateTime(timezone=True),

        nullable=True

    )



    # =============================================
    # Relations
    # =============================================


    project_id: Mapped[int | None] = mapped_column(

        ForeignKey(

            "projects.id",

            ondelete="CASCADE"

        ),

        nullable=True,

        index=True

    )



    organization_id: Mapped[int | None] = mapped_column(

        ForeignKey(

            "organizations.id",

            ondelete="CASCADE"

        ),

        nullable=True,

        index=True

    )



    created_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        server_default=func.now()

    )

    embedding: Mapped[list[float] | None] = mapped_column(
        Vector(1536),
        nullable=True
    )