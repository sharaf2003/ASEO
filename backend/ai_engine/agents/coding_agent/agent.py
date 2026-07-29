# Updated Coding Agent v4

import time


from ai_engine.memory.knowledge_store import KnowledgeStore


from .file_manager import FileManager

from .code_generator import CodeGenerator

from .template_engine import TemplateEngine

from .validator import CodeValidator

from .blueprint_reader import BlueprintReader


from .schema_generator import SchemaGenerator

from .route_generator import RouteGenerator

from .service_generator import ServiceGenerator

from .app_generator import AppGenerator





class CodingAgent:
    """
    ASEO Coding Agent v3


    Converts Planning Blueprint
    into complete backend project.


    Generates:

    - Models
    - Schemas
    - Routes
    - Services
    - FastAPI Application


    """



    def __init__(self):


        # ============================
        # Memory
        # ============================

        self.memory = KnowledgeStore()





        # ============================
        # Coding Components
        # ============================

        self.file_manager = FileManager()


        self.code_generator = CodeGenerator()


        self.template_engine = TemplateEngine()


        self.validator = CodeValidator()


        self.blueprint_reader = BlueprintReader()



        self.schema_generator = SchemaGenerator()


        self.route_generator = RouteGenerator()


        self.service_generator = ServiceGenerator()


        self.app_generator = AppGenerator()






        # ============================
        # Agent Information
        # ============================

        self.agent_info = {


            "name":

                "Coding Agent",


            "version":

                "4.0"

        }







    # =================================
    # Main Execution
    # =================================

    def run(
        self
    ):


        start_time = time.time()



        try:


            # ============================
            # 1. Load Blueprint
            # ============================

            blueprint = self.memory.get_latest_plan()



            if not blueprint:


                return {


                    "status":

                        "failed",


                    "agent_info":

                        self.agent_info,


                    "error":

                        "No project blueprint found"

                }







            # ============================
            # 2. Extract Blueprint
            # ============================

            structure = self.blueprint_reader.extract_structure(
                blueprint
            )


            entities = self.blueprint_reader.extract_entities(
                blueprint
            )


            apis = self.blueprint_reader.extract_apis(
                blueprint
            )







            generated_files = []







            # ============================
            # 3. Create Structure
            # ============================

            for folder in structure:


                path = (

                    "generated_project/"

                    +

                    folder

                )


                self.file_manager.create_directory(
                    path
                )







            # ============================
            # 4. Generate Main App
            # ============================

            main_code = self.app_generator.generate()



            main_path = (

                "generated_project/app/main.py"

            )



            self.file_manager.create_file(
                main_path,
                main_code
            )



            generated_files.append(
                main_path
            )







            # ============================
            # 5. Generate Backend Layers
            # ============================

            for entity in entities:


                table_name = entity["table"]





                # ------------------------
                # Model
                # ------------------------

                model_code = self.code_generator.generate_model(
                    table_name
                )


                model_path = (

                    "generated_project/app/models/"

                    +

                    table_name

                    +

                    ".py"

                )


                self.file_manager.create_file(
                    model_path,
                    model_code
                )


                generated_files.append(
                    model_path
                )







                # ------------------------
                # Schema
                # ------------------------

                schema_code = self.schema_generator.generate(
                    table_name
                )


                schema_path = (

                    "generated_project/app/schemas/"

                    +

                    table_name

                    +

                    "_schema.py"

                )


                self.file_manager.create_file(
                    schema_path,
                    schema_code
                )


                generated_files.append(
                    schema_path
                )







                # ------------------------
                # Route
                # ------------------------

                route_code = self.route_generator.generate(
                    table_name
                )


                route_path = (

                    "generated_project/app/routes/"

                    +

                    table_name

                    +

                    "_routes.py"

                )


                self.file_manager.create_file(
                    route_path,
                    route_code
                )


                generated_files.append(
                    route_path
                )







                # ------------------------
                # Service
                # ------------------------

                service_code = self.service_generator.generate(
                    table_name
                )


                service_path = (

                    "generated_project/app/services/"

                    +

                    table_name

                    +

                    "_service.py"

                )


                self.file_manager.create_file(
                    service_path,
                    service_code
                )


                generated_files.append(
                    service_path
                )










            # ============================
            # 6. Validation
            # ============================

            validation = []



            for file in generated_files:


                validation.append(


                    {

                        "file":

                            file,


                        "valid":

                            self.validator.validate_file(
                                file
                            )

                    }

                )







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


                "generated_files":

                    generated_files,


                "files_count":

                    len(
                        generated_files
                    ),


                "validation":

                    validation

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
