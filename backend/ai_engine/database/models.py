from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer


from .base import Base



class CustomerModel(Base):

    __tablename__ = "customers"


    id = Column(

        String,

        primary_key=True

    )


    name = Column(

        String,

        nullable=False

    )


    plan = Column(

        String,

        default="Free"

    )






class ProjectModel(Base):

    __tablename__ = "projects"


    id = Column(

        String,

        primary_key=True

    )


    name = Column(

        String,

        nullable=False

    )


    status = Column(

        String,

        default="created"

    )


    quality = Column(

        Integer,

        default=0

    )