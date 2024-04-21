import logging


class Logger:
    def __init__(self):
        self.logger = self.get_logger()

    def boot(self):
        self.logger.setLevel(logging.DEBUG)

        logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

        c_handler = logging.StreamHandler()
        c_handler.setFormatter(logFormatter)
        self.logger.addHandler(c_handler)

        file_handler = logging.FileHandler("debug.log")
        file_handler.setFormatter(logFormatter)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        return logging.getLogger('nono')

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)
