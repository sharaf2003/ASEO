from ai_engine.ceo_intelligence import CEOAgent
from ai_engine.cfo_intelligence import CFOAgent
from ai_engine.cmo_intelligence import CMOAgent
from ai_engine.coo_intelligence import COOAgent

from ai_engine.company_memory.memory_adapter import (
    MemoryAdapter
)




class ExecutiveController:
    """
    ASEO Executive Controller v21.1

    Connects:

    CEO +
    CFO +
    CMO +
    COO +
    Company Memory
    """



    def __init__(self):

        self.ceo = CEOAgent()

        self.cfo = CFOAgent()

        self.cmo = CMOAgent()

        self.coo = COOAgent()


        # Persistent Company Memory

        self.memory = MemoryAdapter()





    def analyze(
        self,
        project
    ):


        ceo_result = self.ceo.analyze_company(

            {
                "quality": 95,

                "projects": 5
            }

        )





        cfo_result = self.cfo.analyze_project(

            project,

            [

                "backend_engineer",

                "database_engineer",

                "security_engineer"

            ]

        )





        cmo_result = self.cmo.analyze_growth(

            project["name"]

        )





        coo_result = self.coo.analyze_operations(

            {

                "completed_tasks": 20,

                "pending_tasks": 5

            },

            {

                "completed": 25,

                "total": 30

            }

        )





        # Save executive decision into company memory

        memory_record = self.memory.save_decision(

            project["name"],

            "Executive decision generated",

            {

                "ceo":
                    ceo_result,

                "cfo":
                    cfo_result,

                "cmo":
                    cmo_result,

                "coo":
                    coo_result

            }

        )





        return {


            "ceo":

                ceo_result,


            "cfo":

                cfo_result,


            "cmo":

                cmo_result,


            "coo":

                coo_result,


            "memory":

                memory_record

        }