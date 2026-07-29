class RoleManager:
    """
    ASEO Role Manager v22.4
    """

    def create_role(
        self,
        user,
        role
    ):

        return {

            "user":
                user,

            "role":
                role,

            "status":
                "assigned"

        }