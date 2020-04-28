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
    aic_object = AIC(selected_column_list, ['recovery_rate'])
    result = aic_object.exec(training)
    aic_model = result[0]



    # aic_model, aic_predictor, aic_result_df = AIC.exec( training , selected_column_list, ['recovery_rate'])
    # aic_y_pred = aic_model.predict(testing[aic_predictor])
    # aic_rms = sqrt(mean_squared_error(testing['recovery_rate'], aic_y_pred))



    # criteria = {
    #     'p_value': 0.05
    # }
    # model = StepWise(criteria)
    # stepwise_model, stepwise_predictor, stepwise_result_df = model.exec(training, selected_column_list, ['recovery_rate'])
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



# dump(aic_model, "../../../data/model/aic_model_test")
# print("Saved model to disk")
# aic_test = load("../../../data/model/aic_model_test")
# print(aic_test)

# model_fetcher = ModelFetcher()
# aic_test = model_fetcher.fetch("../../../data/model/aic_model_test")
# print(aic_test)