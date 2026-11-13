from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Topic:
    title: str = ""
    description: str = ""
    importance_score: float = 0.0
    novelty_score: float = 0.0
    trend_score: float = 0.0
    research_potential_score: float = 0.0
    discovered_at: datetime = field(default_factory=datetime.now)
    market_relevance_score: float = 0.0

    def _topic_score(self) -> float:
        return (
            self.importance_score
            + self.novelty_score
            + self.trend_score
            + self.research_potential_score
            + self.market_relevance_score
        ) / 5