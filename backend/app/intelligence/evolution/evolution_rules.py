class ArchitectureEvolutionRules:


    def analyze(
        self,
        architecture: dict
    ):

        recommendations = []

        risks = []


        backend = (
            architecture
            .get("backend", {})
            .get("technology")
        )


        database = (
            architecture
            .get("database", {})
            .get("technology")
        )


        if backend == "Firebase":

            recommendations.append(
                "Add Cloud Functions for advanced backend logic"
            )


            risks.append(
                "Vendor dependency on Firebase"
            )


        if database == "Firebase Firestore":

            recommendations.append(
                "Consider PostgreSQL for complex relational data"
            )


        return {

            "recommendations":
                recommendations,

            "risks":
                risks

        }