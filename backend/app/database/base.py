"""
Base database model for all SQLAlchemy entities.
"""

from sqlalchemy.orm import DeclarativeBase



class Base(DeclarativeBase):
    """
    SQLAlchemy declarative base.
    All models inherit from this class.
    """

    pass