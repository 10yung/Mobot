import pandas as pd
import sys

sys.path.append('../../')

from src.preprocess.utils.Imputation.ImputatorFactory import ImputatorFactory
from src.preprocess.utils.Imputation.ImputatorManager import ImputatorManager
from src.preprocess.utils.Source.CsvFetcher import CsvFetcher
from src.preprocess.Interface.PreprocessCommandInterface import PreprocessCommandInterface


class Imputation(PreprocessCommandInterface):
    def __init__(self, columns: list, dataframe: pd.DataFrame = None):
        self._dataframe = dataframe
        self._columns = columns

    def exec(self) -> pd.DataFrame:
        imputation = ImputatorFactory('mean').generate()
        imputator = ImputatorManager(imputation)
        for column in self._columns:
            imputator.exec(self._dataframe, column)

        return self._dataframe

if __name__ == '__main__':
    print('### Imputation ###')
    source_directory = '../../data/raw'
    target_directory = '../../data/imputed'

    csv_fetcher = CsvFetcher()
    data = csv_fetcher.fetch(source_directory)[0]
    print(data)

    # create csv fetcher object
    mean_imputation = ImputatorFactory('mean').generate()

    # execute get resource
    imputator = ImputatorManager(mean_imputation)

    # impute missing value (N/A) with mean
    imputator.exec(data, 'Pop_Density')
    print(data)
