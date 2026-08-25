"""
ASEO Billing Dashboard Schemas.
"""


from datetime import datetime

from pydantic import BaseModel





# =====================================
# Subscription Summary
# =====================================


class SubscriptionSummary(BaseModel):

    id: int

    plan: str

    status: str

    created_at: datetime



    class Config:

        from_attributes = True





# =====================================
# Usage Summary
# =====================================


class UsageSummary(BaseModel):

    month: str

    total_requests: int

    included_requests: int

    extra_requests: int

    cost: float



    class Config:

        from_attributes = True





# =====================================
# Invoice Summary
# =====================================


class InvoiceSummary(BaseModel):

    id: int

    invoice_number: str

    plan: str

    amount: float

    currency: str

    status: str

    created_at: datetime



    class Config:

        from_attributes = True





# =====================================
# Billing Dashboard Response
# =====================================


class BillingDashboardResponse(BaseModel):

    subscription: SubscriptionSummary

    limits: dict

    usage: UsageSummary

    invoices: list[InvoiceSummary]