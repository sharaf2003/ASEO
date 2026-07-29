import os
import re





class DatabaseReviewer:
    """
    ASEO Database Design Reviewer v2.0

    Reviews SQLAlchemy database models,
    tables, primary keys,
    timestamps and relationships.
    """



    def review(
        self,
        project_path
    ):


        tables = []

        issues = []

        recommendations = []

        files_checked = 0





        for root, dirs, files in os.walk(
            project_path
        ):


            for file in files:



                if not file.endswith(".py"):

                    continue



                # Ignore package files

                if file == "__init__.py":

                    continue





                path = os.path.join(

                    root,

                    file

                )



                files_checked += 1





                try:

                    with open(

                        path,

                        "r",

                        encoding="utf-8"

                    ) as f:


                        content = f.read()



                except Exception:


                    continue





                # Only inspect models folder


                normalized_path = path.replace(

                    "\\",

                    "/"

                )



                if "/models/" not in normalized_path:


                    continue





                # Detect SQLAlchemy models only


                models = re.findall(

                    r"class\s+(\w+)\s*\(\s*Base\s*\)",

                    content

                )



                for model in models:



                    if model not in tables:

                        tables.append(model)







                    # ==========================
                    # Primary Key Check
                    # ==========================


                    primary_key = re.search(

                        r'primary_key\s*=\s*True',

                        content

                    )



                    if not primary_key:


                        issues.append({

                            "file":

                                path,


                            "issue":

                                "Missing primary key",


                            "severity":

                                "high"

                        })







                    # ==========================
                    # Created At Check
                    # ==========================


                    if "created_at" not in content:


                        recommendations.append({

                            "file":

                                path,


                            "recommendation":

                                "Add created_at field"

                        })







        score = 100



        score -= len(issues) * 10



        score -= len(recommendations) * 2




        if score < 0:

            score = 0





        return {


            "database_score":

                score,


            "tables_detected":

                tables,


            "tables_count":

                len(tables),



            "files_checked":

                files_checked,



            "issues":

                issues,



            "recommendations":

                recommendations

        }