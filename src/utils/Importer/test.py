import sys
# import pandas as pd
from src.utils.Importer.ImporterManager import ImporterManager
from src.utils.Importer.ImporterFactory import  ImporterFactory
sys.path.append('../../../')
#
# data = {'First_Name':  ["Henry","Andy","Jane"],
#         'Last_name': ["Liang", "Lin","Su"],
#         }
#
# df_test = pd.DataFrame(data, columns = ['First_Name','Last_name'])
source_directory = '../../../data/source'


if __name__ == '__main__':
    importer_object = ImporterFactory('csv').generate()
    importer_manager = ImporterManager(importer_object)
    importer_manager.exec(source_directory)


