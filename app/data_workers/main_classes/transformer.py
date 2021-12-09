from abc import ABC, abstractmethod


class Transformer(ABC):

    @abstractmethod
    def delete(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def add(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def filter(self, *args, **kwargs):
        raise NotImplementedError
