import pandas as pd
from abc import ABC, abstractmethod


class ImputatorInterface(ABC):
    """
        Define data cleaning process functions for replace missing value
    """

    @abstractmethod
    def impute(self, data: pd.DataFrame, column_name: str) -> pd.DataFrame:
        pass
