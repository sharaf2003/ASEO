from datetime import datetime

from pydantic import BaseModel

class WorkspaceCreate(BaseModel):

    name: str

class WorkspaceResponse(BaseModel):

    id: int

    organization_id: int

    name: str

    created_at: datetime


    class Config:

        from_attributes = True