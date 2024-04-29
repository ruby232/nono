import logging


class Logger:
    """
    Logger class for nono
    """
    def __init__(self):
        self.logger = logging.getLogger('nono')

    def boot(self):
        self.logger.setLevel(logging.DEBUG)

        log_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

        c_handler = logging.StreamHandler()
        c_handler.setFormatter(log_formatter)
        self.logger.addHandler(c_handler)

        # Todo:  change to debug.log path
        file_handler = logging.FileHandler("../../debug.log")
        file_handler.setFormatter(log_formatter)
        self.logger.addHandler(file_handler)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)
