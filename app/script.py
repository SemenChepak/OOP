import time

from data_workers.main_classes.extractor import DataExtractor
from data_workers.main_classes.transformer import DataTransformer
from data_workers.main_classes.writer import DataWriter


class DataTrans(DataTransformer):
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


class BatiaOfData(DataWriter, DataExtractor, DataTrans):
    def __init__(self):
        super(DataWriter, self).__init__()
        super(DataExtractor, self).__init__()
        super(DataTrans, self).__init__()


if __name__ == '__main__':
    batia = BatiaOfData()
    # executor
    df = batia.get_data('cards', 10)
    # writer
    batia.create_json(df)
    batia.create_csv(df)
    # worker
    a = batia.filter(data_frame=df, key='card_no', value='1406169918986365')
    b = batia.delete(data_frame=df, key='card_no', value='1406169918986365')
    df = batia.add(df, 'created_at', time.time())
    batia.create_json(df)
    batia.create_csv(df)
