from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_database
from app.security.dependencies import get_current_user

from app.models.permission import Permission
from app.models.role_permission import RolePermission


# =====================================================
# Permission Checker
# =====================================================


def require_permission(permission_name: str):

    if not permission_name:
        raise ValueError(
            "Permission name is required"
        )


    permission_name = permission_name.lower()



    def checker(

        current_user: dict = Depends(get_current_user),

        db: Session = Depends(get_database)

    ):


        # ---------------------------------------------
        # Get user role
        # ---------------------------------------------

        role = current_user.get(
            "role"
        )


        if not role:

            raise HTTPException(

                status_code=status.HTTP_403_FORBIDDEN,

                detail="Role not found"

            )


        role = str(
            role
        ).strip().upper()



        # ---------------------------------------------
        # Check Permission
        # ---------------------------------------------

        permission = (

            db.query(Permission)

            .join(
                RolePermission,
                Permission.id == RolePermission.permission_id
            )

            .filter(

                RolePermission.role == role,

                Permission.name == permission_name

            )

            .first()

        )



        if not permission:

            raise HTTPException(

                status_code=status.HTTP_403_FORBIDDEN,

                detail=f"You do not have permission: {permission_name}"

            )



        return current_user



    return checker