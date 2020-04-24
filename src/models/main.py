import sys
sys.path.append('../../')

from src.split.SplitFactory import SplitFactory
from src.split.SplitManager import SplitManager
from src.models.AIC.aic import aic
from src.models.SimpleLm.SimpleLm import SimpleLm
from src.models.StepWise.StepWise import StepWise
from src.utils.Exporter.ExportFactory import ExportFactory
from src.utils.Exporter.ExportManager import ExportManager
from src.utils.Importer.ImporterFactory import ImporterFactory
from src.utils.Importer.ImporterManager import ImporterManager



if __name__ == '__main__':
    print('### Model Main ###')

    model_exec_plan = {
        model: [{
            'name': 'AIC',
            'criteria': {}
        }, {
            'name': 'SimpleLm',
            'criteria': {}
        }, {
            'name': 'StepWise',
            'criteria': {
                'name': 'p_value',
                'threshold': [0.01, 0.05, 0.1]
            }
        }]
    }


    # get source
    importer_object = ImporterFactory('csv').generate()
    importer_manager = ImporterManager(importer_object)

    # initialize split object
    ratio_splitter = SplitFactory('ratio').generate()
    training, testing = SplitManager(ratio_splitter).exec(data, 0.8)

    files = [{
        'dir': '../../../data/preprocessed/',
        'files': ['covid_19.csv']
    }]

    data = importer_manager.exec(files)[0]

    training, testing = SplitManager(ratio_splitter).exec(data, 0.8)
    print(training)

    predictor_name = ["Health.expenditures....of.GDP.", "Literacy...."]
    response_name = ['Recovery Rate']

    # ----------
    # Simple Linear Regressionx
    # ----------
    model = SimpleLm()
    result = model.exec(data, predictor_name, response_name)
    print(result)

    # ----------
    # Simple Linear Regression
    # ----------


