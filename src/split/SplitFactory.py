import sys
sys.path.append('../../')

from src.split.RatioSplit import RatioSplit


class SplitFactory:
    def __init__(self, object_name: str):
        self._object_name = object_name

    def generate(self):
        try:
            source_map = {
                'ratio': RatioSplit
            }
            return source_map[self._object_name]()

        except Exception as e:
            print('<<< SourceFactory Error >>>')
            print(f'Exception type {e.__class__.__name__}, Invalid param {e}')
            return None