import logging
from colorlog import ColoredFormatter

LOG_LEVEL = logging.DEBUG
LOGFORMAT = "%(log_color)s%(levelname)s%(reset)s:     %(log_color)4s%(message)s%(reset)s"

logging.root.setLevel(LOG_LEVEL)
formatter = ColoredFormatter(LOGFORMAT)

stream = logging.StreamHandler()
stream.setLevel(LOG_LEVEL)
stream.setFormatter(formatter)

log = logging.getLogger('pythonConfig')
log.setLevel(LOG_LEVEL)
log.addHandler(stream)


class Log:
    log = log

    @classmethod
    def debug(cls, message=None, e=None):
        cls.log.debug(message)

    @classmethod
    def info(cls, message=None, e=None):
        cls.log.info(message)

    @classmethod
    def warn(cls, message=None, e=None):
        cls.log.warn(message)

    @classmethod
    def error(cls, message=None, e=None):
        cls.log.error(message)

    @classmethod
    def critical(cls, message=None, e=None):

        cls.log.critical(message)
