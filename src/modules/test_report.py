from dataclasses import dataclass

from pandas import DataFrame


@dataclass
class TestReport(object):

    def __init__(self):
        self.Ai: tuple[str, DataFrame] | None
        self.Di: tuple[str, DataFrame] | None
        self.Do: tuple[str, DataFrame] | None
        self.IM: tuple[str, DataFrame] | None
        self.protect: tuple[str, DataFrame] | None
        self.diag: tuple[str, DataFrame] | None

    def __str__(self) -> str:
        return f'{self.__class__.__name__}{tuple(self.__dict__)}'
