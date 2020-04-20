import pandas as pd
import sys
import os
import pandas as pd

from src.utils.Exporter.ExportInterface import ExportInterface

sys.path.append('../../')


class CSV_Exporter(ExportInterface):

    @staticmethod
    def save_file(dataframe: pd.DataFrame, target_dir: str, file_name: str):
        try:
            dataframe.to_csv(f'{target_dir}/{file_name}.csv')
            print('save flat table successfully!')
        except Exception as e:
            # append empty list if error happened
            print(e)
