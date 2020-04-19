import pandas as pd
import sys

sys.path.append('../../../../')

from src.preprocess.utils.Imputation.ImputatorInterface import ImputatorInterface


class MedianImputator(ImputatorInterface):
    """
        Substitute missing value by median value
    """

    def impute(self, data: pd.DataFrame, column_name: str) -> pd.DataFrame:
        return data[column_name].fillna((data[column_name].median()), inplace=True)

if __name__ == '__main__':
    print('### MedianImputator ###')