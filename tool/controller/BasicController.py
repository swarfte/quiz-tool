from tool.controller.ControllerInterface import ControllerInterface
from tool.model.ModelInterface import ModelInterface
from tool.observer.ObserverInterface import ObserverInterface


class BasicController(ControllerInterface):
    def __init__(self, model: ModelInterface) -> None:
        self.__model: ModelInterface = None
        self.initialize(model)

    def initialize(self, model: ModelInterface) -> None:
        self.__model = model

    def next(self) -> None:
        self.__model.set_location(self.__model.get_location() + 1)
        self.__model.notify_observers()

    def previous(self) -> None:
        self.__model.set_location(self.__model.get_location() - 1)
        self.__model.notify_observers()

    def first(self) -> None:
        self.__model.set_location(0)
        self.__model.notify_observers()

    def last(self) -> None:
        self.__model.set_location(self.__model.get_size() - 1)
        self.__model.notify_observers()

    def find(self, location: int) -> None:
        self.__model.location = location
        self.__model.notify_observers()

    def reversal(self) -> None:
        self.__model.reversal_state()
        self.__model.notify_observers()

    def get_card(self) -> str:
        if self.__model.get_state():
            return self.__model.get_back(self.__model.get_location())
        else:
            return self.__model.get_front(self.__model.get_location())

    def check_answer(self, user_answer: str) -> bool:
        return self.__model.check_answer(self.__model.get_location(), user_answer)

    def get_index(self) -> int:
        return self.__model.get_location()

    def get_size(self) -> int:
        return self.__model.get_size()

    def register_observer(self, view: ObserverInterface) -> None:
        self.__model.register_observer(view)

    def remove_observer(self, view: ObserverInterface) -> None:
        self.__model.remove_observer(view)

    def notify_observers(self) -> None:
        self.__model.notify_observers()
