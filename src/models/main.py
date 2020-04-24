import sys
sys.path.append('../../')

import pandas as pd
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
        'predictor_name': ["Health.expenditures....of.GDP.", "Literacy...."],
        'response_name': ['Recovery Rate'],
        'experiments': [{
            'name': 'AIC',
        }, {
            'name': 'SimpleLm',
        }, {
            'name': 'StepWise',
            'criteria': {
                'p_value': 0.05
            }
        },{
            'name': 'StepWise',
            'criteria': {
                'p_value': 0.01
            }
        },{
            'name': 'StepWise',
            'criteria': {
                'p_value': 0.02
            }
        },]
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

    model_table = {}
    for model in model_exec_plan['experiments']:
        # AIC
        if model['name'] == 'AIC':
            aic_object = aic()
            aic_result_list = aic.exec(training, model_exec_plan['predictor_name'],
                                       model_exec_plan['response_name'])
            aic_result_model = model['name']
            aic_result_x = aic_result_list[1]
            aic_result_x = ' '.join(aic_result_x)
            aic_result_y = model_exec_plan['response_name'][0]
            model_table[aic_result_model] =[aic_result_y, aic_result_x,'']

        # Simple Linear Regression
        elif model['name'] == 'SimpleLm':
            simple_object = SimpleLm()
            simple_result_list = simple_object.exec(data, model_exec_plan['predictor_name'],
                                                    model_exec_plan['response_name'])
            simple_result_model = model['name']
            simple_result_x = simple_result_list[1]
            simple_result_x = ' '.join(simple_result_x)
            simple_result_y = model_exec_plan['response_name'][0]
            model_table[simple_result_model] =[simple_result_y, simple_result_x,'']

        # StepWise
        elif model['name'] == 'StepWise':
            stepwise_object = StepWise(model['criteria'])
            sw_result_list = stepwise_object.exec(training, model_exec_plan['predictor_name'],
                                                  model_exec_plan['response_name'])
            key, value = list(model['criteria'].items())[0]
            simple_result_model = model['name']+ '_' + str(value)
            sw_result_x = sw_result_list[1]
            sw_result_x = ' '.join(sw_result_x)
            sw_result_y = model_exec_plan['response_name'][0]
            p_val = key + ' ' + str(value)
            model_table[simple_result_model] =[sw_result_y, sw_result_x, p_val]

    model_table = pd.DataFrame.from_dict(model_table, orient='index', columns=['response', 'predictors', 'criteria'])
    model_table = model_table.reset_index()
    model_table.columns = ['model_name','response', 'predictors', 'criteria']
    # print(model_table)

    loader = ExportFactory('csv').generate()
    saver = ExportManager(loader)
    saver.exec(model_table, '../../data/model', 'covid19_modeled')

