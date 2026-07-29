import time


from .memory_searcher import MemorySearcher

from .recommendation_engine import RecommendationEngine





class MemoryRetrievalAgent:
    """
    ASEO Memory Retrieval Agent v1.2

    Retrieves previous experience
    and generates recommendations.

    """



    def __init__(self):


        self.searcher = MemorySearcher()


        self.recommendation_engine = RecommendationEngine()



        self.agent_info = {


            "name":

                "Memory Retrieval Agent",


            "version":

                "1.2"

        }







    def run(
        self,
        project_description
    ):


        start=time.time()



        try:



            keywords = project_description.split()



            projects = {}



            for word in keywords:


                results = self.searcher.search(

                    word

                )


                for project in results:


                    project_id = project.get(

                        "project_id"

                    )


                    projects[project_id] = project






            previous_projects = list(

                projects.values()

            )



            previous_projects.sort(

                key=lambda x:x.get(

                    "created_at",

                    ""

                ),

                reverse=True

            )





            recommendations = self.recommendation_engine.analyze(

                previous_projects

            )






            return {


                "status":

                    "success",



                "agent_info":

                    self.agent_info,



                "query":

                    project_description,



                "matches_count":

                    len(previous_projects),



                "previous_projects":

                    previous_projects,



                "recommendations":

                    recommendations,



                "processing_time":

                    round(

                        time.time()-start,

                        3

                    )

            }





        except Exception as error:


            return {


                "status":

                    "failed",


                "error":

                    str(error)

            }