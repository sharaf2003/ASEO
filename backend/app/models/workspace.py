from datetime import datetime

from sqlalchemy import (
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from sqlalchemy.sql import func

from app.database.base import Base



class Workspace(Base):

    """
    ASEO Workspace.

    Logical environment inside an organization.
    """

    __tablename__ = "workspaces"



    id: Mapped[int] = mapped_column(

        primary_key=True,

        index=True

    )



    organization_id: Mapped[int] = mapped_column(

        ForeignKey(
            "organizations.id"
        ),

        nullable=False

    )



    name: Mapped[str] = mapped_column(

        String(200),

        nullable=False

    )



    created_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        server_default=func.now()

    )