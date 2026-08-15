from abc import ABC, abstractmethod


from app.shared.models.execution import ExecutionContext

from app.agents.memory.agent_memory import AgentMemory



class BaseAgent(ABC):

    """
    Base class for all ASEO autonomous agents.

    Provides a unified execution contract for:

    - PlannerAgent
    - ArchitectAgent
    - DeveloperAgent
    - TesterAgent
    - DeploymentAgent

    Supports:

    - Agent memory
    - Memory retrieval
    - AI model providers
    - Tools
    - Capability registry
    """



    name: str = "BaseAgent"

    role: str = "generic"

    description: str = ""

    capabilities: list[str] = []



    def __init__(

        self,

        db=None,

        project_id: int | None = None,

        organization_id: int | None = None

    ):


        self.db = db

        self.project_id = project_id

        self.organization_id = organization_id


        self.memory = None


        if self.db:

            self.memory = AgentMemory(

                agent_name=self.name,

                db=self.db,

                project_id=self.project_id,

                organization_id=self.organization_id

            )


        self.model_provider = None

        self.tools = []



    # =============================================
    # Main Execution Wrapper
    # =============================================


    def execute(

        self,

        context: ExecutionContext

    ) -> dict:


        self.validate_context(

            context

        )


        try:


            previous_memory = self.retrieve_memory(

                context.metadata.get(

                    "request",

                    ""

                ),

                context

            )


            context.metadata[

                "previous_memory"

            ] = previous_memory



            result = self.run(

                context

            )


            # Update memory usage after successful execution

            self.update_memory_usage(

                context.metadata.get(

                    "memory_ids",

                    []

                )

            )


            self.remember(

                result

            )


            return result



        except Exception as error:


            context.fail(

                str(error)

            )


            if self.memory:


                self.memory.remember_execution(

                    task=context.metadata.get(

                        "request",

                        "Unknown Task"

                    ),

                    result={

                        "error": str(error)

                    },

                    status="FAILED"

                )


            raise



    # =============================================
    # Context Validation
    # =============================================


    def validate_context(

        self,

        context: ExecutionContext

    ):


        if not context:

            raise ValueError(

                "Execution context is required"

            )



    # =============================================
    # Memory
    # =============================================


    def retrieve_memory(

        self,

        keyword: str,

        context: ExecutionContext

    ):


        if not self.memory:

            return []



        memories = self.memory.search_relevant(

            keyword,

            limit=3

        )



        # Save retrieved memory IDs

        context.metadata[

            "memory_ids"

        ] = [

            memory.id

            for memory in memories

        ]



        return [

            {

                "type": memory.memory_type,

                "content": memory.content

            }

            for memory in memories

        ]



    def update_memory_usage(

        self,

        memory_ids: list[int]

    ):


        if not self.memory:

            return



        for memory_id in memory_ids:


            self.memory.mark_used(

                memory_id

            )



    def remember(

        self,

        data: dict

    ):


        if data and self.memory:


            self.memory.remember_execution(

                task=data.get(

                    "agent",

                    self.name

                ),

                result=data,

                status="SUCCESS"

            )



    def get_memory(self):


        if not self.memory:

            return []


        return self.memory.get_memory()



    # =============================================
    # Tools
    # =============================================


    def register_tool(

        self,

        tool

    ):


        self.tools.append(

            tool

        )



    # =============================================
    # Agent Logic
    # =============================================


    @abstractmethod
    def run(

        self,

        context: ExecutionContext

    ) -> dict:


        pass