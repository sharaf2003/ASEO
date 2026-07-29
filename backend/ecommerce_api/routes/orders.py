

from fastapi import APIRouter


router = APIRouter()


@router.get("/orders")
def get_orders():

    return {

        "module":
        "orders"

    }

