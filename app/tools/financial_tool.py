import os
import requests
from config.config import FINNHUB_API_KEY


class FinancialTool:

    BASE_URL = "https://finnhub.io/api/v1"

    def __init__(self):
        self.api_key = FINNHUB_API_KEY

        if not self.api_key:
            raise ValueError("缺少 FINNHUB_API_KEY")

        self.session = requests.Session()

    def _request(self, endpoint: str, params: dict) -> dict:

        params["token"] = self.api_key

        response = self.session.get(
            f"{self.BASE_URL}/{endpoint}",
            params=params,
            timeout=15,
        )

        response.raise_for_status()

        data = response.json()

        if isinstance(data, dict) and data.get("error"):
            raise RuntimeError(data["error"])

        return data

    def get_company_info(self, ticker: str) -> dict:

        return self._request(
            "stock/profile2",
            {"symbol": ticker},
        )

    def get_stock_quote(self, ticker: str) -> dict:

        return self._request(
            "quote",
            {"symbol": ticker},
        )