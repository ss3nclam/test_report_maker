# import logging

# import pandas
from tb1_parser import TB1Parser

from .modules.report_maker import ReportMaker

# logging.basicConfig(level=logging.DEBUG)
# pandas.set_option("display.max_rows", None)
# pandas.set_option('display.max_colwidth', None)

def main():
    parser = TB1Parser("table.xlsx")
    parser.read()
    tb1 = parser.collection

    report = ReportMaker(tb1)
    report.make_sheets()
    report.write("xz.xlsx")
