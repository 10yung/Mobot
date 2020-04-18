# ---
# The bridge class  that bind source drivers and client api for execution
# ---
import sys
sys.path.append('../../../')

from src.preprocess.utils.Source.SourceInterface import SourceInterface


class SourceManager():
    def __init__(self, source_type: SourceInterface):
        self._source_type = source_type

    def get_content(self, directory):
        return self._source_type.fetch(directory)


if __name__ == '__main__':
    print('### SourceManager ###')


