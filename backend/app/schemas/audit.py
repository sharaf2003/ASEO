"""
ASEO Audit Schemas.
"""


from datetime import datetime


from pydantic import BaseModel





# =====================================
# Audit Log Response
# =====================================


class AuditLogResponse(BaseModel):

    id: int

    organization_id: int | None

    user_id: int | None

    action: str

    description: str | None

    created_at: datetime



    class Config:

        from_attributes = True





# =====================================
# Audit Dashboard Response
# =====================================


class AuditDashboardResponse(BaseModel):

    total_events: int

    logs: list[AuditLogResponse]