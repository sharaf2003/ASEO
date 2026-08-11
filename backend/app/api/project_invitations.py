"""
ASEO Generated Module

Project Invitations API.
"""


from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException
)

from sqlalchemy.orm import Session


from app.database.session import get_database

from app.security.dependencies import get_current_user

from app.security.permissions import require_permission


from app.schemas.project_invitation import (
    ProjectInvitationCreate,
    ProjectInvitationResponse
)


from app.services.project_invitation_service import (
    create_invitation,
    get_project_invitations,
    accept_invitation,
    reject_invitation
)


from app.models.project import Project



router = APIRouter()



# =====================================================
# Project Access Check
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

            status_code=404,

            detail="Project not found"

        )


    return project



# =====================================================
# Create Invitation
# =====================================================


@router.post(
    "/projects/{project_id}/invitations",
    response_model=ProjectInvitationResponse,
    status_code=status.HTTP_201_CREATED
)
def create_project_invitation(

    project_id: int,

    data: ProjectInvitationCreate,

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_permission(
            "invitation.create"
        )
    )

):


    organization_id = current_user["organization_id"]


    verify_project_access(

        db,

        project_id,

        organization_id

    )


    return create_invitation(

        db,

        project_id,

        data.email,

        data.role.value,

        int(current_user["sub"]),

        organization_id

    )



# =====================================================
# Get Invitations
# =====================================================


@router.get(
    "/projects/{project_id}/invitations",
    response_model=list[ProjectInvitationResponse]
)
def list_project_invitations(

    project_id: int,

    db: Session = Depends(get_database),

    current_user: dict = Depends(
        require_permission(
            "invitation.view"
        )
    )

):


    organization_id = current_user["organization_id"]


    verify_project_access(

        db,

        project_id,

        organization_id

    )


    return get_project_invitations(

        db,

        project_id,

        organization_id

    )



# =====================================================
# Accept Invitation
# =====================================================


@router.post(
    "/invitations/{invitation_id}/accept",
    response_model=ProjectInvitationResponse
)
def accept_project_invitation(

    invitation_id: int,

    db: Session = Depends(get_database),

    current_user: dict = Depends(get_current_user)

):


    return accept_invitation(

        db,

        invitation_id,

        int(current_user["sub"]),

        current_user["organization_id"]

    )



# =====================================================
# Reject Invitation
# =====================================================


@router.post(
    "/invitations/{invitation_id}/reject",
    response_model=ProjectInvitationResponse
)
def reject_project_invitation(

    invitation_id: int,

    db: Session = Depends(get_database),

    current_user: dict = Depends(get_current_user)

):


    return reject_invitation(

        db,

        invitation_id,

        int(current_user["sub"]),

        current_user["organization_id"]

    )