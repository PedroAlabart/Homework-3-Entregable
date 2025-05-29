from validators.base import IDataValidator
from pandas import DataFrame

class NoNulls(IDataValidator):
    def __init__(self, columns: list[str]):
        self.columns = columns

    def validate(self, df: DataFrame) -> dict:
        nulls = df[self.columns].isnull().any()
        if nulls.any():
            null_cols = nulls[nulls].index.tolist()
            return {"is_valid": False, "errors": [f"Null values in: {null_cols}"]}
        return {"is_valid": True, "errors": []}