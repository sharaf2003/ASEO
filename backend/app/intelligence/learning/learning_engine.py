from app.models.knowledge_pattern import KnowledgePattern
from app.models.decision_memory import DecisionMemory



class LearningEngine:


    def __init__(

        self,

        db=None

    ):

        self.db = db



    def clamp(

        self,

        value: float

    ):

        return max(

            0,

            min(

                value,

                1

            )

        )



    def learn(

        self,

        feedback,

        agent_result: dict

    ):


        if not self.db:

            return {

                "updated": False,

                "reason": "No database connection"

            }



        learned_patterns = []



        architecture = agent_result.get(

            "architecture",

            {}

        )



        technologies = []



        for layer, data in architecture.items():

            if isinstance(data, dict):

                for key, value in data.items():

                    if "technology" in key and value:

                        technologies.append(value)



        #
        # Update Knowledge Patterns
        #

        for technology in technologies:


            pattern = (

                self.db.query(

                    KnowledgePattern

                )

                .filter(

                    KnowledgePattern.name == technology

                )

                .first()

            )



            if not pattern:

                continue



            if feedback.score >= 0.8:


                pattern.success_rate = min(

                    pattern.success_rate + 1,

                    100

                )


            else:


                pattern.success_rate = max(

                    pattern.success_rate - 1,

                    0

                )



            pattern.usage_count += 1



            learned_patterns.append(

                pattern.name

            )



        #
        # Update Decision Memory
        #

        memories = (

            self.db.query(

                DecisionMemory

            )

            .order_by(

                DecisionMemory.id.desc()

            )

            .limit(1)

            .all()

        )



        if memories:


            memory = memories[0]



            if feedback.score >= 0.8:


                memory.success_score = self.clamp(

                    memory.success_score + 0.05

                )


                memory.confidence = self.clamp(

                    memory.confidence + 0.03

                )


                memory.adaptive_decision_score = self.clamp(

                    memory.adaptive_decision_score + 0.02

                )



            else:


                memory.success_score = self.clamp(

                    memory.success_score - 0.05

                )


                memory.confidence = self.clamp(

                    memory.confidence - 0.03

                )


                memory.adaptive_decision_score = self.clamp(

                    memory.adaptive_decision_score - 0.02

                )



            memory.usage_count += 1



        self.db.commit()



        return {


            "updated": True,


            "patterns": learned_patterns,


            "memory_updated": bool(memories)

        }