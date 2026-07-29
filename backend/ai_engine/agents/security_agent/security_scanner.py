import os



class SecurityScanner:
    """
    ASEO Security Scanner v1

    Scans generated project files.
    """



    def scan(
        self,
        project_path
    ):


        issues = []



        for root, dirs, files in os.walk(project_path):


            for file in files:


                if file.endswith(".py"):


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



                    if "password =" in content:


                        issues.append({

                            "file": path,

                            "severity":"high",

                            "issue":
                            "Hardcoded password"

                        })



                    if "secret =" in content:


                        issues.append({

                            "file": path,

                            "severity":"high",

                            "issue":
                            "Hardcoded secret"

                        })



        return issues