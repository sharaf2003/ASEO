import os



class OptimizationScanner:
    """
    ASEO Optimization Scanner v1.0

    Analyzes project performance.
    """



    def scan(
        self,
        project_path
    ):


        recommendations = []

        files_checked = 0

        total_lines = 0



        for root, dirs, files in os.walk(project_path):


            for file in files:


                if file.endswith(".py"):


                    files_checked += 1


                    path = os.path.join(

                        root,

                        file

                    )



                    with open(

                        path,

                        "r",

                        encoding="utf-8"

                    ) as f:


                        content = f.read()



                    lines = len(

                        content.splitlines()

                    )


                    total_lines += lines





                    # Large files

                    if lines > 300:


                        recommendations.append({

                            "file": path,

                            "issue":
                            "Large file",

                            "suggestion":
                            "Split into smaller modules"

                        })





                    # Database query check

                    if "query(" in content:


                        recommendations.append({

                            "file": path,

                            "issue":
                            "Database query detected",

                            "suggestion":
                            "Review indexes and caching"

                        })






        score = 100



        score -= len(recommendations) * 5



        if score < 0:

            score = 0





        return {


            "files_checked":

                files_checked,


            "total_lines":

                total_lines,


            "performance_score":

                score,


            "recommendations":

                recommendations

        }