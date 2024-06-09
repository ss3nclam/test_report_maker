from dataclasses import dataclass

from pandas import DataFrame


@dataclass
class TestReport(object):

    def __init__(self):
        self.Ai: DataFrame | None
        self.Di: DataFrame | None
        self.Do: DataFrame | None
        self.IM: DataFrame | None
        self.protect: DataFrame | None
        self.diag: DataFrame | None

    def __str__(self) -> str:
        return f'{self.__class__.__name__}{tuple(self.__dict__)}'
