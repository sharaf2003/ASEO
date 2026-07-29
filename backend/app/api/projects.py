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



from app.security.dependencies import (
    get_current_user
)


from app.security.roles import (
    require_role
)



from app.database.session import get_database






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
    update_project
)


from app.services.aseo_engine_service import (
    ASEOEngineService
)





router = APIRouter()





# ==========================
# Create Project
# OWNER ONLY
# ==========================


@router.post(
    "",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Project",
    description="Create a new tenant project."
)
def create_project_api(

    project: ProjectCreate,

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_role(
            ["OWNER"]
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

@router.get("/my")
def get_my_projects_api(
    db: Session = Depends(get_database),
    current_user = Depends(get_current_user)
):

    return get_my_projects(
        db,
        int(current_user["sub"])
    )





# ==========================
# Get Tenant Projects
# OWNER + MEMBER
# ==========================


@router.get(
    "",
    response_model=list[ProjectResponse],
    summary="Get Organization Projects",
    description="Retrieve projects belonging to current organization."
)
def list_projects(

    db: Session = Depends(get_database),

    current_user: dict = Depends(get_current_user)

):


    return get_projects(

        db,

        current_user["organization_id"]

    )





# ==========================
# Execute ASEO Engine
# OWNER ONLY
# ==========================


@router.post(
    "/execute",
    summary="Run ASEO Autonomous Engine",
    description="""
    Execute complete ASEO autonomous pipeline:

    - Executive Analysis
    - Agent Selection
    - Collaboration
    - Software Factory
    - Deployment
    - Operations Monitoring

    Execution result is stored in database.
    """
)

@router.put("/{project_id}")
def update_project_api(

    project_id: int,

    project_data: ProjectUpdate,

    db: Session = Depends(get_database),

    current_user = Depends(get_current_user)

):

    return update_project(

        db,

        project_id,

        int(current_user["sub"]),

        project_data

    )

def execute_project_api(

    data: ProjectExecute,

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_role(
            ["OWNER"]
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

            status_code=status.HTTP_404_NOT_FOUND,

            detail="Project not found"

        )





    engine = ASEOEngineService()



    return engine.execute_project(

        db,

        existing_project.name

    )