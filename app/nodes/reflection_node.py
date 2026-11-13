import json

from .base_node import BaseNode
from prompts.reflection import SYSTEM_PROMPT

class ReflectionNode(BaseNode):
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

        当前研究证据：

        {json.dumps(evidences, ensure_ascii=False)}

        当前分析结果：

        {json.dumps(analyses, ensure_ascii=False)}

        当前反思次数：

        {state.reflection_count}

        {SYSTEM_PROMPT}
        """

        response = self.llm.invoke(system_prompt=prompt,user_prompt="请根据以上要求，返回结果。")
        data = json.loads(response)

        if not isinstance(data.get("need_reflection"), bool):
            raise ValueError("need_reflection 必须是布尔值")

        if data["need_reflection"] and not data.get("reflection_query"):
            raise ValueError("需要继续研究时，reflection_query 不能为空")

        return {
            "need_reflection": data["need_reflection"],
            "reflection_query": data.get("reflection_query", ""),
            "reason": data.get("reason", ""),
        }