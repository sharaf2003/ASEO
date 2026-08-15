from datetime import datetime


from app.repositories.decision_memory_repository import (
    DecisionMemoryRepository
)

from app.repositories.memory_system_state_repository import (
    MemorySystemStateRepository
)

from app.intelligence.memory.memory_score_engine import (
    MemoryScoreEngine
)

from app.intelligence.memory.memory_consolidation import (
    MemoryConsolidationEngine
)

from app.intelligence.memory.knowledge_manager import (
    KnowledgeManager
)


class DecisionMemory:

    """
    ASEO Long Term Decision Memory Engine

    Responsibilities:

    - Store previous decisions
    - Retrieve similar decisions
    - Rank previous decisions
    - Calculate decision confidence
    - Improve future decisions
    """



    def __init__(

        self,

        db=None

    ):

        self.db = db

        self.repository = None

        self.state_repository = None

        self.score_engine = MemoryScoreEngine()

        self.consolidation_engine = MemoryConsolidationEngine()

        self.knowledge_manager = None


        if db:

            self.repository = DecisionMemoryRepository(

                db

            )

            self.state_repository = MemorySystemStateRepository(
                db
            )

            self.knowledge_manager = KnowledgeManager(
                db
            )

    

    # =============================================
    # Save Decision Memory
    # =============================================


    def save(

        self,

        decision: dict

    ) -> dict:



        memory = {


            "architecture": decision.get(

                "architecture",

                {}

            ),


            "agent_name": decision.get(

                "agent_name",

                "ArchitectAgent"

            ),


            "decision_history_id": decision.get(

                "decision_history_id"

            ),


            "success_score": decision.get(

                "success_score",

                1

            ),


            "similarity_score": decision.get(

                "similarity_score",

                0

            ),


            "confidence": decision.get(

                "confidence",

                1

            ),

            "adaptive_decision_score": decision.get(

                "adaptive_decision_score",

                0

            ),


            "recency": decision.get(

                "recency",

                0

            ),


            "memory_score": round(

                self.score_engine.calculate_score(

                    similarity_score=decision.get(
                        "similarity_score",
                        0.5
                    ),

                    success_score=decision.get(
                        "success_score",
                        0
                    ),

                    usage_count=decision.get(
                        "usage_count",
                        1
                    ),

                    confidence=decision.get(
                        "confidence",
                        1
                    ),

                    recency=decision.get(
                        "recency",
                        1
                    )

                ),

                2

            ),

            "memory_strength": decision.get(
                "memory_strength",
                0
            ),

            "usage_count": decision.get(

                "usage_count",

                0

            ),


            "extra_data": decision.get(

                "extra_data",

                {}

            ),


            "created_at": datetime.utcnow()

        }



        saved_memory = None



        if self.repository:

            memory["memory_strength"] = self.calculate_memory_strength(
                memory
            )

            saved_memory = self.repository.save_memory(

                memory

            )

            # =============================================
            # Automatic Memory Consolidation Trigger
            # =============================================

            total_memories = len(
                self.repository.get_all_memories()
            )


            state = self.state_repository.get_state()



            if state:


                difference = (
                    total_memories
                    -
                    state.last_consolidation_count
                )


                if difference >= 20:


                    print(
                        "Automatic Memory Consolidation Triggered"
                    )


                    self.consolidate_memories()


        return {


            "saved": True,


            "database_saved": saved_memory is not None,


            "memory": memory,


            "record": saved_memory

        }



    # =============================================
    # Retrieve Stored Memories
    # =============================================


    def retrieve_memories(

        self

    ) -> list:



        if not self.repository:

            return []



        memories = self.repository.get_all_memories()



        results = []


        for memory in memories:


            recency_score = 0


            if getattr(memory, "updated_at", None):

                updated_at = memory.updated_at


                if updated_at.tzinfo:

                    updated_at = updated_at.replace(
                        tzinfo=None
                    )


                days_old = (
                    datetime.utcnow()
                    -
                    updated_at
                ).days


                recency_score = (
                    self.score_engine
                    .calculate_recency_score(
                        days_old
                    )
                )



            results.append(

                {

                    "id": memory.id,


                    "architecture": memory.architecture,


                    "agent_name": memory.agent_name,


                    "success_score": memory.success_score,


                    "memory_score": memory.memory_score,


                    "usage_count": memory.usage_count,


                    "confidence": getattr(
                        memory,
                        "confidence",
                        0
                    ),

                    "adaptive_decision_score": getattr(

                        memory,

                        "adaptive_decision_score",

                        0

                    ),


                    "recency": recency_score

                }

            )



        return results



    # =============================================
    # Search Similar Decisions
    # =============================================


    def search(

        self,

        architecture: dict,

        previous_decisions: list

    ) -> list:



        results = []



        for previous in previous_decisions:


            previous_architecture = previous.get(

                "architecture",

                {}

            )



            similarity = self.calculate_similarity(

                architecture,

                previous_architecture

            )



            if similarity > 0:


                results.append(

                    {


                        "architecture": previous_architecture,


                        "similarity_score": similarity,


                        "success_score": previous.get(

                            "success_score",

                            0

                        ),


                        "usage_count": previous.get(

                            "usage_count",

                            0

                        ),


                        "confidence": previous.get(

                            "confidence",

                            0

                        ),

                        "adaptive_decision_score": previous.get(
                            "adaptive_decision_score",
                            0
                        ),


                        "recency": previous.get(

                            "recency",

                            0

                        ),


                        "reason":

                        "Similar previous successful decision"

                    }

                )



        results = self.rank_decisions(
            results
        )


        return results



    # =============================================
    # Calculate Memory Strength With Decay
    # =============================================

    def calculate_memory_strength(

        self,

        decision: dict

    ) -> float:


        confidence = decision.get(
            "confidence",
            0
        )


        memory_score = decision.get(
            "memory_score",
            0
        )


        usage_count = decision.get(
            "usage_count",
            0
        )


        recency = decision.get(
            "recency",
            0
        )


        usage_factor = min(
            usage_count / 50,
            1
        )


        strength = (

            confidence * 0.4

            +

            memory_score * 0.3

            +

            usage_factor * 0.2

            +

            recency * 0.1

        )


        return round(

            min(
                strength,
                1
            ),

            2

        )

    # =============================================
    # Rank Previous Decisions
    # =============================================


    def rank_decisions(

        self,

        decisions: list

    ) -> list:



        if not decisions:

            return []



        ranked = []



        for decision in decisions:



            memory_score = self.score_engine.calculate_score(

                similarity_score=decision.get(

                    "similarity_score",

                    0

                ),


                success_score=decision.get(

                    "success_score",

                    0

                ),


                usage_count=decision.get(

                    "usage_count",

                    0

                ),


                confidence=decision.get(

                    "confidence",

                    0

                ),


                recency=decision.get(

                    "recency",

                    0

                )

            )



            decision["memory_score"] = round(
                memory_score,
                2
            )

            adaptive_score = decision.get(
                "adaptive_decision_score",
                0
            )


            decision["adaptive_memory_score"] = round(
                (
                    memory_score * 0.8
                )
                +
                (
                    adaptive_score * 0.2
                ),
                2
            )

            memory_strength = self.calculate_memory_strength(
                decision
            )

            decision["memory_strength"] = memory_strength


            decision["confidence"] = round(
                decision.get(
                    "confidence",
                    0
                ),
                2
            )


            ranked.append(

                decision

            )



        ranked.sort(

            key=lambda item:

            item.get(

                "memory_strength",

                0

            ),

            reverse=True

        )



        return ranked



    # =============================================
    # Calculate Similarity
    # =============================================


    def calculate_similarity(

        self,

        current,

        previous

    ) -> float:



        if not current or not previous:

            return 0



        total = 0

        matched = 0



        for layer, value in current.items():


            if layer in previous:


                total += 1



                if value == previous[layer]:

                    matched += 1



        if total == 0:

            return 0



        return round(

            matched / total,

            2

        )



    # =============================================
    # Confidence Calculation
    # =============================================


    def calculate_confidence(

        self,

        decisions: list

    ) -> float:



        if not decisions:

            return 0



        scores = [


            d.get(

                "success_score",

                0

            )


            for d in decisions

        ]



        return round(

            sum(scores) / len(scores),

            2

        )

    def search_memory(
        self,
        request_text: str,
        memories: list
    ) -> list:


        results = []


        request_text = request_text.lower()



        technologies = [

            "fastapi",
            "react",
            "postgresql",
            "docker",
            "flutter",
            "firebase",
            "django",
            "node",
            "angular",
            "spring"

        ]



        requested_technologies = []


        for tech in technologies:

            if tech in request_text:

                requested_technologies.append(
                    tech
                )



        if not requested_technologies:

            return []



        for memory in memories:


            architecture = memory.get(
                "architecture",
                {}
            )


            if not architecture:

                continue



            architecture_text = ""



            for layer, data in architecture.items():


                if isinstance(data, dict):

                    for value in data.values():

                        if value:

                            architecture_text += (
                                str(value).lower()
                                + " "
                            )



            matched = 0



            for tech in requested_technologies:


                if tech in architecture_text:

                    matched += 1



            if matched == 0:

                continue



            similarity = round(

                matched /
                len(requested_technologies),

                2

            )



            if self.repository and memory.get("id"):


                updated_memory = self.repository.increase_usage(

                    memory.get("id")

                )


                if updated_memory:


                    memory["usage_count"] = (
                        updated_memory.usage_count
                    )



            results.append({


                "id": memory.get("id"),


                "architecture": architecture,


                "similarity_score": similarity,


                "success_score": memory.get(

                    "success_score",

                    0

                ),


                "usage_count": memory.get(

                    "usage_count",

                    0

                ),


                "confidence": memory.get(

                    "confidence",

                    0

                ),

                "adaptive_decision_score": memory.get(
                    "adaptive_decision_score",
                    0
                ),


                "recency": memory.get(

                    "recency",

                    0

                )

            })



        return self.rank_decisions(

            results

        )

    def consolidate_memories(
        self
    ):


        memories = self.retrieve_memories()


        patterns = self.consolidation_engine.consolidate(
            memories
        )


        if self.knowledge_manager:

            self.knowledge_manager.store_patterns(
                patterns
            )


        if self.state_repository:

            self.state_repository.update_after_consolidation(

                len(memories)

            )


        return patterns