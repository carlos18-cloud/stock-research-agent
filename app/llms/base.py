from abc import ABC, abstractmethod

class BaseLLM(ABC):

    @abstractmethod
    def invoke(self, system_prompt: str, user_prompt: str) -> str:
        """
        Invoke the LLM with the given system and user prompts.
        """
        pass