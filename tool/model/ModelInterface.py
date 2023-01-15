from abc import ABC, abstractmethod

import tool.database.DatabaseInterface as DatabaseInterface
import tool.observer.ObserverInterface as ObserverInterface


class ModelInterface(ABC):
    @abstractmethod
    def initialize(self, database: DatabaseInterface) -> None:
        pass

    @abstractmethod
    def get_front(self, location: int) -> str:
        pass

    @abstractmethod
    def get_back(self, location: int) -> str:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def get_location(self) -> int:
        pass

    @abstractmethod
    def set_location(self, location: int) -> None:
        pass

    @abstractmethod
    def get_all_fronts(self) -> list:
        pass

    @abstractmethod
    def get_all_backs(self) -> list:
        pass

    @abstractmethod
    def get_state(self) -> bool:
        pass

    @abstractmethod
    def reversal_state(self) -> None:
        pass

    @abstractmethod
    def check_answer(self, location: int, user_answer: str) -> bool:
        pass

    @abstractmethod
    def register_observer(self, observer: ObserverInterface) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: ObserverInterface) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass
