import pandas as pd
import sys
sys.path.append('../../')
from src.split.SplitFactory import SplitFactory
from src.split.SplitManager import SplitManager
from src.preprocess.utils.Source.SourceFactory import SourceFactory
from src.preprocess.utils.Source.SourceManager import SourceManager
from typing import Tuple
from src.split.SplitInterface import SplitInterface


class ColumnSplit(SplitInterface):
    def split(self, dataframe: pd.DataFrame, key_column: str, training_value: str) -> Tuple[pd.DataFrame, pd.DataFrame]:



        training = dataframe.sample(frac=ratio, random_state=0)
        testing = dataframe.drop(training.index)
        return training, testing









if __name__ == '__main__':
    print('### Split Main File')

data = {'First_Name':  ["Henry","Andy","Jane"],
        'Last_name': ["Liang", "Lin","Su"],
        'Country_name' :["Taiwan","Taiwan","Japan"]
        }

df_test = pd.DataFrame(data, columns = ['First_Name','Last_name','Country_name'])






    ratio_splitter = SplitFactory('ratio').generate()

    # execute split function
    training, testing = SplitManager(ratio_splitter).exec(data, 0.8)
    # print(training)
    # print(testing)