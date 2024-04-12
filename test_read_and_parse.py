import logging

import pandas
from tb1_parser import Signal, TB1Parser


# Настройка логера
logging.basicConfig(level=logging.DEBUG)

# Настройка полного вывода таблицы
pandas.set_option("display.max_rows", None)
pandas.set_option('display.max_colwidth', None)


tb1 = TB1Parser('temp/table.xls')
tb1.read()

for key, collection in tb1.collection.items():
    print(key)
    for signal in collection:
        signal: Signal
        if signal.name.lower() != 'резерв':
            print(signal)
