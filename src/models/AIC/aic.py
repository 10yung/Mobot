import sys
sys.path.append('../../../')
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





# calculate aic for regression
def calculate_aic(n, mse, num_params):
	aic = n * log(mse) + 2 * num_params
	return aic

def train_aic_model(X,y):
    model = LinearRegression()
    model.fit(X, y)
    # number of parameters
    num_params = len(model.coef_) + 1
    # print('Number of parameters: %d' % (num_params))
    # predict the training set
    yhat = model.predict(X)
    # calculate the error
    mse = mean_squared_error(y, yhat)
    # print('MSE: %.3f' % mse)
    # calculate the aic
    aic = calculate_aic(len(y), mse, num_params)
    # print('AIC: %.3f' % aic)
    return aic

selected_column_list =['health_expend', 'literacy', 'physicians_density', 'obesity',
       'life_expect', 'h_bed_density', 'imigrate_rate']
X = training[selected_column_list]
y= training['recovery_rate']






def rSubset(arr, r):

    # return list of all subsets of length r
    # to deal with duplicate subsets use
    # set(list(combinations(arr, r)))
    return list(combinations(arr, r))

#
# X = training[selected_column_list]
# y= training['recovery_rate']
#
# train_aic_model(X,y)


aic_info_dict = {}



for x in range(len(selected_column_list)):
    for column_tuple in rSubset(selected_column_list, x):
        column_list = list(column_tuple)
        X = training[column_list]
        y= training['recovery_rate']
        if X.shape[1] != 0:
            aic_score = train_aic_model(X,y)
            aic_info_dict[str(column_list)] = aic_score

# print(aic_info_dict)
answer = min(aic_info_dict, key=aic_info_dict.get)
print(aic_info_dict.values())
# print(answer)
# print(aic_info_dict[answer])













# for element in selected_column_list:
#     X = training[selected_column_list]
#     y= training['recovery_rate']
#     train_aic_model(X,y)
#     print("@@@@@@@@")
#
#     modified_list = list(set(X)-set([element]))
#     X = training[modified_list]
#     y= training['recovery_rate']
#     train_aic_model(X,y)
#     print("=======")