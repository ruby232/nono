import os
import importlib
import inspect

from commands.command import Command
from logger import Logger


class HandlerCommand:
    def __init__(self):
        self.logger = Logger()
        self.commands = []
        self.load_commands()

    def get_commands(self):
        return self.commands

    def load_commands(self):
        commands_folder = "commands"
        for file in os.listdir(commands_folder):
            if not file.endswith('.py') or file == '__init__.py':
                continue

            module = importlib.import_module(f'{commands_folder}.{file[:-3]}')
            for name, command_class in inspect.getmembers(module):
                if inspect.isclass(command_class) and issubclass(command_class, Command) and command_class != Command:
                    self.commands.append(command_class())

    def execute_command(self, phrase):
        command = self.get_command(phrase)
        if command:
            command.execute()
            return True
        self.logger.debug("Not found command in phrase '%s'", phrase)
        return False

    def get_command(self, phrase):
        for command in self.commands:
            phrases = command.get_phrases()
            if phrase in phrases:
                return command
        return None

    def get_phrases(self):
        phrases = []
        for command in self.commands:
            phrases.extend(command.get_phrases())
        return phrases
