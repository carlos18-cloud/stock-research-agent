import json
from pathlib import Path
from datetime import datetime


class ResearchHistory:

    def __init__(self, file_path="memory/research_history.json"):
        self.file_path = Path(file_path)

    def load(self):
        if not self.file_path.exists():
            return []

        return json.loads(
            self.file_path.read_text(encoding="utf-8")
        )

    def save(self, state):
        history = self.load()

        history.append({
            "topic": (
                state.topic.title
                if state.topic else state.question
            ),
            "main_thesis": (
                state.thesis.main_thesis
                if state.thesis else ""
            ),
            "research_time": datetime.now().isoformat(),
            "evidence_count": len(state.evidences),
        })

        self.file_path.parent.mkdir(
            parents=True, exist_ok=True
        )

        self.file_path.write_text(
            json.dumps(history, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )