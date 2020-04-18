import sys
sys.path.append('../../../')

from src.preprocess.utils.Source.CsvFetcher import CsvFetcher


class SourceFactory:
    """
        Manufacture the source object by name
        :return source object
    """
    def __init__(self, source_name: str):
        self._source_name = source_name

    def get_source(self):
        try:
            source_map = {
                'csv': CsvFetcher
            }
            return source_map[self._source_name]()

        except Exception as e:
            print('<<< SourceFactory Error >>>')
            print(f'Exception type {e.__class__.__name__}, Invalid param {e}')
            return None


if __name__ == "__main__":
    print('### SourceFactory ###')
    print(SourceFactory('csv').get_source())
