from vosk import Model, KaldiRecognizer
import pyaudio
import re
import unicodedata

from logger import Logger
from handler_command import HandlerCommand
import json

key_world = 'pedro'


class ListenerVoice:

    def __init__(self, model_dir):
        self.stream = None
        self.recognizer = None
        self.model_dir = model_dir
        self.texts_queue = []
        self.handler_command = HandlerCommand()
        self.logger = Logger()
        self.grammar = [key_world, "[unk]"]

    def start(self):
        model = Model(self.model_dir)
        extra_gramma = self.handler_command.get_phrases()
        self.add_gram(extra_gramma)

        grammar_str = json.dumps(self.grammar)
        self.recognizer = KaldiRecognizer(model, 16000, grammar_str)
        mic = pyaudio.PyAudio()
        self.stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        self.stream.start_stream()

    def listen(self):
        if self.stream is None:
            self.start()

        while True:
            data = self.stream.read(4096)
            if self.recognizer.AcceptWaveform(data):
                json_text = self.recognizer.FinalResult()
                self.logger.debug("Text recognizer: %s", json_text)
                text = f"{json_text[14:-3]}"
                if not text:
                    continue
                self.process_sentence(text)

    def process_sentence(self, sentence):
        self.logger.debug("Input text for user: %s", sentence)

        clear_sentence = self.clear_string(sentence)
        if not self.is_command(clear_sentence):
            return

        command = self.extract_command(clear_sentence)
        if command:
            self.logger.debug("Extract command: %s", command)
            self.handler_command.execute_command(command)

    def clear_string(self, sentence):
        clear = re.sub(r'\s+', ' ', sentence)
        clear = ''.join((c for c in unicodedata.normalize('NFD', clear) if unicodedata.category(c) != 'Mn'))

        clear = re.sub(r'[^a-zA-Z\s]', '', clear)
        clear = clear.lower()
        return clear

    def is_command(self, sentence):
        return key_world in sentence

    def extract_command(self, sentence):
        sub_strings = sentence.split(key_world)
        if len(sub_strings) <= 1:
            return None

        return sub_strings[1].strip()

    def add_gram(self, extra):
        for phrase in extra:
            self.grammar.append(f"{key_world} {phrase}")