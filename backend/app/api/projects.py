"""
ASEO Generated Module

Project API with JWT Authentication,
Tenant Isolation and RBAC.
"""


from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException
)

from sqlalchemy.orm import Session


from app.database.session import get_database


from app.security.permissions import (
    require_permission
)


from app.schemas.project import (
    ProjectCreate,
    ProjectUpdate,
    ProjectResponse,
    ProjectExecute
)


from app.services.project_service import (
    create_project,
    get_projects,
    get_project,
    get_my_projects,
    update_project,
    delete_project
)


from app.services.aseo_engine_service import (
    ASEOEngineService
)



router = APIRouter()



# ==========================
# Create Project
# ==========================


@router.post(
    "",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED
)
def create_project_api(

    project: ProjectCreate,

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_permission(
            "project.create"
        )
    )

):


    return create_project(

        db,

        project,

        int(current_user["sub"]),

        current_user["organization_id"],

        current_user["workspace_id"]

    )





# ==========================
# Get My Projects
# ==========================


@router.get(
    "/my",
    response_model=list[ProjectResponse]
)
def get_my_projects_api(

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_permission(
            "project.view"
        )
    )

):


    return get_my_projects(

        db,

        int(current_user["sub"])

    )





# ==========================
# Get Organization Projects
# ==========================


@router.get(
    "",
    response_model=list[ProjectResponse]
)
def list_projects(

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_permission(
            "project.view"
        )
    )

):


    return get_projects(

        db,

        current_user["organization_id"]

    )





# ==========================
# Update Project
# ==========================


@router.put(
    "/{project_id}",
    response_model=ProjectResponse
)
def update_project_api(

    project_id: int,

    project_data: ProjectUpdate,

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_permission(
            "project.update"
        )
    )

):


    return update_project(

        db,

        project_id,

        int(current_user["sub"]),

        current_user["organization_id"],

        project_data

    )





# ==========================
# Delete Project
# ==========================


@router.delete(
    "/{project_id}"
)
def delete_project_api(

    project_id: int,

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_permission(
            "project.delete"
        )
    )

):


    return delete_project(

        db,

        project_id,

        int(current_user["sub"]),

        current_user["organization_id"]

    )





# ==========================
# Execute ASEO Engine
# ==========================


@router.post(
    "/execute"
)
def execute_project_api(

    data: ProjectExecute,

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_permission(
            "project.execute"
        )
    )

):


    existing_project = get_project(

        db,

        data.project_id,

        current_user["organization_id"]

    )


    if not existing_project:

        raise HTTPException(

            status_code=404,

            detail="Project not found"

        )


    engine = ASEOEngineService()


    return engine.execute_project(

        db,

        existing_project.name

    )