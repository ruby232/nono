from vosk import Model, KaldiRecognizer
import pyaudio

import json
from threading import Event, Thread

from .logger import Logger
from .utils import clear_string
from ..command.handler_command import HandlerCommand
from .shared_data import SharedData
from .config import Config
from ..voice.voice import Voice
from ..voice.voice_factory import VoiceFactory


class ListenerVoice:
    """
    Class for listening the voice and process commands.

    It uses the Vosk library.
    """

    def __init__(self, _shared_data: SharedData):
        self.shared_data = _shared_data
        self.config: Config = Config()

        self.stream = None
        self.recognizer = None
        self.model_dir = self.config.model_dir
        self.texts_queue = []
        self.voice: Voice = VoiceFactory.create_voice(self.config)
        self.handler_command = HandlerCommand(self.config, self.voice)
        self.logger = Logger()

        self.grammar = [self.config.key_world, "[unk]"]
        self.grammar.extend(self.config.extra_gramma)
        self.grammar.extend([self.config.conform_word, self.config.abort_word])

        self.confirm_event = Event()

    def start(self):
        """
        Start listening the voice.
        """
        model = Model(self.model_dir)
        phrases = self.handler_command.get_phrases()
        self.grammar.extend(phrases)

        grammar_str = json.dumps(self.grammar)
        self.recognizer = KaldiRecognizer(model, 16000, grammar_str)
        mic = pyaudio.PyAudio()
        self.stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        self.stream.start_stream()

    def listen(self):
        """
        Listen the voice and process commands.
        """
        if self.stream is None:
            self.start()

        while True:
            data = self.stream.read(4096)
            if self.recognizer.AcceptWaveform(data):
                json_str = self.recognizer.FinalResult()
                json_text = json.loads(json_str)
                text = json_text.get("text")
                if not text:
                    continue

                self.logger.debug("Text recognizer: %s", text)

                # This is for the commands with confirmation.
                if text in [self.config.conform_word, self.config.conform_word]:
                    with self.shared_data.lock:
                        self.shared_data.confirm_result = text == self.config.conform_word
                    self.confirm_event.set()
                    continue

                # Need execute this in a thread for listen confirmation.
                process_thread = Thread(target=self.process_sentence, args=(text, self.confirm_event,))
                process_thread.start()

    def process_sentence(self, sentence: str, confirm_event: Event):
        """
        Processing the sentence and which command to execute.
        """

        self.logger.debug("Input text for user: %s", sentence)
        clear_sentence = clear_string(sentence)
        if not self.is_command(clear_sentence):
            return

        command = self.extract_command(clear_sentence)
        if not command or command in [self.config.conform_word, self.config.conform_word]:
            return
        self.logger.debug("Extract command: %s", command)
        self.handler_command.execute_command(command, confirm_event, self.shared_data)

    def is_command(self, sentence):
        """
        Check if the sentence is a command.
        """
        return self.config.key_world in sentence

    def extract_command(self, sentence):
        """
        Extract the command from the sentence.
        """
        sub_strings = sentence.split(self.config.key_world)
        if len(sub_strings) <= 1:
            return None

        return sub_strings[1].strip()
