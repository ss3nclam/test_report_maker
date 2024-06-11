from dataclasses import dataclass
from typing import Any


@dataclass
class TestReport(object):

    def __init__(self):
        self.__Ai_sheet: Any | None
        self.__Di_sheet: Any | None
        self.__Do_sheet: Any | None
        self.__IM_sheet: Any | None
        self.__Protect_sheet: Any | None
        self.__Diag_sheet: Any | None
        self.__Algorythm_sheet: Any | None

    def __str__(self) -> str:
        return f"{self.__class__.__name__}{tuple(self.__dict__)}"
