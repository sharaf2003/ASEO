from .company_orchestrator import CompanyOrchestrator



class AutonomousCompany:
    """
    ASEO Autonomous Company v21.0
    """



    def __init__(self):

        self.orchestrator = CompanyOrchestrator()



    def build(
        self,
        request
    ):


        return self.orchestrator.run(

            request

        )