from config import Config
from listener_voice import ListenerVoice
from logger import Logger

logger = Logger()
config = Config()
logger.boot()

model_dir = config.model_dir
listener_voice = ListenerVoice(model_dir, config)
listener_voice.listen()

