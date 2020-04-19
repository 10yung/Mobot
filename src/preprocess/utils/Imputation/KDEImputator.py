import pandas as pd
import sys
from sklearn.datasets import make_blobs
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV
import numpy as np

sys.path.append('../../../')

from src.preprocess.utils.Imputation.ImputatorInterface import ImputatorInterface



class KDEImputator(ImputatorInterface):
    """
        Substitute missing value by random value based on Kernel Density Estimation (KDE)
    """
    def impute(self, data: pd.DataFrame, column_name: str) -> pd.DataFrame:
        # Create test-data
        data_x, data_y = make_blobs(n_samples=100, n_features=2, centers=7, cluster_std=0.5, random_state=0)
        # Fit KDE (cross-validation used!)
        params = {'bandwidth': np.logspace(-1, 2, 30)}
        grid = GridSearchCV(KernelDensity(), params)
        grid.fit(data_x)
        kde = grid.best_estimator_
        bandwidth = grid.best_params_['bandwidth']

        # Resample
        N_POINTS_RESAMPLE = 1000
        resampled = kde.sample(N_POINTS_RESAMPLE)

    # TODO:
    # what the kernel is?
    # the resampled return four values if the N_POINTS_RESAMPLE = 2

        return data[column_name].fillna(resampled, inplace=True)




if __name__ == '__main__':
    print('### KDEImputator ###')