# ---
# The bridge class  that bind source drivers and client api
# ---
import sys
sys.path.append('../../../')

from src.preprocess.Interface.SourceInterface import SourceInterface


class SourceManager():
    def __init__(self, source_type: SourceInterface):
        self._source_type = source_type

    def get_content(self, directory):
        return self._source_type.fetch(directory)


if __name__ == '__main__':
    print('### SourceManager ###')


