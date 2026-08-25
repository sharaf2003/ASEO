from app.agents.base_agent import BaseAgent

from app.agents.capabilities import AgentCapability

from app.shared.models.execution import ExecutionContext

from app.shared.models.artifact import Artifact

import copy

from app.intelligence.knowledge_retriever import KnowledgeRetriever

from app.intelligence.pattern_ranker import PatternRanker

from app.intelligence.decision.adaptive_ranker import (
    AdaptiveDecisionRanker
)

from app.intelligence.context.context_extractor import (
    ContextExtractor
)

from app.intelligence.decision_history_retriever import (
    DecisionHistoryRetriever
)

from app.repositories.decision_history_repository import (
    DecisionHistoryRepository
)

from app.intelligence.decision_fusion import DecisionFusion

from app.intelligence.memory.decision_memory import DecisionMemory

from app.intelligence.memory.confidence_engine import (
    ConfidenceEngine
)

from app.intelligence.reasoning.reasoning_engine import (
    ReasoningEngine
)

from app.intelligence.decision_intelligence.architecture_decision_engine import (
    ArchitectureDecisionEngine
)

from app.intelligence.evolution.architecture_evolution_engine import (
    ArchitectureEvolutionEngine
)



class ArchitectAgent(BaseAgent):

    """
    Responsible for designing
    system architecture using:

    - Previous project knowledge
    - Pattern ranking
    - Intelligent recommendations
    """



    name = "ArchitectAgent"

    role = "architect"



    description = (

        "Designs software architecture, "

        "system structure and technical solutions "

        "using accumulated knowledge."

    )



    capabilities = [

        AgentCapability.SYSTEM_DESIGN,

        AgentCapability.SOFTWARE_ARCHITECTURE,

        AgentCapability.DATABASE_DESIGN,

        AgentCapability.SCALABILITY_DESIGN

    ]





    def __init__(

        self,

        db=None,

        project_id=None,

        organization_id=None

    ):


        super().__init__(

            db=db,

            project_id=project_id,

            organization_id=organization_id

        )


        self.knowledge_retriever = None

        self.pattern_ranker = PatternRanker()

        self.adaptive_ranker = AdaptiveDecisionRanker()

        self.context_extractor = ContextExtractor()

        self.decision_repository = None

        self.decision_history_retriever = None

        self.decision_fusion = DecisionFusion()

        self.decision_memory = None

        self.confidence_engine = ConfidenceEngine()

        self.reasoning_engine = ReasoningEngine()

        self.architecture_decision_engine = ArchitectureDecisionEngine()

        self.architecture_evolution_engine = (
            ArchitectureEvolutionEngine(
                db=db
            )
)



        if db:


            self.knowledge_retriever = KnowledgeRetriever(

                db=db

            )

            self.decision_repository = DecisionHistoryRepository(
                db
            )

            self.decision_history_retriever = DecisionHistoryRetriever(
                db=db
            )

            self.decision_memory = DecisionMemory(
                db=db
            )





    def get_recommendations(self):


        if not self.knowledge_retriever:

            return {}



        return self.knowledge_retriever.recommend_stack()





    def select_best_pattern(

        self,

        patterns,

        layer,

        context=None

    ):


        if not patterns:

            return None



        ranked = self.pattern_ranker.rank(

            patterns,

            {

                "layer": layer

            }

        )

        adaptive_patterns = []


        for item in ranked:


            pattern = item.get(
                "pattern",
                {}
            )


            adaptive_patterns.append({

                "id": pattern.get("id"),

                "name": pattern.get("name"),

                "category": pattern.get("category"),

                "context": pattern.get(
                    "context",
                    {}
                ),

                "success_rate": pattern.get(
                    "success_rate",
                    0
                ),

                "priority_score": pattern.get(
                    "priority_score",
                    0.5
                ),

                "confidence": item.get(
                    "confidence",
                    0.5
                ),

                "memory_score": item.get(
                    "memory_score",
                    0.5
                ),

                "recency": item.get(
                    "recency",
                    0.5
                ),

                "failure_penalty": item.get(
                    "failure_penalty",
                    0
                ),

                "adaptive_decision_score": item.get(
                    "adaptive_decision_score",
                    0
                ),

                "original": item

            })



        adaptive_results = self.adaptive_ranker.rank(

            adaptive_patterns,

            {
                "project_type": context.metadata
                .get(
                    "project_context",
                    {}
                )
                .get(
                    "project_type",
                    ""
                )
            }

        )


        if adaptive_results:


            best_result = adaptive_results[0]


            original = dict(

                best_result.get(

                    "original",

                    {}

                )

            )


            original["adaptive_decision_score"] = best_result.get(
                "decision_score",
                0
            )


            return original


        return ranked[0]


    # =============================================
    # Serialize JSON Safe Data
    # =============================================

    def serialize_metadata(

        self,

        data

    ):


        if isinstance(data, dict):

            return {

                key: self.serialize_metadata(value)

                for key, value in data.items()

            }


        if isinstance(data, list):

            return [

                self.serialize_metadata(item)

                for item in data

            ]


        if hasattr(data, "__dict__"):

            return {

                key: self.serialize_metadata(value)

                for key, value in data.__dict__.items()

            }


        return data

    # =============================================
    # Save Architecture Decision History
    # =============================================

    def save_decision_history(

        self,

        context,

        architecture,

        architecture_decisions,

        knowledge_used

    ):

        if not self.decision_repository:

            return None


        agents_used = [

            self.name

        ]


        success_score = 1.0 if knowledge_used else 0.5


        return self.decision_repository.save_decision(

            project_id=getattr(

                context,

                "project_id",

                None

            ),

            architecture=architecture,

            agents_used=agents_used,

            success_score=success_score,

            extra_data={

                "architecture_decisions":
                    architecture_decisions,

                "source":
                    "ArchitectAgent"

            },

            project_context=self.serialize_metadata(

                context.metadata

            )

        )


    # =============================================
    # Apply Previous Architecture Experience
    # =============================================


    def apply_previous_architecture(

        self,

        architecture: dict,

        previous_architectures: list

    ):


        if not previous_architectures:

            return architecture



        best = previous_architectures[0]



        previous = best.get(

            "architecture",

            {}

        )



        if not previous:

            return architecture



        for layer, values in previous.items():

            if layer not in architecture:
                continue

            if not isinstance(values, dict):
                continue

            for key, value in values.items():

                if value and not architecture[layer].get(key):
                    architecture[layer][key] = value


        return architecture



    # =============================================
    # Retrieve Previous Architectures
    # =============================================


    def get_previous_architectures(

        self

    ):


        if not self.decision_history_retriever:

            return []


        return self.decision_history_retriever.retrieve_successful_architectures()
    



    def run(

        self,

        context: ExecutionContext

    ) -> dict:

        print("DEBUG ARCHITECT AGENT RUN CALLED")
        print("DEBUG DECISION MEMORY:")
        print(self.decision_memory)


        task = context.create_task(

            name="Design architecture",

            agent_name=self.name,

            description=(

                "Design the software architecture "

                "based on analyzed requirements "

                "and previous knowledge."

            )

        )



        context.start_task(task)



        try:


            planner_result = context.metadata.get(

                "planner_result",

                {}

            )

            request_text = planner_result.get(
                "request",
                ""
            )

            project_context = self.context_extractor.extract(
                request_text
            )

            reasoning_result = self.reasoning_engine.reason(
                request_text
            )

            context.metadata[
                "project_context"
            ] = project_context

            context.metadata[
                "architecture_reasoning"
            ] = reasoning_result


            # =========================================
            # Retrieve Previous Knowledge
            # =========================================


            recommendations = self.get_recommendations()

            previous_architectures = []

            memory_confidence = 0


            if self.decision_memory:

                stored_memories = (
                    self.decision_memory.retrieve_memories()
                )

                print("DEBUG STORED MEMORIES COUNT:")
                print(len(stored_memories))

                print("DEBUG FIRST MEMORY:")
                print(
                    stored_memories[:1]
                )


                previous_architectures = (
                    self.decision_memory.search_memory(
                        request_text=planner_result.get(
                            "request",
                            ""
                        ),
                        memories=stored_memories
                    )
                )


                # Fallback: use latest successful memories

                if not previous_architectures and stored_memories:

                    previous_architectures = sorted(
                        stored_memories,
                        key=lambda x: (
                            x.get(
                                "success_score",
                                0
                            ),
                            x.get(
                                "memory_score",
                                0
                            ),
                            x.get(
                                "usage_count",
                                0
                            )
                        ),
                        reverse=True
                    )[:1]

                # Keep only the best historical decision

                if previous_architectures:

                    previous_architectures = [
                        previous_architectures[0]
                    ]


            elif self.decision_history_retriever:

                previous_architectures = (
                    self.decision_history_retriever
                    .retrieve_similar_architectures(
                        current_request=planner_result.get(
                            "request",
                            ""
                        )
                    )
                )


            # =========================================
            # Rank Memory Decisions
            # =========================================


            if previous_architectures and self.decision_memory:

                previous_architectures = (
                    self.decision_memory.rank_decisions(
                        previous_architectures
                    )
                )


                best_memory = previous_architectures[0]


                memory_confidence = self.confidence_engine.calculate_confidence(

                    similarity_score=best_memory.get(
                        "similarity_score",
                        0
                    ),

                    success_score=best_memory.get(
                        "success_score",
                        0
                    ),

                    usage_count=best_memory.get(
                        "usage_count",
                        0
                    ),

                    memory_score=best_memory.get(
                        "memory_score",
                        0
                    ),

                    recency=best_memory.get(
                        "recency",
                        0
                    ),

                    adaptive_memory_score=best_memory.get(
                        "adaptive_memory_score",
                        0
                    )

                )


                if memory_confidence < 0.3:

                    previous_architectures = []

                    memory_confidence = 0



            knowledge_used = False

            architecture_decisions = []

            fusion_confidence = 0

            final_decision_score = 0

            architecture_decision = {}

            evolution_score = 1.0

            evolution_feedback_score = 1.0

            architecture_pattern_applied = False

            best = {}

            adaptive_locked_architecture = None

            reasoning_architecture = (
                reasoning_result
                .get("recommendation", {})
                .get("recommended_architecture")
            )

            # =========================================

            # Build Architecture Decision

            # =========================================

            architecture = {

                "backend": {
                    "technology": None,
                    "architecture": None
                },

                "database": {
                    "technology": None,
                    "orm": None
                },

                "frontend": {
                    "technology": None,
                    "type": None
                },

                "deployment": {
                    "technology": None,
                    "environment": None
                }

            }

            if reasoning_architecture:

                for candidate in reasoning_result.get(
                    "candidates",
                    []
                ):

                    if candidate.get("name") == reasoning_architecture:

                        architecture = candidate.get(
                            "architecture",
                            architecture
                        )

                        break

            if self.architecture_decision_engine:

                best_memory = {}

                if previous_architectures:

                    best_memory = previous_architectures[0]


                elif self.decision_memory:

                    stored_memories = (
                        self.decision_memory.retrieve_memories()
                    )

                    if stored_memories:

                        best_memory = sorted(
                            stored_memories,
                            key=lambda x: (
                                x.get(
                                    "success_score",
                                    0
                                ),
                                x.get(
                                    "memory_score",
                                    0
                                ),
                                x.get(
                                    "memory_strength",
                                    0
                                )
                            ),
                            reverse=True
                        )[0]


                performance_confidence = 0


                if best_memory:

                    performance_confidence = best_memory.get(
                        "memory_strength",
                        0
                    )


                if self.architecture_evolution_engine:

                    evolution_result = (
                        self.architecture_evolution_engine.evolve(
                            architecture
                        )
                    )

                    architecture_evolution = {

                        "architecture":
                            evolution_result.architecture,

                        "improvements":
                            evolution_result.improvements,

                        "risks":
                            evolution_result.risks,

                        "future_recommendations":
                            evolution_result.future_recommendations
                    }

                    scores = []

                    for item in evolution_result.improvements:

                        if isinstance(item, dict):

                            scores.append(
                                item.get(
                                    "weight",
                                    0
                                )
                            )

                    if scores:

                        evolution_score = (
                            sum(scores) / len(scores)
                        )
                

                    evolution_memory = (
                        self.architecture_evolution_engine
                        .get_learning_score(
                            architecture
                        )
                    )

                    candidate_evolution_memory = {}

                    for candidate in reasoning_result.get(
                        "candidates",
                        []
                    ):

                        candidate_name = candidate.get(
                            "name"
                        )


                        candidate_architecture = candidate.get(
                            "architecture",
                            {}
                        )


                        candidate_evolution_memory[candidate_name] = (
                            self.architecture_evolution_engine
                            .get_learning_score(
                                candidate_architecture
                            )
                        )

                    if evolution_memory:

                        evolution_feedback_score = (
                            evolution_memory.get(
                                "success_rate",
                                1.0
                            )
                        )               
                

                architecture_evolution = None

                feedback_score = (
                    evolution_feedback_score *
                    evolution_score
                )



                if feedback_score is None:

                    feedback_score = 1.0


                feedback_score = max(
                    0,
                    min(
                        feedback_score,
                        1.0
                    )
                )

                print("DEBUG EVOLUTION FEEDBACK:")
                print(evolution_feedback_score)

                print("DEBUG FINAL FEEDBACK SENT:")
                print(feedback_score)

                architecture_decision = (

                    self.architecture_decision_engine.decide(

                        reasoning_result,

                        best_memory,

                        feedback_score=feedback_score,

                        performance_confidence=performance_confidence,

                        evolution_score=evolution_score,

                        candidates=reasoning_result.get(
                            "candidates",
                            []
                        ),
                        evolution_memory=
                                candidate_evolution_memory
                    )
                )


                final_decision_score = architecture_decision.get(
                    "final_decision_score",
                    final_decision_score
                )


                # Apply adaptive architecture decision

                selected_architecture = architecture_decision.get(
                    "architecture"
                )


                if selected_architecture:

                    for candidate in reasoning_result.get(
                        "candidates",
                        []
                    ):

                        if candidate.get(
                            "name"
                        ) == selected_architecture:

                            architecture = candidate.get(
                                "architecture",
                                architecture
                            )

                            break

                if architecture_decision.get("architecture"):

                    adaptive_locked_architecture = copy.deepcopy(
                        architecture
                    )

            # =========================================
            # Retrieve Consolidated Architecture Patterns
            # =========================================

            architecture_patterns = []

            if self.knowledge_retriever:

                architecture_patterns = (
                    self.knowledge_retriever
                    .retrieve_architecture_patterns(
                        request_text=planner_result.get(
                            "request",
                            ""
                        )
                    )
                )

            # Apply consolidated architecture pattern

            if architecture_patterns:


                best_pattern = architecture_patterns[0]


                project_type = project_context.get(
                    "project_type",
                    ""
                )


                for pattern in architecture_patterns:


                    pattern_context = pattern.get(
                        "context",
                        {}
                    )


                    if pattern_context.get(
                        "project_type"
                    ) == project_type:


                        best_pattern = pattern

                        break



                pattern_context = best_pattern.get(
                    "context",
                    {}
                )


                if not architecture_decision.get("architecture"):

                    architecture = self.apply_previous_architecture(
                        architecture,
                        [
                            {
                                "architecture": pattern_context
                            }
                        ]
                    )


                    knowledge_used = True

                    architecture_pattern_applied = True

                    architecture_decisions.append({

                            "type": "architecture_pattern",

                            "layer": "architecture",

                            "pattern": best_pattern.get(
                                "name"
                            ),

                            "project_type": project_type,

                            "score": 1.0,

                            "reasons": [

                                "Architecture pattern matched project context",

                                f"Project type matched: {project_type}",

                                "Selected from knowledge base"

                            ]

                    })

                    # Restore adaptive decision after knowledge patterns

                    if architecture_decision.get("architecture"):

                        selected_architecture = (
                            architecture_decision.get("architecture")
                        )

                        for candidate in reasoning_result.get(
                            "candidates",
                            []
                        ):

                            if candidate.get(
                                "name"
                            ) == selected_architecture:

                                architecture = candidate.get(
                                    "architecture",
                                    architecture
                                )

                                break

            if previous_architectures and not architecture_decision.get("architecture"):

                top_memory = previous_architectures[0]

                if top_memory.get(
                    "memory_score",
                    0
                ) >= 0.7:

                    architecture = self.apply_previous_architecture(
                        architecture,
                        previous_architectures
                    )

            # Apply learned knowledge

            if architecture_pattern_applied:

                recommendations = {}

            if memory_confidence < 0.7:

                recommendations = {}

            for layer, patterns in recommendations.items():

                if not recommendations:
                    knowledge_used = False



                best = self.select_best_pattern(

                    patterns,

                    layer,

                    context

                )



                if not best:

                    continue



                pattern = best["pattern"]

                fusion_confidence = self.decision_fusion.calculate_confidence(

                    pattern_score=best.get(
                        "score",
                        0
                    ),

                    similarity_score=(
                        previous_architectures[0].get(
                            "similarity_score",
                            0
                        )
                        if previous_architectures
                        else 0
                    ),

                    success_score=(
                        previous_architectures[0].get(
                            "success_score",
                            0
                        )
                        if previous_architectures
                        else 0
                    )

                )

                final_decision_score = (
                    self.decision_fusion
                    .calculate_final_decision_score(

                        pattern_score=best.get(
                            "score",
                            0
                        ),

                        memory_score=(
                            previous_architectures[0].get(
                                "memory_score",
                                0
                            )
                            if previous_architectures
                            else 0
                        ),

                        confidence_score=fusion_confidence

                    )
                )

                architecture_decisions.append({

                    "id": pattern.get(
                        "id"
                    ),

                    "layer": layer,

                    "pattern": pattern.get(
                        "name"
                    ),

                    "category": pattern.get(
                        "category"
                    ),

                    "score": best.get(
                        "score",
                        0
                    ),

                    "adaptive_decision_score": best.get(
                        "adaptive_decision_score",
                        0
                    ),

                    "reason": best.get(
                        "reasons",
                        []
                    )

                })



                if layer == "backend":


                    if pattern["category"] == "technology":

                        architecture["backend"]["technology"] = pattern["name"]

                        knowledge_used = True


                    elif pattern["category"] == "architecture":

                        architecture["backend"]["architecture"] = pattern["name"]

                        knowledge_used = True
                        




                elif layer == "database":


                    if pattern["category"] == "technology":

                        architecture["database"]["technology"] = pattern["name"]

                        knowledge_used = True


                    elif pattern["category"] == "orm":

                        architecture["database"]["orm"] = pattern["name"]

                        knowledge_used = True

                    elif layer == "frontend":

                        if adaptive_locked_architecture:
                            continue

                        if pattern["category"] == "technology":

                            architecture["frontend"]["technology"] = pattern["name"]

                    elif pattern["category"] == "type":

                        architecture["frontend"]["type"] = pattern["name"]

                        knowledge_used = True

                elif layer == "deployment":

                    if pattern["category"] == "technology":

                        architecture["deployment"]["technology"] = pattern["name"]

                        knowledge_used = True

                    elif pattern["category"] == "environment":

                        architecture["deployment"]["environment"] = pattern["name"]

                        knowledge_used = True

            if not knowledge_used and not previous_architectures:

                request_text = planner_result.get(
                    "request",
                    ""
                ).lower()


                if (
                    not architecture_decision.get("architecture")
                    and
                    "flutter" in request_text
                ):

                    architecture["frontend"]["technology"] = "Flutter"
                    architecture["frontend"]["type"] = "Mobile Application"

                    architecture["backend"]["technology"] = "Firebase"
                    architecture["backend"]["architecture"] = "Serverless Backend"

                    architecture["database"]["technology"] = "Firebase Firestore"

                    architecture["deployment"]["technology"] = "Firebase"
                    architecture["deployment"]["environment"] = "Cloud"

            # Restore adaptive decision after all learning modifications

            if adaptive_locked_architecture:

                architecture = adaptive_locked_architecture

            artifact = Artifact(

                execution_id=context.id,

                created_by_agent=self.name,

                artifact_type="ARCHITECTURE",

                name="System Architecture Design",

                content=architecture

            )

            context.add_artifact(

                artifact

            )

            decision_history = self.save_decision_history(

                context,

                architecture,

                architecture_decisions,

                knowledge_used

            )

            decision_memory_saved = False

            if self.decision_memory and decision_history:

                memory_result = self.decision_memory.save(

                    {

                        "decision_history_id": decision_history.id,

                        "agent_name": self.name,

                        "architecture": architecture,

                        "success_score": (

                            1.0

                            if knowledge_used

                            else 0.5

                        ),

                        "similarity_score": (

                            previous_architectures[0].get(

                                "similarity_score",

                                0

                            )

                            if previous_architectures

                            else 0

                        ),

                        "memory_score": final_decision_score,

                        "adaptive_decision_score": max(

                            [

                                decision.get(
                                    "adaptive_decision_score",
                                    0
                                )

                                for decision in architecture_decisions

                            ],

                            default=0

                        ),

                        "confidence": memory_confidence,

                        "usage_count": 0,

                        "extra_data": {

                            "architecture_decisions":

                                architecture_decisions,

                            "project_context":

                                project_context,

                            "source":

                                "ArchitectAgent"
                        }

                    }

                )

                decision_memory_saved = memory_result.get(

                    "database_saved",

                    False

                )

            result = {

                "agent": self.name,

                "role": self.role,

                "capabilities": [

                    capability.value

                    for capability in self.capabilities

                ],

                "planner_input": planner_result,

                "project_context": context.metadata.get(
                    "project_context",
                    {}
                ),

                "architecture_reasoning": reasoning_result,

                "architecture_decision": architecture_decision,

                "architecture": architecture,

                "architecture_evolution": architecture_evolution,

                "knowledge_used": knowledge_used,

                "knowledge_recommendations": recommendations,

                "previous_architectures": previous_architectures,

                "architecture_decisions": architecture_decisions,

                "artifact": artifact.name,

                "decision_saved": bool(
                    decision_history
                ),

                "decision_memory_saved": decision_memory_saved,

                "decision_confidence": max(
                    memory_confidence,
                    final_decision_score
                ),

                "final_decision_score": final_decision_score,

                "decision_reason": {

                    "fusion_explanation": self.decision_fusion.explain(
                        best.get("score",0),
                        previous_architectures[0].get("similarity_score",0)
                            if previous_architectures else 0,
                        previous_architectures[0].get("success_score",0)
                            if previous_architectures else 0
                    ),

                    "reasoning": reasoning_result.get(
                        "recommendation",
                        {}
                    ).get(
                        "reasoning",
                        []
                    ),

                    "advantages": reasoning_result.get(
                        "recommendation",
                        {}
                    ).get(
                        "advantages",
                        []
                    ),

                    "limitations": reasoning_result.get(
                        "recommendation",
                        {}
                    ).get(
                        "limitations",
                        []
                    )
                }
            }

            context.metadata[

                "architecture_result"

            ] = result

            context.complete_task(

                task,

                result

            )



            return result





        except Exception as error:



            context.fail_task(

                task,

                str(error)

            )


            raise

