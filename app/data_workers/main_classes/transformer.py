from abc import ABC, abstractmethod


class DataTransformer(ABC):

    @abstractmethod
    def delete(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def add(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def filter(self, *args, **kwargs):
        raise NotImplementedError
