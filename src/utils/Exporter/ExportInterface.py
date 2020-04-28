import pandas as pd
from abc import ABC, abstractmethod
from typing import Any


class ExportInterface(ABC):
    """
        Define the interface of each exporter
    """
    @abstractmethod
    def save_file(data: Any, target_dir: str, file_name: str):
        pass