from command import Command
from config import Config
from logger import Logger


class HandlerCommand:
    def __init__(self, _config: Config):
        self.commands = []
        self.all_phrases = []
        self.config = _config
        self.logger = Logger()
        self.load()

    def load(self):
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

            command = Command(name, run, phrases)
            self.commands.append(command)

    def get_commands(self):
        return self.commands

    def execute_command(self, phrase):
        command = self.get_command(phrase)
        if command:
            command.execute()
            return True
        self.logger.debug("Not found command in phrase '%s'", phrase)
        return False

    def get_command(self, phrase):
        for command in self.get_commands():
            if command.is_phrase(phrase):
                return command
        return None

    def get_phrases(self):
        return self.all_phrases
