from fastapi import Depends, HTTPException, status

from app.security.dependencies import (
    get_current_user
)


# =====================================================
# Role Checker
# =====================================================

def require_role(
    allowed_roles: list[str]
):

    # Normalize allowed roles once
    normalized_roles = [
        role.upper()
        for role in allowed_roles
    ]


    def role_checker(

        current_user: dict = Depends(get_current_user)

    ):

        user_role = current_user.get(
            "role"
        )


        if not user_role:

            raise HTTPException(

                status_code=status.HTTP_403_FORBIDDEN,

                detail="Role not found"

            )


        # Normalize current user role

        user_role = str(
            user_role
        ).upper()



        if user_role not in normalized_roles:


            raise HTTPException(

                status_code=status.HTTP_403_FORBIDDEN,

                detail="Insufficient permissions"

            )


        return current_user



    return role_checker