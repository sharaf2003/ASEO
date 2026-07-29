class CustomerPortal:
    """
    ASEO Customer Portal v19.6
    """



    def dashboard(
        self,
        user,
        subscription,
        projects
    ):


        return {


            "user":

                user["email"],


            "role":

                user["role"],


            "plan":

                subscription["plan"],


            "projects":

                len(projects),


            "status":

                subscription["status"]

        }