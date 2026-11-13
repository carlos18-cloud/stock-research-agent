from dataclasses import dataclass

@dataclass
class Evidence:
    claim: str
    source: str
    content: str
    source_type: str = "web"
    credibility: float = 0.0