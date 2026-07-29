from ai_engine.saas_backend import (
    UserService,
    ProjectService,
    DashboardService
)



user_service = UserService()


project_service = ProjectService()


dashboard_service = DashboardService()



customer = user_service.create_customer(

    "ASEO Client",

    "Professional"

)



project = project_service.create_project(

    "AI Ecommerce Platform"

)



dashboard = dashboard_service.customer_dashboard(

    customer["id"]

)



print({

    "customer":

        customer,


    "project":

        project,


    "dashboard":

        dashboard

})