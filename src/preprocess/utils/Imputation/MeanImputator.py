import pandas as pd
import sys

sys.path.append('../../../')

from src.preprocess.utils.Imputation.ImputatorInterface import ImputatorInterface


class MeanImputator(ImputatorInterface):
    """
        Substitute missing value by mean value
    """

    def impute(self, data: pd.DataFrame, column_name: str) -> None:
        data[column_name].fillna((data[column_name].mean()), inplace=True)

if __name__ == '__main__':
    print('### MeanImputator ###')