import json
import os
from logger import Logger


class Config(object):
    def __init__(self):
        self.logger = Logger()
        self.key_world = 'wendy'
        self.model_dir = None
        self.commands = None
        self.voice_type = 'GTTS'
        self.voice_lang = 'es'
        self.voice_tld = 'es'
        self.extra_gramma = []
        self.abort_word = None
        self.conform_word = None
        self.load()

    def load(self):
        path = self.get_path()
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
        self.conform_word = config.get("conform_word", "si")
        self.abort_word = config.get("abort_word", "no")
        self.extra_gramma = config.get("extra_gramma", [])

    def get_path(self):
        config_dir = os.path.expanduser('~/.config/nono')
        # Create the directory if it does not exist
        if not os.path.exists(config_dir):
            os.makedirs(config_dir)

        config_file = os.path.join(config_dir, 'config.json')

        if not os.path.exists(config_file):
            # If the file does not exist, create a sample configuration file
            default_config = {
                'model_dir': '~/.config/nono/model',
                'key_world': 'pedro',
                'commands': [
                    {
                        'name': 'brave',
                        'run': 'brave-browser',
                        'phrases': [
                            'ejecutar navegador',
                            'abrir navegador'
                        ]
                    }
                ]
            }
            with open(config_file, 'w') as file:
                json.dump(default_config, file, indent=4)
        return config_file
