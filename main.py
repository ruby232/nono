from config import Config
from listener_voice import ListenerVoice
from logger import Logger
from shared_data import SharedData

confirm_result = None
logger = Logger()
config = Config()
logger.boot()
shared_data = SharedData()

model_dir = config.model_dir
listener_voice = ListenerVoice(model_dir, config, shared_data)
listener_voice.listen()

