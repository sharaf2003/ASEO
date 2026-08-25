from datetime import datetime


from sqlalchemy import (
    String,
    Integer,
    DateTime,
    ForeignKey,
    Numeric
)


from sqlalchemy.orm import (
    Mapped,
    mapped_column
)


from sqlalchemy.sql import func


from app.database.base import Base





class Invoice(Base):

    """
    ASEO SaaS Invoice Model.
    """

    __tablename__ = "invoices"



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



    invoice_number: Mapped[str] = mapped_column(

        String(100),

        unique=True,

        nullable=False

    )



    plan: Mapped[str] = mapped_column(

        String(50),

        nullable=False

    )



    amount: Mapped[float] = mapped_column(

        Numeric(10,2),

        nullable=False

    )



    currency: Mapped[str] = mapped_column(

        String(10),

        default="USD"

    )



    status: Mapped[str] = mapped_column(

        String(50),

        default="pending"

    )



    created_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        server_default=func.now()

    )