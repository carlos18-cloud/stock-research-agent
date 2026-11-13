import json

from .base_node import BaseNode
from prompts.report import SYSTEM_PROMPT
from models.report import Report


class ReportNode(BaseNode):

    def __init__(self, llm):
        self.llm = llm

    def run(self, state):

        if not state.thesis:
            raise ValueError("缺少投资论点，无法生成报告")

        topic = (
            state.topic.title
            if state.topic
            else state.question
        )

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

        thesis = {
            "main_thesis": state.thesis.main_thesis,
            "bull_case": state.thesis.bull_case,
            "bear_case": state.thesis.bear_case,
            "key_risks": state.thesis.key_risks,
        }

        prompt = f"""
研究主题：
{topic}

研究问题：
{json.dumps(state.research_questions, ensure_ascii=False, default=str)}

研究证据：
{json.dumps(evidences, ensure_ascii=False)}

分析结果：
{json.dumps(analyses, ensure_ascii=False)}

投资论点：
{json.dumps(thesis, ensure_ascii=False)}

{SYSTEM_PROMPT}
"""

        content = self.llm.invoke(prompt)

        report = Report(
            title=topic,
            executive_summary=state.thesis.main_thesis,
            sections=[content],
            sources=list({
                e.source for e in state.evidences if e.source
            }),
        )

        state.report = report
        return report