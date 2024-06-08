from typing import Literal

from tb1_parser import ParsedTB1Collection

from .test_report import TestReport


class ReportMaker:

    def __init__(self, tb1_collection: ParsedTB1Collection):
        self.__logs_owner: str = self.__class__.__name__
        self.__tb1_collection = tb1_collection

    def 
