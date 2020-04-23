import sys
import pandas as pd

sys.path.append('../../')

from src.split.SplitFactory import SplitFactory
from src.split.SplitManager import SplitManager
from src.preprocess.utils.Source.SourceFactory import SourceFactory
from src.preprocess.utils.Source.SourceManager import SourceManager


if __name__ == '__main__':
    print('### Split Main File')

    data = {'First_Name':  ["Henry","Andy","Jane"],
            'Last_name': ["Liang", "Lin","Su"],
            'Country_name' :["Taiwan","Taiwan","Japan"]
            }

    df_test = pd.DataFrame(data, columns = ['First_Name','Last_name','Country_name'])

    test_dict = {
        "column_name" : "Country_name",
        "train_values": ["Taiwan"],
        "test_values": ["Japan"]
    }

    # TODO: this will change to Importer object
    # get source
    loader = SourceFactory('csv').generate()
    data = SourceManager(loader).exec('../../data/preprocessed')[0]

    # initialize split object
    ratio_splitter = SplitFactory('ratio').generate()
    column_splitter = SplitFactory('column').generate()

    training, testing = SplitManager(column_splitter).exec(df_test,test_dict)
    print(training)
    print(testing)


    # execute split function
    training, testing = SplitManager(ratio_splitter).exec(data, 0.8)
    # print(training)
    # print(testing)