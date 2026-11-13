import json

from .base_node import BaseNode
from prompts.judge import SYSTEM_PROMPT


class JudgeNode(BaseNode):

    def __init__(self, llm):
        self.llm = llm

    def run(self, state):

        evidences = [
            {
                "claim": e.claim,
                "content": e.content,
                "source": e.source,
            }
            for e in state.evidences
        ]

        analyses = [
            {
                "conclusion": a.conclusion,
                "confidence": a.confidence,
            }
            for a in state.analyses
        ]

        prompt = f"""
研究主题：
{state.topic.title if state.topic else state.question}

研究证据：
{json.dumps(evidences, ensure_ascii=False)}

分析结果：
{json.dumps(analyses, ensure_ascii=False)}

{SYSTEM_PROMPT}
"""

        response = self.llm.invoke(prompt)
        data = json.loads(response)

        if not isinstance(data.get("is_sufficient"), bool):
            raise ValueError("is_sufficient 必须是布尔值")

        return {
            "is_sufficient": data["is_sufficient"],
            "reason": data.get("reason", ""),
            "missing_items": data.get("missing_items", []),
        }