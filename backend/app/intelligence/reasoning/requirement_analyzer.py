class RequirementAnalyzer:
    """
    Analyzes extracted project context
    and converts it into architecture requirements.
    """


    def analyze(
        self,
        context: dict
    ) -> dict:


        analysis = {

            "project_type": context.get(
                "project_type",
                "unknown"
            ),

            "domain": context.get(
                "domain",
                []
            ),

            "scale": "medium",

            "architecture_requirements": [],

            "priorities": []

        }


        project_type = analysis["project_type"]

        domains = analysis["domain"]

        needs = context.get(
            "needs",
            []
        )


        # =============================================
        # Project Type Reasoning
        # =============================================

        if project_type == "mobile":

            analysis["architecture_requirements"].extend(
                [
                    "mobile_backend",
                    "mobile_optimized_api"
                ]
            )

            analysis["priorities"].append(
                "user_experience"
            )


        elif project_type == "web":

            analysis["architecture_requirements"].extend(
                [
                    "web_backend",
                    "frontend_architecture"
                ]
            )

            analysis["priorities"].append(
                "scalability"
            )


        elif project_type == "ai":

            analysis["architecture_requirements"].extend(
                [
                    "model_integration",
                    "data_processing"
                ]
            )

            analysis["priorities"].append(
                "performance"
            )


        # =============================================
        # Domain Reasoning
        # =============================================

        if "ecommerce" in domains:


            analysis["architecture_requirements"].extend(
                [
                    "authentication",
                    "product_management",
                    "payment_system",
                    "database_storage"
                ]
            )


            analysis["priorities"].extend(
                [
                    "security",
                    "transaction_reliability"
                ]
            )


        if "ai" in domains:

            analysis["architecture_requirements"].append(
                "ai_pipeline"
            )


        # =============================================
        # Needs Reasoning
        # =============================================

        if "authentication" in needs:

            analysis["architecture_requirements"].append(
                "secure_authentication"
            )


        if "database" in needs:

            analysis["architecture_requirements"].append(
                "persistent_storage"
            )


        if "payments" in needs:

            analysis["architecture_requirements"].append(
                "payment_gateway"
            )


        # Remove duplicates

        analysis["architecture_requirements"] = list(
            set(
                analysis["architecture_requirements"]
            )
        )


        analysis["priorities"] = list(
            set(
                analysis["priorities"]
            )
        )


        return analysis