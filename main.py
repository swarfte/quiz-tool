import json

from tool.controller.BasicController import BasicController
from tool.database.JsonDatabase import JsonDatabase
from tool.model.BasicModel import BasicModel
from tool.view.BasicView import BasicView


class Main(object):
    def __init__(self) -> None:
        with open("./config/setting.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        self.__database = JsonDatabase(data["path"])
        self.__model = BasicModel(self.__database)
        self.__controller = BasicController(self.__model)
        self.__view = BasicView(self.__controller,
                                width=data["width"],
                                height=data["height"],
                                font_ratio=data["font_ratio"])
        self.__view.run()


if __name__ == "__main__":
    Main()
