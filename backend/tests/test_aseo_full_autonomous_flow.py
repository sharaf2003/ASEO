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



@pytest.mark.integration
def test_aseo_full_autonomous_flow():


    db = next(get_database())


    try:

        project = (
            db.query(Project)
            .first()
        )


        assert project is not None, (
            "No project available for testing"
        )


        engine = ASEOEngineService()


        result = engine.execute_project(

            db,

            project.name,

            project.organization_id

        )


        # =========================
        # Main Validation
        # =========================


        assert result["status"] == "SUCCESS"


        assert result["project_id"] == project.id


        assert result["organization_id"] == (
            project.organization_id
        )


        # =========================
        # Lifecycle Validation
        # =========================


        assert result["lifecycle_status"] == (
            "operational"
        )


        # =========================
        # Agents Validation
        # =========================


        agents = result["agents"]


        assert agents["execution_status"] == (
            "success"
        )


        assert len(
            agents["agents_executed"]
        ) > 0


        # =========================
        # Deployment Validation
        # =========================


        deployment = (
            result["execution"]
            ["deployment"]
        )


        assert deployment["status"] == (
            "live"
        )


    finally:

        db.close()