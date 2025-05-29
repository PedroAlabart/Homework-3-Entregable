from validators.base import IDataValidator
from pandas import DataFrame

class VerifyColumns(IDataValidator):
    def __init__(self, expected_columns: list[str]):
        self.expected_columns = expected_columns

    def validate(self, df: DataFrame) -> dict:
        missing = [col for col in self.expected_columns if col not in df.columns]
        if missing:
            return {"is_valid": False, "errors": [f"Missing columns: {missing}"]}
        return {"is_valid": True, "errors": []}