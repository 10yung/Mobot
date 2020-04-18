import pandas as pd
import sys
sys.path.append('../../')

from src.preprocess.utils.Transform.TransformFactory import TransformFactory
from src.preprocess.utils.Transform.TransformManager import TransformManager
from src.preprocess.utils.Source.CsvFetcher import CsvFetcher


class Transformation:
    def __init__(self, source_dir: str, target_dir: str):
        self._source_dir = source_dir
        self._target_dir = target_dir


if __name__ == '__main__':
    print('### Transformation ###')
    source_directory = '../../data/raw'
    target_directory = '../../data/imputed'

    csv_fetcher = CsvFetcher()
    data = csv_fetcher.fetch(source_directory)[0]
    print(data)

    # create csv fetcher object
    log_transformation = TransformFactory('log').get_transformation()

    # execute get resource
    transform = TransformManager(log_transformation)

    # impute missing value (N/A) with mean
    transform.get_transform(data, 'Literacy....')
    print(data)

