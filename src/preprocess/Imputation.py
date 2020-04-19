import pandas as pd
import sys
sys.path.append('../../')

from src.preprocess.utils.Imputation.ImputatorFactory import ImputatorFactory
from src.preprocess.utils.Imputation.ImputatorManager import ImputatorManager
from src.preprocess.utils.Source.CsvFetcher import CsvFetcher


class Imputation:
    def __init__(self, source_dir: str, target_dir: str):
        self._source_dir = source_dir
        self._target_dir = target_dir

    def save_file(self, dataframe, file_name: str):
        try:
            dataframe.to_csv(f'{self._target_dir}/{file_name}.csv')
            print('save flat table successfully!')
        except Exception as e:
            # append empty list if error happened
            print(e)


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

