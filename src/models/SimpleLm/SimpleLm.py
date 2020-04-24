import statsmodels.api as sm
import pandas as pd
import sys

sys.path.append('../../../')
from src.split.SplitFactory import SplitFactory
from src.split.SplitManager import SplitManager
from src.preprocess.utils.Source.SourceFactory import SourceFactory
from src.preprocess.utils.Source.SourceManager import SourceManager
from src.utils.Importer.ImporterFactory import ImporterFactory
from src.utils.Importer.ImporterManager import ImporterManager
from src.models.LinearModelInterface import LinearModelInterface


class SimpleLm(LinearModelInterface):
    def __init__(self):
        pass

    def exec(self, data: pd.DataFrame, predictor_name: list, response_name: list) -> list:
        X = data[predictor_name]
        Y = data[response_name]
        # print(X)
        model = sm.OLS(Y, X).fit()
        # print(model.resid)
        est_y = model.predict(X).to_frame()
        resid = model.resid.to_frame()
        result_df = pd.concat([Y, est_y, resid], axis=1, sort=False)
        result_df.columns.values[1] = "Est_Recovery_Rate"
        result_df = result_df.rename(columns={"Recovery Rate": "Recovery_Rate", 0:
            "Residuals"}, inplace = False)
        predictor = model.params.index.to_list()
        # print(predictor)
        return (model, predictor, result_df)


if __name__ == '__main__':
    print('### Simple Linear Model')

    # get source
    loader = SourceFactory('csv').generate()
    data = SourceManager(loader).exec('../../../data/preprocessed')[0]

    # initialize split object
    ratio_splitter = SplitFactory('ratio').generate()
    training, testing = SplitManager(ratio_splitter).exec(data, 0.8)

    importer_object = ImporterFactory('csv').generate()
    importer_manager = ImporterManager(importer_object)

    files = [{
        'dir': '../../../data/preprocessed/',
        'files': ['covid19_preprocessed.csv']
    }]
    data = importer_manager.exec(files)[0]

    training, testing = SplitManager(ratio_splitter).exec(data, 0.8)

    predictor_name = ["Health.expenditures....of.GDP.", "Literacy...."]
    response_name = ['Recovery Rate']


    model = SimpleLm()
    result = model.exec(data, predictor_name, response_name)
    print(result)