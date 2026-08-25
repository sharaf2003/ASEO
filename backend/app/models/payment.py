from datetime import datetime


from sqlalchemy import (
    Integer,
    String,
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





class Payment(Base):

    """
    ASEO Payment Transaction Model.
    """

    __tablename__ = "payments"



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



    invoice_id: Mapped[int] = mapped_column(

        ForeignKey(
            "invoices.id"
        ),

        nullable=False,

        index=True

    )



    transaction_id: Mapped[str] = mapped_column(

        String(255),

        unique=True,

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



    provider: Mapped[str] = mapped_column(

        String(50),

        default="manual"

    )



    status: Mapped[str] = mapped_column(

        String(50),

        default="pending"

    )



    created_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        server_default=func.now()

    )