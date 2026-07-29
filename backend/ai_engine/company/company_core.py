from .departments import (
    CompanyDepartments
)


from .company_report import (
    CompanyReport
)




class AutonomousCompanyCore:
    """
    ASEO Autonomous Software Company Core v18.1
    """



    def __init__(
        self
    ):


        self.departments = CompanyDepartments()






    def build_company(
        self,
        request
    ):


        departments = self.departments.all()



        report = CompanyReport(

            request,

            departments

        )



        return {


            "version":

                "18.1",



            "status":

                "company_initialized",



            "company":

                report.to_dict()

        }