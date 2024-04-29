from src.core.listener_voice import ListenerVoice
from src.core.logger import Logger
from src.core.shared_data import SharedData

logger = Logger()
logger.boot()

# This is the shared data object between thread, used for confirmation and arguments in the future.
shared_data = SharedData()

listener_voice = ListenerVoice(shared_data)
listener_voice.listen()

