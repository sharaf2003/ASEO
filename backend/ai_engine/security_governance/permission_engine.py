class PermissionEngine:
    """
    ASEO Permission Engine v22.4
    """

    def check(
        self,
        role,
        action
    ):

        permissions = {

            "admin":
            [
                "read",
                "write",
                "deploy"
            ],

            "developer":
            [
                "read",
                "write"
            ],

            "viewer":
            [
                "read"
            ]

        }


        allowed = action in permissions.get(
            role,
            []
        )


        return {

            "role":
                role,

            "action":
                action,

            "allowed":
                allowed

        }