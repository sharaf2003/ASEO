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


@pytest.mark.performance
def test_aseo_performance_benchmark():


    db = next(get_database())


    try:

        project = (
            db.query(Project)
            .first()
        )


        assert project is not None


        engine = ASEOEngineService()



        start_time = time.perf_counter()



        result = engine.execute_project(

            db,

            project.name,

            project.organization_id

        )



        end_time = time.perf_counter()



        execution_time = (
            end_time - start_time
        )



        agents_count = len(

            result["agents"]
            .get(
                "agents_executed",
                []
            )

        )



        report = {

            "execution_time_seconds":
                round(
                    execution_time,
                    3
                ),

            "agents_executed":
                agents_count,

            "status":
                result["status"],

            "lifecycle":
                result["lifecycle_status"]

        }



        print(
            "\nASEO PERFORMANCE REPORT"
        )


        print(report)



        assert result["status"] == "SUCCESS"


        assert execution_time < 60



    finally:

        db.close()