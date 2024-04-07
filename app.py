# import logging
# import os
# import sys

# import pandas

# from src.report.report import Report
# from src.report.sheet_maker import ReportSheetMaker
# from src.tb1.parser import TB1Parser
# from src.tb1.tb1 import TB1


# # Настройка логера
# logging.basicConfig(level=logging.DEBUG)
# # logging.basicConfig(level=logging.ERROR)

# # Настройка полного вывода таблицы
# pandas.set_option("display.max_rows", None)
# pandas.set_option('display.max_colwidth', None)


# def main():
    
#     # Поиск эксельки
#     logging.info('Поиск эксель-файла в директории...')
#     valid_files = [filename for filename in os.listdir('temp') if filename.endswith(('xlsx', 'xls'))]

#     if len(valid_files) == 1:
#         tb1_filename = f'temp/{valid_files[0]}'
#         logging.info(f'Найден файл - {tb1_filename}')
#     else:
#         logging.error('Неподдерживаемый формат или неверное количество эксель-файлов в директории')
#         sys.exit(1)
    
#     # Попытка создания объекта из файла
#     try:
#         tb1 = TB1()
#         parser = TB1Parser()
#         report_sheet_maker = ReportSheetMaker()
#         report = Report()
#         if tb1.read(tb1_filename):
#             tb_sheet = tb1.get('Ai')
#             signals = parser.get_Ai_signal_list(tb_sheet)
#             report_sheet = report_sheet_maker.get_empty(signals)
#             # report.add_sheet(report_sheet)
#             # report_sheet.to_excel('temp/test.xlsx', index=False)
#             print(report_sheet)
#         else:
#             logging.error('Прекращение работы программы по причине ошибки чтения файла..')
#             sys.exit(1)
#     except Exception as error:
#         logging.error(error)
#         pass


# if __name__ == "__main__":
#     main()


import logging

import pandas

from tb1_parser.tb1_parser import TB1Parser
from tb1_parser.signal import Signal
from tb1_parser.signals_collection import SignalsCollection

# Настройка логера
logging.basicConfig(level=logging.DEBUG)

# Настройка полного вывода таблицы
pandas.set_option("display.max_rows", None)
pandas.set_option('display.max_colwidth', None)


filepath='temp/table.xls'
# filepath='temp/table.xlsx'
# filepath='temp/ЛДАР.421245.751_ТБ1.xlsx'
# filepath='temp/ЛДАР.421245.754 ТБ1.xlsx'
# filepath='temp\ЛДАР.421245.757 ТБ1.xlsx'


parser = TB1Parser(filepath)
parser.read()


for name, collection in parser.collection.items():
    collection: SignalsCollection
    print(collection.signals_type)
    for element in collection:
        element: Signal
        if not element.isreserv():
            print(element)
            # print(f'{element.name}: {element.formated_name}')


# with open('temp/proc_AI.st', 'a') as proc_AI:
#     proc_AI.write('FUNCTION_BLOCK proc_AI\n')

#     proc_AI.write('\nVAR\n')
#     for signal in Ai_signals:
#         signal: AiSignal
#         proc_AI.write(f'\tfb_{signal.formated_name} : fb_AiSourceMlp;\n')
#     proc_AI.write('END_VAR\n')

#     proc_AI.write('\nVAR_EXTERNAL\n')
#     proc_AI.write('\tai : AiConfig;\n\tisSignalsChanged : BOOL;\n')
#     for var in (signal.variable for signal in Ai_signals):
#         proc_AI.write(f'\tar{var.replace('AI', 'AIN_')} : TItemAIN;\n')