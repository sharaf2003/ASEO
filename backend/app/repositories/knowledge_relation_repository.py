from sqlalchemy.orm import Session


class KnowledgeRelationRepository:


    def __init__(

        self,

        db: Session

    ):

        self.db = db