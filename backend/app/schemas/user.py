from datetime import datetime

from pydantic import BaseModel





# ==========================
# Create User Request
# ==========================


class UserCreate(BaseModel):

    name: str

    email: str

    password: str

    role: str = "MEMBER"





# ==========================
# User Response
# ==========================


class UserResponse(BaseModel):

    id: int

    name: str

    organization_id: int

    workspace_id: int

    email: str

    role: str

    created_at: datetime


    class Config:

        from_attributes = True