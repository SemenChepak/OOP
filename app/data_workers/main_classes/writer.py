import csv
import json
import time

from creds.PATH_holder.path_holder import PATH_OUTPUT


class DataWriter:

    def create_csv(self, data_frame):
        keys = data_frame[0].keys()
        with open(f'{PATH_OUTPUT}\\csv\\cr_{int(time.time())}', 'w') as f:
            dict_writer = csv.DictWriter(f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data_frame)

    def create_json(self, data_frame):
        with open(f'{PATH_OUTPUT}\\json\\cr_{int(time.time())}', 'w') as f:
            json.dump(data_frame, f)
