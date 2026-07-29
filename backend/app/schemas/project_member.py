"""
ASEO Generated Module

Project Member schemas.
"""


from datetime import datetime


from pydantic import BaseModel





# ==========================
# Create Project Member
# ==========================


class ProjectMemberCreate(BaseModel):

    user_id: int

    role: str = "VIEWER"







# ==========================
# Project Member Response
# ==========================


class ProjectMemberResponse(BaseModel):

    id: int

    project_id: int

    user_id: int

    role: str

    created_at: datetime



    class Config:

        from_attributes = True