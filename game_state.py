import abc
from abc import ABC


class GameState(ABC):
    @abc.abstractmethod
    def execute(self):
        raise NotImplementedError("This method should be overridden by subclasses")