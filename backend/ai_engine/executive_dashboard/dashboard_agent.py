from .health_monitor import (
    HealthMonitor
)

from .dashboard_builder import (
    DashboardBuilder
)

from .executive_report import (
    ExecutiveReport
)



class DashboardAgent:
    """
    ASEO Executive Dashboard Agent v20.9
    """



    def __init__(self):

        self.monitor = HealthMonitor()

        self.builder = DashboardBuilder()

        self.report = ExecutiveReport()





    def create_dashboard(
        self,
        ceo,
        cfo,
        cmo,
        coo
    ):


        dashboard = self.builder.build(

            ceo,

            cfo,

            cmo,

            coo

        )


        health = self.monitor.calculate(

            {

                "financial":
                    cfo.get(
                        "score",
                        90
                    ),

                "growth":
                    cmo.get(
                        "score",
                        90
                    ),

                "operations":
                    coo.get(
                        "score",
                        90
                    )

            }

        )


        return self.report.generate(

            dashboard,

            health

        )