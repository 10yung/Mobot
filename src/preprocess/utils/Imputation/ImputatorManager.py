# ---
# The bridge class  that bind imputation object and client api for execution
# ---
import sys
import pandas as pd
sys.path.append('../../../')

from src.preprocess.utils.Imputation.ImputatorInterface import ImputatorInterface


class ImputatorManager:
    def __init__(self, imputation_type: ImputatorInterface):
        self._imputation_type = imputation_type

    def get_imputation(self, data: pd.DataFrame, column_name: str) -> None:

        # execute imputation without copying a new dataframe
        self._imputation_type.impute(data, column_name)


if __name__ == '__main__':
    print('### SourceManager ###')



