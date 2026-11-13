import json

from .base_node import BaseNode
from prompts.analysis import SYSTEM_PROMPT
from models.analysis import Analysis
from models.evidence import Evidence

class AnalysisNode(BaseNode):
    def __init__(self, llm):
        self.llm = llm

    def run(self, state):
        topic = (
            state.topic.title
            if state.topic
            else state.question
        )

        evidences = state.evidences

        if not evidences:
            raise ValueError("没有 Evidence，无法进行分析")

        materialss = [{
            "claim": e.claim,
            "content": e.content,
            "source": e.source,
            "source_type": e.source_type,
            "credibility": e.credibility,
        } for e in evidences]

        prompt = f"""
        研究主题：{topic}
        研究证据：{json.dumps(materialss, ensure_ascii=False)}
        {SYSTEM_PROMPT}
        """
        response = self.llm.invoke(system_prompt=prompt,user_prompt="请根据以上要求回复我")
        data = json.loads(response)
        analysis = Analysis(
            topic=topic,
            conclusion=data["conclusion"],
            supporting_evidence=data["supporting_evidence"],
            confidence=float(data["confidence"]),
        )

        state.analyses.append(analysis)

        return analysis