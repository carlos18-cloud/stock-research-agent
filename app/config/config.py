import os

from dotenv import load_dotenv

load_dotenv()

TONGYI_API_KEY = os.getenv("TONGYI_API_KEY")
TONGYI_BASE_URL = os.getenv("TONGYI_BASE_URL")
TONGYI_MODEL = os.getenv("TONGYI_MODEL")

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")