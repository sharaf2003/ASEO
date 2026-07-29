"""
ASEO Generated Module

Project Members API.
"""


from fastapi import (
    APIRouter,
    Depends,
    status
)

from sqlalchemy.orm import Session


from app.database.session import get_database

from app.database.session import get_database

from app.security.dependencies import (
    get_current_user
)


from app.schemas.project_member import (
    ProjectMemberCreate,
    ProjectMemberResponse
)


from app.services.project_member_service import (
    add_member,
    get_members,
    remove_member
)




router = APIRouter()





# ==========================
# Add Member
# ==========================


@router.post(
    "/projects/{project_id}/members",
    response_model=ProjectMemberResponse,
    status_code=status.HTTP_201_CREATED
)
def add_project_member(

    project_id: int,

    data: ProjectMemberCreate,

    db: Session = Depends(get_database),

    current_user: dict = Depends(get_current_user)

):


    return add_member(

        db,

        project_id,

        data.user_id,

        data.role

    )







# ==========================
# Get Members
# ==========================


@router.get(
    "/projects/{project_id}/members",
    response_model=list[ProjectMemberResponse]
)
def list_project_members(

    project_id: int,

    db: Session = Depends(get_database),

    current_user: dict = Depends(get_current_user)

):


    return get_members(

        db,

        project_id

    )

@router.delete(
    "/projects/{project_id}/members/{user_id}"
)
def remove_project_member(
    project_id: int,
    user_id: int,
    db: Session = Depends(get_database),
    current_user = Depends(get_current_user)
):

    return remove_member(
        db,
        project_id,
        user_id,
        current_user["sub"]
    )