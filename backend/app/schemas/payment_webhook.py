"""
ASEO Payment Webhook Schemas.
"""


from pydantic import BaseModel





class PaymentWebhookRequest(BaseModel):

    transaction_id: str

    invoice_id: int

    status: str

    provider: str = "manual"