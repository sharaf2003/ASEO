"""
ASEO Generated Module

Project Invitation service layer.
"""

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.project_invitation import ProjectInvitation
from app.models.project import Project
from app.models.user import User
from app.models.project_member import ProjectMember

from app.repositories.project_invitation_repository import (
    ProjectInvitationRepository
)


repository = ProjectInvitationRepository()


# =====================================================
# Allowed Invitation Roles
# =====================================================

ALLOWED_INVITATION_ROLES = [
    "MEMBER",
    "DEVELOPER",
]


# =====================================================
# Helpers
# =====================================================


def get_project(
    db: Session,
    project_id: int,
    organization_id: int,
):

    project = (
        db.query(Project)
        .filter(
            Project.id == project_id,
            Project.organization_id == organization_id,
        )
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found",
        )

    return project


def validate_role(
    role: str,
):

    if not role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invitation role is required",
        )

    role = str(role).strip().upper()

    if role not in ALLOWED_INVITATION_ROLES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "Invalid invitation role. "
                "Allowed roles: MEMBER, DEVELOPER"
            ),
        )

    return role


# =====================================================
# Create Invitation
# =====================================================


def create_invitation(
    db: Session,
    project_id: int,
    email: str,
    role: str,
    current_user_id: int,
    organization_id: int,
):

    project = get_project(
        db,
        project_id,
        organization_id,
    )

    # Only project owner can invite members
    if project.owner_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only project owner can invite members",
        )

    role = validate_role(
        role
    )

    email = email.lower().strip()

    # -------------------------------------------------
    # Check invited user
    # -------------------------------------------------

    user = (
        db.query(User)
        .filter(
            User.email == email,
            User.organization_id == organization_id,
        )
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found in this organization",
        )

    # Owner cannot be invited
    if project.owner_id == user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Project owner cannot be invited",
        )

    # -------------------------------------------------
    # Check existing membership
    # -------------------------------------------------

    existing_member = (
        db.query(ProjectMember)
        .filter(
            ProjectMember.project_id == project_id,
            ProjectMember.user_id == user.id,
        )
        .first()
    )

    if existing_member:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User is already a member of this project",
        )

    # -------------------------------------------------
    # Check pending invitation
    # -------------------------------------------------

    existing = repository.get_pending_by_email(
        db,
        project_id,
        email,
    )

    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invitation already exists",
        )

    invitation = ProjectInvitation(
        project_id=project_id,
        email=email,
        role=role,
        status="PENDING",
    )

    return repository.create(
        db,
        invitation,
    )


# =====================================================
# Get Project Invitations
# =====================================================


def get_project_invitations(
    db: Session,
    project_id: int,
    organization_id: int,
):

    get_project(
        db,
        project_id,
        organization_id,
    )

    return repository.get_project_invitations(
        db,
        project_id,
    )


# =====================================================
# Accept Invitation
# =====================================================


def accept_invitation(
    db: Session,
    invitation_id: int,
    user_id: int,
    organization_id: int,
):

    invitation = repository.get_by_id(
        db,
        invitation_id,
    )

    if not invitation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invitation not found",
        )

    if invitation.status != "PENDING":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invitation is not active",
        )

    # -------------------------------------------------
    # Verify project belongs to organization
    # -------------------------------------------------

    project = get_project(
        db,
        invitation.project_id,
        organization_id,
    )

    # -------------------------------------------------
    # Verify invitation belongs to current user
    # -------------------------------------------------

    user = (
        db.query(User)
        .filter(
            User.id == user_id,
            User.organization_id == organization_id,
        )
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User does not belong to this organization",
        )

    if user.email.lower().strip() != invitation.email.lower().strip():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This invitation does not belong to this user",
        )

    # Project owner should never accept member invitation
    if project.owner_id == user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Project owner cannot accept member invitation",
        )

    # -------------------------------------------------
    # Prevent duplicate membership
    # -------------------------------------------------

    existing_member = (
        db.query(ProjectMember)
        .filter(
            ProjectMember.project_id == invitation.project_id,
            ProjectMember.user_id == user.id,
        )
        .first()
    )

    if existing_member:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User is already a member of this project",
        )

    member = ProjectMember(
        project_id=invitation.project_id,
        user_id=user.id,
        role=invitation.role,
        status="ACTIVE",
    )

    try:

        db.add(member)

        invitation.status = "ACCEPTED"

        db.commit()

        db.refresh(invitation)

        return invitation

    except Exception:

        db.rollback()

        raise


# =====================================================
# Reject Invitation
# =====================================================


def reject_invitation(
    db: Session,
    invitation_id: int,
    user_id: int,
    organization_id: int,
):

    invitation = repository.get_by_id(
        db,
        invitation_id,
    )

    if not invitation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invitation not found",
        )

    if invitation.status != "PENDING":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invitation is not active",
        )

    # -------------------------------------------------
    # Verify project belongs to organization
    # -------------------------------------------------

    get_project(
        db,
        invitation.project_id,
        organization_id,
    )

    # -------------------------------------------------
    # Verify invitation belongs to current user
    # -------------------------------------------------

    user = (
        db.query(User)
        .filter(
            User.id == user_id,
            User.organization_id == organization_id,
        )
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User does not belong to this organization",
        )

    if user.email.lower().strip() != invitation.email.lower().strip():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This invitation does not belong to this user",
        )

    try:

        invitation.status = "REJECTED"

        db.commit()

        db.refresh(invitation)

        return invitation

    except Exception:

        db.rollback()

        raise