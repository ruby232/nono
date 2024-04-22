from abc import abstractmethod


class Command:
    @abstractmethod
    def get_phrases(self):
        pass

    @abstractmethod
    def execute(self):
        pass
