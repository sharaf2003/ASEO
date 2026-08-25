from datetime import datetime


from sqlalchemy import (
    String,
    Integer,
    Numeric,
    DateTime,
    ForeignKey
)


from sqlalchemy.orm import (
    Mapped,
    mapped_column
)


from sqlalchemy.sql import func


from app.database.base import Base





class UsageBilling(Base):

    """
    ASEO Usage Billing Model.
    """

    __tablename__ = "usage_billings"



    id: Mapped[int] = mapped_column(

        Integer,

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



    month: Mapped[str] = mapped_column(

        String(7),

        nullable=False

    )



    total_requests: Mapped[int] = mapped_column(

        Integer,

        default=0

    )



    included_requests: Mapped[int] = mapped_column(

        Integer,

        default=0

    )



    extra_requests: Mapped[int] = mapped_column(

        Integer,

        default=0

    )



    cost: Mapped[float] = mapped_column(

        Numeric(10,2),

        default=0

    )



    created_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        server_default=func.now()

    )