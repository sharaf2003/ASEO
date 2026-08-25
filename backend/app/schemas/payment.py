"""
ASEO Payment Schemas.
"""


from datetime import datetime


from pydantic import BaseModel





# =====================================
# Create Payment Request
# =====================================


class PaymentCreate(BaseModel):

    invoice_id: int

    amount: float

    provider: str = "manual"





# =====================================
# Payment Response
# =====================================


class PaymentResponse(BaseModel):

    id: int

    invoice_id: int

    transaction_id: str

    amount: float

    currency: str

    provider: str

    status: str

    created_at: datetime



    class Config:

        from_attributes = True