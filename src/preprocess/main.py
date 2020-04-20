import sys

sys.path.append('../../')

from src.preprocess.CreateFlatTable import CreateFlatTable
from src.preprocess.Imputation import Imputation
from src.preprocess.Transformation import Transformation
from src.preprocess.PreprocessCommandContainer import PreprocessCommandContainer
from src.utils.Exporter.ExportFactory import ExportFactory
from src.utils.Exporter.ExportManager import ExportManager

if __name__ == '__main__':
    print('### Preprocess Main file ###')

    preprocess_exec_plan = {
        'source_dir': '../../data/source',

        'imputation': [
            {
                'columns': ['Pop_Density', 'Death Rate'],
                'type': 'mean'
            },
            {
                'columns': ['Literacy....'],
                'type': 'zero'
            }
        ],
        'transformation': [
            {
                'columns': ['Pop_Density'],
                'type': 'log'
            },
            {
                'columns': ['Literacy....'],
                'type': 'root_square'
            }
        ]
    }

    preprocess_command_register = PreprocessCommandContainer()

    # register command
    # TODO: extract merge functionss and get source
    preprocess_command_register.register('create_flat_from_csv',
                                         CreateFlatTable(preprocess_exec_plan['source_dir'],
                                                         {'merge_key': 'Country', 'from_type': 'csv'}))
    # ----------
    # register imputation
    # ----------
    imputation_types = [el['type'] for el in preprocess_exec_plan['imputation']]
    for imputation_type in imputation_types:
        preprocess_command_register.register(f'imputation_by_{imputation_type}', Imputation({'type': imputation_type}))

    # register transform
    transform_types = [el['type'] for el in preprocess_exec_plan['transformation']]
    for transform_type in transform_types:
        preprocess_command_register.register(f'transform_by_{transform_type}', Transformation({'type': transform_type}))

    # ----------
    # execute command
    # ----------
    flat_table = preprocess_command_register.get('create_flat_from_csv').exec()
    print('before preprocess')
    print(flat_table)

    for imputation in preprocess_exec_plan['imputation']:
        preprocess_command_register.get(f"imputation_by_{imputation['type']}").exec(imputation['columns'], flat_table)

    for transform in preprocess_exec_plan['transformation']:
        preprocess_command_register.get(f"transform_by_{transform['type']}").exec(transform['columns'], flat_table)
    print('after preprocess')
    print(flat_table)

    loader = ExportFactory('csv').generate()
    saver = ExportManager(loader)
    saver.exec(flat_table, '../../data/preprocessed', 'covid19_preprocessed.csv')

