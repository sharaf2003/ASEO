from app.repositories.decision_memory_repository import DecisionMemoryRepository
from app.intelligence.memory.memory_consolidation import MemoryConsolidationEngine



class DatabaseMemoryConsolidator:


    def __init__(self, db):

        self.repository = DecisionMemoryRepository(
            db
        )

        self.engine = MemoryConsolidationEngine()



    def consolidate(self):


        memories = self.repository.get_all_memories()



        memory_data = []



        for memory in memories:


            memory_data.append({

                "id": memory.id,

                "architecture": memory.architecture,

                "success_score": memory.success_score,

                "confidence": memory.confidence,

                "adaptive_decision_score": memory.adaptive_decision_score,

                "memory_score": memory.memory_score,

                "usage_count": memory.usage_count

            })



        return self.engine.consolidate(

            memory_data

        )