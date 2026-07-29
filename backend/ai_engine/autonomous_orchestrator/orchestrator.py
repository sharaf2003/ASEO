from ai_engine.engineering_brain import (
    EngineeringAnalyzer,
    EngineeringPlanner
)


from ai_engine.agent_team import (
    EngineeringTeamManager
)


from ai_engine.engineering_memory import (
    EngineeringMemoryEngine
)


from ai_engine.llm_router import (
    IntelligenceRouter
)


from ai_engine.autonomous_decision import (
    AutonomousDecisionEngine
)




class AutonomousEngineeringOrchestrator:
    """
    ASEO Autonomous Engineering Orchestrator v16.8.1

    Central Intelligence Coordinator

    Improvements:
    - Smart Memory Retrieval
    - Better Intelligence Selection
    - Improved Decision Confidence
    """



    def __init__(
        self
    ):


        self.brain = EngineeringAnalyzer()


        self.planner = EngineeringPlanner()


        self.team = EngineeringTeamManager()


        self.memory = EngineeringMemoryEngine()


        self.router = IntelligenceRouter()


        self.decision = AutonomousDecisionEngine()






    def _extract_memory_keywords(
        self,
        requirement
    ):


        keywords = []



        words = requirement.lower().split()



        ignored = [

            "build",

            "create",

            "make",

            "develop",

            "a",

            "an",

            "the",

            "system",

            "platform"

        ]



        for word in words:

            if word not in ignored:

                keywords.append(word)



        return keywords






    def engineer(
        self,
        requirement
    ):


        # 1 - Understand requirement

        analysis = self.brain.analyze(

            requirement

        )



        plan = self.planner.create_plan(

            analysis

        )






        # 2 - Smart Memory Retrieval

        memory_results = []



        keywords = self._extract_memory_keywords(

            requirement

        )



        for keyword in keywords:


            results = self.memory.recall(

                keyword

            )


            memory_results.extend(

                results

            )





        memory_used = len(memory_results) > 0






        # 3 - Engineering Team Analysis

        agents = self.team.analyze_requirement(

            requirement

        )






        # 4 - Select Intelligence

        model = self.router.select_model(

            requirement + " architecture design"

        )







        # 5 - Final Autonomous Decision

        decision_sources = [

            "brain",

            "agents"

        ]



        if memory_used:

            decision_sources.append(

                "memory"

            )


        decision_sources.append(

            "improvement"

        )




        decision = self.decision.decide(

            requirement,


            decision_sources

        )







        return {


            "version":

                "16.8.1",



            "status":

                "engineering_completed",



            "requirement":

                requirement,



            "analysis":

                analysis,



            "plan":

                plan,



            "agents":

                agents,



            "memory_used":

                memory_used,



            "memory_results":

                memory_results,



            "selected_intelligence":

                model,



            "decision":

                decision

        }