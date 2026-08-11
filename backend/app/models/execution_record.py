from datetime import datetime

from sqlalchemy import (
    String,
    DateTime,
    JSON,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from sqlalchemy.sql import func

from app.database.base import Base



class ExecutionRecord(Base):

    """
    Stores ASEO autonomous execution history.

    Each execution belongs to a project.
    """

    __tablename__ = "execution_records"



    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )



    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id"),
        nullable=False,
        index=True
    )



    request: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )



    team: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True
    )



    software: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True
    )



    deployment: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True
    )



    operations: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True
    )



    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="QUEUED"
    )



    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )



    finished_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )



    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )



    project = relationship(
        "Project",
        back_populates="executions"
    )