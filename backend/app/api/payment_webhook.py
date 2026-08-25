"""
ASEO Payment Webhook API.
"""


from fastapi import (
    APIRouter,
    Depends
)


from sqlalchemy.orm import Session


from app.database.session import (
    get_database
)


from app.schemas.payment_webhook import (
    PaymentWebhookRequest
)


from app.services.payment_service import (
    PaymentService
)





router = APIRouter()


service = PaymentService()





# =====================================================
# Payment Provider Webhook
# =====================================================


@router.post(
    "/webhook",
    summary="Payment Provider Webhook"
)
def payment_webhook(

    data: PaymentWebhookRequest,

    db: Session = Depends(get_database)

):


    payment = service.handle_webhook(

        db,

        data.transaction_id,

        data.invoice_id,

        data.status,

        data.provider

    )


    return {

        "status": "received",

        "payment_id": payment.id,

        "payment_status": payment.status

    }