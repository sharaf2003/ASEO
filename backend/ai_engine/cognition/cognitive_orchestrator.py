from .cognitive_context import CognitiveContext
from .evidence_fusion import EvidenceFusion
from .decision_pipeline import DecisionPipeline


from ai_engine.intelligence.reasoning.reasoning_engine import (
    ReasoningEngine
)


from ai_engine.intelligence.memory.memory_manager import (
    MemoryManager
)


from ai_engine.intelligence.patterns import (
    PatternAnalyzer,
    PatternScorer,
    PatternRegistry
)





class CognitiveOrchestrator:
    """
    ASEO Cognitive Brain v23

    Pattern First Reasoning

    Memory
    +
    Pattern Registry
    +
    Pattern Evolution
    +
    Feedback Learning
    +
    Evidence Fusion
    +
    Reasoning
    """



    def __init__(
        self,
        memory=None,
        pattern_registry=None
    ):


        self.reasoning_engine = ReasoningEngine()


        self.evidence_fusion = EvidenceFusion()


        self.pipeline = DecisionPipeline()



        self.memory_manager = (

            memory

            if memory

            else MemoryManager()

        )



        self.pattern_analyzer = PatternAnalyzer()


        self.pattern_scorer = PatternScorer()



        self.pattern_registry = (

            pattern_registry

            if pattern_registry

            else PatternRegistry()

        )



        # Last used pattern for feedback

        self.last_pattern = None






    def analyze(
        self,
        requirement
    ):



        context = CognitiveContext(

            requirement

        )




        # =====================================
        # 1 - Memory Retrieval
        # =====================================


        memories = self.memory_manager.recall(

            requirement

        )



        print(
            "DEBUG MEMORIES =",
            memories
        )





        # =====================================
        # 2 - Pattern Generation
        # =====================================


        patterns = self.pattern_analyzer.analyze(

            memories

        )



        print(
            "DEBUG PATTERNS =",
            patterns
        )




        registered_patterns = []

        seen = set()



        for pattern in patterns:


            name = pattern.get(
                "name"
            )


            if name in seen:

                continue



            seen.add(name)



            registered = self.pattern_registry.register(

                pattern

            )


            if registered:

                registered_patterns.append(

                    registered

                )








        # =====================================
        # 3 - Pattern Scoring
        # =====================================


        scored_patterns = []



        for pattern in registered_patterns:


            scored = self.pattern_scorer.score(

                pattern

            )


            pattern.update(

                scored

            )


            scored_patterns.append(

                pattern

            )




        context.patterns.extend(

            scored_patterns

        )








        # =====================================
        # 4 - Evidence Collection
        # =====================================


        for memory in memories:


            context.add_evidence(

                {

                    "source":

                        "memory",


                    "weight":

                        memory.get(

                            "confidence",

                            0

                        )

                }

            )





        for pattern in scored_patterns:


            context.add_evidence(

                {

                    "source":

                        "pattern_registry",


                    "weight":

                        pattern.get(

                            "score",

                            0

                        )

                }

            )









        # =====================================
        # 5 - Pattern First Decision
        # =====================================


        learned_decision = None



        if scored_patterns:


            best_pattern = max(

                scored_patterns,

                key=lambda x:

                    (

                        x.get(
                            "confidence",
                            0
                        ),

                        x.get(
                            "score",
                            0
                        )

                    )

            )



            if best_pattern.get(
                "confidence",
                0
            ) >= 0.90:



                self.last_pattern = best_pattern.get(
                    "name"
                )



                learned_decision = {


                    "action":

                        best_pattern.get(
                            "architecture"
                        ),



                    "reasoning":

                        "Decision generated from registered engineering pattern.",



                    "confidence":

                        best_pattern.get(
                            "confidence"
                        )

                }









        # =====================================
        # 6 - Reasoning Fallback
        # =====================================


        if learned_decision is None:


            reasoning_result = self.reasoning_engine.analyze(

                requirement

            )



            learned_decision = {


                "action":

                    reasoning_result.action,



                "reasoning":

                    reasoning_result.reasoning,



                "confidence":

                    reasoning_result.confidence

            }





        context.reasoning.append(

            learned_decision

        )





        context.add_evidence(

            {

                "source":

                    "decision_engine",


                "weight":

                    learned_decision["confidence"]

            }

        )








        # =====================================
        # 7 - Evidence Fusion
        # =====================================


        context = self.evidence_fusion.combine(

            context

        )






        # =====================================
        # 8 - Final Decision
        # =====================================


        return self.pipeline.create_decision(

            context

        )

    # =====================================
    # Feedback Learning Loop
    # =====================================

    def feedback(
        self,
        success=True,
        pattern_name=None
    ):


        # إذا لم يتم إرسال اسم Pattern
        # استخدم آخر Pattern تم استخدامه

        if pattern_name is None:

            pattern_name = self.last_pattern



        if not pattern_name:

            return None




        updated = self.pattern_registry.record_result(

            pattern_name,

            success

        )


        return updated