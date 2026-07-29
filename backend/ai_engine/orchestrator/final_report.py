class FinalReportGenerator:
    """
    ASEO Final Report Generator v3.1

    Generates complete ASEO system reports,
    scores agents and summarizes execution.
    """



    def calculate_score(
        self,
        agents
    ):


        scores = []



        for name, result in agents.items():


            if not isinstance(result, dict):

                continue



            status = result.get(

                "status",

                "unknown"

            )



            if status in [

                "passed",

                "success",

                "completed"

            ]:

                scores.append(100)



            elif status == "warning":

                scores.append(85)



            elif status == "skipped":

                scores.append(90)



            elif status == "failed":

                scores.append(0)



        if not scores:

            return 0



        return round(

            sum(scores) / len(scores)

        )





    def normalize_status(
        self,
        name,
        result
    ):


        status = result.get(

            "status",

            "unknown"

        )



        # Missing requirement files are not fatal

        if (

            name == "document"

            and status == "failed"

            and "File not found" in str(result)

        ):

            return "warning"



        return status





    def generate(
        self,
        project,
        execution,
        testing=None,
        agents=None
    ):


        agents = agents or {}



        failed = []

        warnings = []

        normalized_agents = {}





        for name, result in agents.items():


            if not isinstance(result, dict):

                continue



            status = self.normalize_status(

                name,

                result

            )



            normalized_agents[name] = {


                "status":

                    status


            }





            if status == "failed":

                failed.append(name)



            elif status == "warning":

                warnings.append(name)







        if failed:


            pipeline_status = "failed"



        elif warnings:


            pipeline_status = "completed_with_warnings"



        else:


            pipeline_status = "completed"







        score = self.calculate_score(

            normalized_agents

        )





        summary = execution.get(

            "summary",

            {}

        )





        return {


            "project":

                project,



            "pipeline_status":

                pipeline_status,



            "ASEO_score":

                score,



            "production_ready":

                len(failed) == 0,



            "agents":

                normalized_agents,



            "execution":

                execution,



            "summary":

                {


                    "total_steps":

                        summary.get(

                            "total",

                            0

                        ),



                    "completed":

                        summary.get(

                            "completed",

                            0

                        ),



                    "failed":

                        summary.get(

                            "failed",

                            0

                        ),



                    "warnings":

                        summary.get(

                            "warnings",

                            0

                        )

                },



            "issues":

                {


                    "failed_agents":

                        failed,



                    "warning_agents":

                        warnings

                },



            "quality":

                testing

        }