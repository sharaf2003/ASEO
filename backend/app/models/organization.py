from datetime import datetime

from sqlalchemy import (
    String,
    DateTime
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from sqlalchemy.sql import func

from app.database.base import Base




class Organization(Base):

    """
    ASEO Tenant Organization.

    Represents customer/company account.
    """

    __tablename__ = "organizations"



    id: Mapped[int] = mapped_column(

        primary_key=True,

        index=True

    )



    name: Mapped[str] = mapped_column(

        String(200),

        nullable=False,

        unique=True

    )



    plan: Mapped[str] = mapped_column(

        String(50),

        default="free"

    )



    created_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        server_default=func.now()

    )