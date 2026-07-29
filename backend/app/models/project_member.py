from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.base import Base


class ProjectMember(Base):

    __tablename__ = "project_members"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    project_id = Column(
        Integer,
        ForeignKey(
            "projects.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )


    user_id = Column(
        Integer,
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )


    role = Column(
        String(50),
        nullable=False,
        default="MEMBER"
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )


    user = relationship(
        "User",
        back_populates="project_memberships"
    )


    project = relationship(
        "Project",
        back_populates="members"
    )