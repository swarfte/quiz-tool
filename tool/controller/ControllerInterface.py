from abc import ABC, abstractmethod

from tool.model.ModelInterface import ModelInterface
from tool.observer.ObserverInterface import ObserverInterface


class ControllerInterface(ABC):
    @abstractmethod
    def initialize(self, model: ModelInterface) -> None:
        pass

    @abstractmethod
    def next(self) -> None:
        pass

    @abstractmethod
    def previous(self) -> None:
        pass

    @abstractmethod
    def first(self) -> None:
        pass

    @abstractmethod
    def last(self) -> None:
        pass

    @abstractmethod
    def find(self, location: int) -> None:
        pass

    @abstractmethod
    def reversal(self) -> None:
        pass

    @abstractmethod
    def get_card(self) -> str:
        pass

    @abstractmethod
    def get_index(self) -> int:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def check_answer(self, user_answer: str) -> bool:
        pass

    @abstractmethod
    def register_observer(self, view: ObserverInterface) -> None:
        pass

    @abstractmethod
    def remove_observer(self, view: ObserverInterface) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass
