import pandas as pd
from abc import ABC, abstractmethod


class PreprocessCommandInterface:
    """
        This interface is for framing the action preprocess action
    """
    @abstractmethod
    def exec(self) -> pd.DataFrame:
        pass
