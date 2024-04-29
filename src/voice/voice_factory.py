from ..core.config import Config
from .voice_gtts import VoiceGTTS
from .voice_ttsx3 import VoiceTTSX3


class VoiceFactory:
    """
    Factory for creating voice objects,  based on the configuration.
    """
    @staticmethod
    def create_voice(config: Config):
        """
        :param config: Configuration object.
        :return: Voice Object
        """

        voice_type = config.voice_type
        language = config.voice_lang
        tld = config.voice_tld
        if voice_type == 'TTSX3':
            return VoiceTTSX3(language, tld)

        if voice_type == 'GTTS':
            return VoiceGTTS(language, tld)

        raise ValueError("Invalid type of voice")