from dataclasses import dataclass
from uuid import uuid4



@dataclass
class KnowledgeNode:
    """
    ASEO Knowledge Graph Node v14
    """

    name: str

    node_type: str

    metadata: dict = None



    def __post_init__(self):

        self.id = str(uuid4())


        if self.metadata is None:

            self.metadata = {}



    def to_dict(self):

        return {

            "id":
                self.id,

            "name":
                self.name,

            "type":
                self.node_type,

            "metadata":
                self.metadata

        }