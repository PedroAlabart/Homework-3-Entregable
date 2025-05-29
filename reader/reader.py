from abc import ABC, abstractmethod
from pathlib import Path
import pandas as pd
from pandas import DataFrame

from validators.base import IDataValidator

# ---------- Reader Abstract Class ----------

class IReader(ABC):
    def __init__(self, filename: Path):
        self.filename = filename

    @abstractmethod
    def read_file(self) -> DataFrame:
        pass

# ---------- Specific Readers ----------

class JSONReader(IReader):
    def read_file(self):
        return pd.read_json(self.filename)


class CSVReader(IReader):
    def read_file(self):
        return pd.read_csv(self.filename)

# ---------- Factory for Reader ----------

class ReaderFactory:
    @staticmethod
    def create_reader(file_type: str, filename: Path) -> IReader:
        if file_type == 'json':
            return JSONReader(filename)
        elif file_type == 'csv':
            return CSVReader(filename)
        else:
            raise NotImplementedError(f"No reader available for file type: {file_type}")

# ---------- BatchReader ----------

class BatchReader:
    def __init__(self, sources: list[dict], validator: IDataValidator):
        self.sources = sources
        self.validator = validator

    def load_all(self) -> DataFrame:
        dfs = []

        for source in self.sources:
            try:
                reader = ReaderFactory.create_reader(source['extension'], source['path'])
                df = reader.read_file()

                result = self.validator.validate(df)
                if result["is_valid"]:
                    dfs.append(df)
                else:
                    print(f"[WARNING] Validation failed for {source['path']}:")
                    for error in result["errors"]:
                        print("-", error)

            except Exception as e:
                print(f"[ERROR] Failed to process {source['path']}: {e}")

        return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()
