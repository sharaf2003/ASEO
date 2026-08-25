"""
ASEO Audit Dashboard API.
"""


from fastapi import (
    APIRouter,
    Depends
)


from sqlalchemy.orm import Session


from app.database.session import (
    get_database
)


from app.security.roles import (
    require_role
)


from app.services.audit_service import (
    AuditService
)


from app.schemas.audit import (
    AuditDashboardResponse,
    AuditLogResponse
)





router = APIRouter()


service = AuditService()





# =====================================
# Organization Audit Logs
# OWNER ONLY
# =====================================


@router.get(

    "/organization",

    response_model=AuditDashboardResponse,

    summary="Get Organization Audit Logs"

)
def get_organization_audit(

    db: Session = Depends(get_database),

    current_user: dict = Depends(

        require_role(

            ["OWNER"]

        )

    )

):


    logs = service.get_organization_logs(

        db,

        current_user["organization_id"]

    )


    return {

        "total_events": len(logs),

        "logs": logs

    }






# =====================================
# User Audit Logs
# OWNER ONLY
# =====================================


@router.get(

    "/user/{user_id}",

    response_model=list[AuditLogResponse],

    summary="Get User Audit Logs"

)
def get_user_audit(

    user_id: int,

    db: Session = Depends(get_database),

    current_user: dict = Depends(

        require_role(

            ["OWNER"]

        )

    )

):


    return service.get_user_logs(

        db,

        user_id

    )