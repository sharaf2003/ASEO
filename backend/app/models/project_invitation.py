from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.base import Base



class ProjectInvitation(Base):

    __tablename__ = "project_invitations"


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
        nullable=False,
        index=True
    )


    email = Column(
        String(255),
        nullable=False,
        index=True
    )


    role = Column(
        String(50),
        nullable=False,
        default="MEMBER"
    )


    status = Column(
        String(50),
        nullable=False,
        default="PENDING"
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )


    expires_at = Column(
        DateTime(timezone=True),
        nullable=True
    )


    project = relationship(
        "Project",
        back_populates="invitations"
    )