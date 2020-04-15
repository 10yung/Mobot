import pandas as pd
import sys
sys.path.append('../../')

from functools import reduce
from src.preprocess.utils.SourceManager import SourceManager
from src.preprocess.utils.CsvFetcher import CsvFetcher
from src.preprocess.utils.SourceFactory import SourceFactory


class CreateFlatTable:
    def __init__(self, source_dir: str, target_dir: str):
        self._source_dir = source_dir
        self._target_dir = target_dir

    @staticmethod
    def merge_files(dataframe_list: list, merge_key: str):
        return reduce(lambda left, right: pd.merge(left, right, on=merge_key), dataframe_list)

    def save_file(self, dataframe, file_name: str):
        try:
            dataframe.to_csv(f'{self._target_dir}/{file_name}.csv')
            print('save flat table successfully!')
        except Exception as e:
            # append empty list if error happened
            print(e)


if __name__ == '__main__':
    print('### CreateFlatTable ###')
    source_directory = '../../data/source'
    target_directory = '../../data/raw'

    # create csv fetcher object
    csv_loader = SourceFactory('csv').get_source()

    # execute get resource
    csv_fetcher = SourceManager(csv_loader)

    df_list = csv_fetcher.get_content('../../data/source')
    table_creator = CreateFlatTable(source_directory, target_directory)
    df = table_creator.merge_files(df_list, 'Country')
    table_creator.save_file(df, 'covid_19')
    # CreateTable('../../data/raw', '../../data/')