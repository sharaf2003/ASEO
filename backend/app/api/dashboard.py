from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session


from app.security.dependencies import (
    get_current_user
)


from app.database.session import get_database


from app.services.dashboard_service import (
    DashboardService
)





router = APIRouter()


service = DashboardService()





@router.get(
    "/projects/{project_id}/dashboard",
    summary="Project Dashboard"
)
def project_dashboard(

    project_id: int,

    db: Session = Depends(get_database),

    current_user: dict = Depends(get_current_user)

):


    return service.get_dashboard(

        db,

        project_id,

        current_user["organization_id"]

    )