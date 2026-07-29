from datetime import datetime

from pydantic import BaseModel



class OrganizationCreate(BaseModel):

    name: str

    plan: str = "free"




class OrganizationResponse(BaseModel):

    id: int

    name: str

    plan: str

    created_at: datetime


    class Config:

        from_attributes = True