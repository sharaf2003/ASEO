import time

import pytest

from app.services.aseo_engine_service import (
    ASEOEngineService
)

from app.database.session import (
    get_database
)

from app.models.project import (
    Project
)


@pytest.mark.load
def test_aseo_load_execution():


    db = next(get_database())


    try:

        projects = (
            db.query(Project)
            .limit(5)
            .all()
        )


        assert len(projects) > 0



        engine = ASEOEngineService()



        results = []

        start = time.perf_counter()



        for project in projects:


            result = engine.execute_project(

                db,

                project.name,

                project.organization_id

            )


            results.append(result)



        end = time.perf_counter()



        total_time = end - start



        successful = sum(

            1

            for result in results

            if result["status"] == "SUCCESS"

        )



        report = {


            "projects_tested":

                len(projects),


            "successful":

                successful,


            "failed":

                len(projects) - successful,


            "total_time_seconds":

                round(total_time, 3),


            "average_time_seconds":

                round(

                    total_time / len(projects),

                    3

                )

        }



        print(
            "\nASEO LOAD TEST REPORT"
        )


        print(report)



        assert successful == len(projects)



    finally:

        db.close()