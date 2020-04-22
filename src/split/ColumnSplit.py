import pandas as pd
import sys
sys.path.append('../../')

from typing import Tuple
from src.split.SplitInterface import SplitInterface


class ColumnSplit(SplitInterface):
    def split(self, dataframe: pd.DataFrame, key_column :str , key_values_for_train: list) -> Tuple[pd.DataFrame, pd.DataFrame]:
        train_boolean_value = dataframe[key_column].isin(key_values_for_train)
        training = dataframe[train_boolean_value]
        testing = dataframe[~train_boolean_value]
        return training, testing


if __name__ == '__main__':
    print('### Split Main File')

data = {'First_Name':  ["Henry","Andy","Jane"],
        'Last_name': ["Liang", "Lin","Su"],
        'Country_name' :["Taiwan","Taiwan","Japan"]
        }

df_test = pd.DataFrame(data, columns = ['First_Name','Last_name','Country_name'])



# column_splitter = SplitFactory('column').generate()
# print(column_splitter)
# SplitManager(column_splitter).exec_1(df_test,'Country_name',["Taiwan"])
#
# print(training)
# print(testing)