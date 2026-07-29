from pydantic import BaseModel





class LoginRequest(BaseModel):

    email: str

    password: str





class UserTokenData(BaseModel):

    id: int

    name: str

    email: str

    role: str

    organization_id: int

    workspace_id: int





class TokenResponse(BaseModel):

    access_token: str

    token_type: str = "bearer"

    user: UserTokenData