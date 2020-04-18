# ---
# The bridge class  that bind transform object and client api for execution
# ---
import sys
import pandas as pd
sys.path.append('../../../')

from src.preprocess.utils.Transform.TransformInterface import TransformInterface


class TransformManager:
    def __init__(self, transform_type: TransformInterface):
        self._transform_type = transform_type

    def get_transform(self, data: pd.DataFrame, column_name: str):
        return self._transform_type.transform(data, column_name)


if __name__ == '__main__':
    print('### TransformManager ###')



