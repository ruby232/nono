import pyttsx3


class Voice():
    def __init__(self):
        self.engine = pyttsx3.init()
        voice_id = 'spanish'  # Or, 'spanish-latin-am'
        self.engine.setProperty('voice', voice_id)
        self.engine.setProperty('rate', 120)
        self.engine.setProperty('voice', 'spanish')
        self.engine.setProperty('volume', 1)

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()