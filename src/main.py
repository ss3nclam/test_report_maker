from tb1_parser import TB1Parser

from .modules.report_maker import ReportMaker


def main():
    parser = TB1Parser("table.xlsx")
    parser.read()
    tb1 = parser.collection

    report = ReportMaker(tb1)
    report.make_sheets()
    report.write("out.xlsx")
