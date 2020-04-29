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


if __name__ == '__main__':
    print("Hello")
    print("=====")


    # fetch csv file and split train/testing
    ratio_splitter = SplitFactory('ratio').generate()
    importer_object = ImporterFactory('csv').generate()
    csv_fetcher_object = ImporterManager(importer_object)
    files = [{
        'dir': '../../../data/preprocessed/',
        'files': ['covid19_preprocessed.csv']
    }]
    data = csv_fetcher_object.exec(files)[0]
    training, testing = SplitManager(ratio_splitter).exec(data, 0.8)
    # print(testing)



    # get model list
    model_files = [{
        'dir': '../../../data/model/models/',
        'files': ["sklearn_AIC.pkl","statsmodels_SimpleLm","statsmodels_StepWise_0.1","statsmodels_StepWise_0.01","statsmodels_StepWise_0.02"]
    }]
    fetcher_object = ImporterFactory('model').generate()
    model_object = ImporterManager(fetcher_object)
    model_list_test = model_object.exec(model_files)
    # model_dict = {v : k for v, k in enumerate(model_list_test)}
    # print(model_dict)

    # get model info and to dict
    importer_object = ImporterFactory('csv').generate()
    csv_fetcher_object = ImporterManager(importer_object)
    model_info = [{
        'dir': '../../../data/model/',
        'files': ['covid19_modeled1.csv']
    }]
    data = csv_fetcher_object.exec(model_info)[0]
    print(type(data))
    RMSE = RMSE()
    answer = RMSE.get_rmse(testing,data,model_list_test)
    print(answer)
















    # selected_column_list =['health_expend', 'literacy', 'physicians_density', 'obesity',
    #        'life_expect', 'h_bed_density', 'imigrate_rate']

    # aic_object = AIC(selected_column_list, ['recovery_rate'])
    # aic_model, aic_predictor, aic_result_df = aic_object.exec( training )
    # aic_y_pred = aic_model_test.predict(testing[aic_predictor])
    # # aic_rms = sqrt(mean_squared_error(testing['recovery_rate'], aic_y_pred))
    # # print(aic_rms)
    # RMSE =RMSE()
    # answer = RMSE.get_rmse(testing,aic_predictor,'recovery_rate',aic_model_test)
    # print(answer)

    # criteria = {
    #     'p_value': 0.05
    # }
    # model = StepWise(selected_column_list,['recovery_rate'])
    # stepwise_model, stepwise_predictor, stepwise_result_df = model.exec(training,criteria )
    #
    #
    #
    # answer1 = RMSE.get_rmse(testing,stepwise_predictor,'recovery_rate',sk_model)
    # print(answer1)

    # stepwise_y_pred = stepwise_model.predict(testing[stepwise_predictor])
    # stepwise_rms = sqrt(mean_squared_error(testing['recovery_rate'], stepwise_y_pred))
    # # print(stepwise_result_df)
    #
    # model = SimpleLm()
    # simple_model, simple_predictor, simple_result_df = model.exec(training, selected_column_list, ['recovery_rate'])
    # simple_y_pred = simple_model.predict(testing[simple_predictor])
    # Simple_rms = sqrt(mean_squared_error(testing['recovery_rate'], simple_y_pred))





    # print("Stepwise RMSE : ",stepwise_rms)
    # print("AIC RMSE : ",aic_rms)
    # print("Simple RMSE : ",Simple_rms)

