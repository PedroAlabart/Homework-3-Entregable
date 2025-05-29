from validators.validator_builder import ValidatorBuilder
from reader.reader import BatchReader

from config import(
    NECCESARY_COLUMNS,
    EXTRACTION_PATHS
)


validator = (ValidatorBuilder() 
    .with_column_check(NECCESARY_COLUMNS) 
    .with_non_nulls(NECCESARY_COLUMNS) 
    .build())

reader = BatchReader(sources=EXTRACTION_PATHS, validator=validator)
df_final = reader.load_all()
print(df_final)


asd