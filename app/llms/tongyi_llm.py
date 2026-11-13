from openai import OpenAI
from .base import BaseLLM

class TongyiLLM(BaseLLM):
    def __init__(self, api_key: str, base_url: str, model: str):
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )
        self.model=model

    def invoke(self, system_prompt: str, user_prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.choices[0].message.content