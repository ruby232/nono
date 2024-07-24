from .command import Command
from ..core.config import Config
from ..core.logger import Logger
from ..core.nlp import NLP
from ..voice.voice import Voice


class HandlerCommand:
    """
    Handler for commands.
    """
    def __init__(self, _config: Config, _voice: Voice):
        self.voice = _voice
        self.commands = []
        self.all_phrases = []
        self.config = _config
        self.logger = Logger()
        self.nlp = None
        self.load()

    def load(self):
        """
        Loads the commands from the config.
        """
        if not self.config.commands:
            self.logger.error("Not found commands in config.")
            return

        for command_conf in self.config.commands:
            if 'name' not in command_conf:
                self.logger.error("The key 'name' not found in config.")
                continue
            name = command_conf['name']

            if 'run' not in command_conf:
                self.logger.error("The key 'run' not found in config.")
                continue
            run = command_conf['run']

            if 'phrases' not in command_conf:
                self.logger.error("The key 'phrases' not found in config.")
                continue
            phrases = command_conf['phrases']
            self.all_phrases.extend(phrases)

            command = Command(name, run, phrases, self.voice)
            self.commands.append(command)

        commands = self.get_commands()
        self.nlp = NLP(commands)

    def get_commands(self):
        return self.commands

    def execute_command(self, phrase):
        command = self.get_command(phrase)
        if command:
            command.execute()
            return True

        # @todo:  poner los textos en el idioma configurado
        self.voice.say(f"No se encontró comando para la frase, {phrase}")
        self.logger.debug("Not found command in phrase '%s'", phrase)
        return False

    def get_command(self, phrase):
        """
        Gets the command from the phrase.
        """
        for command in self.get_commands():
            if command.is_phrase(phrase):
                return command

        if self.nlp:
            return self.nlp.predict(phrase)

        return None

    def get_phrases(self):
        return self.all_phrases
