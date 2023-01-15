from tool.database.DatabaseInterface import DatabaseInterface
from tool.model.ModelInterface import ModelInterface
from tool.observer.ObserverInterface import ObserverInterface


class BasicModel(ModelInterface):
    def __init__(self, database: DatabaseInterface) -> None:
        self.__location: int = 0
        self.__database: list = []
        self.__observers: list = []
        self.__is_reversal: bool = False
        self.initialize(database)

    def initialize(self, database: DatabaseInterface) -> None:
        self.__database = database.get_database()

    def get_front(self, location: int) -> str:
        return self.__database[location]['front']

    def get_back(self, location: int) -> str:
        return self.__database[location]['back']

    def get_size(self) -> int:
        return len(self.__database)

    def get_location(self) -> int:
        return self.__location

    def set_location(self, location: int) -> None:
        if 0 <= location < self.get_size():
            self.__location = location
            self.notify_observers()

    def get_all_fronts(self) -> list:
        return [self.get_front(i) for i in range(self.get_size())]

    def get_all_backs(self) -> list:
        return [self.get_back(i) for i in range(self.get_size())]

    def check_answer(self, location: int, user_answer: str) -> bool:
        if self.__is_reversal:
            return self.get_front(location).lower() == user_answer.lower()
        else:
            return self.get_back(location).lower() == user_answer.lower()

    def get_state(self) -> bool:
        return self.__is_reversal

    def reversal_state(self) -> None:
        self.__is_reversal = not self.__is_reversal

    def register_observer(self, observer: ObserverInterface) -> None:
        self.__observers.append(observer)

    def remove_observer(self, observer: ObserverInterface) -> None:
        self.__observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self.__observers:
            observer.update()
