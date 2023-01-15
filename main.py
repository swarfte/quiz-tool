import json

from tool.controller.BasicController import BasicController
from tool.database.JsonDatabase import JsonDatabase
from tool.model.BasicModel import BasicModel
from tool.view.BasicView import BasicView


class Main(object):
    def __init__(self) -> None:
        with open("./config/setting.json", "r", encoding="utf-8") as f:
            path = json.load(f)["path"]
        self.__database = JsonDatabase(path)
        self.__model = BasicModel(self.__database)
        self.__controller = BasicController(self.__model)
        self.__view = BasicView(self.__controller)
        self.__view.run()


if __name__ == "__main__":
    Main()
