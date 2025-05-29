from validators.validator_builder import ValidatorBuilder
from reader.reader import BatchReader

from config import(
    NECCESARY_COLUMNS,
    EXTRACTION_PATHS
)


from reports.KPIs import (
    FetchLatestEntriesPerRoom,
    LastTenCriticalEntries,
    MetricsStrategy
)




validator = (ValidatorBuilder() 
    .with_column_check(NECCESARY_COLUMNS) 
    .with_non_nulls(NECCESARY_COLUMNS) 
    .with_safe_timestamp_conversion('timestamp')
    .build())

reader = BatchReader(sources=EXTRACTION_PATHS, validator=validator)
data = reader.load_all()


#Metrics related functions
metric_strategy = MetricsStrategy(data)


#Strategy 1
print("First Metric")
last_entires = FetchLatestEntriesPerRoom()
metric_strategy.set_KPI(last_entires)
metric_strategy.get_metric()


#Strategy 2
last_ten_critical_entries = LastTenCriticalEntries()
metric_strategy.set_KPI(last_ten_critical_entries)
metric_strategy.get_metric()