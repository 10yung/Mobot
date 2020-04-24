import sys
sys.path.append('../../../')
import ast
import pandas as pd
from src.split.SplitFactory import SplitFactory
from src.split.SplitManager import SplitManager
from src.preprocess.utils.Source.SourceFactory import SourceFactory
from src.preprocess.utils.Source.SourceManager import SourceManager
from src.utils.Importer.ImporterFactory import ImporterFactory
from src.utils.Importer.ImporterManager import ImporterManager
from math import log
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from statsmodels.regression.linear_model import OLS
from statsmodels.tools import add_constant
from itertools import combinations
from src.models.AIC.aic import aic


if __name__ == '__main__':
 print("Hello")
 print("=====")


ratio_splitter = SplitFactory('ratio').generate()
importer_object = ImporterFactory('csv').generate()
importer_manager = ImporterManager(importer_object)
files = [{
    'dir': '../../../data/preprocessed/',
    'files': ['new_covid19.csv']
}]
data = importer_manager.exec(files)[0]

training, testing = SplitManager(ratio_splitter).exec(data, 0.8)

selected_column_list =['health_expend', 'literacy', 'physicians_density', 'obesity',
       'life_expect', 'h_bed_density', 'imigrate_rate']

# aic_object = aic()
# answer_list = aic.exec( training , selected_column_list, 'recovery_rate')
# print(answer_list)