class ArchitectureGenerator:
    """
    Generates possible architecture candidates
    based on analyzed requirements.
    """


    def generate(
        self,
        requirements: dict
    ) -> list:


        candidates = []


        project_type = requirements.get(
            "project_type"
        )


        domains = requirements.get(
            "domain",
            []
        )


        # =============================================
        # Mobile Ecommerce Candidates
        # =============================================

        if (
            project_type == "mobile"
            and
            "ecommerce" in domains
        ):


            # Candidate 1
            candidates.append(

                {
                    "name": "Firebase Serverless",

                    "architecture": {

                        "frontend": {
                            "technology": "Flutter",
                            "type": "Mobile Application"
                        },

                        "backend": {
                            "technology": "Firebase",
                            "architecture": "Serverless Backend"
                        },

                        "database": {
                            "technology": "Firebase Firestore",
                            "orm": None
                        },

                        "deployment": {
                            "technology": "Firebase",
                            "environment": "Cloud"
                        }

                    },

                    "strengths": [

                        "fast development",

                        "low maintenance",

                        "good for MVP"

                    ],

                    "weaknesses": [

                        "vendor lock-in",

                        "less backend control"

                    ]

                }

            )


            # Candidate 2
            candidates.append(

                {
                    "name": "FastAPI Enterprise",

                    "architecture": {

                        "frontend": {
                            "technology": "Flutter",
                            "type": "Mobile Application"
                        },

                        "backend": {
                            "technology": "FastAPI",
                            "architecture": "REST API"
                        },

                        "database": {
                            "technology": "PostgreSQL",
                            "orm": "SQLAlchemy"
                        },

                        "deployment": {
                            "technology": "Docker",
                            "environment": "Cloud"
                        }

                    },


                    "strengths": [

                        "high scalability",

                        "full backend control",

                        "better customization"

                    ],


                    "weaknesses": [

                        "higher maintenance",

                        "slower development"

                    ]

                }

            )


            # Candidate 3
            candidates.append(

                {
                    "name": "Node Mongo Stack",

                    "architecture": {

                        "frontend": {
                            "technology": "Flutter",
                            "type": "Mobile Application"
                        },


                        "backend": {
                            "technology": "Node.js",
                            "architecture": "REST API"
                        },


                        "database": {
                            "technology": "MongoDB",
                            "orm": None
                        },


                        "deployment": {
                            "technology": "Docker",
                            "environment": "Cloud"
                        }

                    },


                    "strengths": [

                        "flexible schema",

                        "fast prototyping"

                    ],


                    "weaknesses": [

                        "less relational consistency"

                    ]

                }

            )


        return candidates