import sys

sys.path.append('../../')

from src.preprocess.CreateFlatTable import CreateFlatTable
from src.preprocess.Imputation import Imputation
from src.preprocess.Transformation import Transformation


if __name__ == '__main__':
    print('### Preprocess Main file ###')

    source_directory = '../../data/source'
    target_directory = '../../data/raw'
    flat_table = CreateFlatTable(source_directory, target_directory, 'covid_19').exec()
    print('before preprocess')
    print(flat_table)

    Imputation(['Pop_Density'], flat_table).exec()
    Transformation(['Pop_Density'], flat_table).exec()
    print('after preprocess')
    print(flat_table)
