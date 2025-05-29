from abc import ABC, abstractmethod

from pandas import DataFrame


class IDataValidator(ABC):
    @abstractmethod
    def validate(self, df: DataFrame) -> dict:
        pass
