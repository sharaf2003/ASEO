"""
ASEO Invoice Schemas.
"""

from datetime import datetime

from pydantic import BaseModel





# =====================================
# Invoice Response
# =====================================


class InvoiceResponse(BaseModel):

    id: int

    organization_id: int

    invoice_number: str

    plan: str

    amount: float

    currency: str

    status: str

    created_at: datetime



    class Config:

        from_attributes = True