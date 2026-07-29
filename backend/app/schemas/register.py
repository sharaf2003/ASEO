from pydantic import BaseModel



class RegisterRequest(BaseModel):

    organization_name: str

    name: str

    email: str

    password: str





class RegisterResponse(BaseModel):

    message: str

    user_id: int

    organization_id: int

    workspace_id: int

    name: str

    email: str

    role: str