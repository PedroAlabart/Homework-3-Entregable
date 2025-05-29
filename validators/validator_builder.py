# from validators.verify_columns import VerifyColumns
# from validators.non_nulls import NoNulls
from validators.base import IDataValidator
import pandas as pd

class Validator(IDataValidator):
    def __init__(self, rules: list):
        self.rules = rules
        self.errors = []

    def validate(self, df: pd.DataFrame) -> dict:
        self.errors.clear()
        for rule in self.rules:
            result = rule(df)
            if result is not None:
                self.errors.append(result)

        return {
            "is_valid": len(self.errors) == 0,
            "errors": self.errors
        }

class ValidatorBuilder:
    def __init__(self):
        self.rules = []

    def with_column_check(self, columns):
        def rule(df):
            missing = [col for col in columns if col not in df.columns]
            if missing:
                return f"Missing columns: {missing}"
        self.rules.append(rule)
        return self

    def with_non_nulls(self, columns):
        def rule(df):
            nulls = df[columns].isnull().any()
            if nulls.any():
                return f"Nulls in columns: {nulls[nulls].index.tolist()}"
        self.rules.append(rule)
        return self

    def build(self):
        return Validator(self.rules)