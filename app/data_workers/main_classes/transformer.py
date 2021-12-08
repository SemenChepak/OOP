from abc import ABC, abstractmethod


class DataTransformer(ABC):

    @abstractmethod
    def delete_duplicate(self):
        raise NotImplementedError

    @abstractmethod
    def add_column(self):
        raise NotImplementedError

    @abstractmethod
    def filter_by(self):
        raise NotImplementedError

    @abstractmethod
    def show(self):
        raise NotImplementedError

