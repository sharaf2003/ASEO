from datetime import datetime

from sqlalchemy.orm import Session

from app.agents.memory.memory_repository import MemoryRepository





class AgentMemory:

    """
    Agent memory management layer.

    Uses MemoryRepository for persistent storage.

    Stores:

    - Past executions
    - Successful results
    - Failed attempts
    - Learned patterns
    - Ranked experiences
    """



    def __init__(

        self,

        agent_name: str,

        db: Session,

        project_id: int | None = None,

        organization_id: int | None = None

    ):


        self.agent_name = agent_name

        self.project_id = project_id

        self.organization_id = organization_id


        self.repository = MemoryRepository(

            db

        )



    # =============================================
    # Store Execution
    # =============================================


    def remember_execution(

        self,

        task: str,

        result: dict,

        status: str

    ):


        memory_type = (

            "SUCCESS"

            if status == "SUCCESS"

            else "FAILED"

        )


        return self.repository.save(

            agent_name=self.agent_name,

            memory_type=memory_type,

            content={

                "task": task,

                "result": result,

                "status": status,

                "timestamp": datetime.utcnow()

            },

            project_id=self.project_id,

            organization_id=self.organization_id

        )



    # =============================================
    # Add Pattern
    # =============================================


    def add_pattern(

        self,

        pattern: str

    ):


        return self.repository.save(

            agent_name=self.agent_name,

            memory_type="PATTERN",

            content={

                "pattern": pattern,

                "created_at": datetime.utcnow()

            },

            project_id=self.project_id,

            organization_id=self.organization_id

        )



    # =============================================
    # Retrieve All Memory
    # =============================================


    def get_memory(self):


        return self.repository.get_by_agent(

            self.agent_name

        )



    # =============================================
    # Search Memory
    # =============================================


    def search(

        self,

        keyword: str

    ):


        return self.repository.search(

            keyword

        )



    # =============================================
    # Intelligent Memory Search
    # =============================================


    def search_relevant(

        self,

        keyword: str,

        limit: int = 5

    ):


        """
        Search memories using:

        - Similarity
        - Success score
        - Usage count
        - Recent usage

        Ranking is handled by
        MemoryRepository.
        """


        memories = self.repository.search_relevant(

            keyword,

            limit

        )


        return memories



    # =============================================
    # Mark Memory Used
    # =============================================


    def mark_used(

        self,

        memory_id: int

    ):


        return self.repository.mark_used(

            memory_id

        )