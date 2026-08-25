"""
ASEO Payments API.
"""


from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException
)


from sqlalchemy.orm import Session


from app.database.session import (
    get_database
)


from app.security.roles import (
    require_role
)


from app.schemas.payment import (
    PaymentCreate,
    PaymentResponse
)


from app.services.payment_service import (
    PaymentService
)


from app.repositories.invoice_repository import (
    InvoiceRepository
)





router = APIRouter()


service = PaymentService()

invoice_repository = InvoiceRepository()





# =====================================================
# Create Payment
# OWNER ONLY
# =====================================================


@router.post(
    "",
    response_model=PaymentResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Payment"
)
def create_payment(

    data: PaymentCreate,

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_role(
            ["OWNER"]
        )
    )

):


    invoice = invoice_repository.get_by_id(

        db,

        data.invoice_id

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



    return service.create_payment(

        db,

        current_user["organization_id"],

        data.invoice_id,

        data.amount,

        data.provider

    )





# =====================================================
# List Payments
# OWNER ONLY
# =====================================================


@router.get(
    "",
    response_model=list[PaymentResponse],
    summary="List Payments"
)
def list_payments(

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_role(
            ["OWNER"]
        )
    )

):


    return service.get_payments(

        db,

        current_user["organization_id"]

    )