from datetime import datetime

from sqlalchemy import (
    String,
    DateTime,
    JSON,
    ForeignKey,
    Text
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from sqlalchemy.sql import func

from app.database.base import Base



class Task(Base):

    """
    Persistent execution task.

    Stores autonomous agent tasks
    generated during execution lifecycle.
    """

    __tablename__ = "tasks"


    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )


    execution_id: Mapped[int] = mapped_column(
        ForeignKey(
            "execution_records.id"
        ),
        nullable=False,
        index=True
    )


    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )


    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )


    agent_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )


    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="PENDING"
    )


    input_data: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True
    )


    output_data: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )


    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )


    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )


    execution = relationship(
        "ExecutionRecord",
        back_populates="tasks"
    )