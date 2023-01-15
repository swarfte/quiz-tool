import json

from tool.database.DatabaseInterface import DatabaseInterface


class JsonDatabase(DatabaseInterface):

    def __init__(self, path: str) -> None:
        self.__json_file: list = []
        self.initialize(path)

    def initialize(self, path: str) -> None:
        with open(path, 'r', encoding="utf-8") as file:
            self.__json_file = json.load(file)

    def get_database(self) -> list:
        return self.__json_file