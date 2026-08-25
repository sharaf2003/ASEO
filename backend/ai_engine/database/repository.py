from .models import (
    CustomerModel,
    ProjectModel,
    AgentMemoryModel,
    KnowledgePatternModel,
    KnowledgeRelationModel,
    DecisionMemoryModel
)



class DatabaseRepository:
    """
    ASEO Database Repository v29

    Persistent Intelligence Repository

    Handles:

    Business Data
    +
    Memory
    +
    Pattern Intelligence
    +
    Pattern Evolution
    +
    Pattern Relations
    +
    Decision Memory
    """

    def _serialize_pattern(self, pattern):
        """
        Convert non JSON serializable values
        into JSON compatible values.
        """

        clean = {}

        for key, value in pattern.items():

            if hasattr(value, "isoformat"):

                clean[key] = value.isoformat()

            else:

                clean[key] = value


        return clean

    # ==========================
    # Customers
    # ==========================


    def create_customer(
        self,
        db,
        customer
    ):

        db.add(customer)

        db.commit()

        db.refresh(customer)

        return customer






    # ==========================
    # Projects
    # ==========================


    def create_project(
        self,
        db,
        project
    ):

        db.add(project)

        db.commit()

        db.refresh(project)

        return project








    # ==========================
    # Agent Memory
    # ==========================


    def save_agent_memory(
        self,
        db,
        agent_name,
        memory_type,
        content,
        project_id=None,
        organization_id=None
    ):


        existing = (

            db.query(
                AgentMemoryModel
            )

            .filter(

                AgentMemoryModel.agent_name == agent_name,

                AgentMemoryModel.memory_type == memory_type

            )

            .first()

        )


        if existing:


            existing.content = content


            db.commit()

            db.refresh(existing)


            return existing





        memory = AgentMemoryModel(

            agent_name=agent_name,

            memory_type=memory_type,

            content=content,

            project_id=project_id,

            organization_id=organization_id

        )


        db.add(memory)

        db.commit()

        db.refresh(memory)


        return memory






    def get_agent_memories(
        self,
        db,
        agent_name=None,
        memory_type=None
    ):


        query = db.query(
            AgentMemoryModel
        )


        if agent_name:

            query = query.filter(

                AgentMemoryModel.agent_name == agent_name

            )


        if memory_type:

            query = query.filter(

                AgentMemoryModel.memory_type == memory_type

            )


        return query.all()

    # ==========================
    # Knowledge Patterns
    # ==========================


    def save_pattern(
        self,
        db,
        category,
        name,
        usage_count,
        success_rate,
        extra_data=None
    ):


        pattern = {

            "category": category,

            "name": name,

            "usage_count": usage_count,

            "success_rate": success_rate,

            "extra_data": extra_data

        }


        return self.save_or_update_pattern(

            db,

            pattern

        )








    # ==========================
    # Save Or Update Pattern
    # ==========================

    def save_or_update_pattern(
        self,
        db,
        pattern
    ):


        pattern = self._serialize_pattern(
            pattern
        )


        name = pattern.get(
            "name"
        )


        if not name:

            return None


        existing = (

            db.query(
                KnowledgePatternModel
            )

            .filter(

                KnowledgePatternModel.name == name

            )

            .first()

        )


        if existing:

            existing.usage_count = pattern.get(
                "usage_count",
                existing.usage_count or 0
            )

            existing.success_rate = pattern.get(
                "success_rate",
                existing.success_rate or 0
            )

            existing.pattern_family = pattern.get(
                "pattern_family",
                existing.pattern_family
            )

            existing.variant = pattern.get(
                "variant",
                existing.variant
            )

            existing.confidence_score = pattern.get(
                "confidence",
                existing.confidence_score or 0
            )

            existing.priority_score = pattern.get(
                "priority_score",
                existing.priority_score or 0.5
            )

            existing.context = pattern.get(
                "context",
                existing.context
            )

            existing.extra_data = pattern


            db.commit()

            db.refresh(existing)

            return existing

        new_pattern = KnowledgePatternModel(

            category=pattern.get(
                "category",
                "general"
            ),

            name=name,

            pattern_family=pattern.get(
                "pattern_family",
                name
            ),

            variant=pattern.get(
                "variant",
                pattern.get(
                    "architecture",
                    ""
                )
            ),

            confidence_score=pattern.get(
                "confidence",
                0
            ),

            priority_score=pattern.get(
                "priority_score",
                0.5
            ),

            context=pattern.get(
                "context",
                {}
            ),

            usage_count=pattern.get(
                "usage_count",
                0
            ),

            success_rate=pattern.get(
                "success_rate",
                0
            ),

            last_success_at=pattern.get(
                "last_success_at"
            ),

            extra_data=pattern

        )


        db.add(
            new_pattern
        )


        db.commit()


        db.refresh(
            new_pattern
        )


        return new_pattern


    # ==========================
    # Find Patterns
    # ==========================


    def find_patterns(
        self,
        db,
        name=None
    ):


        query = db.query(

            KnowledgePatternModel

        )


        if name:


            query = query.filter(

                KnowledgePatternModel.name == name

            )


        return query.all()







    # ==========================
    # All Patterns
    # ==========================


    def get_all_patterns(
        self,
        db
    ):


        return (

            db.query(

                KnowledgePatternModel

            )

            .all()

        )






    # ==========================
    # Pattern Relations
    # ==========================


    def create_pattern_relation(
        self,
        db,
        source_id,
        target_id,
        relation_type,
        confidence=0.5,
        usage_count=0,
        extra_data=None
    ):


        existing = (

            db.query(
                KnowledgeRelationModel
            )

            .filter(

                KnowledgeRelationModel.source_id == source_id,

                KnowledgeRelationModel.target_id == target_id,

                KnowledgeRelationModel.relation_type == relation_type

            )

            .first()

        )


        if existing:


            existing.confidence = max(

                existing.confidence,

                confidence

            )


            existing.usage_count += 1


            existing.extra_data = extra_data


            db.commit()

            db.refresh(existing)


            return existing





        relation = KnowledgeRelationModel(


            source_id=source_id,


            target_id=target_id,


            relation_type=relation_type,


            confidence=confidence,


            usage_count=usage_count,


            extra_data=extra_data

        )



        db.add(relation)


        db.commit()


        db.refresh(relation)



        return relation







    def get_pattern_relations(
        self,
        db,
        pattern_id
    ):


        return (

            db.query(

                KnowledgeRelationModel

            )

            .filter(

                (

                    KnowledgeRelationModel.source_id == pattern_id

                )

                |

                (

                    KnowledgeRelationModel.target_id == pattern_id

                )

            )

            .all()

        )






    def get_related_patterns(
        self,
        db,
        pattern_id
    ):


        relations = (

            db.query(

                KnowledgeRelationModel

            )

            .filter(

                KnowledgeRelationModel.source_id == pattern_id

            )

            .all()

        )



        results = []



        for relation in relations:



            pattern = (

                db.query(

                    KnowledgePatternModel

                )

                .filter(

                    KnowledgePatternModel.id == relation.target_id

                )

                .first()

            )



            if pattern:


                results.append({

                    "id":
                        pattern.id,


                    "name":
                        pattern.name,


                    "category":
                        pattern.category,


                    "variant":
                        pattern.variant,


                    "confidence":
                        pattern.confidence_score,


                    "relation":
                        relation.relation_type,


                    "relation_confidence":
                        relation.confidence

                })



        return results