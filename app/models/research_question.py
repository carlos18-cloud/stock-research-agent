from dataclasses import dataclass

@dataclass
class ResearchQuestion:
    question: str = ""
    dimension: str = ""
    priority: int = 0
    status: str = "pending"  # pending, in_progress, completed