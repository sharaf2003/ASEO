from datetime import datetime


from sqlalchemy import (
    Integer,
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





class APIRateLimit(Base):

    """
    ASEO API Rate Limit.

    Defines request limits
    for external API keys.
    """



    __tablename__ = "api_rate_limits"





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





    requests_per_minute: Mapped[int] = mapped_column(

        Integer,

        nullable=False,

        default=100

    )





    requests_per_day: Mapped[int] = mapped_column(

        Integer,

        nullable=False,

        default=10000

    )





    requests_per_month: Mapped[int] = mapped_column(

        Integer,

        nullable=False,

        default=100000

    )





    created_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        server_default=func.now()

    )





    updated_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        server_default=func.now(),

        onupdate=func.now()

    )





    api_key = relationship(

        "APIKey"

    )