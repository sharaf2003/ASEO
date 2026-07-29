import os



class ArchitectureReviewer:
    """
    ASEO Architecture Review Agent v1.0

    Responsible for reviewing
    software architecture decisions.
    """



    def review(self, project_path):


        issues = []

        recommendations = []

        files_checked = 0



        architecture_patterns = {

            "MVC": False,

            "Clean Architecture": False,

            "Layered": False

        }



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



                    # Detect architecture style


                    if "models" in path:

                        architecture_patterns["MVC"] = True



                    if "services" in path:

                        architecture_patterns["Layered"] = True



                    if "repositories" in path:

                        architecture_patterns["Clean Architecture"] = True




                    # Check route business logic


                    if "routes" in path:


                        if "def " in content and "service" not in content:


                            recommendations.append({

                                "file": path,

                                "recommendation":

                                "Move business logic from routes to services"

                            })





        detected = "Unknown"



        for pattern, exists in architecture_patterns.items():

            if exists:

                detected = pattern





        score = 100



        score -= len(issues) * 10



        if score < 0:

            score = 0





        return {


            "architecture_score":

                score,


            "architecture_pattern":

                detected,


            "files_checked":

                files_checked,


            "issues":

                issues,


            "recommendations":

                recommendations

        }