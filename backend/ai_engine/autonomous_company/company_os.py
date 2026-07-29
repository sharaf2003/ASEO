from .autonomous_controller import AutonomousController




class ASEOCompanyOS:
    """
    ASEO Company Operating System v20.0
    """



    def __init__(self):

        self.controller = AutonomousController()





    def run_company(
        self,
        request
    ):


        return self.controller.run(

            request

        )