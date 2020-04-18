import pandas as pd
import sys

sys.path.append('../../../')

from src.preprocess.utils.Imputation.ImputatorInterface import ImputatorInterface


class ZeroImputator(ImputatorInterface):
    """
        Substitute missing value by 0
    """

    def impute(self, data: pd.DataFrame, column_name: str) -> pd.DataFrame:
        return data[column_name].fillna(0, inplace=True)

if __name__ == '__main__':
    print('### MedianImputator ###')