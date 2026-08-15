from datetime import datetime

from app.intelligence.knowledge_feedback import KnowledgeFeedback

from app.repositories.knowledge_repository import KnowledgeRepository

from app.repositories.knowledge_relation_repository import (
    KnowledgeRelationRepository
)





class LearningEngine:

    """
    ASEO Learning Engine v4

    Responsibilities:

    - Analyze executions
    - Extract knowledge patterns
    - Store knowledge context
    - Build intelligent knowledge relations
    - Improve future decisions
    """



    def __init__(

        self,

        db=None,

        knowledge_engine=None

    ):


        self.knowledge_engine = knowledge_engine


        self.knowledge_repository = None

        self.relation_repository = None

        self.feedback_engine = None



        if db:


            self.knowledge_repository = KnowledgeRepository(

                db

            )


            self.relation_repository = KnowledgeRelationRepository(

                db

            )

            self.feedback_engine = KnowledgeFeedback(
                db=db
            )





    # =============================================
    # Learn From Execution
    # =============================================


    def learn_from_execution(

        self,

        execution_result: dict

    ) -> dict:



        status = execution_result.get(

            "status",

            "UNKNOWN"

        )



        result = execution_result.get(

            "result",

            execution_result

        )



        self.extract_knowledge(

            result,

            status

        )

        self.apply_feedback(
            result,
            status
        )



        return {


            "timestamp":

                datetime.utcnow().isoformat(),



            "status":

                status,



            "confidence":

                self.calculate_confidence(

                    execution_result

                ),



            "lessons": [

                "Knowledge extracted successfully"

            ]

        }





    # =============================================
    # Extract Knowledge
    # =============================================


    def extract_knowledge(

        self,

        result: dict,

        status: str

    ):



        if not self.knowledge_repository:

            return



        success = (

            str(status).upper()

            ==

            "SUCCESS"

        )



        patterns = []



        architecture = result.get(

            "architecture",

            {}

        )



        if isinstance(architecture, dict):


            for layer, values in architecture.items():



                if isinstance(values, dict):


                    for key, value in values.items():


                        if isinstance(value, str):


                            pattern = self.save_pattern(

                                category=key,

                                name=value,

                                success=success,

                                context={

                                    "layer": layer,

                                    "source": "architecture"

                                }

                            )


                            if pattern:

                                patterns.append(pattern)



                elif isinstance(values, str):


                    pattern = self.save_pattern(

                        category=layer,

                        name=values,

                        success=success,

                        context={

                            "layer": layer,

                            "source": "architecture"

                        }

                    )


                    if pattern:

                        patterns.append(pattern)





        technologies = result.get(

            "technologies",

            []

        )



        for technology in technologies:


            pattern = self.save_pattern(

                category="technology",

                name=str(technology),

                success=success,

                context={

                    "layer": "technology",

                    "source": "technology_stack"

                }

            )


            if pattern:

                patterns.append(pattern)





        self.create_relations(

            patterns

        )





    # =============================================
    # Save Pattern
    # =============================================


    def save_pattern(

        self,

        category: str,

        name: str,

        success: bool,

        context: dict | None = None

    ):



        return self.knowledge_repository.add_pattern(

            category=category,

            name=name,

            success=success,

            metadata={

                "source":

                    "learning_engine"

            },

            context=context

        )





    # =============================================
    # Create Intelligent Relations
    # =============================================


    def create_relations(

        self,

        patterns: list

    ):



        if not self.relation_repository:

            return


        # Check each pair only once
        for index, source in enumerate(patterns):


            for target in patterns[index + 1:]:



                if source.id == target.id:

                    continue



                relation = self.detect_relation_type(

                    source,

                    target

                )



                if relation:


                    self.relation_repository.add_relation(

                        source_id=source.id,

                        target_id=target.id,

                        relation_type=relation,

                        confidence=1.0,

                        extra_data={

                            "source":

                                "context_engine"

                        }

                    )



                else:


                    # Try reverse direction only
                    reverse_relation = self.detect_relation_type(

                        target,

                        source

                    )


                    if reverse_relation:


                        self.relation_repository.add_relation(

                            source_id=target.id,

                            target_id=source.id,

                            relation_type=reverse_relation,

                            confidence=1.0,

                            extra_data={

                                "source":

                                    "context_engine"

                            }

                        )


    # =============================================
    # Context Based Relation Detection
    # =============================================


    def detect_relation_type(

        self,

        source,

        target

    ):



        source_context = source.context or {}

        target_context = target.context or {}



        source_layer = source_context.get(

            "layer"

        )


        target_layer = target_context.get(

            "layer"

        )



        source_category = source.category.lower()

        target_category = target.category.lower()


        # =============================================
        # Backend Knowledge
        # =============================================


        if source_layer == "backend":


            if (

                target_layer == "backend"

                and

                target_category == "architecture"

            ):

                return "implements"


        # =============================================
        # Database Knowledge
        # =============================================


        if (

            source_category == "orm"

            and

            target_layer == "database"

            and

            target_category == "technology"

        ):

            return "uses"


        # =============================================
        # Frontend Knowledge
        # =============================================


        if source_layer == "frontend":


            if (

                target_layer == "frontend"

                and

                target_category == "type"

            ):

                return "has_type"


        # =============================================
        # Deployment Knowledge
        # =============================================


        if source_layer == "deployment":


            if (

                target_layer == "deployment"

                and

                target_category == "environment"

            ):

                return "deployed_on"




        return None





    # =============================================
    # Confidence
    # =============================================


    def calculate_confidence(

        self,

        result: dict

    ) -> float:



        status = str(

            result.get(

                "status",

                ""

            )

        ).upper()



        if status == "SUCCESS":

            return 1.0



        if status == "FAILED":

            return 0.0



        return 0.5





    # =============================================
    # Improvement
    # =============================================


    def generate_improvement(

        self,

        lesson: dict

    ) -> dict:


        return {


            "type":

                "decision_update",



            "confidence":

                lesson["confidence"],



            "recommendation":

                lesson["lessons"]

        }
        
    # =============================================
    # Apply Knowledge Feedback
    # =============================================

    def apply_feedback(

        self,

        result: dict,

        status: str

    ):


        if not self.feedback_engine:

            return



        success = (

            str(status).upper()

            ==

            "SUCCESS"

        )


        self.feedback_engine.update(

            result,

            success

        )