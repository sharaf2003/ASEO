import time

import pytest

from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed
)

from app.services.aseo_engine_service import (
    ASEOEngineService
)

from app.database.session import (
    get_database
)

from app.models.project import (
    Project
)

from app.models.workspace import (
    Workspace
)

from app.models.user import (
    User
)

from app.models.organization import (
    Organization
)

from app.models.execution_record import ExecutionRecord

from app.models.artifact import Artifact



def run_project(project):

    db = next(get_database())

    try:

        engine = ASEOEngineService()


        result = engine.execute_project(

            db,

            project["name"],

            project["organization_id"]

        )


        return {

            "project_id":
                project["id"],

            "status":
                result["status"],

            "lifecycle":
                result["lifecycle_status"]

        }


    finally:

        db.close()





@pytest.mark.parallel
def test_aseo_parallel_execution():


    db = next(get_database())


    project_data = []


    try:


        organization = (
            db.query(Organization)
            .first()
        )


        workspace = (
            db.query(Workspace)
            .first()
        )


        user = (
            db.query(User)
            .first()
        )


        assert organization
        assert workspace
        assert user



        for index in range(20):


            project = Project(

                organization_id=
                    organization.id,

                workspace_id=
                    workspace.id,

                owner_id=
                    user.id,

                name=
                    f"ASEO Parallel Test {index}",

                description=
                    "Parallel execution test",

                status=
                    "created"

            )


            db.add(project)

            db.commit()

            db.refresh(project)



            project_data.append({

                "id":
                    project.id,

                "name":
                    project.name,

                "organization_id":
                    project.organization_id

            })


    finally:

        db.close()



    start = time.perf_counter()


    results = []


    try:


        with ThreadPoolExecutor(
            max_workers=20
        ) as executor:


            futures = [

                executor.submit(
                    run_project,
                    project
                )

                for project in project_data

            ]


            for future in as_completed(futures):

                results.append(
                    future.result()
                )



        end = time.perf_counter()


        successful = sum(

            1

            for result in results

            if result["status"] == "SUCCESS"

        )



        report = {

            "projects":
                len(project_data),

            "successful":
                successful,

            "failed":
                len(project_data)
                - successful,

            "parallel_time_seconds":
                round(
                    end-start,
                    3
                )

        }


        print(
            "\nASEO PARALLEL EXECUTION REPORT"
        )

        print(report)


        assert successful == len(project_data)
        

    finally:

        db = next(get_database())

        try:

            for project in project_data:


                execution_ids = [

                    row.id

                    for row in (
                        db.query(ExecutionRecord.id)
                        .filter(
                            ExecutionRecord.project_id ==
                            project["id"]
                        )
                        .all()
                    )

                ]


                if execution_ids:


                    # Delete artifacts first

                    db.query(Artifact)\
                        .filter(
                            Artifact.execution_id.in_(
                                execution_ids
                            )
                        )\
                        .delete(
                            synchronize_session=False
                        )


                    # Delete executions

                    db.query(ExecutionRecord)\
                        .filter(
                            ExecutionRecord.id.in_(
                                execution_ids
                            )
                        )\
                        .delete(
                            synchronize_session=False
                        )


                # Delete project

                db.query(Project)\
                    .filter(
                        Project.id ==
                        project["id"]
                    )\
                    .delete(
                        synchronize_session=False
                    )


            db.commit()


        finally:

            db.close()