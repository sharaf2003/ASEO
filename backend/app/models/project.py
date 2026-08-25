from datetime import datetime

import uuid

from sqlalchemy import (
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from sqlalchemy.sql import func

from app.database.base import Base



class Project(Base):
    """
    Project database model.

    Represents generated ASEO projects.
    """


    __tablename__ = "projects"



    id: Mapped[int] = mapped_column(

        String(36),

        primary_key=True,

        default=lambda: str(uuid.uuid4()),

        index=True

    )
    organization_id: Mapped[int] = mapped_column(

        ForeignKey(
            "organizations.id",
            ondelete="CASCADE"
        ),

        nullable=False,

        index=True

    )



    workspace_id: Mapped[int] = mapped_column(

        ForeignKey(
            "workspaces.id",
            ondelete="CASCADE"
        ),

        nullable=False,

        index=True

    )

    owner_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
               "users.id",
               ondelete="CASCADE"
        ),
        nullable=False,
        index=True
    )

    owner = relationship(
        "User",
        back_populates="projects"
        
    )

    name: Mapped[str] = mapped_column(

        String(200),

        nullable=False,

        index=True

    )



    description: Mapped[str | None] = mapped_column(

        Text,

        nullable=True

    )



    status: Mapped[str] = mapped_column(

        String(50),

        nullable=False,

        default="created",

        index=True

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



    # ==========================
    # Execution History
    # ==========================

    executions = relationship(

        "ExecutionRecord",

        back_populates="project",

        cascade="all, delete-orphan"

    )

    members = relationship(
        "ProjectMember",
        back_populates="project",
        cascade="all, delete-orphan"
    )
    
    invitations = relationship(
        "ProjectInvitation",
        back_populates="project",
        cascade="all, delete-orphan"
    )