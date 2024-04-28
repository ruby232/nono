import os
from hashlib import md5
from gtts import gTTS
from playsound import playsound

from voice import Voice


class VoiceGTTS(Voice):
    def __init__(self, _lenguaje, _tld):
        super().__init__( _lenguaje, _tld)
        self.lang = _lenguaje
        self.tld = _tld

        self.voices_files = os.path.expanduser('~/.config/nono/voices')
        # Create the directory if it does not exist
        if not os.path.exists(self.voices_files):
            os.makedirs(self.voices_files)

    def say(self, text):
        text_md5 = md5(text.encode('utf-8')).hexdigest()
        voice_file = f"{self.voices_files}/{text_md5}.mp3"
        if os.path.exists(voice_file):
            self.play(voice_file)
            return

        audio = gTTS(text=text, lang=self.lang, slow=False, tld=self.tld)
        audio.save(voice_file)
        self.play(voice_file)

    def play(self, file):
        playsound(file)
