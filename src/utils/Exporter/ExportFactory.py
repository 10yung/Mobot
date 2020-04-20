import sys
sys.path.append('../../../')

from src.utils.Interface.FactoryInterface import FactoryInterface
from src.utils.Exporter.CSV_Exporter import CSV_Exporter



class ExportFactory(FactoryInterface):
    """
        Manufacture the source object by name
        :return source object
    """
    def __init__(self, object_name: str):
        self._object_name = object_name

    def generate(self):
        try:
            export_map = {
                'csv': CSV_Exporter
            }
            return export_map[self._object_name]()

        except Exception as e:
            print('<<< SourceFactory Error >>>')
            print(f'Exception type {e.__class__.__name__}, Invalid param {e}')
            return None
