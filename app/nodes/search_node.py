from .base_node import BaseNode
from llms.base import BaseLLM
from tools.search_tool import SearchTool

class SearchNode(BaseNode):
    def __init__(self, llm: BaseLLM):
        self.llm = llm
        self.search_tool = SearchTool()

    def run(self, state) -> list[dict]:
        question = state.question
        system_prompt = f"""
        你是一个股票研究助手，帮助用户进行股票研究。
        研究的问题：{question}
        只需要你返回一句Query，不要解释，字数最大限制1500字。
        """

        query = self.llm.invoke(system_prompt, user_prompt="请生成一个搜索Query")
        results = self.search_tool.search(query)
        state.search_results.extend(results)
        return results