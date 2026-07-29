from .autonomous_company import AutonomousCompany



class ASEOAICompany:
    """
    ASEO AI Company Platform v21.0
    """



    def __init__(self):

        self.company = AutonomousCompany()



    def execute(
        self,
        request
    ):


        return self.company.build(

            request

        )