from abc import ABC, abstractmethod


class DatabaseInterface(ABC):
    @abstractmethod
    def initialize(self, path: str) -> None:
        pass

    @abstractmethod
    def get_database(self) -> dict|list:
        pass
