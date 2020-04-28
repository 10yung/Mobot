import sys
import os
import pandas as pd
sys.path.append('../../')

from src.utils.Exporter.ExportInterface import ExportInterface


class ModelExporter(ExportInterface):
    def __init__(self):
        pass

    @staticmethod
    def save_file(model: object, target_dir: str, file_name: str):
        pass