from enum import Enum



class AgentCapability(str, Enum):

    """
    Defines capabilities supported by ASEO agents.

    These capabilities will later be used for:

    - Agent selection
    - Task routing
    - AI model selection
    """



    # =============================================
    # Planning
    # =============================================

    REQUIREMENT_ANALYSIS = (
        "requirement_analysis"
    )


    PROJECT_PLANNING = (
        "project_planning"
    )



    # =============================================
    # Architecture
    # =============================================

    SYSTEM_DESIGN = (
        "system_design"
    )


    SOFTWARE_ARCHITECTURE = (
        "software_architecture"
    )


    DATABASE_DESIGN = (
        "database_design"
    )


    SCALABILITY_DESIGN = (
        "scalability_design"
    )



    # =============================================
    # Development
    # =============================================

    BACKEND_DEVELOPMENT = (
        "backend_development"
    )


    FRONTEND_DEVELOPMENT = (
        "frontend_development"
    )


    API_DEVELOPMENT = (
        "api_development"
    )


    DATABASE_IMPLEMENTATION = (
        "database_implementation"
    )


    CODE_GENERATION = (
        "code_generation"
    )



    # =============================================
    # Testing
    # =============================================

    UNIT_TESTING = (
        "unit_testing"
    )


    INTEGRATION_TESTING = (
        "integration_testing"
    )


    SECURITY_TESTING = (
        "security_testing"
    )


    QUALITY_ASSURANCE = (
        "quality_assurance"
    )



    # =============================================
    # Deployment
    # =============================================

    DOCKER = (
        "docker"
    )


    CI_CD = (
        "ci_cd"
    )


    CLOUD_DEPLOYMENT = (
        "cloud_deployment"
    )


    MONITORING = (
        "monitoring"
    )