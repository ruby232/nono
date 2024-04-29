import shlex
import subprocess
from threading import Event

from ..core.logger import Logger
from ..core.shared_data import SharedData
from ..voice.voice import Voice


class Command:
    """
    Class that represents a command.
    """

    def __init__(self, _name, _run, _phrases, _need_confirmation, _voice: Voice):
        self.logger = Logger()
        self.name = _name
        self.run = _run
        self.phrases = _phrases
        self.voice = _voice
        self.need_confirmation = _need_confirmation

    def get_phrases(self):
        return self.phrases

    def is_phrase(self, phrase):
        return phrase in self.phrases

    def execute(self, confirm_event: Event, shared_data: SharedData):
        """
        Executes the command.
        :param confirm_event: Event to wait, is for confirmation if is needed.
        :param shared_data: Shared data to between threats.
        """

        # The commands with confirmation waits for the user to say "si" or "no"
        if self.need_confirmation:
            # @todo:  poner los textos en el idioma configurado
            self.voice.say(f"Diga si para ejecutar, no para abortar.")
            confirm_event.clear()
            confirm_event.wait(5)
            with shared_data.lock:
                if not confirm_event.is_set() or not shared_data.confirm_result:
                    # @todo:  poner los textos en el idioma configurado
                    self.voice.say(f"Abortando comando, {self.name}.")
                    return

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
