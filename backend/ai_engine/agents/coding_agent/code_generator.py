class CodeGenerator:
    """
    ASEO Code Generator v4

    Generates layered architecture source code.

    Creates separated:
    - Models
    - Schemas
    - Services
    - Routes
    - Repositories
    """



    def generate_model(
        self,
        entity
    ):

        class_name = entity.capitalize()

        return f"""

from sqlalchemy import Column, Integer, DateTime
from app.database.base import Base
from datetime import datetime


class {class_name}(Base):

    __tablename__ = "{entity.lower()}s"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

"""



    def generate_service(
        self,
        entity
    ):

        class_name = entity.capitalize()

        return f"""

from app.repositories.{entity}_repository import {entity}_repository


def create_{entity}(
    db,
    data
):

    return {entity}_repository.create(
        db,
        data
    )



def get_{entity}s(
    db
):

    return {entity}_repository.get_all(
        db
    )

"""



    def generate_repository(
        self,
        entity
    ):

        return f"""

def create(
    db,
    data
):

    db.add(data)
    db.commit()
    db.refresh(data)

    return data



def get_all(
    db
):

    return db.query(
        data
    ).all()

"""



    def generate_route(
        self,
        entity
    ):

        return f"""

from fastapi import APIRouter, Depends

from app.services.{entity}_service import (
    create_{entity},
    get_{entity}s
)


router = APIRouter()



@router.post("/{entity}s")
def create_endpoint(
    data
):

    return create_{entity}(
        data
    )



@router.get("/{entity}s")
def list_endpoint():

    return get_{entity}s()

"""