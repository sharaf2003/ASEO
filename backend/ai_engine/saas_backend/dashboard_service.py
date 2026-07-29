from ai_engine.database import (
    SessionLocal,
    CustomerModel,
    ProjectModel
)



class DashboardService:
    """
    ASEO Dashboard Service v19.9
    """



    def customer_dashboard(
        self,
        customer_id
    ):

        db = SessionLocal()


        customers = db.query(

            CustomerModel

        ).all()


        projects = db.query(

            ProjectModel

        ).all()


        db.close()


        return {


            "customers":

                len(customers),


            "projects":

                len(projects),


            "status":

                "active"

        }