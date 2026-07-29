"""
ASEO Generated Module

Project Member service layer.
"""


from fastapi import HTTPException, status

from sqlalchemy.orm import Session


from app.models.project_member import ProjectMember

from app.models.project import Project

from app.repositories.project_member_repository import (
    ProjectMemberRepository
)


repository = ProjectMemberRepository()


# ==========================
# Add Member To Project
# ==========================


def add_member(

    db: Session,

    project_id: int,

    user_id: int,

    role: str

):


    existing_member = repository.get_member(

        db,

        project_id,

        user_id

    )


    if existing_member:

        raise HTTPException(

            status_code=status.HTTP_400_BAD_REQUEST,

            detail="User is already a member of this project"

        )


    member = ProjectMember(

        project_id=project_id,

        user_id=user_id,

        role=role

    )


    return repository.create(

        db,

        member

    )





# ==========================
# Get Project Members
# ==========================


def get_members(

    db: Session,

    project_id: int

):


    return repository.get_project_members(

        db,

        project_id

    )





# ==========================
# Remove Member From Project
# ==========================


def remove_member(

    db: Session,

    project_id: int,

    user_id: int,

    current_user_id: int

):


    # Check if current user is project owner

    owner = (

        db.query(Project)

        .filter(

            Project.id == project_id,

            Project.owner_id == current_user_id

        )

        .first()

    )


    if not owner:

        raise HTTPException(

            status_code=status.HTTP_403_FORBIDDEN,

            detail="Only project owner can remove members"

        )



    member = repository.delete(

        db,

        project_id,

        user_id

    )


    if not member:

        raise HTTPException(

            status_code=status.HTTP_404_NOT_FOUND,

            detail="Member not found"

        )



    return {

        "message": "Member removed successfully"

    }