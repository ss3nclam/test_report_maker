from os import listdir

from tb1_parser import TB1Parser

from .modules.report_maker import ReportMaker


def main():
    excel_files = (
        filename
        for filename in listdir()
        if filename.endswith((".xlsx", ".xls"))
        and not filename.startswith("report")
    )

    for filename in excel_files:
        parser = TB1Parser(filename)
        parser.read()
        tb1 = parser.collection

        report = ReportMaker(tb1)
        report.make_sheets()
        report.write(f"report_{filename.split('.')[0]}.xlsx")
