

from fastapi import APIRouter


router = APIRouter()


@router.get("/authentication")
def get_authentication():

    return {

        "module":
        "authentication"

    }

