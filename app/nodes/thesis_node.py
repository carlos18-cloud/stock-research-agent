import json

from .base_node import BaseNode
from prompts.thesis import SYSTEM_PROMPT
from models.thesis import Thesis


class ThesisNode(BaseNode):

    def __init__(self, llm):
        self.llm = llm

    def run(self, state):

        if not state.evidences or not state.analyses:
            raise ValueError("缺少研究证据或分析结果")

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

        thesis = Thesis(
            main_thesis=data["main_thesis"],
            bull_case=data["bull_case"],
            bear_case=data["bear_case"],
            key_risks=data["key_risks"],
        )

        state.thesis = thesis
        return thesis