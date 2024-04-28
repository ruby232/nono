import shlex
import subprocess

# from listener_confirmation import ListenerConfirmation
from logger import Logger
from voice import Voice

class Command:
    def __init__(self, _name, _run, _phrases, _voice: Voice):
        self.logger = Logger()
        self.name = _name
        self.run = _run
        self.phrases = _phrases
        self.voice = _voice
        # self.listenerConfirmation = ListenerConfirmation()

    def get_phrases(self):
        return self.phrases

    def is_phrase(self, phrase):
        return phrase in self.phrases

    def need_confirmation(self):
        return True

    def execute(self):
        if self.need_confirmation():
            self.voice.say(f"Esta seguro que desea ejecutar, {self.name}.")
        #     if not self.listenerConfirmation.confirmation():
        #         self.voice.say(f"Abortando comando, {self.name}.")
        try:
            args = shlex.split(self.run)
            subprocess.Popen(args,
                             stdout=open('/dev/null', 'w'),
                             stderr=open('/dev/null', 'w'),
                             start_new_session=True)
        except:
            self.logger.debug("Error trying to execute the command: '%s'", self.run)
            self.voice.say(f"Falló al intentar ejecutar el comando, {self.run}.")
