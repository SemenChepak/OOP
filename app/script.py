import time

from data_workers.main_classes.extractor import Extractor
from data_workers.main_classes.transformer import Transformer
from data_workers.main_classes.writer import Writer


class Trans(Transformer):
    def __init__(self):
        pass

    def filter(self, data_frame, key, value):
        new_df = []
        for row in data_frame:
            if row[key] == value:
                new_df.append(row)
        return new_df

    def delete(self, data_frame, key, value):
        new_df = []
        for row in data_frame:
            if row[key] != value:
                new_df.append(row)
        return new_df

    def add(self, data_frame, key, value):
        for row in data_frame:
            row[key] = value
        return data_frame


class Batia:
    def __init__(self):
        self.writer = Writer()
        self.extractor = Extractor()
        self.trans = Trans()

if __name__ == '__main__':
    batia = Batia()
    # executor
    df = batia.extractor.get_data_msq('cards', 10)
    # writer
    batia.writer.create_json(df)
    batia.writer.create_csv(df)
    # worker
    a = batia.trans.filter(data_frame=df, key='card_no', value='1406169918986365')
    b = batia.trans.delete(data_frame=df, key='card_no', value='1406169918986365')
    df = batia.trans.add(df, 'created_at', time.time())
    batia.writer.create_json(df)
    batia.writer.create_csv(df)
