import os



class QualityScanner:
    """
    ASEO Quality Scanner v1.1

    Checks and improves code quality.
    """



    def scan(
        self,
        project_path
    ):


        issues = []

        files_checked = 0

        documentation_files = 0



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





                    if '"""' in content:


                        documentation_files += 1



                    else:


                        issues.append({

                            "file": path,

                            "issue":
                            "Missing documentation",

                            "severity":
                            "low"

                        })





                    if len(content.splitlines()) > 300:


                        issues.append({

                            "file": path,

                            "issue":
                            "Large file size",

                            "severity":
                            "medium"

                        })





        score = self.calculate_score(

            issues

        )



        return {


            "files_checked":

                files_checked,


            "documentation_files":

                documentation_files,


            "quality_score":

                score,


            "issues":

                issues

        }







    def calculate_score(
        self,
        issues
    ):


        score = 100



        for issue in issues:


            severity = issue.get(

                "severity"

            )



            if severity == "critical":

                score -= 15



            elif severity == "medium":

                score -= 5



            elif severity == "low":

                score -= 1




        if score < 0:

            score = 0



        return score