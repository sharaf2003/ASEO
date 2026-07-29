from fastapi import Depends, HTTPException, status

from fastapi.security import OAuth2PasswordBearer

from app.security.jwt import decode_access_token





# ==========================
# OAuth2 Configuration
# ==========================


oauth2_scheme = OAuth2PasswordBearer(

    tokenUrl="/api/auth/login"

)





# ==========================
# Current User
# ==========================


def get_current_user(

    token: str = Depends(oauth2_scheme)

):


    payload = decode_access_token(

        token

    )



    if not payload:


        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Invalid authentication token",

            headers={

                "WWW-Authenticate": "Bearer"

            }

        )



    return payload