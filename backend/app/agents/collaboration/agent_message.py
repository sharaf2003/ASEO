from dataclasses import dataclass
from datetime import datetime



@dataclass
class AgentMessage:

    sender: str

    receiver: str

    message_type: str

    content: dict

    created_at: datetime = datetime.utcnow()