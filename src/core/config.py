import json
from .logger import Logger
from .utils import get_config_file_path


class Config(object):
    """
    Class to manage the configuration of the application.
    """

    def __init__(self):
        self.continue_word = None
        self.pause_word = None
        self.logger = Logger()
        self.key_world = 'wendy'
        self.model_dir = None
        self.commands = None
        self.voice_type = 'GTTS'
        self.voice_lang = 'es'
        self.voice_tld = 'es'
        self.extra_gramma = []
        self.load()

    def load(self):
        """
        Load the configuration from a JSON file.
        """
        path = get_config_file_path()
        self.logger.debug("Load config from file '%s'", path)
        with open(path, 'r') as file:
            config = json.load(file)
        self.key_world = config.get("key_world")

        if self.key_world is None:
            self.logger.error("Key 'key_world' not found in config")

        self.commands = config.get("commands")
        if self.commands is None:
            self.logger.error("Key 'commands' not found in config")

        self.model_dir = config.get("model_dir")
        if self.model_dir is None:
            self.logger.error("Key 'model_dir' not found in config")

        self.voice_type = config.get("voice_type", 'GTTS')
        self.voice_lang = config.get("voice_lang", 'es')
        self.voice_tld = config.get("voice_tld", 'es')
        self.extra_gramma = config.get("extra_gramma", [])
        self.pause_word = config.get("pause_word", "pausa")
        self.continue_word = config.get("continue_word", "continua")
