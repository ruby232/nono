import os
from hashlib import md5
from gtts import gTTS
from playsound import playsound

from .voice import Voice


class VoiceGTTS(Voice):
    """
    Class to generate and play text-to-speech audio using the gTTS library.
    """
    def __init__(self, _language, _tld):
        super().__init__(_language, _tld)
        self.lang = _language
        self.tld = _tld

        self.voices_files = os.path.expanduser('~/.config/nono/voices')
        # Create the directory if it does not exist
        if not os.path.exists(self.voices_files):
            os.makedirs(self.voices_files)

    def say(self, text):
        """
        Generate and play the audio for the given text.
        gtts does not allow direct text playback, so the audios are generated once and loaded if already generated.
        """
        text_md5 = md5(text.encode('utf-8')).hexdigest()
        voice_file = f"{self.voices_files}/{text_md5}.mp3"
        if os.path.exists(voice_file):
            self.play(voice_file)
            return

        audio = gTTS(text=text, lang=self.lang, slow=False, tld=self.tld)
        audio.save(voice_file)
        self.play(voice_file)

    def play(self, file):
        """
        Play the audio file.
        There are several ways to play audios, this is the simplest one I saw.
        """
        playsound(file)
