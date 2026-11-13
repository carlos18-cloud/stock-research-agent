import json
from .base_node import BaseNode
from llms.base import BaseLLM
from models.topic import Topic
from prompts.topic_discovery import SYSTEM_PROMPT

class TopicDiscoveryNode(BaseNode):
    def __init__(self, llm: BaseLLM):
        self.llm = llm

    def run(self, focus_areas: list[str]) -> list[Topic]:
        prompt = f"""
        用户长期关注的领域：{",".join(focus_areas)}
        请发现5个近期值得深入研究的候选主题
        {SYSTEM_PROMPT}
        """
        response = self.llm.invoke(prompt,user_prompt="请按照json格式返回结果")
        data = json.loads(response)

        return [
            Topic(
                title=item["title"],
                description=item.get("description", ""),
                trend_score=item.get("trend_score", 0),
                importance_score=item.get(
                    "importance_score", 0
                ),
                novelty_score=item.get(
                    "novelty_score", 0
                ),
                research_potential_score=item.get(
                    "research_potential_score", 0
                ),
            )
            for item in data
        ]

