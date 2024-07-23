from src.core.listener_voice import ListenerVoice
from src.core.logger import Logger

logger = Logger()
logger.boot()

listener_voice = ListenerVoice()
listener_voice.listen()

