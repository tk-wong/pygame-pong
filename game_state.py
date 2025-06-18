import abc
from abc import ABC


class GameState(ABC):
    @abc.abstractmethod
    def execute(self, game):
        raise NotImplementedError("This method should be overridden by subclasses")