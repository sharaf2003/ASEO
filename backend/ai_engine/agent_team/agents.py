from .base_agent import (
    BaseAgent
)



class ProductAnalystAgent(BaseAgent):


    def __init__(self):

        super().__init__(

            "product_analyst",

            "Product Analyst",

            "requirements analysis"

        )





class ArchitectAgent(BaseAgent):


    def __init__(self):

        super().__init__(

            "architect",

            "System Architect",

            "system architecture"

        )





class BackendEngineerAgent(BaseAgent):


    def __init__(self):

        super().__init__(

            "backend_engineer",

            "Backend Engineer",

            "API development"

        )





class DatabaseEngineerAgent(BaseAgent):


    def __init__(self):

        super().__init__(

            "database_engineer",

            "Database Engineer",

            "database design"

        )





class SecurityEngineerAgent(BaseAgent):


    def __init__(self):

        super().__init__(

            "security_engineer",

            "Security Engineer",

            "application security"

        )





class QAEngineerAgent(BaseAgent):


    def __init__(self):

        super().__init__(

            "qa_engineer",

            "QA Engineer",

            "testing"

        )





class DevOpsEngineerAgent(BaseAgent):


    def __init__(self):

        super().__init__(

            "devops_engineer",

            "DevOps Engineer",

            "deployment"

        )