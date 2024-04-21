from listener_voice import ListenerVoice
from logger import Logger

logger = Logger()
logger.boot()

model_dir = r"/home/natsu/Proyectos/onebyt/learnings/python/nono/vosk-models/vosk-model-small-es-0.42"
listener_voice = ListenerVoice(model_dir)
listener_voice.listen()

