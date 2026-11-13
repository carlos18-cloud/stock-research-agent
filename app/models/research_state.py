from dataclasses import dataclass, field

from models.topic import Topic
from models.research_question import ResearchQuestion
from models.evidence import Evidence
from models.analysis import Analysis
from models.thesis import Thesis
from models.report import Report


@dataclass
class ResearchState:

    question: str = ""
    topic: Topic | None = None

    research_questions: list[ResearchQuestion] = field(
        default_factory=list
    )

    search_results: list[dict] = field(
        default_factory=list
    )

    news_results: list[dict] = field(
        default_factory=list
    )

    evidences: list[Evidence] = field(
        default_factory=list
    )

    analyses: list[Analysis] = field(
        default_factory=list
    )

    thesis: Thesis | None = None
    report: Report | None = None

    reflection_count: int = 0
    max_reflection_count: int = 3