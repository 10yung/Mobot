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
from math import log,sqrt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from statsmodels.regression.linear_model import OLS
from statsmodels.tools import add_constant
from itertools import combinations
from src.models.AIC.AIC import AIC
from src.models.SimpleLm.SimpleLm import SimpleLm
from src.models.StepWise.StepWise import StepWise
from sklearn.metrics import mean_squared_error
from joblib import dump, load


class RMSE:
    @staticmethod
    def get_rmse(testing_data: pd.DataFrame, predictors: list, response: list, model):
            y_pred = model.predict(testing_data[predictors])
            rmse = sqrt(mean_squared_error(testing_data[response], y_pred))
            return rmse


if __name__ == '__main__':
    print("Test")
    print("=====")


    # Fetch csv file and split train/testing
    ratio_splitter = SplitFactory('ratio').generate()
    importer_object = ImporterFactory('csv').generate()
    csv_fetcher_object = ImporterManager(importer_object)
    files = [{
        'dir': '../../../data/preprocessed/',
        'files': ['covid19_preprocessed.csv']
    }]
    data = csv_fetcher_object.exec(files)[0]
    training, testing = SplitManager(ratio_splitter).exec(data, 0.8)


    # Import Model
    model_files = [{
        'dir': '../../../data/model/models/',
        'files': ["AIC"]
    }]
    fetcher_object = ImporterFactory('model').generate()
    model_object = ImporterManager(fetcher_object)
    model_list_test = model_object.exec(model_files)

    # Test Parameters
    predictors_list = ['Health.expenditures....of.GDP.', 'Literacy....', 'Physicians.density..physicians.1.000.population.', 'Obesity - adult prevalence rate (%)', 'Life expectancy at birth (years)', 'H_bed_density', 'Imigrate_Rate', 'Pop_Density', 'GDP - per capita (PPP) (US$)']
    response_list =['Recovery Rate']

    # Test Class Static Method
    RMSE_Object = RMSE()
    answer = RMSE_Object.get_rmse(testing,predictors_list,response_list,model_list_test[0])
    print(answer)

