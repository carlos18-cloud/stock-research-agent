from dataclasses import dataclass, field

@dataclass
class Report:
    title: str
    executive_summary: str = ""
    sections: list[str] = field(default_factory=list)
    sources: list[str] = field(default_factory=list)