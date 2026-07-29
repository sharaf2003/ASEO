import os



class SeniorReviewer:

    """
    ASEO Senior Code Reviewer v1.0

    Reviews generated projects
    using software engineering standards.
    """



    def review(self, project_path):


        issues = []

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

                        issues.append({

                            "file": path,

                            "issue":
                            "Large class/file",

                            "severity":
                            "medium"

                        })



                    # Missing classes documentation

                    if "class " in content and '"""' not in content:


                        recommendations.append({

                            "file": path,

                            "recommendation":
                            "Add class documentation"

                        })



                    # Business logic inside routes

                    if "\\routes\\" in path:


                        if "if " in content or "for " in content:


                            recommendations.append({

                                "file": path,

                                "recommendation":
                                "Move business logic to services"

                            })





        score = 100



        score -= len(issues) * 5



        if score < 0:

            score = 0





        return {


            "files_checked":

                files_checked,


            "total_lines":

                total_lines,


            "code_review_score":

                score,


            "issues":

                issues,


            "recommendations":

                recommendations

        }