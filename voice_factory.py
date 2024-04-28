from config import Config
from voice_gtts import VoiceGTTS
from voice_ttsx3 import VoiceTTSX3


class VoiceFactory:
    @staticmethod
    def create_voice(config: Config):
        type = config.voice_type
        language = config.voice_lang
        tld = config.voice_tld
        if type == 'TTSX3':
            return VoiceTTSX3(language, tld)
        elif type == 'GTTS':
            return VoiceGTTS(language, tld)

        else:
            raise ValueError("Invalid type of voice")