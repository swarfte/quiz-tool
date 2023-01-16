from pandas import read_csv

from tool.database.DatabaseInterface import DatabaseInterface


class CsvDatabase(DatabaseInterface):
    def __init__(self, path: str) -> None:
        self.__csv_file: list = []
        self.initialize(path)

    def initialize(self, path: str) -> None:
        self.__csv_file = read_csv(path)
        self.__csv_file = self.__csv_file.values.tolist()
        temp = []
        for card in self.__csv_file:
            temp.append(
                {
                    "front": card[0],
                    "back": card[1]
                }
            )
        self.__csv_file = temp

    def get_database(self) -> list:
        return self.__csv_file
