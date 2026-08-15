from datetime import datetime

from sqlalchemy import cast, Text

from sqlalchemy.orm import Session

from app.models.agent_memory import AgentMemory

from app.intelligence.memory_ranking import MemoryRankingEngine





class MemoryRepository:

    """
    Persistent storage layer for agent memories.

    Uses PostgreSQL storage.

    Supports:

    - Agent experiences
    - Successful executions
    - Failed attempts
    - Learned patterns
    - Memory ranking
    """



    def __init__(

        self,

        db: Session

    ):


        self.db = db

        self.ranking_engine = MemoryRankingEngine()



    # =============================================
    # JSON Safe Converter
    # =============================================


    def json_safe(

        self,

        value

    ):


        if isinstance(value, datetime):

            return value.isoformat()



        if isinstance(value, dict):

            return {

                key: self.json_safe(val)

                for key, val in value.items()

            }



        if isinstance(value, list):

            return [

                self.json_safe(item)

                for item in value

            ]



        return value



    # =============================================
    # Save Memory
    # =============================================


    def save(

        self,

        agent_name: str,

        memory_type: str,

        content: dict,

        project_id: int | None = None,

        organization_id: int | None = None

    ):


        content = self.json_safe(

            content

        )


        success_score = (

            100.0

            if memory_type == "SUCCESS"

            else 0.0

        )


        memory = AgentMemory(

            agent_name=agent_name,

            memory_type=memory_type,

            content=content,

            project_id=project_id,

            organization_id=organization_id,

            success_score=success_score,

            usage_count=0,

            last_used=datetime.utcnow()

        )


        try:


            self.db.add(

                memory

            )


            self.db.commit()


            self.db.refresh(

                memory

            )


            return memory



        except Exception:


            self.db.rollback()

            raise



    # =============================================
    # Get Agent Memories
    # =============================================


    def get_by_agent(

        self,

        agent_name: str

    ):


        return (

            self.db.query(AgentMemory)

            .filter(

                AgentMemory.agent_name == agent_name

            )

            .order_by(

                AgentMemory.success_score.desc(),

                AgentMemory.created_at.desc()

            )

            .all()

        )



    # =============================================
    # Search Memory
    # =============================================


    def search(

        self,

        keyword: str

    ):


        return (

            self.db.query(AgentMemory)

            .filter(

                cast(

                    AgentMemory.content,

                    Text

                ).ilike(

                    f"%{keyword}%"

                )

            )

            .order_by(

                AgentMemory.success_score.desc(),

                AgentMemory.created_at.desc()

            )

            .all()

        )



    # =============================================
    # Similarity Calculation
    # =============================================


    def calculate_similarity(

        self,

        text_a: str,

        text_b: str

    ) -> float:


        words_a = set(

            text_a.lower().split()

        )


        words_b = set(

            text_b.lower().split()

        )


        if not words_a or not words_b:

            return 0



        common = words_a.intersection(

            words_b

        )


        return (

            len(common)

            /

            max(

                len(words_a),

                len(words_b)

            )

        ) * 100



    # =============================================
    # Search Relevant Memories
    # =============================================


    def search_relevant(

        self,

        keyword: str,

        limit: int = 5

    ):


        memories = (

            self.db.query(AgentMemory)

            .filter(

                cast(

                    AgentMemory.content,

                    Text

                ).ilike(

                    f"%{keyword}%"

                )

            )

            .all()

        )



        if not memories:

            return []



        similarity_scores = {}



        for memory in memories:


            similarity_scores[memory.id] = (

                self.calculate_similarity(

                    keyword,

                    str(memory.content)

                )

            )



        ranked_memories = self.ranking_engine.rank(

            memories,

            similarity_scores

        )



        return [

            item["memory"]

            for item in ranked_memories[:limit]

        ]



    # =============================================
    # Mark Memory As Used
    # =============================================


    def mark_used(

        self,

        memory_id: int

    ):


        memory = (

            self.db.query(AgentMemory)

            .filter(

                AgentMemory.id == memory_id

            )

            .first()

        )



        if not memory:

            return None



        memory.usage_count += 1

        memory.last_used = datetime.utcnow()



        self.db.commit()


        self.db.refresh(

            memory

        )


        return memory