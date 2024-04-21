from abc import abstractmethod


class Command:
    @abstractmethod
    def get_phrase(self):
        pass

    @abstractmethod
    def execute(self):
        pass
