import pandas as pd
import numpy as np
import sys

sys.path.append('../../../')

from src.preprocess.utils.Transform.TransformInterface import TransformInterface


class RootSquareTransform(TransformInterface):
    """
        Transform value by log(x+1)
    """

    def transform(self, data: pd.DataFrame, column_name: str) -> None:
        data[column_name] = data[column_name].transform(lambda x: np.sqrt(x))


if __name__ == '__main__':
    print('### RootSquareTransform ###')
