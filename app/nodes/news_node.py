from .base_node import BaseNode
from llms.base import BaseLLM
from tools.news_tool import NewsTool
from config.config import TAVILY_API_KEY

class NewsNode(BaseNode):
    def __init__(self, llm: BaseLLM):
        self.llm = llm
        self.news_tool = NewsTool(api_key=TAVILY_API_KEY)

    def run(self, state) -> list[dict]:
        results = self.news_tool.search_news(query=state.question, time_range="week")
        state.news_results.extend(results)
        return results
        
