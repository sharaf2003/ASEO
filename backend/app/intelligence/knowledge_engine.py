from datetime import datetime



class KnowledgeEngine:

    """
    ASEO Knowledge Engine v1

    Responsible for converting
    agent experiences into structured
    knowledge.

    Sources:

    - Agent memories
    - Project executions
    - Successful solutions
    - Failed attempts
    """



    def __init__(

        self,

        memory_repository=None

    ):


        self.memory_repository = memory_repository



    # =============================================
    # Extract Knowledge
    # =============================================


    def extract_knowledge(

        self,

        memory

    ) -> dict:


        content = memory.content



        knowledge = {

            "agent": memory.agent_name,

            "type": memory.memory_type,

            "source_memory_id": memory.id,

            "created_at": datetime.utcnow().isoformat(),

            "knowledge": {}

        }



        if isinstance(content, dict):


            if "architecture" in content:


                knowledge["knowledge"][

                    "architecture"

                ] = content["architecture"]



            if "implementation" in content:


                knowledge["knowledge"][

                    "implementation"

                ] = content["implementation"]



            if "result" in content:


                knowledge["knowledge"][

                    "result"

                ] = content["result"]



            if "error" in content:


                knowledge["knowledge"][

                    "error"

                ] = content["error"]



        return knowledge



    # =============================================
    # Build Knowledge Base
    # =============================================


    def build_from_memories(

        self,

        memories: list

    ) -> list[dict]:


        knowledge_items = []



        for memory in memories:


            knowledge_items.append(

                self.extract_knowledge(

                    memory

                )

            )



        return knowledge_items



    # =============================================
    # Find Relevant Knowledge
    # =============================================


    def find_relevant(

        self,

        query: str,

        memories: list,

        similarity_engine

    ):


        results = []



        for memory in memories:


            text = str(

                memory.content

            )


            similarity = similarity_engine.calculate_similarity(

                query,

                text

            )



            results.append(

                {

                    "memory_id": memory.id,

                    "agent": memory.agent_name,

                    "similarity": similarity,

                    "content": memory.content

                }

            )



        return sorted(

            results,

            key=lambda x: x["similarity"],

            reverse=True

        )