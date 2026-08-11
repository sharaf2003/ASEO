from datetime import datetime


from sqlalchemy import (
    Column,
    String,
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
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.project_member import ProjectMember




class User(Base):

    """
    ASEO Platform User.

    Belongs to an organization
    and workspace.
    """

    __tablename__ = "users"



    id: Mapped[int] = mapped_column(

        primary_key=True,

        index=True

    )



    organization_id: Mapped[int] = mapped_column(

        ForeignKey(
            "organizations.id"
        ),

        nullable=False,

        index=True

    )



    workspace_id: Mapped[int] = mapped_column(

        ForeignKey(
            "workspaces.id"
        ),

        nullable=False,

        index=True

    )



    email: Mapped[str] = mapped_column(

        String(255),

        nullable=False,

        unique=True,

        index=True

    )



    password_hash: Mapped[str] = mapped_column(

        String(255),

        nullable=False

    )



    role: Mapped[str] = mapped_column(

        String(50),

        nullable=False,

        default="MEMBER"

    )



    created_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        server_default=func.now()

    )
    name = Column(
        String(100),
        nullable=False
    )   
    projects = relationship(
        "Project",
        back_populates="owner",
        cascade="all, delete-orphan"
    )
    
    project_memberships = relationship(
        "ProjectMember",
        back_populates="user",
        cascade="all, delete-orphan"
    )