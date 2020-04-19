import pandas as pd
import sys

sys.path.append('../../')

from src.preprocess.utils.Transform.TransformFactory import TransformFactory
from src.preprocess.utils.Transform.TransformManager import TransformManager
from src.preprocess.utils.Source.CsvFetcher import CsvFetcher
from src.preprocess.Interface.PreprocessCommandInterface import PreprocessCommandInterface


class Transformation(PreprocessCommandInterface):
    def __init__(self, columns: list, dataframe: pd.DataFrame = None):
        self._dataframe = dataframe
        self._columns = columns

    def exec(self) -> pd.DataFrame:
        transform = TransformFactory('log').generate()
        transformer = TransformManager(transform)
        for column in self._columns:
            transformer.exec(self._dataframe, column)
        return self._dataframe


if __name__ == '__main__':
    print('### Transformation ###')
    source_directory = '../../data/raw'
    target_directory = '../../data/imputed'

    csv_fetcher = CsvFetcher()
    data = csv_fetcher.fetch(source_directory)[0]
    print(data)

    # create csv fetcher object
    log_transformation = TransformFactory('log').generate()

    # execute get resource
    transform = TransformManager(log_transformation)

    # impute missing value (N/A) with mean
    transform.exec(data, 'Literacy....')
    print(data)
