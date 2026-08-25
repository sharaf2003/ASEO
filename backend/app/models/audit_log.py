from datetime import datetime


from sqlalchemy import (
    String,
    DateTime,
    Integer,
    Text
)


from sqlalchemy.orm import (
    Mapped,
    mapped_column
)


from sqlalchemy.sql import func


from app.database.base import Base





class AuditLog(Base):

    """
    ASEO Audit Log Model.
    """



    __tablename__ = "audit_logs"



    id: Mapped[int] = mapped_column(

        primary_key=True,

        index=True

    )



    organization_id: Mapped[int | None] = mapped_column(

        Integer,

        nullable=True,

        index=True

    )



    user_id: Mapped[int | None] = mapped_column(

        Integer,

        nullable=True

    )



    action: Mapped[str] = mapped_column(

        String(100),

        nullable=False

    )



    description: Mapped[str | None] = mapped_column(

        Text,

        nullable=True

    )



    created_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        server_default=func.now()

    )