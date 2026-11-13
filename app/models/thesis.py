from dataclasses import dataclass, field

@dataclass
class Thesis:
    main_thesis: str
    bull_case: list[str] = field(default_factory=list)
    bear_case: list[str] = field(default_factory=list)
    key_risks: list[str] = field(default_factory=list)