import pandas as pd
import sys
sys.path.append('../../')

from typing import Tuple
from src.split.SplitInterface import SplitInterface


class RatioSplit(SplitInterface):
    def split(self, dataframe: pd.DataFrame, ratio: float,) -> Tuple[pd.DataFrame, pd.DataFrame]:
        training = dataframe.sample(frac=ratio, random_state=0)
        testing = dataframe.drop(training.index)
        return training, testing

if __name__ == '__main__':
    print('### RatioSplit ###')
