import pandas as pd

from abc import ABC, abstractmethod


class ExportInterface(ABC):
    """
        Define the interface of each exporter
    """

    @abstractmethod
    def save_file(dataframe: pd.DataFrame, target_dir: str, file_name: str):
        pass