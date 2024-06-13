from openpyxl import Workbook
from tb1_parser import AiSignal, ParsedTB1Collection, SignalsCollection

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
    "IM": (
        "№",
        "Наименование параметра",
        "Состояние",
        "Индикация на мнемосхеме",
        "Сообщение в журнале",
    ),
    "Prot": (
        "№",
        "Наименование параметра",
        "Корректность взвода защиты (с экрана)",
        "Снятие взвода защит (с экрана)",
        'Снятие взвода защит (с экрана) в окне "События"',
        "Корректность взвода защиты из алгоритма",
        'Корректность взвода защиты из алгоритма в окне "События"',
        "Корректность ввода в ремонт",
        "Корректность вывод ремонта из алгоритма",
        "Корректность ввода/вывода в ремонт (сообщения)",
    ),
    "Diag": (
        "№",
        "Наименование параметра",
        "Модуль ПЛК",
        "Канал",
        "Вспл. подсказки",
        "Привязка",
        "Индикация",
    ),
    "Alg": (
        "№",
        "Фазы (НУ)",
        "№ Фазы",
        "Соответствие описанию",
        "Проверка на исполнение",
        "Проверка на ошибку фазы (неуспешное выполнение фазы (error))",
        "Формирование ошибки алгоритма при наличии ошибки фазы",
    ),
}


class ReportMaker:

    def __init__(self, collection: ParsedTB1Collection) -> None:
        """
        docstring
        """
        if not isinstance(collection, ParsedTB1Collection):
            raise TypeError("некорректный тип аргумента")

        self.__logs_owner: str = self.__class__.__name__
        self.__collection: ParsedTB1Collection = collection.filter(
            key=lambda signal: signal.isused()
        )
        self.__wb = Workbook()

    def __get_identical_cells(self, sheet, column: str):
        """
        docstring
        """
        pass

    def __fill_Ai_sheet(self):
        """
        docstring
        """
        sheet = self.__wb["Ai"]
        for index, signal in enumerate(self.__collection["Ai"]):
            signal: AiSignal
            sheet.append((index + 1, signal.name, "знач."))
            sp_dict = {
                key: value
                for key, value in {
                    "НГ": signal.LL,
                    "НА": signal.LA,
                    "НП": signal.LW,
                    "ВП": signal.HW,
                    "ВА": signal.HA,
                    "ВГ": signal.HL,
                }.items()
                if value is not None
            }
            for sp_name, sp_value in sp_dict.items():
                sheet.append((index + 1, signal.name, sp_name, sp_value))
        # print(set(cell.value for cell in sheet['A'][1:]))
        

    def make_sheets(self):
        """
        docstring
        """
        for ws_name, ws_columns in SHEETS_CONFIG.items():
            self.__wb.create_sheet(ws_name) if ws_columns else None
            self.__wb[ws_name].append(ws_columns)
        del self.__wb["Sheet"]

        self.__fill_Ai_sheet()

    def write(self, filename: str):
        """
        docstring
        """
        self.__wb.save(filename)
