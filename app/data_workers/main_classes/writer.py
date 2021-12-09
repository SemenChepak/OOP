import csv
import json
import time

from creds.path_holder.path_holder import PATH_OUTPUT_CSV, PATH_OUTPUT_JSON
from logs.logger.logger import Logger


class Writer:
    def __init__(self):
        self._logger = Logger(self)

    def create_csv(self, data_frame):
        date = int(time.time())

        self._logger.info(f'Starting creating csv name:<<{date}>>')

        keys = data_frame[0].keys()

        self._logger.info(f'Headers {keys}')

        with open(f'{PATH_OUTPUT_CSV}cr_{date}', 'w', newline='') as f:
            dict_writer = csv.DictWriter(f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data_frame)

        self._logger.info(f'file created')

    def create_json(self, data_frame):
        date = int(time.time())

        self._logger.info(f'Starting creating csv name:<<{date}>>')

        with open(f'{PATH_OUTPUT_JSON}cr_{date}', 'w') as f:
            json.dump(data_frame, f)

        self._logger.info(f'file created')
