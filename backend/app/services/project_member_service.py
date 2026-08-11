"""
ASEO Generated Module

Project Member service layer.
"""

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.project_member import ProjectMember
from app.models.project import Project
from app.models.user import User

from app.repositories.project_member_repository import (
    ProjectMemberRepository
)


repository = ProjectMemberRepository()


# =====================================================
# Allowed Project Member Roles
# =====================================================

ALLOWED_MEMBER_ROLES = [
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


def get_user(
    db: Session,
    user_id: int,
    organization_id: int,
):

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
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user


def validate_member_role(
    role: str,
):

    if not role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Project member role is required",
        )

    role = str(role).strip().upper()

    if role not in ALLOWED_MEMBER_ROLES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "Invalid project member role. "
                "Allowed roles: MEMBER, DEVELOPER"
            ),
        )

    return role


# =====================================================
# Add Member
# =====================================================


def add_member(
    db: Session,
    project_id: int,
    user_id: int,
    role: str,
    organization_id: int,
):

    project = get_project(
        db,
        project_id,
        organization_id,
    )

    user = get_user(
        db,
        user_id,
        organization_id,
    )

    role = validate_member_role(
        role
    )

    # Prevent adding project owner as member
    if project.owner_id == user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Project owner cannot be added as member",
        )

    existing_member = repository.get_member(
        db,
        project_id,
        user_id,
    )

    if existing_member:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User is already a member of this project",
        )

    member = ProjectMember(
        project_id=project_id,
        user_id=user_id,
        role=role,
    )

    return repository.create(
        db,
        member,
    )


# =====================================================
# Get Members
# =====================================================


def get_members(
    db: Session,
    project_id: int,
    organization_id: int,
):

    get_project(
        db,
        project_id,
        organization_id,
    )

    return repository.get_project_members(
        db,
        project_id,
    )


# =====================================================
# Update Member Role
# =====================================================


def update_member_role(
    db: Session,
    project_id: int,
    user_id: int,
    role: str,
    current_user_id: int,
    organization_id: int,
):

    project = get_project(
        db,
        project_id,
        organization_id,
    )

    # Only project owner can change roles
    if project.owner_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only project owner can update member role",
        )

    role = validate_member_role(
        role
    )

    # Owner role cannot be changed
    if project.owner_id == user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot change project owner role",
        )

    # Make sure the target user belongs
    # to the same organization.
    get_user(
        db,
        user_id,
        organization_id,
    )

    member = repository.get_member(
        db,
        project_id,
        user_id,
    )

    if not member:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Member not found",
        )

    member.role = role

    try:

        db.commit()
        db.refresh(member)

        return member

    except Exception:

        db.rollback()
        raise


# =====================================================
# Remove Member
# =====================================================


def remove_member(
    db: Session,
    project_id: int,
    user_id: int,
    current_user_id: int,
    organization_id: int,
):

    project = get_project(
        db,
        project_id,
        organization_id,
    )

    # Only project owner can remove members
    if project.owner_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only project owner can remove members",
        )

    # Prevent deleting project owner
    if project.owner_id == user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot remove project owner",
        )

    # Make sure target user belongs
    # to the same organization.
    get_user(
        db,
        user_id,
        organization_id,
    )

    member = repository.remove(
        db,
        project_id,
        user_id,
    )

    if not member:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Member not found",
        )

    return {
        "message": "Member removed successfully"
    }