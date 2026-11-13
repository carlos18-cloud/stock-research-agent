from .base_node import BaseNode
import json

from models.evidence import Evidence
from prompts.evidence import SYSTEM_PROMPT

class EvidenceNode(BaseNode):
    def __init__(self, llm):
        self.llm = llm

    def run(self, state, materials=None) -> list[Evidence]:
        if materials is None:
            materials = state.search_results + state.news_results

        if not materials:
            return []

        prompt = f"""
        以下是收集到的研究资料：
        {json.dumps(materials, ensure_ascii=False)}
        {SYSTEM_PROMPT}
        """

        response = self.llm.invoke(system_prompt = prompt,user_prompt = "请根据以上资料生成研究证据。")
        data = json.loads(response)
        evidences = [Evidence(**e) for e in data]
        state.evidences.extend(evidences)
        return evidences