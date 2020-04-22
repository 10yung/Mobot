import pandas as pd
from typing import Tuple


def split(dataframe: pd.DataFrame, key_column :str , key_vlaue_for_train: list) -> Tuple[pd.DataFrame, pd.DataFrame]:
        train_bool = dataframe[key_column].isin(key_vlaue_for_train)
        training = dataframe[train_bool]
        testing = dataframe[~train_bool]
        return training, testing



if __name__ == '__main__':
    print('### Test')

data = {'First_Name':  ["Henry","Andy","Jane"],
        'Last_name': ["Liang", "Lin","Su"],
        'Country_name' :["Taiwan","Taiwan","Japan"]
        }

df_test = pd.DataFrame(data, columns = ['First_Name','Last_name','Country_name'])
# print(df_test)


training, testing = split(df_test,'Country_name',["Taiwan"])

print(training)
print(testing)