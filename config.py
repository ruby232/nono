import json
import os
from logger import Logger


class Config(object):
    def __init__(self):
        self.logger = Logger()
        self.key_world = 'pedro'
        self.model_dir = None
        self.commands = None
        # Todo: pasar esto para el json
        self.voice_type = 'GTTS'
        self.voice_lang = 'es'
        self.voice_tld = 'es'
        self.load()

    def load(self):
        path = self.get_path()
        self.logger.debug("Load config from file '%s'", path)
        with open(path, 'r') as file:
            config = json.load(file)

        if "key_world" in config:
            self.key_world = config["key_world"]
        else:
            self.logger.error("Key 'key_world' not found in config")

        if "commands" in config:
            self.commands = config["commands"]
        else:
            self.logger.error("Key 'commands' not found in config")

        if "model_dir" in config:
            self.model_dir = config["model_dir"]
        else:
            self.logger.error("Key 'model_dir' not found in config")

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
