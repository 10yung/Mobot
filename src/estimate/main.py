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
from src.estimate.RMSE.RMSE import RMSE
from src.utils.Exporter.ExportFactory import ExportFactory
from src.utils.Exporter.ExportManager import ExportManager
from src.utils.Exporter.CsvExporter import CsvExporter




if __name__ == '__main__':
    print("Hello")
    print("=====")


    # fetch csv file and split train/testing
    ratio_splitter = SplitFactory('ratio').generate()
    importer_object = ImporterFactory('csv').generate()
    csv_fetcher_object = ImporterManager(importer_object)
    files = [{
        'dir': '../../data/preprocessed/',
        'files': ['covid19_preprocessed.csv']
    }]
    data = csv_fetcher_object.exec(files)[0]
    training, testing = SplitManager(ratio_splitter).exec(data, 0.8)
    # print(testing)



    # get model list
    # model_files = [{
    #     'dir': '../../../data/model/models/',
    #     'files': ["sklearn_AIC.pkl","statsmodels_SimpleLm","statsmodels_StepWise_0.1","statsmodels_StepWise_0.01","statsmodels_StepWise_0.02"]
    # }]
    # fetcher_object = ImporterFactory('model').generate()
    # model_object = ImporterManager(fetcher_object)
    # model_list_test = model_object.exec(model_files)
    # model_dict = {v : k for v, k in enumerate(model_list_test)}
    # print(model_dict)

    # get model info and to dict
    importer_object = ImporterFactory('csv').generate()
    csv_fetcher_object = ImporterManager(importer_object)
    model_info = [{
        'dir': '../../data/model/',
        'files': ['covid19_modeled1.csv']
    }]
    data = csv_fetcher_object.exec(model_info)[0]

    data_dict = data.to_dict()
    # print(data_dict)

    model_name_list =[]
    for index,model in data_dict['model_name'].items():
        model_name_list.append(model)
    print(model_name_list)

    model_files = [{
    'dir': '../../data/model/models/',
    'files': model_name_list
    }]
    fetcher_object = ImporterFactory('model').generate()
    model_object = ImporterManager(fetcher_object)
    model_list_test = model_object.exec(model_files)
    model_dict = {v : k for v, k in enumerate(model_list_test)}
    print(model_dict)



    RMSE = RMSE()


    rmse_list =[]
    for (index,response), (index,predictors),(index,model) in zip(data_dict['response'].items(), data_dict['predictors'].items(),model_dict.items()):
        predictors = predictors.split('/')
        response = response.strip("'][").split(', ')
        rmse = RMSE.get_rmse(testing,predictors,response,model)
        rmse_list.append(rmse)

    rmse_df = pd.DataFrame(rmse_list,columns = ['rmse'])


    result_df = pd.concat([data, rmse_df], axis=1)
    print(result_df)

    csv_exporter  = ExportFactory('csv').generate()
    exporter =  ExportManager(csv_exporter)
    exporter.exec(result_df, '../../data/estimate', "estimated_model_data")


