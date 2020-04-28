import os
import pandas as pd
import sys
sys.path.append('../../../')
from joblib import dump, load
from src.utils.Importer.ImporterInterface import ImporterInterface


class ModelFetcher(ImporterInterface):

    def fetch(self, profiles:list):
        for profile in profiles:
            for file_name in profile['files']:
                    file = profile['dir']+file_name
                    model = load(file)
                    return model


if __name__ == '__main__':
    print("Hello")
    print("=====")

    files = [{
        'dir': '../../../data/model/models/',
        'files': ["sklearn_AIC.pkl"]
    }]


    model_fetcher = ModelFetcher()
    aic_test = model_fetcher.fetch(files)
    print(aic_test)