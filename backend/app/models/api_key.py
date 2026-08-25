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





class APIKey(Base):

    """
    ASEO External API Key.

    Represents an API credential
    owned by an organization.
    """

    __tablename__ = "api_keys"



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



    name: Mapped[str] = mapped_column(

        String(100),

        nullable=False

    )



    key_hash: Mapped[str] = mapped_column(

        String(255),

        nullable=False,

        unique=True,

        index=True

    )



    status: Mapped[str] = mapped_column(

        String(50),

        nullable=False,

        default="active"

    )



    created_at: Mapped[datetime] = mapped_column(

        DateTime(timezone=True),

        server_default=func.now()

    )



    expires_at: Mapped[datetime | None] = mapped_column(

        DateTime(timezone=True),

        nullable=True

    )



    last_used_at: Mapped[datetime | None] = mapped_column(

        DateTime(timezone=True),

        nullable=True

    )



    organization = relationship(

        "Organization"

    )