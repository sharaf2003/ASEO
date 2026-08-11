"""
ASEO Generated Module

Project service layer.
"""


from sqlalchemy.orm import Session

from fastapi import HTTPException


from app.models.project import Project

from app.models.project_member import ProjectMember


from app.repositories.project_repository import (
    ProjectRepository
)



repository = ProjectRepository()



# ==========================
# Create Project
# ==========================


def create_project(

    db: Session,

    project_data,

    user_id: int,

    organization_id: int,

    workspace_id: int

):


    project = Project(

        owner_id=user_id,

        organization_id=organization_id,

        workspace_id=workspace_id,

        name=project_data.name,

        description=project_data.description,

        status="created"

    )


    project = repository.create(

        db,

        project

    )


    member = ProjectMember(

        project_id=project.id,

        user_id=user_id,

        role="OWNER"

    )


    db.add(member)

    db.commit()

    db.refresh(project)


    return project





# ==========================
# Get Organization Projects
# ==========================


def get_projects(

    db: Session,

    organization_id: int

):


    return repository.get_all(

        db,

        organization_id

    )





# ==========================
# Get Single Project
# ==========================


def get_project(

    db: Session,

    project_id: int,

    organization_id: int

):


    project = repository.get_by_id(

        db,

        project_id,

        organization_id

    )


    if not project:

        raise HTTPException(

            status_code=404,

            detail="Project not found"

        )


    return project





# ==========================
# Get My Projects
# ==========================


def get_my_projects(

    db: Session,

    user_id: int

):


    return repository.get_my_projects(

        db,

        user_id

    )





# ==========================
# Update Project
# ==========================


def update_project(

    db: Session,

    project_id: int,

    user_id: int,

    organization_id: int,

    project_data

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


    if project.owner_id != user_id:

        raise HTTPException(

            status_code=403,

            detail="Only project owner can update project"

        )


    if project_data.name is not None:

        project.name = project_data.name



    if project_data.description is not None:

        project.description = project_data.description



    if project_data.status is not None:

        project.status = project_data.status



    return repository.update(

        db,

        project

    )





# ==========================
# Delete Project
# ==========================


def delete_project(

    db: Session,

    project_id: int,

    user_id: int,

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


    if project.owner_id != user_id:

        raise HTTPException(

            status_code=403,

            detail="Only project owner can delete project"

        )


    return repository.delete(

        db,

        project

    )