class CompanyAnalyzer:
    """
    ASEO Company Analyzer v20.5
    """

    def analyze(
        self,
        company_data
    ):


        quality = company_data.get(
            "quality",
            0
        )


        projects = company_data.get(
            "projects",
            0
        )


        if quality >= 90:

            status = "healthy"

        elif quality >= 70:

            status = "stable"

        else:

            status = "needs_improvement"



        return {

            "status":
                status,

            "quality":
                quality,

            "projects":
                projects,

            "analysis":
                "Company performance analyzed"

        }