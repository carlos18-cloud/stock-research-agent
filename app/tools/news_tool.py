import os
from tavily import TavilyClient

class NewsTool:
    def __init__(self, api_key: str):
        self.client = TavilyClient(api_key=api_key)

    def search_news(self, query: str, time_range: str = "week", max_results: int = 5):
        response = self.client.search(query=query, topic="news", time_range=time_range, max_results=max_results)
        return response.get("results", [])
    