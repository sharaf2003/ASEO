from datetime import datetime


from sqlalchemy import (
    String,
    DateTime,
    ForeignKey,
    Integer
)


from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)


from sqlalchemy.sql import func


from app.database.base import Base





class APIUsage(Base):

    """
    ASEO API Usage Tracking.

    Stores external API consumption
    for billing and analytics.
    """

    __tablename__ = "api_usage"



    id: Mapped[int] = mapped_column(

        primary_key=True,

        index=True

    )



    api_key_id: Mapped[int] = mapped_column(

        ForeignKey(
            "api_keys.id"
        ),

        nullable=False,

        index=True

    )



    endpoint: Mapped[str] = mapped_column(

        String(255),

        nullable=False

    )



    requests_count: Mapped[int] = mapped_column(

        Integer,

        nullable=False,

        default=1

    )



    created_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        server_default=func.now()

    )



    api_key = relationship(

        "APIKey"

    )