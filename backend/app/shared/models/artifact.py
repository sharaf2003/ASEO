from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from app.shared.enums.artifact_type import ArtifactType

@dataclass
class Artifact:
    """
    Domain representation of an ASEO artifact.

    Represents any output produced by
    an autonomous agent during execution.
    """

    id: int | None = None


    execution_id: int | None = None


    created_by_agent: str = ""


    artifact_type: ArtifactType = ArtifactType.DOCUMENTATION


    name: str = ""


    content: Any = None


    metadata: dict[str, Any] = field(
        default_factory=dict
    )


    created_at: datetime = field(
        default_factory=datetime.utcnow
    )



    def update_content(
        self,
        content: Any
    ):
        """
        Update artifact content.
        """

        self.content = content



    def add_metadata(
        self,
        key: str,
        value: Any
    ):
        """
        Add metadata information.
        """

        self.metadata[key] = value