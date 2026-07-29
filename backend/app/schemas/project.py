from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProjectCreate(BaseModel):
    """
    Schema used to create a new project.
    """

    name: str

    description: str | None = None



class ProjectUpdate(BaseModel):
    """
    Schema used to update a project.
    """

    name: str | None = None

    description: str | None = None

    status: str | None = None



class ProjectExecute(BaseModel):
    """
    Schema used to execute a project.
    """

    project_id: int



class ProjectResponse(BaseModel):
    """
    Schema returned from API.
    """

    id: int

    name: str

    description: str | None = None

    status: str

    created_at: datetime

    updated_at: datetime


    model_config = ConfigDict(
        from_attributes=True
    )