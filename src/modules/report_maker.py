from typing import Any

from openpyxl import Workbook
from tb1_parser import ParsedTB1Collection, SignalsCollection

# TODO перенести в файл конфига
SHEETS_CONFIG = {
    "Ai": (
        "№",
        "Наименование параметра",
        "Тип",
        "Значение уставки",
        "Аналоговые параметры",
        "Главный экран",
        "Контекстное меню",
        "События",
        "Тренды",
        "Общее (Смена уставок)",
        "Рестарт ПЛК (Смена уставок)",
        "Графика (Вывод в ремонт)",
        "События (Вывод в ремонт)",
        "Блокировка защиты (Вывод в ремонт)",
    ),
    "Di": (
        "№",
        "Наименование параметра",
        "Состояние",
        "Логическое значение",
        "Главный экран",
        "Сообщения",
        "Контекстное меню",
        "Тип сообщения",
    ),
    "Do": (
        "№",
        "Наименование параметра",
        "Состояние",
        "Логическое значение",
        "Индикация команды (для кранов)",
        "Сообщение о подаче команды",
        "Исполнение на имитаторе",
    ),
    "IM": (None),
    "Prot": (None),
    "Diag": (None),
    "Alg": (None),
}


class ReportMaker:

    def __init__(self, collection: ParsedTB1Collection) -> None:
        """
        docstring
        """
        if not isinstance(collection, ParsedTB1Collection):
            raise TypeError("некорректный тип аргумента")
        
        self.__logs_owner: str = self.__class__.__name__
        self.__collection: ParsedTB1Collection = collection
        self.__wb = Workbook()

        # TODO перенести в метод создания листов
        for ws_name, ws_columns in SHEETS_CONFIG.items():
            self.__wb.create_sheet(ws_name) if ws_columns else None

    def __make_Ai_sheet(self, signals: SignalsCollection):
        """
        docstring
        """
        pass

    def write(self, filename: str):
        self.__wb.save(filename)
