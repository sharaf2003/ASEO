"""
ASEO Generated Module

Project Invitation schemas.
"""


from datetime import datetime

from enum import Enum

from pydantic import BaseModel





# ==========================
# Invitation Roles
# ==========================


class ProjectInvitationRole(str, Enum):

    MEMBER = "MEMBER"

    DEVELOPER = "DEVELOPER"





# ==========================
# Invitation Status
# ==========================


class ProjectInvitationStatus(str, Enum):

    PENDING = "PENDING"

    ACCEPTED = "ACCEPTED"

    REJECTED = "REJECTED"

    EXPIRED = "EXPIRED"





# ==========================
# Create Invitation Request
# ==========================


class ProjectInvitationCreate(BaseModel):

    email: str

    role: ProjectInvitationRole = (
        ProjectInvitationRole.MEMBER
    )





# ==========================
# Response
# ==========================


class ProjectInvitationResponse(BaseModel):

    id: int

    project_id: int

    email: str

    role: str

    status: str

    created_at: datetime

    expires_at: datetime | None



    class Config:

        from_attributes = True