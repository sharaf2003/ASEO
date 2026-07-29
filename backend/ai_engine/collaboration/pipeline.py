from .states import PipelineState




class AgentPipeline:
    """
    ASEO Multi Agent Pipeline Engine v13
    """



    def __init__(self):

        self.stages = []

        self.history = []





    def add_stage(
        self,
        name,
        agent
    ):


        self.stages.append(

            {

                "name":
                    name,

                "agent":
                    agent

            }

        )





    def run(
        self,
        context
    ):


        current_context = context



        for stage in self.stages:


            name = stage["name"]

            agent = stage["agent"]



            state = PipelineState(

                stage=name,

                agent=name

            )


            try:


                state.status = "running"



                result = agent.execute(

                    current_context

                )



                state.status = "completed"



                state.result = result



                current_context.update(

                    result

                )



            except Exception as error:


                state.status = "failed"



                state.result = {

                    "error":
                        str(error)

                }


            self.history.append(

                state

            )


            if state.status == "failed":

                break





        return {


            "status":
                "completed",


            "result":
                current_context,


            "stages":
                [

                    item.to_dict()

                    for item

                    in self.history

                ]

        }