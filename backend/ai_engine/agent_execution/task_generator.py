from uuid import uuid4



class TaskGenerator:
    """
    ASEO Task Generator v21.2
    """



    def generate(
        self,
        decision
    ):


        tasks = [

            {
                "id": str(uuid4()),
                "task":
                    "Design backend architecture",
                "agent":
                    "backend_engineer"
            },

            {
                "id": str(uuid4()),
                "task":
                    "Design database schema",
                "agent":
                    "database_engineer"
            },

            {
                "id": str(uuid4()),
                "task":
                    "Review security requirements",
                "agent":
                    "security_engineer"
            }

        ]


        return {

            "decision":
                decision,

            "tasks":
                tasks

        }