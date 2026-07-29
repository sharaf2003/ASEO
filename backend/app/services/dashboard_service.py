from sqlalchemy.orm import Session

from fastapi import HTTPException, status


from app.repositories.dashboard_repository import (
    DashboardRepository
)





class DashboardService:
    """
    Service layer for project dashboard.

    Handles tenant-isolated dashboard data.
    """



    def __init__(self):

        self.repository = DashboardRepository()





    def get_dashboard(

        self,

        db: Session,

        project_id: int,

        organization_id: int

    ):


        project = self.repository.get_project(

            db,

            project_id,

            organization_id

        )



        if not project:

            raise HTTPException(

                status_code=status.HTTP_404_NOT_FOUND,

                detail="Project not found"

            )





        executions = self.repository.get_executions(

            db,

            project_id,

            organization_id

        )





        latest = executions[0] if executions else None





        return {


            "project": {


                "id":

                    project.id,


                "name":

                    project.name,


                "status":

                    project.status

            },



            "executions": {


                "total":

                    len(executions),



                "latest_status":

                    latest.status

                    if latest

                    else None

            },



            "deployment":

                latest.deployment

                if latest

                else None,



            "operations":

                latest.operations

                if latest

                else None

        }