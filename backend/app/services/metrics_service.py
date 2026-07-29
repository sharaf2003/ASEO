from sqlalchemy.orm import Session

from fastapi import HTTPException, status


from app.repositories.metrics_repository import (
    MetricsRepository
)





class MetricsService:
    """
    ASEO Metrics Engine v23.0

    Calculates:

    - Project Health
    - Quality Score
    - Deployment Status
    - Operations Status
    - Execution Statistics
    """



    def __init__(self):

        self.repository = MetricsRepository()





    def calculate_metrics(

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





        latest = (

            executions[0]

            if executions

            else None

        )





        quality_score = 0

        deployment_score = 0

        health_score = 0





        if latest:


            if latest.software:

                quality_score = 95





            if latest.deployment:

                if latest.deployment.get(

                    "status"

                ) == "live":

                    deployment_score = 100





            if latest.operations:

                health = latest.operations.get(

                    "health",

                    {}

                )



                health_score = health.get(

                    "availability",

                    0

                )







        return {


            "project": {


                "id":

                    project.id,


                "name":

                    project.name,


                "status":

                    project.status

            },



            "metrics": {


                "executions":

                    len(executions),



                "quality_score":

                    quality_score,



                "deployment_score":

                    deployment_score,



                "health_score":

                    health_score

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