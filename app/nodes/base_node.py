from abc import ABC, abstractmethod

class BaseNode(ABC):

    @abstractmethod
    def run(self, *args, **kwargs):
        pass