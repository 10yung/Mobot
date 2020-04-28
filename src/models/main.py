import pandas as pd
import sys

sys.path.append('../../')

from src.split.SplitFactory import SplitFactory
from src.split.SplitManager import SplitManager
from src.models.ModelRegister import ModelRegister
from src.models.AIC.AIC import AIC
from src.models.SimpleLm.SimpleLm import SimpleLm
from src.models.StepWise.StepWise import StepWise
from src.utils.Exporter.ExportFactory import ExportFactory
from src.utils.Exporter.ExportManager import ExportManager
from src.utils.Importer.ImporterFactory import ImporterFactory
from src.utils.Importer.ImporterManager import ImporterManager



if __name__ == '__main__':
    print('### Model Main ###')

    model_exec_plan = {
        'predictor_name': ["Health.expenditures....of.GDP.", "Literacy...."],
        'response_name': ['Recovery Rate'],
        'experiments': [{
            'name': 'AIC',
            'criteria': {}
        }, {
            'name': 'SimpleLm',
            'criteria': {}
        }, {
            'name': 'StepWise',
            'criteria': {
                'p_value': 0.05
            }
        }, {
            'name': 'StepWise',
            'criteria': {
                'p_value': 0.01
            }
        }, {
            'name': 'StepWise',
            'criteria': {
                'p_value': 0.02
            }
        }, ]
    }

    # get source
    importer_object = ImporterFactory('csv').generate()
    importer_manager = ImporterManager(importer_object)

    files = [{
        'dir': '../../data/preprocessed/',
        'files': ['covid19_preprocessed.csv']
    }]

    data = importer_manager.exec(files)[0]
    # initialize split object
    ratio_splitter = SplitFactory('ratio').generate()
    training, testing = SplitManager(ratio_splitter).exec(data, 0.8)

    # register models
    model_register = ModelRegister()

    model_map = {
        'AIC': AIC,
        'StepWise': StepWise,
        'SimpleLm': SimpleLm
    }

    for model in model_exec_plan['experiments']:
        model_name = model['name']
        model_register.register(model_name, model_map[model_name], model_exec_plan['predictor_name'],
                                model_exec_plan['response_name'])

    # execute models base on execution plan
    model_table = {}
    for model in model_exec_plan['experiments']:
        result = model_register.exec(model['name'], training, model['criteria'])

        if len(model['criteria'].items()) == 0:
            criteria = ''
            model_name = model['name']
        else:
            key, value = list(model['criteria'].items())[0]
            criteria = key + ' ' + str(value)
            model_name = model['name'] + '_' + str(value)

        model_table[model_name] = [model_exec_plan['response_name'], ' '.join(result[1]), criteria]

    model_table = pd.DataFrame.from_dict(model_table, orient='index', columns=['response', 'predictors', 'criteria'])
    model_table = model_table.reset_index()
    model_table.columns = ['model_name', 'response', 'predictors', 'criteria']
    # print(model_table)

    loader = ExportFactory('csv').generate()
    saver = ExportManager(loader)
    saver.exec(model_table, '../../data/model', 'covid19_modeled')
