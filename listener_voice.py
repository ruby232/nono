from vosk import Model, KaldiRecognizer
import pyaudio
import re
import unicodedata

from config import Config
from logger import Logger
from handler_command import HandlerCommand
import json

from shared_data import SharedData
from voice import Voice
from threading import Event, Thread


class ListenerVoice:

    def __init__(self, model_dir: str, _config: Config, _shared_data: SharedData):
        self.shared_data = _shared_data
        self.config = _config
        self.stream = None
        self.recognizer = None
        self.model_dir = model_dir
        self.texts_queue = []
        self.voice = Voice()
        self.handler_command = HandlerCommand(_config, self.voice)
        self.logger = Logger()
        self.grammar = [self.config.key_world, "si", "no", "[unk]"]
        self.process_thread = None
        self.confirm_event = Event()

    def start_listening(self):
        self.process_thread = Thread(target=self.listen)
        self.process_thread.start()

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

                # Esto es para los comandos con confirmacion
                if text == "si" or text == "no":
                    with self.shared_data.lock:
                        self.shared_data.confirm_result = text == "si"
                    self.confirm_event.set()
                    continue

                process_thread = Thread(target=self.process_sentence, args=(text, self.confirm_event, ))
                process_thread.start()

    def process_sentence(self, sentence: str, confirm_event: Event):
        self.logger.debug("Input text for user: %s", sentence)

        clear_sentence = self.clear_string(sentence)
        if not self.is_command(clear_sentence):
            return

        command = self.extract_command(clear_sentence)
        if command:
            self.logger.debug("Extract command: %s", command)
            self.handler_command.execute_command(command, confirm_event, self.shared_data)
            return

    def clear_string(self, sentence):
        clear = re.sub(r'\s+', ' ', sentence)
        clear = ''.join((c for c in unicodedata.normalize('NFD', clear) if unicodedata.category(c) != 'Mn'))

        clear = re.sub(r'[^a-zA-Z\s]', '', clear)
        clear = clear.lower()
        return clear

    def is_command(self, sentence):
        return self.config.key_world in sentence

    def extract_command(self, sentence):
        sub_strings = sentence.split(self.config.key_world)
        if len(sub_strings) <= 1:
            return None

        return sub_strings[1].strip()

    def add_gram(self, extra):
        for phrase in extra:
            self.grammar.append(f"{self.config.key_world} {phrase}")