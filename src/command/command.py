import shlex
import subprocess

from ..core.logger import Logger
from ..voice.voice import Voice


class Command:
    """
    Class that represents a command.
    """

    def __init__(self, _name, _run, _phrases, _voice: Voice):
        self.logger = Logger()
        self.name = _name
        self.run = _run
        self.phrases = _phrases
        self.voice = _voice

    def get_phrases(self):
        return self.phrases

    def is_phrase(self, phrase):
        return phrase in self.phrases

    def execute(self):
        """
        Executes the command.
        """

        # @todo:  poner los textos en el idioma configurado
        self.voice.say(f"Ejecutando, {self.name}.")
        try:
            args = shlex.split(self.run)
            subprocess.Popen(args,
                             stdout=open('/dev/null', 'w'),
                             stderr=open('/dev/null', 'w'),
                             start_new_session=True)
        except:
            self.logger.debug("Error trying to execute the command: '%s'", self.run)
            # @todo:  poner los textos en el idioma configurado
            self.voice.say(f"Falló al intentar ejecutar el comando, {self.run}.")
