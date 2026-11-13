from tools.financial_tool import FinancialTool
from .base_node import BaseNode


class FinancialNode(BaseNode):
    def __init__(self, llm):
        self.llm = llm
        self.financial_tool = FinancialTool()

    def run(self, ticker: str) -> dict:

        return {
            "company_info": self.financial_tool.get_company_info(ticker),
            "stock_history": self.financial_tool.get_stock_quote(ticker),
        }