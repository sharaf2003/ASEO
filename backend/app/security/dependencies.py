from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.security.jwt import decode_access_token


# =====================================================
# OAuth2 Configuration
# =====================================================

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/auth/login"
)


# =====================================================
# Current User
# =====================================================

def get_current_user(
    token: str = Depends(oauth2_scheme),
):
    """
    Validate the access token and return its payload.
    """

    payload = decode_access_token(token)

    # -------------------------------------------------
    # Token validation
    # -------------------------------------------------

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
            headers={
                "WWW-Authenticate": "Bearer"
            },
        )

    # -------------------------------------------------
    # Token type validation
    # -------------------------------------------------

    if payload.get("type") != "access":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token type",
            headers={
                "WWW-Authenticate": "Bearer"
            },
        )

    # -------------------------------------------------
    # Valid token
    # -------------------------------------------------

    return payload