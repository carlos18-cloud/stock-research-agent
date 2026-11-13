import json

from .base_node import BaseNode
from llms.base import BaseLLM
from models.research_question import ResearchQuestion
from models.topic import Topic
from prompts.planning import SYSTEM_PROMPT

class ResearchPlanningNode(BaseNode):
    def __init__(self, llm: BaseLLM):
        self.llm = llm

    def run(self, topic: Topic) -> list[ResearchQuestion]:
        prompt = f"""
        用户提供的候选研究主题：{topic.title}
        主题描述：{topic.description}
        {SYSTEM_PROMPT}
        """
        response = self.llm.invoke(prompt, user_prompt="请按照json格式返回结果")
        data = json.loads(response)

        return [
            ResearchQuestion(
                question=item["question"],
                dimension=item.get("dimension", ""),
                priority=item.get("priority", 0),
            )
            for item in data
        ]