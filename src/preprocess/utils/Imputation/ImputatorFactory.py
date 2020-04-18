import sys
sys.path.append('../../../')

from src.preprocess.utils.Imputation.MeanImputator import MeanImputator


class ImputatorFactory:
    """
        Manufacture the imputator object by name
        :return source object
    """
    def __init__(self, imputator_name: str):
        self._imputator_name = imputator_name

    def get_imputation(self):
        try:
            imputation_map = {
                'mean': MeanImputator
            }
            return imputation_map[self._imputator_name]()

        except Exception as e:
            print('<<< ImputatorFactory Error >>>')
            print(f'Exception type {e.__class__.__name__}, Invalid param {e}')
            return None


if __name__ == "__main__":
    print('### Imputator Factory ###')
    print(ImputatorFactory('mean').get_imputation())
