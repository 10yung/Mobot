import os
import pandas as pd
import sys
sys.path.append('../../../')
from joblib import dump, load
from src.utils.Importer.ImporterInterface import ImporterInterface


class ModelFetcher(ImporterInterface):
    def fetch(self, profile):
        model = load(profile)
        return model




if __name__ == '__main__':
    print("Hello")
    print("=====")

    model_fetcher = ModelFetcher()
    aic_test = model_fetcher.fetch("../../../data/model/aic_model_test")
    print(aic_test)