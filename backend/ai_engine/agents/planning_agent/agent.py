import time



from ai_engine.memory.knowledge_store import KnowledgeStore



from .planner import ProjectPlanner

from .task_generator import TaskGenerator

from .architecture_planner import ArchitecturePlanner

from .database_planner import DatabasePlanner

from .api_planner import APIPlanner

from .structure_generator import StructureGenerator

from .execution_planner import ExecutionPlanner





class PlanningAgent:
    """
    ASEO Planning Agent v5.0


    Generates:

    - Project Plan
    - Architecture Plan
    - Database Design
    - API Design
    - Project Structure
    - Execution Roadmap


    Uses:

    - Knowledge Store
    - Previous Project Memory
    - Recommendations

    """



    def __init__(self):


        self.memory = KnowledgeStore()



        self.planner = ProjectPlanner()


        self.task_generator = TaskGenerator()


        self.architecture_planner = ArchitecturePlanner()


        self.database_planner = DatabasePlanner()


        self.api_planner = APIPlanner()


        self.structure_generator = StructureGenerator()


        self.execution_planner = ExecutionPlanner()





        self.agent_info = {


            "name":

                "Planning Agent",


            "version":

                "5.0"

        }







    def run(
        self,
        memory_context=None
    ):


        start_time = time.time()



        try:


            # ============================
            # Load Knowledge
            # ============================


            knowledge = self.memory.get_summary()





            # ============================
            # Memory Recommendations
            # ============================


            recommendations = {}



            if memory_context:


                recommendations = memory_context.get(

                    "recommendations",

                    {}

                )







            # ============================
            # Enhance Knowledge
            # ============================


            enhanced_knowledge = knowledge.copy ()
            enhanced_knowledge["memory_recommendations"] = recommendations







            # ============================
            # Project Plan
            # ============================


            project_plan = self.planner.create_plan(

                enhanced_knowledge

            )







            # ============================
            # Architecture
            # ============================


            architecture = self.architecture_planner.create_architecture(

                enhanced_knowledge

            )



            if recommendations:


                architecture["based_on_memory"] = True


                architecture["memory_recommendations"] = recommendations







            # ============================
            # Database Design
            # ============================


            database_design = self.database_planner.create_schema(

                enhanced_knowledge

            )







            # ============================
            # API Design
            # ============================


            api_design = self.api_planner.create_apis(

                enhanced_knowledge

            )







            # ============================
            # Project Structure
            # ============================


            project_structure = self.structure_generator.generate(

                architecture

            )







            # ============================
            # Execution Roadmap
            # ============================


            execution_order = self.execution_planner.create_order(

                project_plan

            )







            # ============================
            # Blueprint
            # ============================


            blueprint = {


                "project_plan":

                    project_plan,


                "architecture":

                    architecture,


                "database_design":

                    database_design,


                "api_design":

                    api_design,


                "project_structure":

                    project_structure,


                "execution_order":

                    execution_order,


                "memory_context":

                    memory_context

            }







            self.memory.store_plan(

                blueprint

            )



            knowledge = self.memory.get_summary()







            processing_time = round(

                time.time() - start_time,

                3

            )







            return {


                "status":

                    "success",



                "agent_info":

                    self.agent_info,



                "processing_time":

                    processing_time,



                "knowledge":

                    knowledge,



                "memory_context":

                    memory_context,



                "blueprint":

                    blueprint

            }








        except Exception as error:


            return {


                "status":

                    "failed",



                "agent_info":

                    self.agent_info,



                "error":

                    str(error)

            }