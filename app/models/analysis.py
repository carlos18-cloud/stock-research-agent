from dataclasses import dataclass

@dataclass
class Analysis:
    topic: str
    conclusion: str
    supporting_evidence: list[str]
    confidence: float = 0.0