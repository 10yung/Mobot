from typing import TypeVar
from src.preprocess.Interface.PreprocessCommandInterface import PreprocessCommandInterface

PreprocessCommandContainerType = TypeVar('PreprocessCommandContainerType', object, SourceInterface)


class PreprocessCommandContainer:
    """
    This class is for registering preprocess command
    """
    def __init__(self):
        self._steps = {}

    def register(self, step_name, step: PreprocessCommandContainerType):
        self._steps[step_name] = step

    def run(self, step_name):
        if step_name in self._steps.keys():
            self._steps[step_name].exec()
        else:
            print(f"Command [{step_name}] not recognised")