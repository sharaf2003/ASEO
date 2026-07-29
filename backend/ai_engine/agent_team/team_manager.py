from .agents import (
    ProductAnalystAgent,
    ArchitectAgent,
    BackendEngineerAgent,
    DatabaseEngineerAgent,
    SecurityEngineerAgent,
    QAEngineerAgent,
    DevOpsEngineerAgent
)



class EngineeringTeamManager:
    """
    ASEO Engineering Team Manager v16
    """



    def __init__(self):


        self.agents = [

            ProductAnalystAgent(),

            ArchitectAgent(),

            BackendEngineerAgent(),

            DatabaseEngineerAgent(),

            SecurityEngineerAgent(),

            QAEngineerAgent(),

            DevOpsEngineerAgent()

        ]





    def analyze_requirement(
        self,
        requirement
    ):


        results = []



        for agent in self.agents:


            results.append(

                agent.analyze(

                    requirement

                )

            )



        return {


            "team_size":

                len(self.agents),


            "agents":

                results

        }