"""
ASEO Generated Module

Project Members API.
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


from app.schemas.project_member import (
    ProjectMemberCreate,
    ProjectMemberUpdate,
    ProjectMemberResponse
)


from app.services.project_member_service import (
    add_member,
    get_members,
    remove_member,
    update_member_role
)


from app.models.project import Project



router = APIRouter()



# =====================================================
# Project Ownership Check
# =====================================================


def verify_project_access(
    db: Session,
    project_id: int,
    organization_id: int
):

    project = (

        db.query(Project)

        .filter(

            Project.id == project_id,

            Project.organization_id == organization_id

        )

        .first()

    )


    if not project:

        raise HTTPException(

            status_code=status.HTTP_404_NOT_FOUND,

            detail="Project not found"

        )


    return project



# =====================================================
# Add Member
# =====================================================


@router.post(
    "/projects/{project_id}/members",
    response_model=ProjectMemberResponse,
    status_code=status.HTTP_201_CREATED
)
def add_project_member(

    project_id: int,

    data: ProjectMemberCreate,

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_permission(
            "member.add"
        )
    )

):


    organization_id = current_user["organization_id"]


    verify_project_access(
        db,
        project_id,
        organization_id
    )


    return add_member(

        db,

        project_id,

        data.user_id,

        data.role.value,

        organization_id

    )



# =====================================================
# Get Members
# =====================================================


@router.get(
    "/projects/{project_id}/members",
    response_model=list[ProjectMemberResponse]
)
def list_project_members(

    project_id: int,

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_permission(
            "member.view"
        )
    )

):


    organization_id = current_user["organization_id"]


    verify_project_access(
        db,
        project_id,
        organization_id
    )


    return get_members(

        db,

        project_id,

        organization_id

    )



# =====================================================
# Update Member Role
# =====================================================


@router.put(
    "/projects/{project_id}/members/{user_id}",
    response_model=ProjectMemberResponse
)
def update_project_member_role(

    project_id: int,

    user_id: int,

    data: ProjectMemberUpdate,

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_permission(
            "member.update"
        )
    )

):


    organization_id = current_user["organization_id"]


    verify_project_access(
        db,
        project_id,
        organization_id
    )


    return update_member_role(

        db,

        project_id,

        user_id,

        data.role.value,

        int(current_user["sub"]),

        organization_id

    )



# =====================================================
# Remove Member
# =====================================================


@router.delete(
    "/projects/{project_id}/members/{user_id}"
)
def remove_project_member(

    project_id: int,

    user_id: int,

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_permission(
            "member.remove"
        )
    )

):


    organization_id = current_user["organization_id"]


    verify_project_access(
        db,
        project_id,
        organization_id
    )


    return remove_member(

        db,

        project_id,

        user_id,

        int(current_user["sub"]),

        organization_id

    )