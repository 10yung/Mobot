import sys
import pandas as pd

sys.path.append('../../')

from src.split.SplitFactory import SplitFactory
from src.split.SplitManager import SplitManager
from src.preprocess.utils.Source.SourceFactory import SourceFactory
from src.preprocess.utils.Source.SourceManager import SourceManager


if __name__ == '__main__':
    print('### Split Main File')

    # TODO: this will change to Importer object
    # get source
    loader = SourceFactory('csv').generate()
    data = SourceManager(loader).exec('../../data/preprocessed')[0]

    # initialize split object
    ratio_splitter = SplitFactory('ratio').generate()

    # execute split function
    training, testing = SplitManager(ratio_splitter).exec(data, 0.8)
    # print(training)
    # print(testing)