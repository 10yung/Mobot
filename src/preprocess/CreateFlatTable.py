import pandas as pd
import sys

sys.path.append('../../')

from functools import reduce
from src.preprocess.utils.Source.SourceManager import SourceManager
from src.preprocess.utils.Source.SourceFactory import SourceFactory
from src.preprocess.Interface.PreprocessCommandInterface import PreprocessCommandInterface
from src.utils.Exporter.DataframeExporter import DataframeExporter

class CreateFlatTable(PreprocessCommandInterface):
    def __init__(self, source_dir: str, target_dir: str, file_name: str):
        self._source_dir = source_dir
        self._target_dir = target_dir
        self._file_name = file_name

    def exec(self) -> pd.DataFrame:
        """
        Create flat table from all the csv file within source folder
        :return: None
        """
        loader = SourceFactory('csv').generate()
        fetcher = SourceManager(loader)
        dfs = fetcher.exec(self._source_dir)
        result = self.merge_files(dfs, 'Country')
        DataframeExporter.save_file(result, self._target_dir, self._file_name)
        return result

    @staticmethod
    def merge_files(dataframe_list: list, merge_key: str):
        return reduce(lambda left, right: pd.merge(left, right, on=merge_key), dataframe_list)


if __name__ == '__main__':
    print('### CreateFlatTable ###')
    source_directory = '../../data/source'
    target_directory = '../../data/raw'

    # create csv fetcher object
    csv_loader = SourceFactory('csv').generate()

    # execute get resource
    csv_fetcher = SourceManager(csv_loader)

    df_list = csv_fetcher.exec('../../data/source')
    table_creator = CreateFlatTable(source_directory, target_directory, 'covid_19')
    df = table_creator.merge_files(df_list, 'Country')
    table_creator.save_file(df, 'covid_19')
    # CreateTable('../../data/raw', '../../data/')
