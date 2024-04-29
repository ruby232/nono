from abc import ABC, abstractmethod


class Voice(ABC):
    """
    Abstract class Text-to-speech conversion.
    """
    def __init__(self, _lenguaje, _tld):
        pass

    @abstractmethod
    def say(self, text):
        """
        Abstract method to say something.
        :param text: text to be converted to speech.
        """
        pass
