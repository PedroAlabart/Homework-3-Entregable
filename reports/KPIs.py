from abc import ABC, abstractmethod
from UI.print_prettier import pretty_print_df

from pandas import DataFrame, Series


class IKPI(ABC):
    @abstractmethod
    def print_metric(self, data) -> Series | DataFrame | float:
        raise NotImplementedError


class FetchLatestEntriesPerRoom(IKPI):
    @pretty_print_df
    def print_metric(self, data):
        # Obtener el último registro por sala
        ultimos_registros = data.loc[data.groupby('sala')['timestamp'].idxmax()]

        # Opcional: ordenar por sala
        ultimos_registros = ultimos_registros.sort_values(by='sala')
        return ultimos_registros

    
class LastTenCriticalEntries(IKPI):
    @pretty_print_df
    def print_metric(self, data):
        criticas = data[data['estado'] == 'WARNING'].sort_values(by='timestamp', ascending=False).head()

        
        return criticas
       

class TotalUnitsByCategory(IKPI):
    def print_metric(self, data):
        return data.groupby('categoria')['cantidad'].sum()
    

class MetricsStrategy:
    def __init__(self, data, KPI = None):
        self.data = data
        self.KPI = KPI

    def set_KPI(self, KPI: IKPI):
        self.KPI = KPI

    def get_metric(self):
        assert self.KPI is not None
        self.KPI.print_metric(self.data)
    




