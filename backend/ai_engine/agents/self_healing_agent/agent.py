# ai_engine/agents/self_healing_agent/agent.py


import time



from .error_analyzer import ErrorAnalyzer

from .fix_engine import FixEngine

from .repair_manager import RepairManager

from .file_repairer import FileRepairer

from .repair_loop import RepairLoop





class SelfHealingAgent:
    """
    ASEO Self-Healing Agent v3


    Responsibilities:

    - Analyze testing failures
    - Generate fixes
    - Apply repairs
    - Retry testing
    - Produce repair history

    """



    def __init__(self):


        # ============================
        # Components
        # ============================


        self.error_analyzer = ErrorAnalyzer()



        self.fix_engine = FixEngine()



        self.repair_manager = RepairManager()



        self.file_repairer = FileRepairer()



        self.repair_loop = RepairLoop()





        # ============================
        # Agent Information
        # ============================


        self.agent_info = {


            "name":

                "Self-Healing Agent",



            "version":

                "3.0"

        }







    # =================================
    # Resolve File Path
    # =================================


    def resolve_file_path(
        self,
        file_path
    ):


        import os



        paths = [

            file_path,

            os.path.join(
                "generated_project",
                file_path
            )

        ]



        for path in paths:


            if os.path.exists(path):

                return path



        return file_path







    # =================================
    # Main Execution
    # =================================


    def run(
        self,
        testing_report,
        testing_agent=None
    ):


        start_time = time.time()



        try:


            current_report = testing_report



            attempt = 0



            history = []







            # ============================
            # Repair Loop
            # ============================


            while self.repair_loop.should_continue(

                attempt,

                current_report

            ):



                attempt += 1



                errors = self.error_analyzer.analyze(

                    current_report

                )



                repairs = []







                for error in errors:



                    fix = self.fix_engine.generate_fix(

                        error

                    )





                    repair_plan = self.repair_manager.repair(

                        fix

                    )





                    file_path = self.resolve_file_path(

                        error["file"]

                    )





                    repair_result = self.file_repairer.repair(

                        file_path,

                        fix

                    )





                    repairs.append(

                        {


                            "file":

                                file_path,



                            "fix":

                                fix,



                            "plan":

                                repair_plan,



                            "result":

                                repair_result


                        }

                    )







                history.append(

                    {


                        "attempt":

                            attempt,



                        "repairs":

                            repairs


                    }

                )







                # ============================
                # Run Testing Again
                # ============================


                if testing_agent:


                    current_report = testing_agent.run()



                else:


                    break







            processing_time = round(

                time.time() - start_time,

                3

            )







            return {


                "status":

                    current_report.get(

                        "status",

                        "unknown"

                    ),



                "agent_info":

                    self.agent_info,



                "attempts":

                    attempt,



                "history":

                    history,



                "final_report":

                    current_report,



                "processing_time":

                    processing_time

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