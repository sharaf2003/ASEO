"""
ASEO Billing Dashboard API.
"""


from fastapi import (
    APIRouter,
    Depends,
    Query
)


from sqlalchemy.orm import Session


from app.database.session import (
    get_database
)


from app.security.roles import (
    require_role
)


from app.services.billing_dashboard_service import (
    BillingDashboardService
)


from app.schemas.billing_dashboard import (
    BillingDashboardResponse
)





router = APIRouter()


service = BillingDashboardService()





# =====================================================
# Customer Billing Dashboard
# OWNER ONLY
# =====================================================


@router.get(
    "/dashboard",
    response_model=BillingDashboardResponse,
    summary="Get Billing Dashboard"
)
def get_billing_dashboard(

    month: str = Query(

        ...,

        description="Billing month format YYYY-MM"

    ),

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_role(
            ["OWNER"]
        )
    )

):


    return service.get_dashboard(

        db,

        current_user["organization_id"],

        month

    )