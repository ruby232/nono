import json
import os
import re
import unicodedata


def get_config_file_path():
    """
    Get the path to the configuration file.
    """
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


def clear_string(sentence):
    """
    Clear the string from special characters and spaces.
    """
    clear = re.sub(r'\s+', ' ', sentence)
    clear = ''.join((c for c in unicodedata.normalize('NFD', clear) if unicodedata.category(c) != 'Mn'))

    clear = re.sub(r'[^a-zA-Z\s]', '', clear)
    clear = clear.lower()
    return clear
