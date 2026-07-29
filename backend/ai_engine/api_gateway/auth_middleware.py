class AuthMiddleware:
    """
    ASEO Authentication Middleware v22.6
    """

    def authenticate(
        self,
        api_key
    ):

        if api_key:

            return {

                "authenticated":
                    True,

                "api_key":
                    api_key

            }


        return {

            "authenticated":
                False

        }