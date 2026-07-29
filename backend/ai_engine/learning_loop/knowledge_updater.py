from datetime import datetime
from uuid import uuid4



class KnowledgeUpdater:
    """
    ASEO Knowledge Updater v20.3
    """

    def __init__(self):

        self.knowledge = []



    def update(
        self,
        project,
        decision,
        analysis
    ):


        record = {

            "id":
                str(uuid4()),

            "project":
                project,

            "decision":
                decision,

            "quality":
                analysis["quality"],

            "success":
                analysis["success"],

            "created_at":
                datetime.now().isoformat()

        }


        self.knowledge.append(record)


        return record