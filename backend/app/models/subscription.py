from datetime import datetime


from sqlalchemy import (
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





class Subscription(Base):

    """
    ASEO SaaS Subscription.

    Represents organization subscription plan.
    """



    __tablename__ = "subscriptions"





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





    plan: Mapped[str] = mapped_column(

        String(50),

        nullable=False,

        default="free"

    )





    status: Mapped[str] = mapped_column(

        String(50),

        nullable=False,

        default="active"

    )





    started_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        server_default=func.now()

    )





    expires_at: Mapped[datetime | None] = mapped_column(

        DateTime(timezone=True),

        nullable=True

    )





    organization = relationship(

        "Organization"

    )