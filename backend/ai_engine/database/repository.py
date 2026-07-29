from .models import (
    CustomerModel,
    ProjectModel
)



class DatabaseRepository:
    """
    ASEO Database Repository v19.8
    """



    def create_customer(
        self,
        db,
        customer
    ):


        db.add(customer)

        db.commit()

        db.refresh(customer)


        return customer






    def create_project(
        self,
        db,
        project
    ):


        db.add(project)

        db.commit()

        db.refresh(project)


        return project
    