from fastapi import APIRouter



router = APIRouter()



users = []





@router.post("/register")
def register(
    email: str,
    password: str
):


    user = {


        "email":

            email,


        "status":

            "created"

    }


    users.append(user)



    return user






@router.post("/login")
def login(
    email: str,
    password: str
):


    for user in users:


        if user["email"] == email:


            return {


                "authenticated":

                    True,


                "user":

                    user

            }



    return {


        "authenticated":

            False

    }