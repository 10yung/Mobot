import sys
import os
import pandas as pd
sys.path.append('../../')

from src.utils.Exporter.ExportInterface import ExportInterface


class ModelExporter(ExportInterface):
    def __init__(self):
        pass

    @staticmethod
    def save_file(target: object, target_dir: str, file_name: str):
        """
        Save the model object to static file in the models folder
        :param target: model object <statsmodel> <skilearn>
        :param target_dir: string 'project model folder'
        :param file_name: string 'model name'
        :return:
        """
        target.save(f'{target_dir}/{file_name}')
        print('Model saved!')