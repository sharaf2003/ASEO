from app.agents.registry import AgentRegistry

from app.intelligence.similarity_engine import SimilarityEngine

from app.intelligence.knowledge_engine import KnowledgeEngine

from app.intelligence.pattern_analyzer import PatternAnalyzer

from app.intelligence.decision_model import DecisionModel

from app.intelligence.knowledge_retriever import KnowledgeRetriever

from app.intelligence.pattern_ranker import PatternRanker

from app.agents.agent_plan import AgentExecutionPlan





class AgentDecisionEngine:

    """
    ASEO Agent Decision Engine v3

    Responsible for selecting agents using:

    - Agent Memory
    - Knowledge Patterns
    - Knowledge Retrieval
    - Pattern Ranking
    - Similarity Analysis
    - Decision Model
    - Capability fallback
    """



    def __init__(

        self,

        db=None,

        project_id: int | None = None,

        organization_id: int | None = None,

        memories: list | None = None

    ):


        self.registry = AgentRegistry(

            db=db,

            project_id=project_id,

            organization_id=organization_id

        )


        self.memories = memories or []

        self.last_decision = {}



        # =============================================
        # Intelligence Core
        # =============================================


        self.similarity_engine = SimilarityEngine()


        self.knowledge_engine = KnowledgeEngine()


        self.pattern_analyzer = PatternAnalyzer()



        self.decision_model = DecisionModel(

            knowledge_engine=self.knowledge_engine,

            pattern_analyzer=self.pattern_analyzer,

            similarity_engine=self.similarity_engine

        )



        # =============================================
        # Knowledge Intelligence
        # =============================================


        self.knowledge_retriever = None


        self.pattern_ranker = PatternRanker()



        if db:


            self.knowledge_retriever = KnowledgeRetriever(

                db=db

            )


    # =============================================
    # Agent Memory Intelligence
    # =============================================


    def intelligence_analysis(

        self,

        request: str

    ) -> dict:


        if not self.memories:

            return {}



        return self.decision_model.analyze(

            request,

            self.memories

        )





    # =============================================
    # Knowledge Intelligence Analysis
    # =============================================


    def knowledge_analysis(

        self,

        request: str

    ) -> dict:


        if not self.knowledge_retriever:

            return {}



        knowledge = self.knowledge_retriever.recommend_stack()



        ranked_knowledge = {}



        for layer, patterns in knowledge.items():


            ranked = self.pattern_ranker.rank(

                patterns,

                {

                    "layer": layer

                }

            )


            ranked_knowledge[layer] = ranked



        return ranked_knowledge

    # =============================================
    # Select Agents With Intelligence
    # =============================================


    def select_agents(

        self,

        request: str

    ):


        selected_agents = []



        # =============================================
        # 1. Agent Memory Intelligence
        # =============================================


        memory_result = self.intelligence_analysis(

            request

        )



        # =============================================
        # 2. Knowledge Intelligence
        # =============================================


        knowledge_result = self.knowledge_analysis(

            request

        )



        # =============================================
        # Intelligent Decision
        # =============================================


        confidence = 0


        if memory_result:


            confidence = memory_result.get(

                "confidence",

                0

            )



        # Knowledge confidence

        if knowledge_result:


            confidence = max(

                confidence,

                0.5

            )



        # =============================================
        # Select From Intelligence
        # =============================================


        if confidence >= 0.5:
            planner = self.registry.get_agent(
                "PlannerAgent"
            )

            if planner:

                selected_agents.append(
                    planner
                )



            # Architecture knowledge

            if knowledge_result and knowledge_result.get(

                "backend"

            ):


                architect = self.registry.get_agent(

                    "ArchitectAgent"

                )


                if architect:

                    selected_agents.append(

                        architect

                    )



            # Development knowledge

            if knowledge_result and (

                knowledge_result.get("backend")

                or

                knowledge_result.get("frontend")

            ):


                developer = self.registry.get_agent(

                    "DeveloperAgent"

                )


                if developer:

                    selected_agents.append(

                        developer

                    )


            if selected_agents:


                self.last_decision = {

                    "source": "knowledge_intelligence",

                    "confidence": confidence,

                    "knowledge_used": bool(knowledge_result),

                    "agents": [

                        agent.name

                        for agent in selected_agents

                    ]

                }


                return selected_agents
        # =============================================
        # Rule Based Capability Fallback
        # =============================================

        required_capabilities = (

            self.analyze_request(

                request

            )

        )

        if not required_capabilities:

            default_agents = [

                "PlannerAgent",

                "ArchitectAgent",

                "DeveloperAgent"

            ]

            for name in default_agents:

                agent = self.registry.get_agent(

                    name

                )

                if agent:

                    selected_agents.append(

                        agent

                    )

            return selected_agents
        
        for capability in required_capabilities:


            agents = self.registry.find_by_capability(

                capability

            )


            for agent in agents:


                if agent not in selected_agents:


                    selected_agents.append(

                        agent

                    )


        self.last_decision = {

            "source": "capability_fallback",

            "confidence": confidence,

            "knowledge_used": bool(knowledge_result),

            "agents": [

                agent.name

                for agent in selected_agents

            ]

        }


        return selected_agents


    # =============================================
    # Create Multi Agent Execution Plan
    # =============================================

    def create_execution_plan(

        self,

        agents: list

    ):


        return AgentExecutionPlan(

            agents=agents,

            execution_order=[

                agent.name

                for agent in agents

            ],

            reasons=[

                f"{agent.name} selected by intelligence decision"

                for agent in agents

            ]

        )

    def select_execution_plan(

        self,

        request: str

    ):

        agents = self.select_agents(

            request

        )


        if not agents:

            return AgentExecutionPlan(

                agents=[],

                execution_order=[],

                reasons=[

                    "No suitable agents found"

                ]

            )


        return self.create_execution_plan(

            agents

        )