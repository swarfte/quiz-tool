from abc import abstractmethod

from tool.observer.ObserverInterface import ObserverInterface


class ViewInterface(ObserverInterface):

    @abstractmethod
    def initialize(self) -> None:
        pass

    @abstractmethod
    def run(self) -> None:
        pass
