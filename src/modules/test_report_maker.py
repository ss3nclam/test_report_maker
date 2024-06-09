import logging

from pandas import DataFrame
from tb1_parser import AiSignal, DiSignal, ParsedTB1Collection

from . import TestReport

REPORT_CONFIG: dict = {
    'Ai': {
        'sheet_name': 'Аналог. вх.',
        'columns': [
            '№',
            'Наименование параметра',
            'Тип',
            'Значение уставки',
            'Аналоговые параметры',
            'Главный экран',
            'Всплывающее окно',
            'Сообщения',
            'Тренды',
            'Смена уставок',
            'Вывод в ремонт (графика)',
            'Вывод в ремонт (журнал сообщений)',
            'Вывод в ремонт (блокировка срабатывая защиты)'
        ]
    },
    'Di': {
        'sheet_name': 'Дискр. вх.',
        'columns': [
            "Наименование параметра",
            "Логическое значение",
            "Главный экран",
            "Сообщения",
            "Всплывающее окно",
            "Всплывающее окно",
            "Всплывающее окно",
            "Тип сообщения"
        ]
    },
    'Do': {
        'sheet_name': 'Дискр. вых.',
        'columns': [
            "Наименование параметра",
            "Логическое значение",
            "Индикация команды (для кранов)",
            "Сообщение о подаче команды",
            "Исполнение на имитаторе"
        ]
    }
}


class TestReportMaker:

    def __init__(self, parsed_collection: ParsedTB1Collection) -> None:
        self.__logs_owner: str = self.__class__.__name__

        self.__parsed_collection = parsed_collection
        self.report = TestReport()

    # REFACT Отрефакторить метод создания Ai листа
    def make_Ai_sheet(self):
        try:
            columns = REPORT_CONFIG['Ai']['columns']
            sheet = DataFrame(columns=columns)

            for index, signal in enumerate(signal for signal in self.__parsed_collection['Ai'] if signal.isused()):
                signal: AiSignal
                sheet.loc[len(sheet.index)] = [str(index + 1), signal.name, 'знач.', *['']*(len(columns) - 3)]
                setpoints = {'НГ': signal.LL, 'НА': signal.LA, 'НП': signal.LW, 'ВП': signal.HW, 'ВА': signal.HA, 'ВГ': signal.HL}
                for name, value in setpoints.items():
                    value: float | None
                    if value is not None:
                        sheet.loc[len(sheet.index)] = ['', '', name, round(value) if value.is_integer() else value, *['']*(len(columns) - 4)]

            self.report.Ai = sheet

        except Exception as error:
            logging.error(f'{self.__logs_owner}:Ai_sheet: ошибка формирования листа - {error}')

    def __make_Di_sheet(self):
        pass
    
    def __make_Do_sheet(self):
        pass
    
    def __make_logics_sheet(self):
        pass
    
    def __make_protections_sheet(self):
        pass
 
    def __make_diagnostics_sheet(self):
        pass

    def init_sheets(self):
        pass

    def write_to_excel(self, filename: str):
        pass
