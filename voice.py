from abc import ABC, abstractmethod

class Voice(ABC):
    def __init__(self, _lenguaje, _tld):
        pass

    @abstractmethod
    def say(self, text):
        pass

