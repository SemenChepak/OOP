import csv
import json
import time

from creds.PATH_holder.path_holder import PATH_OUTPUT
from logs.Logger.Loger import DataLogger


class DataWriter:
    def __init__(self):
        self._logger = DataLogger(self)

    def create_csv(self, data_frame):
        date = int(time.time())

        self._logger.info(f'Starting creating csv name:<<{date}>>')

        keys = data_frame[0].keys()

        self._logger.info(f'Headers {keys}')

        with open(f'{PATH_OUTPUT}\\csv\\cr_{date}', 'w') as f:
            dict_writer = csv.DictWriter(f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data_frame)

        self._logger.info(f'file created')

    def create_json(self, data_frame):
        date = int(time.time())

        self._logger.info(f'Starting creating csv name:<<{date}>>')

        with open(f'{PATH_OUTPUT}\\json\\cr_{date}', 'w') as f:
            json.dump(data_frame, f)

        self._logger.info(f'file created')
