from dataclasses import dataclass
from typing import List



@dataclass
class DocumentAnalysisResult:

    document_type: str

    title: str

    requirements: List[str]

    confidence: float