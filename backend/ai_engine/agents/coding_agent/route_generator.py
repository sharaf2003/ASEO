# Updated Route Generator v2

class RouteGenerator:
    """
    ASEO Route Generator v2

    Generates API-only routes.
    Business logic remains inside services.
    """

    def generate(
        self,
        entity
    ):

        return f"""
from fastapi import APIRouter, Depends

from app.services.{entity}_service import (
    get_{entity}s,
    create_{entity}
)


router = APIRouter(
    prefix="/{entity}s",
    tags=["{entity}s"]
)



@router.get("/")
def list_{entity}s():

    return get_{entity}s()



@router.post("/")
def create_{entity}_endpoint(
    data: dict
):

    return create_{entity}(
        data
    )
"""