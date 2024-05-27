import logging

import pandas
from tb1_parser import TB1Parser

from .modules import TestReportMaker

# Настройки
logging.basicConfig(level=logging.DEBUG)
pandas.set_option("display.max_rows", None)
pandas.set_option('display.max_colwidth', None)

filename = 'ЛДАР.421245.751_ТБ1.xlsx'
parser = TB1Parser(filename)
parser.read()

report_maker = TestReportMaker(parser.collection)
report_maker.make()
report_maker.write(f"{''.join(filename.split('.')[:-1])}_report.xlsx")