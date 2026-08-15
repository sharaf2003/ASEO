from sqlalchemy import Column, Integer, DateTime

from datetime import datetime

from app.database.base import Base



class MemorySystemState(Base):


    __tablename__ = "memory_system_state"


    id = Column(
        Integer,
        primary_key=True
    )


    last_consolidation_count = Column(
        Integer,
        default=0
    )


    total_consolidations = Column(
        Integer,
        default=0
    )


    last_consolidation_time = Column(
        DateTime,
        default=datetime.utcnow
    )