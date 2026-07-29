from ai_engine.database import (
    SessionLocal,
    CustomerModel
)

from uuid import uuid4



class UserService:
    """
    ASEO User Service v19.9
    """



    def create_customer(
        self,
        name,
        plan
    ):

        db = SessionLocal()


        customer = CustomerModel(

            id=str(uuid4()),

            name=name,

            plan=plan

        )


        db.add(customer)

        db.commit()

        db.refresh(customer)

        db.close()


        return {

            "id":
                customer.id,

            "name":
                customer.name,

            "plan":
                customer.plan

        }