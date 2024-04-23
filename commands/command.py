import subprocess


class Command:
    def __init__(self, _name, _run, _phrases):
        self.name = _name
        self.run = _run
        self.phrases = _phrases

    def get_phrases(self):
        return self.phrases

    def is_phrase(self, phrase):
        # @todo, esto hay que mejorarlo
        return phrase in self.phrases


    def execute(self):
        proceso = subprocess.Popen(self.run)