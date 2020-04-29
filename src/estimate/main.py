import sys
sys.path.append('../../')
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







if __name__ == '__main__':
    print("Hello")
    print("=====")








class RMSE:

    @staticmethod
    def get_rmse(testing, data: pd.DataFrame, model_list:list):
        rmse_list =[]
        data_dict = data.to_dict()
        model_dict = {v : k for v, k in enumerate(model_list)}
        for (index,response), (index,predictors),(index,model) in zip(data_dict['response'].items(), data_dict['predictors'].items(),model_dict.items()):
            predictors = predictors.split('/')
            y_pred = model.predict(testing[predictors])
            response = response.strip("'][").split(', ')
            # print(response)
            rmse = sqrt(mean_squared_error(testing[response], y_pred))
            rmse_list.append(rmse)
        return rmse_list