"""
ASEO Billing API

Handles SaaS billing operations.
"""


from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)


from sqlalchemy.orm import Session


from app.database.session import (
    get_database
)


from app.security.roles import (
    require_role
)


from app.services.billing_service import (
    BillingService
)


from app.schemas.invoice import (
    InvoiceResponse
)





router = APIRouter()


service = BillingService()





# =====================================================
# Get Organization Invoices
# OWNER ONLY
# =====================================================


@router.get(
    "/invoices",
    response_model=list[InvoiceResponse],
    summary="Get Organization Invoices"
)
def get_invoices(

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_role(
            ["OWNER"]
        )
    )

):


    return service.get_invoices(

        db,

        current_user["organization_id"]

    )





# =====================================================
# Pay Invoice
# OWNER ONLY
# =====================================================


@router.post(
    "/invoices/{invoice_id}/pay",
    response_model=InvoiceResponse,
    summary="Mark Invoice As Paid"
)
def pay_invoice(

    invoice_id: int,

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_role(
            ["OWNER"]
        )
    )

):


    invoice = service.repository.get_by_id(

        db,

        invoice_id

    )


    if not invoice:

        raise HTTPException(

            status_code=404,

            detail="Invoice not found"

        )



    if invoice.organization_id != current_user["organization_id"]:

        raise HTTPException(

            status_code=403,

            detail="Not allowed"

        )



    return service.mark_paid(

        db,

        invoice

    )