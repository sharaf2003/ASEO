from enum import Enum


class ArtifactType(str, Enum):
    """
    Types of artifacts produced during software engineering workflows.
    """

    REQUIREMENTS = "requirements"
    ARCHITECTURE = "architecture"
    DATABASE_SCHEMA = "database_schema"
    API_SPECIFICATION = "api_specification"
    BACKEND_CODE = "backend_code"
    FRONTEND_CODE = "frontend_code"
    TEST_REPORT = "test_report"
    DEPLOYMENT_PACKAGE = "deployment_package"
    DOCUMENTATION = "documentation"