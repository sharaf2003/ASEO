import os
import re



class APIReviewer:
    """
    ASEO API Contract Validator Reviewer v3.0

    Reviews REST API design,
    endpoints, router prefixes,
    contracts, response models
    and REST conventions.
    """



    def review(
        self,
        project_path
    ):


        endpoints = []

        issues = []

        recommendations = []

        files_checked = 0


        router_prefixes = {}



        # ==========================
        # Detect Router Prefixes
        # ==========================


        prefix_pattern = re.compile(

            r'include_router\s*\('
            r'\s*'
            r'(\w+)\.router'
            r'.*?'
            r'prefix\s*=\s*["\']([^"\']+)["\']',

            re.MULTILINE | re.DOTALL

        )



        # Detect API routes

        route_pattern = re.compile(

            r'@(app|router)\.'
            r'(get|post|put|delete|patch)'
            r'\s*\('
            r'\s*'
            r'["\']([^"\']*)["\']',

            re.MULTILINE

        )





        api_files = {}



        # ==========================
        # Read Files
        # ==========================


        for root, dirs, files in os.walk(project_path):


            for file in files:


                if not file.endswith(".py"):

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





                # Find router prefixes

                prefixes = prefix_pattern.findall(

                    content

                )


                for router, prefix in prefixes:

                    router_prefixes[router] = prefix





                # Save api files

                if "/api/" in path.replace("\\", "/"):

                    router_name = os.path.splitext(

                        file

                    )[0]


                    api_files[router_name] = path





        # ==========================
        # Detect Endpoints
        # ==========================


        for api_name, api_path in api_files.items():


            try:

                with open(

                    api_path,

                    "r",

                    encoding="utf-8"

                ) as f:

                    content = f.read()


            except Exception:

                continue





            routes = route_pattern.findall(

                content

            )



            prefix = router_prefixes.get(

                api_name,

                ""

            )



            for route in routes:


                endpoint = route[2]



                full_endpoint = (

                    prefix +

                    endpoint

                )



                if full_endpoint == "":

                    full_endpoint = "/"




                endpoints.append({

                    "method":

                        route[1].upper(),


                    "endpoint":

                        full_endpoint,


                    "file":

                        api_path

                })





                if (

                    "response_model"

                    not in content

                ):


                    recommendations.append({

                        "file":

                            api_path,


                        "recommendation":

                            "Add response_model validation"

                    })







        # ==========================
        # Main App Routes
        # ==========================


        main_path = os.path.join(

            project_path,

            "main.py"

        )


        if os.path.exists(main_path):


            with open(

                main_path,

                "r",

                encoding="utf-8"

            ) as f:


                content = f.read()



            routes = route_pattern.findall(

                content

            )



            for route in routes:


                endpoints.append({

                    "method":

                        route[1].upper(),


                    "endpoint":

                        route[2],


                    "file":

                        main_path

                })





        # ==========================
        # REST Checks
        # ==========================


        for endpoint in endpoints:


            if (

                endpoint["endpoint"].endswith("/")

                and

                endpoint["endpoint"] != "/"

            ):


                issues.append({

                    "endpoint":

                        endpoint["endpoint"],


                    "issue":

                        "Trailing slash convention",


                    "severity":

                        "low"

                })





        score = 100


        score -= len(issues) * 5


        score -= len(recommendations) * 2



        if score < 0:

            score = 0





        return {


            "api_score":

                score,


            "endpoints_checked":

                len(endpoints),


            "endpoints":

                endpoints,


            "files_checked":

                files_checked,


            "issues":

                issues,


            "recommendations":

                recommendations

        }