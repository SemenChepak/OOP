import logging
import getpass
from creds.PATH_holder.path_holder import PATH_LOGS

logging.basicConfig(filename=f"{PATH_LOGS}\\logs",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S', )


class DataLogger(object):
    def __init__(self, name):
        self.filename = f"{PATH_LOGS}\\logs",
        self.filemode = 'a'
        self.format = '%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s'
        self.level = logging.INFO
        self.datefmt = '%H:%M:%S'
        self.logger = logging.getLogger(getpass.getuser())
        self.logger.setLevel(self.level)
        self.name = name

    def info(self, msg, extra=None):
        self.logger.info(f'{self.name} {msg}', extra=extra)

    def error(self, msg, extra=None):
        self.logger.error(f'{self.name} {msg}', extra=extra)

    def debug(self, msg, extra=None):
        self.logger.debug(f'{self.name} {msg}', extra=extra)

    def warn(self, msg, extra=None):
        self.logger.warning(f'{self.name} {msg}', extra=extra)

