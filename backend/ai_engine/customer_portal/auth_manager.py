from .user import User



class AuthManager:
    """
    ASEO Authentication Manager v19.6
    """



    def __init__(
        self
    ):

        self.users = {}





    def register(
        self,
        email,
        password,
        role,
        customer_id
    ):


        user = User(

            email,

            password,

            role,

            customer_id

        )


        self.users[user.id] = user


        return user.to_dict()






    def login(
        self,
        email,
        password
    ):


        for user in self.users.values():


            if (

                user.email == email

                and

                user.password == password

            ):


                return {

                    "authenticated":
                        True,

                    "user":
                        user.to_dict()

                }



        return {

            "authenticated":
                False

        }