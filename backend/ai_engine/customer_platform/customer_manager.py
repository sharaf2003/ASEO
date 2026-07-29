from .customer import Customer
from .workspace import Workspace



class CustomerManager:
    """
    ASEO Customer Management System v19.4
    """



    def __init__(
        self
    ):

        self.customers = {}

        self.workspaces = {}





    def create_customer(
        self,
        name,
        plan
    ):


        customer = Customer(

            name,

            plan

        )


        self.customers[

            customer.id

        ] = customer



        return customer.to_dict()






    def create_workspace(
        self,
        customer_id,
        name
    ):


        workspace = Workspace(

            name,

            customer_id

        )



        self.workspaces[

            workspace.id

        ] = workspace



        customer = self.customers.get(

            customer_id

        )


        if customer:

            customer.add_workspace(

                workspace.id

            )



        return workspace.to_dict()





    def customer_dashboard(
        self,
        customer_id
    ):


        customer = self.customers.get(

            customer_id

        )


        if not customer:

            return None



        return {


            "customer":

                customer.name,


            "plan":

                customer.plan,


            "workspaces":

                len(customer.workspaces)

        }