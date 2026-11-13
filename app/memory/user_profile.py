import json
from pathlib import Path


class UserProfile:

    def __init__(self, file_path="memory/user_profile.json"):
        self.file_path = Path(file_path)

    def load(self):
        if not self.file_path.exists():
            return {
                "market": "US Stocks",
                "research_focus": [
                    "AI",
                    "Semiconductors",
                    "Cloud Computing",
                    "Robotics",
                ],
                "investment_perspective": True,
            }

        return json.loads(
            self.file_path.read_text(encoding="utf-8")
        )

    def save(self, profile: dict):
        self.file_path.parent.mkdir(
            parents=True, exist_ok=True
        )

        self.file_path.write_text(
            json.dumps(profile, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )