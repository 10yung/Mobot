import pandas as pd
import sys
sys.path.append('../../')

from src.estimate.RMSE.RMSE import RMSE
from src.utils.Importer.ImporterFactory import ImporterFactory
from src.utils.Importer.ImporterManager import ImporterManager
from src.utils.Exporter.ExportFactory import ExportFactory
from src.utils.Exporter.ExportManager import ExportManager


class Estimate:
    def __init__(self, exec_plan: dict):
        self._exec_plan = exec_plan

    def exec(self):
        # fetch csv file and split train/testing
        importer = ImporterFactory('csv').generate()
        importer_manager = ImporterManager(importer)
        training, testing = importer_manager.exec(self._exec_plan['source_dir'])

        # Get model info data and to dict
        importer_object = ImporterFactory('csv').generate()
        csv_fetcher_object = ImporterManager(importer_object)
        data = csv_fetcher_object.exec(self._exec_plan['models_summary'])[0]
        data_dict = data.to_dict()

        # Build Model Name List Using Model Info Data
        model_name_list =[]
        for index, model in data_dict['model_name'].items():
            model_name_list.append(model)

        # Import a list of models and convert to dict
        model_files = [{
            'dir': self._exec_plan['models_dir'],
            'files': model_name_list
        }]
        fetcher_object = ImporterFactory('model').generate()
        model_object = ImporterManager(fetcher_object)
        model_list_test = model_object.exec(model_files)
        model_dict = {v : k for v, k in enumerate(model_list_test)}

        # Get a list of RMSE
        rmse_list =[]
        for (index, response), (index, predictors),(index,model) in zip(data_dict['response'].items(), data_dict['predictors'].items(),model_dict.items()):
            predictors = predictors.split('/')
            response = response.strip("'][").split(', ')
            rmse = RMSE().get_rmse(testing,predictors,response,model)
            rmse_list.append(rmse)

        # Concat model info dataframe and rmse dataframe
        rmse_df = pd.DataFrame(rmse_list, columns=['rmse'])
        result_df = pd.concat([data, rmse_df], axis=1)

        # Export Result Dataframe
        csv_exporter  = ExportFactory('csv').generate()
        exporter =  ExportManager(csv_exporter)
        exporter.exec(result_df, self._exec_plan['summary_target']['dir'], estimate_exec_plan['summary_target']['name'])



if __name__ == '__main__':
    print("### Estimate Main ###")

    estimate_exec_plan = {
        'source_dir': [{
                'dir': '../../data/split/',
                'files': ['training.csv']
        }, {
                'dir': '../../data/split/',
                'files': ['testing.csv']
        }],
        'models_summary': [{
            'dir': '../../data/model/',
            'files': ['covid19_modeled1.csv'],
        }],
        'models_dir': '../../data/model/models/',
        'summary_target': {
            'dir': '../../data/estimate',
            'name': 'estimated_model_data'
        },
    }

    estimator = Estimate(estimate_exec_plan)
    estimator.exec()

